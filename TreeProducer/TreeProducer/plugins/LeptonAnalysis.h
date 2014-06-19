#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// Transient Tracks
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"

#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"

// For track extrapolation
#include "TrackingTools/TrajectoryState/interface/TrajectoryStateOnSurface.h"

#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "RecoVertex/AdaptiveVertexFit/interface/AdaptiveVertexFitter.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "TreeProducer/TreeProducer/interface/PseudoLepton.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

#include "TreeProducer/TreeProducer/interface/GenEventProperties.h"
#include <RecoTracker/Record/interface/NavigationSchoolRecord.h>
#include "PhysicsTools/RecoUtils/interface/CheckHitPattern.h"
#include "TrackingTools/IPTools/interface/IPTools.h"

#include "TTree.h"
#include "TProfile2D.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include <map>

#include "TrackPropagation/SteppingHelixPropagator/interface/SteppingHelixPropagator.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"

#include "TreeProducer/TreeProducer/interface/Candidates.h"
#include "TreeProducer/TreeProducer/interface/TreeLepton.h"
#include "TreeProducer/TreeProducer/interface/TreeDipseudoLeptonCandidate.h"

#include "TreeProducer/TreeProducer/interface/TreePhoton.h"
#include "TreeProducer/TreeProducer/interface/TreeDiphotonCandidate.h"

class LeptonAnalysis : public edm::EDAnalyzer {

  public:
  explicit LeptonAnalysis(const edm::ParameterSet&);
  ~LeptonAnalysis();

  private:

  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  void endLuminosityBlock(const edm::LuminosityBlock & lumi, const edm::EventSetup & setup);
  virtual void endJob() ;

  void fillMuonTime(MuonTime & time, const int nDof,
		    const float & timeAtIpInOut, const float & timeAtIpInOutErr,
		    const float & timeAtIpOutIn, const float & timeAtIpOutInErr);
  void fillMuonTime(MuonTime & time, const reco::MuonTime & mt);

  void fillMuonTime(MuonTime & time, const reco::MuonTimeExtra & mt);

  // decay channels
  typedef enum { __lepTypeElectron,
    __lepTypeMuon,
    __lepTypeTau,
    __lepTypeTrack,
    __lepTypePhoton}
  leptonType;
  std::string leptonName_;


  // Useful, but leave out for now as unused
  //  // types of candidates that we distinguish
  //  typedef enum { __catSignal,             // fully reconstructed signal
  //                 __catSignalWrongChannel, // fully reconstructed signal, but wrong decay mode
  //                 __catSignalMixed,        // both leptons from signal, but wrong pairing
  //                 __catOneSigOneBkgWithGen,// one lepton from signal, one from unrelated GenParticle
  //                 __catOneSigOneBadReco,   // one lepton from signal, one without GenParticle at all
  //                 __catGoodButWrongType,   // fully reconstructed *other* resonance (e.g. Z)
  //                 __catBackground }        // both leptons are of non-signal origin
  //               categoryType;

  // FIXME
  // Or just checks it does what we want
  // int getGenParticleMatch(const edm::Handle<edm::View<reco::GenParticle> > & mcParticles,
  //     const PseudoLepton& lepton, const edm::EventSetup& iSetup);

  /// Return the closest stable genParticle in deltaR
  template<class A>
  int getGenParticleMatch(const edm::Handle<edm::View<reco::GenParticle> > & mcParticles,
			  const A& lepton, const edm::EventSetup& iSetup)
  {
    double minDeltaR=999;
    int genIndex=-999;

    //  std::cout << "---> Lepton" << std::endl;
    //  std::cout << "Pt of lepton : " << lepton.pt() << std::endl;
    //  std::cout << "Eta, phi of particle : " << lepton.eta() << " " << lepton.phi() << std::endl;
    //  std::cout << "px, py, pz : " << lepton.px() << " " << lepton.py() << " " << lepton.pz() << std::endl;
    //
    //
    //  std::cout << "---> Gen Particles" << std::endl;
    // Loop over genParticles
    for (unsigned imc=0; imc<mcParticles->size(); imc++) {
      reco::GenParticle mcPart=(*mcParticles)[imc];

      // Only choose status == 1 || 2 particles
      if (mcPart.status()==3) continue;

      // Ignore neutral genParticles, as we are looking for charged leptons
      // FIXME will probably be terrible for photons
      if (mcPart.charge()==0) continue;

      // Ignore particles which decay further - check this?
      if (mcPart.numberOfDaughters()>0) continue;

      // Get trajectory state of this gen particle closest to beamline
      double dR=9999;
      try {
	// TrajectoryStateClosestToBeamLine tsAtClosestApproach = getGenParticleStateClosestToBeamline( iSetup, mcPart);
	// GlobalVector p = tsAtClosestApproach.trackStateAtPCA().momentum();
	FreeTrajectoryState tsAtClosestApproach = getGenParticleStateClosestToBeamline( iSetup, mcPart);
	GlobalVector p = tsAtClosestApproach.momentum();

	// Now do deltaR between track and gen particle ts
	dR=deltaR(lepton.momentum().eta(),lepton.momentum().phi(),p.eta(),p.phi());
	// dR=deltaR(lepton.eta(),lepton.phi(),p.eta(),p.phi());
      } catch(cms::Exception& e) {};

      if (dR<minDeltaR) {
	minDeltaR=dR;
	genIndex=imc;
      }
    }

    if (minDeltaR<0.1) {
      return genIndex;
    } else {
      return -999;
    }
  }


  // Get gen particle state closest to beamline
  // Fot matching gen particles to tracks
  // TrajectoryStateClosestToBeamLine getGenParticleStateClosestToBeamline( const edm::EventSetup& iSetup, const  reco::GenParticle & part );
  FreeTrajectoryState getGenParticleStateClosestToBeamline( const edm::EventSetup& iSetup, const  reco::GenParticle & part );

  // FIXME
  // Unused at the moment
  //  int decayChannel(const reco::Candidate&);

  // Given a genParticle/Candidate, will see if this lepton comes from a signal MC particle
  const reco::Candidate* signalOrigin(const reco::Candidate*);

  // EVENT INFO
  // Fill info on event based quantities e.g. run, lumi, event, MET
  void fillEventBasedInfo(const edm::Event&,const edm::EventSetup&);

  // PSEUDO LEPTONS
  // Fill info on individual pseudoleptons e.g. d0, pt, calo & trigger match
  void fillPseudoLeptons(const edm::Event& iEvent, const edm::EventSetup& iSetup,
			 const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles);
  // Create and fill info on di-pseudolepton candidates e.g. Lxy, refitted pt of leptons
  void fillDipseudoleptonCandidates(const edm::Event& iEvent, const edm::EventSetup& iSetup,
				    const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles );
  void fillCandidateInfo( TreeDipseudoLeptonCandidate & candidate, const TreeLepton & highPtLepton, const TreeLepton & lowPtLepton, const edm::Event& iEvent, const edm::EventSetup& iSetup, bool correctTipLip, const edm::Handle<edm::View<PseudoLepton> > & particles );

  float extrapolateToMuon(const PseudoLepton & tk, const PseudoLepton & rsa,
			  const GlobalPoint & position, const edm::ESHandle<MagneticField> & theMagField);

  // void findMatchedMuons(const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles);
  void findMatchedMuons(const edm::EventSetup& iSetup, const edm::Handle<edm::View<PseudoLepton> > & particles);

  // PHOTONS
  // Note: photons include electrons where the track hasn't been reconstructed
  // Fill info on individual photon candidates
  void fillPhotons(const edm::Event&);
  // Fill info on diphoton candidates
  void fillDiphotonCandidates(const edm::Event&);

  // JETS
  // Fill info on individual jet candidates
  void fillJets(const edm::Event&);
  // Fill info on dijet candidates
  void fillDijetCandidates(const edm::Event&);

  // Check if interesting trigger has fired in this event
  bool doTrigger(const edm::Event&);

  // Find a trigger match to a pseudolepton
  const reco::Particle::LorentzVector * findTrigMatch(const PseudoLepton & lepton,
      const edm::Handle< pat::TriggerEvent > & triggerEvent, double & deltaR );

  // OLD method for comparison
  const int findTrigMatch_OLD(const PseudoLepton & lepton,
      const edm::Handle< pat::TriggerEvent > & triggerEvent, double & deltaR,
      const edm::Handle< pat::TriggerObjectStandAloneCollection > & saTriggerObjects );

  // Find a calo match to a pseudolepton
  const reco::SuperCluster * findCaloMatch(const PseudoLepton & lepton,
      const edm::Handle< std::vector<reco::SuperCluster> > & barrelSuperClusters,
      const edm::Handle< std::vector<reco::SuperCluster> > & endcapSuperClusters,
      double & deltaR, double & deltaEta, double & deltaPhi );

  // Find a photon to match to a pseudolepton
  const pat::Photon * findPhotonMatch(const PseudoLepton & lepton,
      const edm::Handle< std::vector<pat::Photon> > & photons,
      double &min_deltaR );

  // Extrapolate transient track to surface given by a global point and return delta R
  const double extrapolateAndDeltaR( const reco::TransientTrack & tTrack,
      const GlobalPoint & point, double & deltaEta, double & deltaPhi  );

  // OLD method for comparison
  const reco::SuperCluster * findCaloMatch_OLD(const PseudoLepton & lepton,
      const edm::Handle< std::vector<reco::SuperCluster> > & barrelSuperClusters,
      const edm::Handle< std::vector<reco::SuperCluster> > & endcapSuperClusters,
      double & deltaR );

  // FIXME
  // Unused, but could be good to apply/check any standard ID?
  //  template<class Lepton> bool leptonID(const Lepton&);
  //  bool leptonID(const pat::Electron&);

  // Refit primary vertex excluding the two leptons in the candidate
  reco::Vertex refitPrimaryVertex( const reco::TransientTrack & leptonH, const reco::TransientTrack & leptonL );


  // Computes absolute tracker isolation
  double trackerIsolation(const edm::Event& iEvent,
      const reco::Track & plept,
      const reco::Track & pveto,
      const double innerCone=0.03);


  // FIX ME
  // At the moment, everything goes through the PseudoLepton method
  // Check implementation for muons
  reco::TransientTrack leptonTrack(const PseudoLepton &);
  reco::TransientTrack leptonTrack(const pat::Electron &);
  reco::TransientTrack leptonTrack(const pat::Muon &);
  reco::TransientTrack leptonTrack(const pat::Tau &);

  reco::Track correctImpactParameter(const reco::Track &track, const float deltaD0, const float deltaDZ, const bool usePV);
  reco::TransientTrack CorrectTransientTrack(const reco::Track &track, const float deltaD0, const float deltaDZ, const bool usePV);
  reco::TransientTrack CorrectTransientTrack(const reco::TransientTrack &tTrack, const float deltaD0, const float deltaDZ, const bool usePV);

  // Find matches between standalone candidates and track-based candidates
  const TreeLepton getLepton( unsigned int index );
  void findCandidateMatches( const edm::Event& iEvent, const edm::EventSetup& iSetup,
			     const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles );

  // Detector timing
  // No implementation yet
  double leptonTiming(const pat::Electron &);
  double leptonTiming(const pat::Muon &);
  double leptonTiming(const pat::Tau &);
  double leptonTiming(const PseudoLepton &);

  // Initialization
  void initializeVars();

  // beamspot
  reco::BeamSpot beamSpot_;

  // primary vertex
  reco::Vertex primaryVertex_;
  VertexState primaryVertexState_;

  // for displaced vertex fit
  edm::ESHandle<TransientTrackBuilder> trackBuilder_;
  KalmanVertexFitter* vertexFitter_;
  CheckHitPattern checkHitPattern_;

  // FIXME
  // Unused
  // container for additional signal particle information
  //  typedef struct {
  //    double rt;
  //    double r;
  //    double ndaughters;
  //  } GenInfo_t;
  //  std::map<const reco::Candidate*,GenInfo_t*> GenInfoMap_;

  // input tags  
  edm::InputTag leptonCollTag_[4];
  edm::InputTag generatorTag_;
  edm::InputTag pileupTag_;
  edm::InputTag genEventInfoTag_;
  edm::InputTag trigger_;
  edm::InputTag triggerEvent_;
  edm::InputTag barrelSuperClusters_;
  edm::InputTag endcapSuperClusters_;
  edm::InputTag photons_;
  edm::InputTag recoMuonTag_;
  edm::InputTag timeTags_;

  // analysis setup
  std::vector<int> signalPDGId_;
  int leptonPDGId_;
  leptonType thisLepton_;
  std::vector<std::string> hltPaths_;

  // Loose selection on track pt (and SC Et in electron channel)
  double leptonPtCut_;
  double leptonRSAPtCut_;
  double leptonSCEtCut_;

  // Use MC Truth info?
  bool useMCTruth_;

  // Is this data?
  bool isData_;

  // trigger and event filter summary storage
  unsigned numProcessedEvents_;
  unsigned numEventsPassingEventFilters_;
  unsigned numEventsPassingTrigger_;
  unsigned numEventsPassingPreFilter_;

  std::map<std::string,unsigned> trigFilterSummary_;
  std::map<std::string,unsigned> trigPathSummary_;

  // To count the total number of events on which the producer runs
  TH1F * hTotalProcessedEvents_;
  TH1F * hEventsPassingEventsFilter_;
  TH1F * hEventsPassingTrigger_;
  TH1F * hEventsPassingPreFilter_;

  // The tree with all the variables
  edm::Service<TFileService> fs_;
  TTree* outputTree_;

  std::vector<std::string> triggers_;

  // Structure holding all the variables
  Candidates candidates_;
  std::vector<TreeLepton*> tempLeptons_;

  // File and histograms containing d0 and z0 corrections
  edm::FileInPath tiplipCorrectionFile_;
  TFile * tiplipTfile_;
  TProfile2D * z0Corrections_;
  TProfile2D * z0Corrections_badRunRange_;
  TProfile2D * d0Corrections_;
  TProfile2D * d0Corrections_badRunRange_;
  int badRangeMin_;
  int badRangeMax_;
  // Checks if run is in bad run range
  bool inBadRunRange();
  const SteppingHelixPropagator * steppingHelixPropAny_;
  const SteppingHelixPropagator * steppingHelixPropAlong_;

  edm::Handle<reco::MuonCollection> recoMuons;
  edm::Handle<reco::MuonTimeExtraMap> timeMap1;
  edm::Handle<reco::MuonTimeExtraMap> timeMap2;
  edm::Handle<reco::MuonTimeExtraMap> timeMap3;
};
