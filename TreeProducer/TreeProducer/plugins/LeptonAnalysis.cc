#include "TreeProducer/TreeProducer/plugins/LeptonAnalysis.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
// #include "DataFormats/Common/interface/Vector.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "Math/Vector4D.h"
#include "Math/GenVector/Boost.h"
#include "TDCacheFile.h"
#include "DataFormats/Math/interface/angle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/MuonReco/interface/MuonTime.h"

#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h"
#include "FWCore/Framework/interface/LuminosityBlock.h"
#include "DataFormats/Common/interface/MergeableCounter.h"

#include <sstream>
#include <iomanip>

// PAT
#include "PhysicsTools/PatUtils/interface/TriggerHelper.h"
#include "DataFormats/PatCandidates/interface/TriggerPath.h"
#include "DataFormats/PatCandidates/interface/TriggerFilter.h"
#include "DataFormats/PatCandidates/interface/GenericParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"

void LeptonAnalysis::endLuminosityBlock(const edm::LuminosityBlock & lumi, const edm::EventSetup & setup)
{
  // Total number of events is the sum of the events in each of these luminosity blocks
  edm::Handle<edm::MergeableCounter> nEventsTotalCounter;
  lumi.getByLabel("nEventsTotal", nEventsTotalCounter);
  numProcessedEvents_ += nEventsTotalCounter->value;

  edm::Handle<edm::MergeableCounter> nEventsAfterEventFilters;
  lumi.getByLabel("nEventsPostEventFilter", nEventsAfterEventFilters);
  numEventsPassingEventFilters_ += nEventsAfterEventFilters->value;

  edm::Handle<edm::MergeableCounter> nEventsAfterHLTFilter;
  lumi.getByLabel("nEventsPostHLTFilter", nEventsAfterHLTFilter);
  numEventsPassingTrigger_ += nEventsAfterHLTFilter->value;

  edm::Handle<edm::MergeableCounter> nEventsAfterPreFilter;
  lumi.getByLabel("nEventsPostPreFilter", nEventsAfterPreFilter);
  numEventsPassingPreFilter_ += nEventsAfterPreFilter->value;
}

LeptonAnalysis::LeptonAnalysis(const edm::ParameterSet& iConfig):
  checkHitPattern_(),
  generatorTag_(iConfig.getParameter<edm::InputTag>("generatorSrc")),
  pileupTag_(edm::InputTag("addPileupInfo")),
  genEventInfoTag_(edm::InputTag("generator")),
  trigger_(iConfig.getParameter<edm::InputTag>("trigger")),
  triggerEvent_(iConfig.getParameter<edm::InputTag>("triggerEvent")),
  barrelSuperClusters_(iConfig.getParameter<edm::InputTag>("barrelSuperClusters")),
  endcapSuperClusters_(iConfig.getParameter<edm::InputTag>("endcapSuperClusters")),
  photons_(iConfig.getParameter<edm::InputTag>("photons")),
  recoMuonTag_(iConfig.getParameter<edm::InputTag>("recoMuonSrc")),
  timeTags_(iConfig.getParameter<edm::InputTag>("timeExtraSrc")),
  signalPDGId_(iConfig.getParameter<std::vector<int>>("signalPDGId")),
  leptonPDGId_(iConfig.getParameter<int>("leptonPDGId")),
  hltPaths_(iConfig.getParameter<std::vector<std::string> >("hltPaths")),
  leptonPtCut_(iConfig.getParameter<double>("leptonPtCut")),
  leptonRSAPtCut_(iConfig.getParameter<double>("leptonRSAPtCut")),
  leptonSCEtCut_(iConfig.getParameter<double>("leptonSCEtCut")),
  useMCTruth_(iConfig.getParameter<bool>("UseMCTruth")),
  isData_(iConfig.getParameter<bool>("isData")),
  numProcessedEvents_(0),
  numEventsPassingEventFilters_(0),
  numEventsPassingTrigger_(0),
  numEventsPassingPreFilter_(0),
  // tiplipCorrectionFile_(iConfig.getParameter<edm::FileInPath>("tiplipCorrectionFile")),
  badRangeMin_(iConfig.getParameter<int>("badRangeMin")),
  badRangeMax_(iConfig.getParameter<int>("badRangeMax")),
  steppingHelixPropAny_(0),
  steppingHelixPropAlong_(0)
{
  if (leptonPDGId_==11) {
    thisLepton_=__lepTypeElectron;
    leptonName_="electron";
  } else if (leptonPDGId_==13) {
    thisLepton_=__lepTypeMuon;
    leptonName_="muon";
  } else if (leptonPDGId_==15) {
    thisLepton_=__lepTypeTau;
    leptonName_="tau";
  } else if (leptonPDGId_==-11) {
    thisLepton_=__lepTypeTrack;
    leptonName_="etrack";
  } else if (leptonPDGId_==-13) {
    thisLepton_=__lepTypeTrack;
    leptonName_="mutrack";
  } else if (leptonPDGId_==-15) {
    thisLepton_=__lepTypeTrack;
    leptonName_="tautrack";
  } else if (leptonPDGId_==22) {
    thisLepton_=__lepTypePhoton;
    leptonName_="photon";
  } else {
    throw cms::Exception("InvalidLeptonPDG") << "abs(leptonPDGId) must be 11, 13 or 15";
  }
  std::cout << "ANALYSIS CHANNEL: " << leptonName_ << std::endl;

  leptonCollTag_[__lepTypeElectron]=iConfig.getParameter<edm::InputTag>("electronSrc");
  leptonCollTag_[__lepTypeMuon]=iConfig.getParameter<edm::InputTag>("muonSrc");
  leptonCollTag_[__lepTypeTau]=iConfig.getParameter<edm::InputTag>("tauSrc");
  leptonCollTag_[__lepTypeTrack]=iConfig.getParameter<edm::InputTag>("trackSrc");

  // introduce short dCache read timeout to work around problems at RAL
  TDCacheFile::SetOpenTimeout(1800);

  // Create the tree
  edm::Service<TFileService> fs_;
  outputTree_ = fs_->make<TTree>("outputTree","outputTree");
  // Single lepton variables
  outputTree_->Branch("candidates","Candidates",&candidates_,32000,0);
  outputTree_->Branch("triggers","std::vector<std::string>",&triggers_,32000,0);

  // To save the total number of processed events
  hTotalProcessedEvents_ = new TH1F("totalProcessedEvents", "Total processed events", 1, 0, 1);
  hEventsPassingEventsFilter_ = new TH1F("eventsPassingEventFilters", "Events passing event filters", 1, 0, 1);
  hEventsPassingTrigger_ = new TH1F("eventsPassingTrigger", "Events passing trigger selection", 1, 0, 1);
  hEventsPassingPreFilter_ = new TH1F("eventsPassingPreFilter", "Events passing prefilter selection", 1, 0, 1);
}

LeptonAnalysis::~LeptonAnalysis()
{
//  tiplipTfile_->Close();
}

void LeptonAnalysis::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  std::cout << "starting the analyze" << std::endl;

  // event setup
  iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",trackBuilder_);
  //  if (checkHitPattern_==NULL) checkHitPattern_ = new CheckHitPattern();

  // if( steppingHelixProp_ == 0 ) {
  edm::ESHandle<Propagator> muonPropagatorAnyHandle;
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAny", muonPropagatorAnyHandle);
  steppingHelixPropAny_ = dynamic_cast<const SteppingHelixPropagator*>(&*muonPropagatorAnyHandle);

  edm::ESHandle<Propagator> muonPropagatorAlongHandle;
  iSetup.get<TrackingComponentsRecord>().get("SteppingHelixPropagatorAlong", muonPropagatorAlongHandle);
  steppingHelixPropAlong_ = dynamic_cast<const SteppingHelixPropagator*>(&*muonPropagatorAlongHandle);
  // }

  // Take the reco::muons and timeExtra to match and extract timing of RSA
  iEvent.getByLabel(recoMuonTag_,recoMuons);
  // Load timing information
  iEvent.getByLabel(timeTags_.label(),"combined",timeMap1);
  iEvent.getByLabel(timeTags_.label(),"dt",timeMap2);
  iEvent.getByLabel(timeTags_.label(),"csc",timeMap3);

  std::cout << "loaded time tags" << std::endl;

  // look at trigger information, this fills the vars_.triggers vector of strings
  bool passesTrigger = doTrigger(iEvent);

  if( passesTrigger ) {

    // Initialize all variables
    initializeVars();

    // get beamspot
    edm::Handle<reco::BeamSpot> beamSpotHandle;
    iEvent.getByLabel ("offlineBeamSpot", beamSpotHandle);
    beamSpot_=(*beamSpotHandle);

    // Fill event based variables
    fillEventBasedInfo(iEvent,iSetup);

    // Get the pseudoleptons
    edm::Handle<edm::View<PseudoLepton> > particles;
    iEvent.getByLabel(leptonCollTag_[__lepTypeTrack], particles);

    // Get the magnetic field
    edm::ESHandle<MagneticField> theMagField;
    // iSetup.get<IdealMagneticFieldRecord>().get(theMagField);

    // Fill pseudo leptons
    fillPseudoLeptons(iEvent, iSetup, theMagField, particles);

    // Fill dipseudo lepton candidates
    fillDipseudoleptonCandidates(iEvent, iSetup, theMagField, particles);

    if ( leptonName_=="photon") {
      // Fill photons
      fillPhotons(iEvent);

      // Fill diphoton candidates
      fillDiphotonCandidates(iEvent);
    }

    // Fill Tree
    outputTree_->Fill();
  }
}

void LeptonAnalysis::fillEventBasedInfo(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  // Get the run, event and lumi info
  // Put into tree
  candidates_.run = iEvent.id().run();
  candidates_.lumi = iEvent.id().luminosityBlock();
  candidates_.event = iEvent.id().event();

  // Get the MET info
  try {
    edm::Handle<std::vector<pat::MET> > metHandle;
    iEvent.getByLabel ("patMETs", metHandle);
    // MET info into tree
    candidates_.MET = metHandle->begin()->pt();
    candidates_.METPhi = metHandle->begin()->phi();
  }
  catch (...) {
    //    std::cout << "No pat MET collection found in input file" << std::endl;
  }

  // Get reco primary vertex info
  edm::Handle<reco::VertexCollection> primaryVertexHandle_;
  iEvent.getByLabel ("offlinePrimaryVerticesWithBS", primaryVertexHandle_);

  // there should always be a vertex in this collection. even if the primary vertex fit failed,
  // a fake vertex based on the beam spot should be present
  if (primaryVertexHandle_->size()==0) {
    std::cout << "no primary vertex found! skipping event" << std::endl;
    return;
  }

  // Set main PV
  primaryVertex_ = primaryVertexHandle_->front();

  VertexState PVstate(GlobalPoint(primaryVertex_.x(),primaryVertex_.y(),primaryVertex_.z()),GlobalError(primaryVertex_.covariance()));
  primaryVertexState_=PVstate;

  candidates_.pv_x = primaryVertex_.x();
  candidates_.pv_y = primaryVertex_.y();
  candidates_.pv_z = primaryVertex_.z();
  candidates_.pv_xError = primaryVertex_.xError();
  candidates_.pv_yError = primaryVertex_.yError();
  candidates_.pv_zError = primaryVertex_.zError();
  candidates_.pv_nTracks = primaryVertex_.nTracks();
  candidates_.pv_chi2 = primaryVertex_.chi2();
  candidates_.pv_ndof = primaryVertex_.ndof();

  candidates_.bs_x = beamSpot_.x0();
  candidates_.bs_y = beamSpot_.y0();
  candidates_.bs_z = beamSpot_.z0();

  // count number of proper primary vertices in event
  int numPV=0;
  for (unsigned i=0; i<primaryVertexHandle_->size(); i++) {
    if (!(*primaryVertexHandle_)[i].isFake()) ++numPV;
  }

  // Reco pv info into tree
  candidates_.numPV = numPV;

  // evaluate generator-level event properties needed for reweighting,
  // such as PDF, pile-up vertices,
  // decay channels and lifetimes of long-lived particles etc
  if( useMCTruth_ ) {
    GenEventProperties genProp(iEvent,iSetup,signalPDGId_,generatorTag_,
        pileupTag_,genEventInfoTag_);

    // MC pv info into tree
    candidates_.nvtx_m1 = genProp.numPileup(-1);
    candidates_.nvtx_0 = genProp.numPileup(0);
    candidates_.nvtx_p1 = genProp.numPileup(1);
    candidates_.nvtx_true = genProp.numTruePUInteractions();

    // MC info on decay types etc.
    // Only interested if there are two decays (as in our signal MC)
    if ( genProp.numDecays() > 0 ) {
      candidates_.ll1_motherPdgId = genProp.motherId(0);
      candidates_.ll1_daughterPdgId = genProp.decayMode(0);
      candidates_.ll1_ctau = genProp.ctau(0);
      candidates_.ll1_pt = genProp.pt(0);
      candidates_.ll1_pz = genProp.pz(0);
      candidates_.ll1_E = genProp.E(0);
      candidates_.ll1_Et = genProp.Et(0);
      candidates_.ll1_decayLength2D = genProp.decayLength2D(0);
      // std::cout << "ll1 gen-Lxy = " << genProp.decayLength2D(0) << std::endl;
      candidates_.ll1_decayLength3D = genProp.decayLength3D(0);
      candidates_.res1_PdgId = genProp.resId(0);
      candidates_.res1_Pt = genProp.resPt(0);
      candidates_.res1_Pz = genProp.resPz(0);
      if ( genProp.decayMode(0) != 0 ) {
        candidates_.ll1_daughter1_PdgId=genProp.daughterPdgId(0);
        candidates_.ll1_daughter1_Pt=genProp.daughterPt(0);
        candidates_.ll1_daughter1_Eta=genProp.daughterEta(0);
        candidates_.ll1_daughter1_D0=genProp.daughterD0(0);
        candidates_.ll1_daughter1_Z0=genProp.daughterZ0(0);
        candidates_.ll1_daughter2_PdgId=genProp.daughterPdgId(1);
        candidates_.ll1_daughter2_Pt=genProp.daughterPt(1);
        candidates_.ll1_daughter2_Eta=genProp.daughterEta(1);
        candidates_.ll1_daughter2_D0=genProp.daughterD0(1);
        candidates_.ll1_daughter2_Z0=genProp.daughterZ0(1);
      }
      if ( genProp.numDecays() > 1 ) {
        candidates_.ll2_motherPdgId = genProp.motherId(1);
        candidates_.ll2_daughterPdgId = genProp.decayMode(1);
        candidates_.ll2_ctau = genProp.ctau(1);
        candidates_.ll2_pt = genProp.pt(1);
        candidates_.ll2_pz = genProp.pz(1);
        candidates_.ll2_E = genProp.E(1);
        candidates_.ll2_Et = genProp.Et(1);
        candidates_.ll2_decayLength2D = genProp.decayLength2D(1);
	// std::cout << "ll2 gen-Lxy = " << genProp.decayLength2D(1) << std::endl;
        candidates_.ll2_decayLength3D = genProp.decayLength3D(1);
        candidates_.res2_PdgId = genProp.resId(1);
        candidates_.res2_Pt = genProp.resPt(1);
        candidates_.res2_Pz = genProp.resPz(1);
        if ( genProp.decayMode(1) != 0 ) {
          candidates_.ll2_daughter1_PdgId=genProp.daughterPdgId(2);
          candidates_.ll2_daughter1_Pt=genProp.daughterPt(2);
          candidates_.ll2_daughter1_Eta=genProp.daughterEta(2);
          candidates_.ll2_daughter1_D0=genProp.daughterD0(2);
          candidates_.ll2_daughter1_Z0=genProp.daughterZ0(2);
          candidates_.ll2_daughter2_PdgId=genProp.daughterPdgId(3);
          candidates_.ll2_daughter2_Pt=genProp.daughterPt(3);
          candidates_.ll2_daughter2_Eta=genProp.daughterEta(3);
          candidates_.ll2_daughter2_D0=genProp.daughterD0(3);
          candidates_.ll2_daughter2_Z0=genProp.daughterZ0(3);
        }
      }
    }
  }
}

void LeptonAnalysis::fillPseudoLeptons(const edm::Event& iEvent, const edm::EventSetup& iSetup,
				       const edm::ESHandle<MagneticField> & theMagField,
				       const edm::Handle<edm::View<PseudoLepton> > & particles)
{
  // Load superCluster collections if this is for electrons
  edm::Handle< std::vector<reco::SuperCluster> > barrelSuperClusters;
  edm::Handle< std::vector<reco::SuperCluster> > endcapSuperClusters;
  edm::Handle< std::vector<pat::Photon> > photons;
  if( leptonName_ == "etrack" ) {
    iEvent.getByLabel( barrelSuperClusters_, barrelSuperClusters );
    if (barrelSuperClusters.failedToGet()) {
      std::cout << "WARNING: cannot access barrel superclusters for matching" << std::endl;
    }
    iEvent.getByLabel( endcapSuperClusters_, endcapSuperClusters );
    if (endcapSuperClusters.failedToGet()) {
      std::cout << "WARNING: cannot access endcap superclusters for matching" << std::endl;
    }
    iEvent.getByLabel( photons_, photons );
    if (photons.failedToGet()) {
      std::cout << "WARNING: cannot access photons for matching" << std::endl;
    }
  }

  // Load gen particles or set the flag to false if they are not available
  bool MCTruthFound = true;
  edm::Handle<edm::View<reco::GenParticle> > mcParticles;
  if( useMCTruth_ ) {
    iEvent.getByLabel(generatorTag_,mcParticles);
    if(mcParticles.failedToGet()) {
      std::cout << "WARNING: cannot access MC truth information." << std::endl;
      MCTruthFound = false;
    }
  }

  // Load trigger objects
  edm::Handle< pat::TriggerEvent > triggerEvent;
  iEvent.getByLabel( triggerEvent_, triggerEvent );
  if (triggerEvent.failedToGet()) {
    std::cout << "WARNING: cannot access triggerEvent for matching" << std::endl;
  }

  // SA PAT trigger objects
  edm::Handle< pat::TriggerObjectStandAloneCollection > saTriggerObjects;
  iEvent.getByLabel( trigger_, saTriggerObjects );
  if (saTriggerObjects.failedToGet()) {
    std::cout << "WARNING: no stand alone trigger objects found" << std::endl;
  }

  int lepton_index=0;

  // First loop on pseudoleptons to fill lepton-based information (trigger matches, calo-matches, muon-matches, etc...)
  for( typename edm::View<PseudoLepton>::const_iterator it = particles->begin(); it != particles->end(); ++it ) {
    if( it->isStandAloneMuon() ) {
      if ( it->pt() < leptonRSAPtCut_ ) continue;
    }
    else if(it->pt() < leptonPtCut_) continue;

    // If this is the electron channel, only interested in track matched to TO
    // Also cut on matched SC Et in electron channel
    // Do not save if it doesn't have a calo match
    if ( leptonName_ == "etrack" ) {
      // Only consider tracks here - no muons
      if ( !(it->isCentralTrack() ) ) continue;

      // Check if track has a photon match
      double deltaR_Photon = 999;

      const pat::Photon * matchedPhoton = findPhotonMatch(*it, photons, deltaR_Photon);

      // Apply cut if it does
      if ( !useMCTruth_ ) {
	if ( matchedPhoton != 0 ) {
	  if (matchedPhoton->et() < leptonSCEtCut_ ) continue;
	}
	else continue;
      }
    }

    // Save this lepton
    candidates_.leptons_.push_back(TreeLepton());
    TreeLepton & lepton = candidates_.leptons_.back();

    // Save calo matching info if this is the electron channel
    if ( leptonName_ == "etrack" ) {
      double deltaR = 999;
      double deltaEta = 999;
      double deltaPhi = 999;
      const reco::SuperCluster * matchedSC = findCaloMatch(*it, barrelSuperClusters, endcapSuperClusters, deltaR, deltaEta, deltaPhi );
      if ( matchedSC == 0 ) {
        lepton.hasCaloMatch=0;
      }
      else {
        lepton.hasCaloMatch=1;
        lepton.cmDeltaR=deltaR;
        lepton.cmDeltaEta=fabs(deltaEta);
        lepton.cmDeltaPhi=fabs(deltaPhi);
        lepton.scEnergy = matchedSC->energy();
        lepton.scEt = matchedSC->energy() * sin( matchedSC->position().theta() );
        lepton.scEta = matchedSC->eta();
        lepton.scPhi = matchedSC->phi();

        // Compare with old method
        double deltaR_OLD=999;
        const reco::SuperCluster * matchedSC_OLD = findCaloMatch_OLD(*it, barrelSuperClusters, endcapSuperClusters, deltaR_OLD);

        // Check if we get a different SC and note "old" deltaR
        if ( matchedSC_OLD == matchedSC ) lepton.differentSCToOldMethod = 0;
        else lepton.differentSCToOldMethod = 1;

        lepton.cmDeltaR_old = deltaR_OLD;
      }

      // Save photon matching info
      double deltaR_Photon = 999;
      const pat::Photon * matchedPhoton = findPhotonMatch(*it, photons, deltaR_Photon);
      if ( matchedPhoton == 0 ) {
        lepton.hasPhotonMatch=0;
      }
      else {
        lepton.hasPhotonMatch=1;
        lepton.pmDeltaR=deltaR_Photon;
        lepton.photonEnergy=matchedPhoton->energy();
        if ( matchedSC != 0 ) lepton.sameSCAsMatched = ( matchedPhoton->superCluster()->energy() == matchedSC->energy() ) ? 1 : 0;
        else lepton.sameSCAsMatched=0;
        lepton.photonSCEnergy = matchedPhoton->superCluster()->energy();
        lepton.photonSCEt = matchedPhoton->superCluster()->energy() * matchedPhoton->superCluster()->energy() * sin(matchedPhoton->superCluster()->position().theta());
        lepton.photonEt = matchedPhoton->et();
        lepton.photonEta = matchedPhoton->eta();
        lepton.photonPhi = matchedPhoton->phi();
        // Photon Id variables
        lepton.photonHadronicOverEm = matchedPhoton->hadronicOverEm();
        lepton.photonHadTowOverEm = matchedPhoton->hadTowOverEm();
        lepton.photonSigmaIetaIeta = matchedPhoton->sigmaEtaEta();
        lepton.photonR9 = matchedPhoton->r9();
      }
    }

    lepton.index=lepton_index;
    lepton_index++;

    // Index in pseudo lepton collection
    lepton.pseudoLeptonIndex = it - particles->begin();

    // Build the transient track. This contains information on the beamspot and will be used later for extrapolations and vertex fitting.
    reco::TransientTrack tTrack = leptonTrack(*it);

    // Is track valid?
    if ( tTrack.isValid() ) {
      lepton.validTrack=true;
      lepton.algo = it->algo();

      // Pt etc. of track
      lepton.pt = it->pt();

      lepton.eta = it->eta();
      lepton.phi = it->phi();
      lepton.charge = it->charge();

      // Impact parameter
      // wrt beamline
      double d0=-9999;
      double d0significance=-9999;
      try {
        d0=tTrack.stateAtBeamLine().transverseImpactParameter().value();
        d0significance=tTrack.stateAtBeamLine().transverseImpactParameter().significance();

      } catch (cms::Exception& e) {
        // FIXME
        // Currently make this track non-valid.
        // Setting d0 and d0significance to -9999 implies that these should fail the cut on d0 significance
        // But we cut on abs(d0 significance) so they may pass?
        lepton.validTrack=false;
      };

      lepton.d0_BS = d0;
      lepton.d0Significance_BS = d0significance;

      // Impact parameter
      // wrt PV
      d0=-9999;
      d0significance=-9999;
      double dz=-9999;
      double dzsignificance=-9999;
      try {
        d0=fabs(tTrack.trajectoryStateClosestToPoint(
                  GlobalPoint(primaryVertex_.x(),primaryVertex_.y(),primaryVertex_.z())).perigeeParameters().transverseImpactParameter());
        double error=tTrack.trajectoryStateClosestToPoint(
              GlobalPoint(primaryVertex_.x(),primaryVertex_.y(),primaryVertex_.z())).perigeeError().transverseImpactParameterError();
        d0significance=d0/error;

        dz=tTrack.trajectoryStateClosestToPoint(
              GlobalPoint(primaryVertex_.x(),primaryVertex_.y(),primaryVertex_.z())).perigeeParameters().longitudinalImpactParameter();
        error=tTrack.trajectoryStateClosestToPoint(
              GlobalPoint(primaryVertex_.x(),primaryVertex_.y(),primaryVertex_.z())).perigeeError().longitudinalImpactParameterError();
        dzsignificance=dz/error;

      } catch (cms::Exception& e) {
        lepton.validTrack=false;
      }

      lepton.d0_PV = d0;
      lepton.d0Significance_PV = d0significance;
      lepton.dz_PV = dz;
      lepton.dzsignificance_PV = dzsignificance;

      // Impact parameter
      // wrt PV including error on PV
      d0=-9999;
      d0significance=-9999;
      double d03D=-9999;
      double d03DSignificance=-9999;
      try {
        d0 = fabs(IPTools::absoluteTransverseImpactParameter(tTrack, primaryVertex_).second.value());
        d0significance = d0/fabs(IPTools::absoluteTransverseImpactParameter(tTrack, primaryVertex_).second.error());
        d03D  = fabs(IPTools::absoluteImpactParameter3D(tTrack, primaryVertex_).second.value());
        d03DSignificance = d03D / fabs(IPTools::absoluteImpactParameter3D(tTrack, primaryVertex_).second.error());
      } catch (cms::Exception& e) {
        lepton.validTrack=false;
      }

      lepton.d0Significance_PV_includingPVError = d0significance;
      lepton.d03D_PV = d03D;
      lepton.d03DSignificance_PV_includingPVError = d03DSignificance;

      // What type of muon?
      lepton.isStandAloneMuon = it->isStandAloneMuon();
      lepton.isGlobalMuon = it->isGlobalMuon();
      lepton.isTrackerMuon = it->isTrackerMuon();
      lepton.isCentralTrack = it->isCentralTrack();
      lepton.isLooseMuon = it->isLooseMuon();

      //New tree variables for SA Muon Analysis
      //Added by Melih Feb 11, 2014 Fermilab

      try {
        lepton.dtStationsWithValidHits = it->hitPattern().dtStationsWithValidHits();
        lepton.cscStationsWithValidHits = it->hitPattern().cscStationsWithValidHits();
        lepton.dtStationsWithAnyHits = it->hitPattern().dtStationsWithAnyHits();
        lepton.cscStationsWithAnyHits = it->hitPattern().cscStationsWithAnyHits();
        lepton.muonStationsWithAnyHits = it->hitPattern().muonStationsWithAnyHits();
        lepton.numberOfHits = it->hitPattern().numberOfHits();
        lepton.numberOfValidHits = it->hitPattern().numberOfValidHits();
        lepton.numberOfValidMuonCSCHits = it->hitPattern().numberOfValidMuonCSCHits();
        lepton.numberOfValidMuonDTHits = it->hitPattern().numberOfValidMuonDTHits();
        lepton.numberOfValidMuonHits = it->hitPattern().numberOfValidMuonHits();
        lepton.numberOfLostHits = it->hitPattern().numberOfLostHits();
        lepton.numberOfLostMuonCSCHits = it->hitPattern().numberOfLostMuonCSCHits();
        lepton.numberOfLostMuonDTHits = it->hitPattern().numberOfLostMuonDTHits();
        lepton.numberOfLostMuonHits = it->hitPattern().numberOfLostMuonHits();
      } catch (...) {
        lepton.dtStationsWithValidHits = -999;
        lepton.cscStationsWithValidHits = -999;
        lepton.dtStationsWithAnyHits = -999;
        lepton.cscStationsWithAnyHits = -999;
        lepton.muonStationsWithAnyHits = -999;
        lepton.numberOfHits = -999;
        lepton.numberOfValidHits = -999;
        lepton.numberOfValidMuonCSCHits = -999;
        lepton.numberOfValidMuonDTHits = -999;
        lepton.numberOfValidMuonHits = -999;
        lepton.numberOfLostHits = -999;
        lepton.numberOfLostMuonCSCHits = -999;
        lepton.numberOfLostMuonDTHits = -999;
        lepton.numberOfLostMuonHits = -999;
      }

      // Quality cuts
      lepton.nLayers3D = tTrack.hitPattern().pixelLayersWithMeasurement() + tTrack.hitPattern().numberOfValidStripLayersWithMonoAndStereo();
      lepton.nLayers = tTrack.hitPattern().trackerLayersWithMeasurement();
      lepton.tip = it->dxy(beamSpot_.position());
      lepton.lip = it->dsz(beamSpot_.position());
      lepton.trackChi2 = tTrack.normalizedChi2();
      if ( it->quality( reco::TrackBase::TrackQuality::highPurity ) ) lepton.highPurity = 1;
      else lepton.highPurity = 0;

      // Tracker isolation
      lepton.iso = trackerIsolation(iEvent,tTrack.track(),tTrack.track());

      // Gen info for this lepton
      if ( useMCTruth_ && MCTruthFound ) {
	// Extrapolate the track
	FreeTrajectoryState fts(GlobalPoint(it->vx(),it->vy(),it->vz()),
				GlobalVector(it->px(),it->py(),it->pz()),
				it->charge(),
				0);//theMagField.product());
	FreeTrajectoryState ftsPCA(steppingHelixPropAny_->propagate(fts, beamSpot_));

        // Find closest stable (status == 1) genParticle by deltaR (correct for DV)
        int genIndex = getGenParticleMatch( mcParticles, ftsPCA, iSetup );

        if (genIndex>=0) {
          const reco::GenParticle matchedGenParticle = mcParticles->at(genIndex);

          // Get gen particle at point closest to beamline
          // This can then be compared to tracks
          FreeTrajectoryState tsAtClosestApproach = getGenParticleStateClosestToBeamline( iSetup, matchedGenParticle);
          GlobalVector p = tsAtClosestApproach.momentum();
          GlobalPoint v = tsAtClosestApproach.position();

          lepton.genIndex = genIndex;
          lepton.genPdgId = matchedGenParticle.pdgId();
          lepton.genPt = matchedGenParticle.pt();
          lepton.genVertexX = matchedGenParticle.vx();
          lepton.genVertexY = matchedGenParticle.vy();
          lepton.genVertexZ = matchedGenParticle.vz();
          lepton.genPhi = p.phi();
          lepton.genEta = p.eta();
          lepton.genTheta = p.theta();
          lepton.genD0 = (-v.x()*sin(p.phi())+v.y()*cos(p.phi()));

          // Note origin of this lepton
          // Will get more info on this later when matched candidate is formed
          const reco::Candidate * origin = signalOrigin(&matchedGenParticle);
          if ( origin != NULL ) {
            lepton.genSignalOriginPdgId = origin->pdgId();
            GenEventProperties::DecayLengthAndType dlt(GenEventProperties::getDecayLengthAndType(*origin));
            lepton.genSignalOriginCtau = dlt.ctau;
            lepton.genSignalOriginLxy = dlt.decayLength2D;
          }
          else lepton.genSignalOriginPdgId = 0;
        }
      }

      // Trigger matching
      double deltaR=999;

      int matchedTOIndex = findTrigMatch_OLD(*it, triggerEvent,deltaR,saTriggerObjects);
      if ( matchedTOIndex != 0 ) {
        lepton.triggerMatch = 1;
        lepton.triggerObjectIndex = matchedTOIndex;
        lepton.tmDeltaR=deltaR;
      }
      else lepton.triggerMatch=0;

      // Reference point on track
      lepton.vx = it->vx();
      lepton.vy = it->vy();
      lepton.vz = it->vz();

      // Add muon timing information
      // ---------------------------
      if (leptonName_=="mutrack" || leptonName_=="muon") {
	if( !lepton.isStandAloneMuon ) continue;

	// std::cout << "getting the timing" << std::endl;


        // Match the RSA to the SA. This is needed because RSA are not in the reco::Muon and we need
        // to access timing information from the reco::Muon. The RSA is a refit of the SA, the timing
        // of the hits is the same (but do not use anything with IP or beamspot constraint).
        // Analyze the short info stored directly in reco::Muon
        const math::XYZPoint & rsaInnerPoint(it->innerPosition());
        const math::XYZPoint & rsaOuterPoint(it->outerPosition());

        float minDxIn = 1000.;
        float minDyIn = 1000.;
        float minDzIn = 1000.;
        float minDxOut = 1000.;
        float minDyOut = 1000.;
        float minDzOut = 1000.;
        int imucount = 0;

        // Loop over the standAloneMuons and take the one with the closest inner and outer position.
        // Only save the timing if the matching is close enough (<5cm in x,y and <50cm in z).
        const reco::Muon * matchedSA = 0;
        int imucountMatch = -1;
        for (reco::MuonCollection::const_iterator sa=recoMuons->begin(); sa!=recoMuons->end(); ++sa, ++imucount) {
          if( sa->isStandAloneMuon() ) {

            // std::cout << "pseudoLeptonProducer: filling timing information" << std::endl;

            const math::XYZPoint & saInnerPoint(sa->standAloneMuon()->innerPosition());
            const math::XYZPoint & saOuterPoint(sa->standAloneMuon()->outerPosition());
            if( fabs(saInnerPoint.x() - rsaInnerPoint.x()) < minDxIn &&
                fabs(saInnerPoint.y() - rsaInnerPoint.y()) < minDyIn &&
                fabs(saOuterPoint.x() - rsaOuterPoint.x()) < minDxOut &&
                fabs(saOuterPoint.y() - rsaOuterPoint.y()) < minDyOut ) {
              minDxIn = fabs(saInnerPoint.x() - rsaInnerPoint.x());
              minDyIn = fabs(saInnerPoint.y() - rsaInnerPoint.y());
              minDzIn = fabs(saInnerPoint.z() - rsaInnerPoint.z());
              minDxOut = fabs(saOuterPoint.x() - rsaOuterPoint.x());
              minDyOut = fabs(saOuterPoint.y() - rsaOuterPoint.y());
              minDzOut = fabs(saOuterPoint.z() - rsaOuterPoint.z());

              // Check for good matching and fill timing information
              if( minDxIn > 5 || minDyIn > 5 || minDxOut > 5 || minDyOut > 5 || minDzIn > 50 || minDzOut > 50 ) continue;

              matchedSA = &*sa;
              imucountMatch = imucount;
            }
          }
        }
// Save the closest match
        lepton.minDxIn = minDxIn;
        lepton.minDyIn = minDyIn;
        lepton.minDzIn = minDzIn;
        lepton.minDxOut = minDxOut;
        lepton.minDyOut = minDyOut;
        lepton.minDzOut = minDzOut;

        if( matchedSA != 0 && imucountMatch != -1 ) {
          if (matchedSA->isTimeValid()) {
            // std::cout << "pseudoLeptonProducer: time is valid for muon pt = " << it->pt() << std::endl;
            fillMuonTime(lepton.muonTime, matchedSA->time());
          }
	  // Save the MuonTimeExtra information
          reco::MuonRef muonR(recoMuons,imucountMatch);

          // std::cout << "filling timing: for muon pt = " << lepton.pt << ", nDof = " << matchedSA->time().nDof << std::endl;
          // std::cout << "rsa inner position = " << rsaInnerPoint << ", outer position = " << rsaOuterPoint << std::endl;
          // std::cout << "sa inner position =  " << matchedSA->standAloneMuon()->innerPosition() << ", outer position = " << matchedSA->standAloneMuon()->outerPosition() << std::endl;

          const reco::MuonTimeExtraMap & timeMapCmb = *timeMap1;
          const reco::MuonTimeExtraMap & timeMapDT = *timeMap2;
          const reco::MuonTimeExtraMap & timeMapCSC = *timeMap3;
          fillMuonTime(lepton.muonTimeC, timeMapCmb[muonR]);
          fillMuonTime(lepton.muonTimeDT, timeMapDT[muonR]);
          fillMuonTime(lepton.muonTimeCSC, timeMapCSC[muonR]);

          if( matchedSA->isEnergyValid() ) {
            const reco::MuonEnergy & muonEnergy = matchedSA->calEnergy();
            lepton.emMax = muonEnergy.emMax;
            lepton.ecal_time = muonEnergy.ecal_time;

            // std::cout << "ecal_time = " << lepton.ecal_time << std::endl;

            lepton.ecal_timeErr = muonEnergy.ecal_timeError;
            lepton.hadMax = muonEnergy.hadMax;
            lepton.hcal_time = muonEnergy.hcal_time;
            lepton.hcal_timeErr = muonEnergy.hcal_timeError;
            // From the MuonTimingValidator
            lepton.emErr = 1.5/muonEnergy.emMax;
            // From the MuonTimingValidator
            lepton.hadErr = 1.; // DUMMY !!
          }
        }
      }
    }
    else lepton.validTrack=false;
  }

  // The loop on the leptons is done, now find track matches.
  findMatchedMuons(iSetup, particles);
}


void LeptonAnalysis::fillMuonTime(MuonTime & time, const int nDof,
                                  const float & timeAtIpInOut, const float & timeAtIpInOutErr,
                                  const float & timeAtIpOutIn, const float & timeAtIpOutInErr)
{
  // number of muon stations used
  time.nDof = nDof;

  // std::cout << "nDof = " << nDof << std::endl;

  // time of arrival at the IP for the Beta=1 hypothesis
  //  a) particle is moving from inside out
  time.timeAtIpInOut = timeAtIpInOut;
  time.timeAtIpInOutErr = timeAtIpInOutErr;
  //  b) particle is moving from outside in
  time.timeAtIpOutIn = timeAtIpOutIn;
  time.timeAtIpOutInErr = timeAtIpOutInErr;
}


void LeptonAnalysis::fillMuonTime(MuonTime & time, const reco::MuonTime & mt)
{
  fillMuonTime(time, mt.nDof, mt.timeAtIpInOut, mt.timeAtIpInOutErr, mt.timeAtIpOutIn, mt.timeAtIpOutInErr);
}


void LeptonAnalysis::fillMuonTime(MuonTime & time, const reco::MuonTimeExtra & mt)
{
  fillMuonTime(time, mt.nDof(), mt.timeAtIpInOut(), mt.timeAtIpInOutErr(), mt.timeAtIpOutIn(), mt.timeAtIpOutInErr());
  // 1/beta for prompt particle hypothesis
  time.inverseBeta = mt.inverseBeta();
  time.inverseBetaErr = mt.inverseBetaErr();
  // unconstrained 1/beta (time is free)
  time.freeInverseBeta = mt.freeInverseBeta();
  time.freeInverseBetaErr = mt.freeInverseBetaErr();
}


void LeptonAnalysis::findMatchedMuons(const edm::EventSetup& iSetup, const edm::Handle<edm::View<PseudoLepton> > & particles)
{
  for( std::vector<TreeLepton>::iterator rsa = candidates_.leptons_.begin(); rsa != candidates_.leptons_.end(); ++rsa ) {
    if( rsa->isStandAloneMuon ) {
      PseudoLepton rsaLepton = particles->at(rsa->pseudoLeptonIndex);
      GlobalPoint position( rsaLepton.innerPosition().x(), rsaLepton.innerPosition().y(), rsaLepton.innerPosition().z() );

      float minDR_1 = 10000.;
      float minDR_2 = 10000.;
      float minDR_3 = 10000.;
      float minDR_4 = 10000.;
      float minDR_5 = 10000.;
      float minDR_10 = 10000.;
      float minDR_15 = 10000.;
      float minDR_20 = 10000.;
      float minDR_26 = 10000.;

      float minGBDR_1 = 10000.;
      float minGBDR_2 = 10000.;
      float minGBDR_3 = 10000.;
      float minGBDR_4 = 10000.;
      float minGBDR_5 = 10000.;
      float minGBDR_10 = 10000.;
      float minGBDR_15 = 10000.;
      float minGBDR_20 = 10000.;
      float minGBDR_26 = 10000.;

      for( typename edm::View<PseudoLepton>::const_iterator tk = particles->begin(); tk != particles->end(); ++tk ) {
	// Get the magnetic field
	edm::ESHandle<MagneticField> theInMagField;
	// iSetup.get<IdealMagneticFieldRecord>().get(theInMagField);

	if( tk->isCentralTrack() ) {
	  // PseudoLepton tkLepton = particles->at(tk->pseudoLeptonIndex);
	  float dR = extrapolateToMuon(*tk, rsaLepton, position, theInMagField);
	  // to avoid nan. nan is different from any number, even itself, by the IEEE standard.
	  if( dR == dR ) {
	    if( tk->pt() > 1. && minDR_1 > dR ) minDR_1 = dR;
	    if( tk->pt() > 2. && minDR_2 > dR ) minDR_2 = dR;
	    if( tk->pt() > 3. && minDR_3 > dR ) minDR_3 = dR;
	    if( tk->pt() > 4. && minDR_4 > dR ) minDR_4 = dR;
	    if( tk->pt() > 5. && minDR_5 > dR ) minDR_5 = dR;
	    if( tk->pt() > 10. && minDR_10 > dR ) minDR_10 = dR;
	    if( tk->pt() > 15. && minDR_15 > dR ) minDR_15 = dR;
	    if( tk->pt() > 20. && minDR_20 > dR ) minDR_20 = dR;
	    if( tk->pt() > 26. && minDR_26 > dR ) minDR_26 = dR;
	  }
	}
	else if( tk->isGlobalMuon() ) {
	  float dR = extrapolateToMuon(*tk, rsaLepton, position, theInMagField);
	  // to avoid nan. nan is different from any number, even itself, by the IEEE standard.
	  if( dR == dR ) {
	    if( tk->pt() > 1. && minGBDR_1 > dR ) minGBDR_1 = dR;
	    if( tk->pt() > 2. && minGBDR_2 > dR ) minGBDR_2 = dR;
	    if( tk->pt() > 3. && minGBDR_3 > dR ) minGBDR_3 = dR;
	    if( tk->pt() > 4. && minGBDR_4 > dR ) minGBDR_4 = dR;
	    if( tk->pt() > 5. && minGBDR_5 > dR ) minGBDR_5 = dR;
	    if( tk->pt() > 10. && minGBDR_10 > dR ) minGBDR_10 = dR;
	    if( tk->pt() > 15. && minGBDR_15 > dR ) minGBDR_15 = dR;
	    if( tk->pt() > 20. && minGBDR_20 > dR ) minGBDR_20 = dR;
	    if( tk->pt() > 26. && minGBDR_26 > dR ) minGBDR_26 = dR;
	  }
	}
      }
      rsa->minMatchedDeltaR_1 = minDR_1;
      rsa->minMatchedDeltaR_2 = minDR_2;
      rsa->minMatchedDeltaR_3 = minDR_3;
      rsa->minMatchedDeltaR_4 = minDR_4;
      rsa->minMatchedDeltaR_5 = minDR_5;
      rsa->minMatchedDeltaR_10 = minDR_10;
      rsa->minMatchedDeltaR_15 = minDR_15;
      rsa->minMatchedDeltaR_20 = minDR_20;
      rsa->minMatchedDeltaR_26 = minDR_26;

      rsa->minMatchedGBDeltaR_1 = minGBDR_1;
      rsa->minMatchedGBDeltaR_2 = minGBDR_2;
      rsa->minMatchedGBDeltaR_3 = minGBDR_3;
      rsa->minMatchedGBDeltaR_4 = minGBDR_4;
      rsa->minMatchedGBDeltaR_5 = minGBDR_5;
      rsa->minMatchedGBDeltaR_10 = minGBDR_10;
      rsa->minMatchedGBDeltaR_15 = minGBDR_15;
      rsa->minMatchedGBDeltaR_20 = minGBDR_20;
      rsa->minMatchedGBDeltaR_26 = minGBDR_26;
    }
  }
}


void LeptonAnalysis::fillPhotons(const edm::Event& iEvent)
{

  // Here you need to loop over all photons/super clusters
  // for (...) {

  // Save this photon
  candidates_.photons_.push_back(TreePhoton());
  TreePhoton & photon = candidates_.photons_.back();

  // Fill with rubbish for now
  photon.et=26;
  photon.eta=-1.5;
  photon.phi=0.4;
  photon.time=2.4;

  // } //end for loop over all photons
}

void LeptonAnalysis::fillJets(const edm::Event& iEvent)
{

}

const reco::Particle::LorentzVector * LeptonAnalysis::findTrigMatch(const PseudoLepton & lepton,
    const edm::Handle< pat::TriggerEvent > & triggerEvent,
    double &min_deltaR)
{
  // find deltaR match among trigger objects
  min_deltaR=9999.;
  const reco::Particle::LorentzVector* trig_mom=0;

  // Get transient track for this lepton
  reco::TransientTrack tTrack = leptonTrack( lepton );

  // loop over all triggers we are interested in
  for (unsigned itrig=0; itrig<hltPaths_.size(); itrig++) {
    if (!triggerEvent->path(hltPaths_[itrig])) continue;
    if (!triggerEvent->path(hltPaths_[itrig])->wasAccept()) continue;
    // get all trigger objects associated with this HLT path
    const pat::TriggerObjectRefVector triggerObjects(triggerEvent->pathObjects(hltPaths_[itrig],false));
    for (unsigned i=0; i<triggerObjects.size(); i++) {

      //FIXME
      // Not sure what to do here.  Taking "vertex" position of trigger object to get surface...
      GlobalPoint trigObjectPoint( triggerObjects[i]->vx(), triggerObjects[i]->vy(), triggerObjects[i]->vz() );

      double deltaEta=999;
      double deltaPhi=999;
      // Calculate deltaR between SC and track extrapolated to point
      double dR = extrapolateAndDeltaR( tTrack, trigObjectPoint, deltaEta, deltaPhi );
      if (dR<min_deltaR) {
        min_deltaR=dR;
        trig_mom=&(triggerObjects[i]->p4());
      }
    }
  }

  bool trigMatch=(min_deltaR<0.1);
  if (trigMatch) {
    return trig_mom;
  }
  return 0;
}

const int LeptonAnalysis::findTrigMatch_OLD(const PseudoLepton & lepton,
    const edm::Handle< pat::TriggerEvent > & triggerEvent,
    double &min_deltaR,
    const edm::Handle< pat::TriggerObjectStandAloneCollection > & saTriggerObjects)
{
  // find deltaR match among trigger objects
  double lep_eta = lepton.eta();
  double lep_phi = lepton.phi();
  min_deltaR=9999.;
  const reco::Particle::LorentzVector* trig_mom=0;

  // Index to keep track of which TO we match to
  int triggerObjectIndex=0;
  int matchedTOIndex=0;

  // loop over all triggers we are interested in
  for (unsigned itrig=0; itrig<hltPaths_.size(); itrig++) {
    if (!triggerEvent->path(hltPaths_[itrig])) continue;
    if (!triggerEvent->path(hltPaths_[itrig])->wasAccept()) continue;

    // get all trigger objects associated with this HLT path
    const pat::TriggerObjectRefVector triggerObjects(triggerEvent->pathObjects(hltPaths_[itrig]));//,false));
    for (unsigned i=0; i<triggerObjects.size(); i++) {
      ++triggerObjectIndex;
      double trig_eta=triggerObjects[i]->eta();
      double trig_phi=triggerObjects[i]->phi();
      double dR=deltaR(lep_eta,lep_phi,trig_eta,trig_phi);
      //      std::cout << "Trigger object number " << i << " Collection : " << triggerObjects[i]->collection().c_str() << " Delta R : " << dR << std::endl;
      if (dR<min_deltaR) {
        matchedTOIndex=triggerObjectIndex;
        min_deltaR=dR;
        trig_mom=&(triggerObjects[i]->p4());
      }
    }
  }

  bool trigMatch=(min_deltaR<0.1);
  if (trigMatch && trig_mom != 0) {
    return matchedTOIndex;
  }
  return 0;
}

// Given a PseudoLepton and the barrel and endcap superclusters returns a pointer to a maching supercluster or a null pointer if no match was found.
const reco::SuperCluster * LeptonAnalysis::findCaloMatch_OLD(const PseudoLepton & lepton,
    const edm::Handle< std::vector<reco::SuperCluster> > & barrelSuperClusters,
    const edm::Handle< std::vector<reco::SuperCluster> > & endcapSuperClusters,
    double &min_deltaR )
{

  //
  // OLD METHOD
  //

  // find deltaR match among superclusters
  double lep_eta=lepton.eta();
  double lep_phi=lepton.phi();
  min_deltaR=9999.;
  const reco::SuperCluster * matchingSC = 0;

  const double deltaRcut=0.2;

  // loop over all barrel superclusters
  if (fabs(lep_eta)<1.48+1.5*deltaRcut) {
    for (unsigned iclus=0; iclus<barrelSuperClusters->size(); iclus++) {
      double clus_eta=(*barrelSuperClusters)[iclus].eta();
      double clus_phi=(*barrelSuperClusters)[iclus].phi();
      double dR=deltaR(lep_eta,lep_phi,clus_eta,clus_phi);
      if (dR<min_deltaR) {
        min_deltaR=dR;
        matchingSC = &(*barrelSuperClusters)[iclus];
      }
    }
  }
  // loop over all endcap superclusters
  if (fabs(lep_eta)>1.48-1.5*deltaRcut) {
    for (unsigned iclus=0; iclus<endcapSuperClusters->size(); iclus++) {
      double clus_eta=(*endcapSuperClusters)[iclus].eta();
      double clus_phi=(*endcapSuperClusters)[iclus].phi();
      double dR=deltaR(lep_eta,lep_phi,clus_eta,clus_phi);
      if (dR<min_deltaR) {
        min_deltaR=dR;
        matchingSC = &(*endcapSuperClusters)[iclus];
      }
    }
  }

  bool caloMatch = (min_deltaR<deltaRcut);
  if( caloMatch ) return matchingSC;
  return 0;
}

// Given a PseudoLepton and the barrel and endcap superclusters returns a pointer to a maching supercluster or a null pointer if no match was found.
const reco::SuperCluster * LeptonAnalysis::findCaloMatch(const PseudoLepton & lepton,
    const edm::Handle< std::vector<reco::SuperCluster> > & barrelSuperClusters,
    const edm::Handle< std::vector<reco::SuperCluster> > & endcapSuperClusters,
    double &min_deltaR, double &min_deltaEta, double &min_deltaPhi )
{

  //
  // NEW METHOD
  //

  double deltaRcut = 0.2;
  min_deltaR=9999.;
  min_deltaPhi=9999.;
  min_deltaEta=9999.;
  const reco::SuperCluster * matchingSC = 0;

  // Get transient track for this lepton
  reco::TransientTrack tTrack = leptonTrack( lepton );

  // Loop over EB SCs
  std::vector<reco::SuperCluster>::const_iterator iclus = barrelSuperClusters->begin();
  for ( ; iclus != barrelSuperClusters->end(); iclus++) {


    // Point on SC surface
    GlobalPoint scPoint( iclus->x(), iclus->y(), iclus->z() );

    // Calculate deltaR between SC and track extrapolated to ECAL surface
    double dEta = 9999.;
    double dPhi = 9999.;
    double dR = extrapolateAndDeltaR( tTrack, scPoint, dEta, dPhi );

    if (dR<min_deltaR) {
      min_deltaR=dR;
      min_deltaPhi=dPhi;
      min_deltaEta=dEta;
      matchingSC = &(*iclus);
    }
  }

  // Similarly for EE SCs
  iclus = endcapSuperClusters->begin();
  for ( ; iclus != endcapSuperClusters->end(); iclus++) {

    GlobalPoint scPoint( iclus->x(), iclus->y(), iclus->z() );

    double dEta = 9999.;
    double dPhi = 9999.;
    double dR = extrapolateAndDeltaR( tTrack, scPoint, dEta, dPhi );

    if (dR<min_deltaR) {
      min_deltaR=dR;
      min_deltaPhi=dPhi;
      min_deltaEta=dEta;
      matchingSC = &(*iclus);
    }
  }

  bool caloMatch = (min_deltaR<deltaRcut);
  if( caloMatch ) return matchingSC;

  return 0;
}

// Given a PseudoLepton and the reco pat photons returns a pointer to a matching photon or a null pointer if no match was found.
const pat::Photon * LeptonAnalysis::findPhotonMatch(const PseudoLepton & lepton,
    const edm::Handle< std::vector<pat::Photon> > & photons,
    double &min_deltaR )
{
  double deltaRcut = 0.2;
  min_deltaR=9999.;

  // Pointer to the matched photon
  const pat::Photon * matchingPhoton = 0;

  // Get transient track for this lepton
  reco::TransientTrack tTrack = leptonTrack( lepton );

  // Loop over pat photons
  std::vector<pat::Photon>::const_iterator iphoton = photons->begin();
  for ( ; iphoton != photons->end(); iphoton++) {

    // Point on ECAL surface
    GlobalPoint photonPoint( iphoton->caloPosition().x(), iphoton->caloPosition().y(), iphoton->caloPosition().z() );

    // Calculate deltaR between SC and track extrapolated to ECAL surface
    double dEta = 9999.;
    double dPhi = 9999.;
    double dR = extrapolateAndDeltaR( tTrack, photonPoint, dEta, dPhi );

    if (dR<min_deltaR) {
      min_deltaR=dR;
      matchingPhoton = &(*iphoton);
    }
  }

  bool caloMatch = (min_deltaR<deltaRcut);
  if( caloMatch ) return matchingPhoton;

  return 0;
}


// Extrapolate track to surface given by SC and return delta R between two points
const double LeptonAnalysis::extrapolateAndDeltaR( const reco::TransientTrack & tTrack,
						   const GlobalPoint & point, double &deltaEta, double &dPhi )
{

  // Extrapolate track to surface of a point
  TrajectoryStateOnSurface trajOnSurface = tTrack.stateOnSurface( point );

  if ( !trajOnSurface.isValid() ) return 9999;

  GlobalPoint trackPositionAtSurface = trajOnSurface.globalPosition();

  // Calculate deltaEta and deltaPhi
  deltaEta=point.eta()-trackPositionAtSurface.eta();
  dPhi=deltaPhi( point.phi(), trackPositionAtSurface.phi() );

  // Return deltaR between two points
  return deltaR( point, trackPositionAtSurface  );
}

/// Check if the triggers selected via cfg are firing for this event.
bool LeptonAnalysis::doTrigger(const edm::Event& iEvent)
{
  // PAT trigger information
  edm::Handle< pat::TriggerEvent > triggerEvent;
  iEvent.getByLabel( triggerEvent_, triggerEvent );
  if (triggerEvent.failedToGet()) {
    std::cout << "WARNING: no TriggerEvent found" << std::endl;
    return false;
  }

  bool takeAllPaths = (hltPaths_.size() == 1 && hltPaths_[0] == "*");
  // now loop over all paths etc and fill histogram for each one that was found
  triggers_.clear();
  for (unsigned i=0; i<triggerEvent->acceptedPaths().size(); i++) {
    std::string trigname(triggerEvent->acceptedPaths()[i]->name());
    ++trigPathSummary_[trigname];
    for (unsigned itrg=0; itrg<hltPaths_.size(); itrg++) {
      if ( hltPaths_[itrg]=="*" ) takeAllPaths=true;
      if( takeAllPaths || trigname==hltPaths_[itrg] ) {
        // FIXME: might want to select a reduced number of triggers to save space in the tree.
        triggers_.push_back(trigname);
      }
    }
  }
  return (triggers_.size()>0);
}


FreeTrajectoryState LeptonAnalysis::getGenParticleStateClosestToBeamline( const edm::EventSetup& iSetup,
                                                                          const  reco::GenParticle & part ) {
  FreeTrajectoryState fts(GlobalPoint(part.vx(),part.vy(),part.vz()),
			  GlobalVector(part.px(),part.py(),part.pz()),
			  part.charge(),
			  0); //theMagField.product());
  FreeTrajectoryState ftsPCA(steppingHelixPropAny_->propagate(fts, beamSpot_));
  return ftsPCA;
}

/// Compute the sumPt in a cone. This is absolute isolation.
double LeptonAnalysis::trackerIsolation(const edm::Event& iEvent,
    const reco::Track & plept,
    const reco::Track & pveto,
    const double innerCone )
{
  // FIXME: move to relative isolation
  // FIXME: move the Handle outside and pass it as an argument

  // get PseudoLepton collection. these are high quality tracks
  // and standalone muons. we will only use the tracks for isolation, not muons.
  edm::Handle< PseudoLeptonCollection > trackCollection;
  iEvent.getByLabel( leptonCollTag_[__lepTypeTrack], trackCollection );
  if (trackCollection.failedToGet()) {
    std::cout << "WARNING: PseudoLepton collection not found" << std::endl;
    return -1;
  }

  // loop over all tracks and get deltaR with respect to both leptons
  double sumPt=0;
  for (PseudoLeptonCollection::const_iterator trk=trackCollection->begin();
      trk!=trackCollection->end(); trk++) {
    if (trk->isStandAloneMuon()) continue;
    double deltaRlept=deltaR(plept.eta(),plept.phi(),trk->eta(),trk->phi());
    double deltaRveto=deltaR(pveto.eta(),pveto.phi(),trk->eta(),trk->phi());
    if (deltaRlept<0.3 && deltaRlept>innerCone && deltaRveto>0.03) {
      // inside isolation code, but not close enough to any of the two tracks to suspect
      // that this might actually be one of the two tracks
      sumPt+=trk->pt();
    }
  }
  return sumPt;
}

// Refit primary vertex without two leptons in candidate
reco::Vertex LeptonAnalysis::refitPrimaryVertex( const reco::TransientTrack & leptonH, const reco::TransientTrack & leptonL ) {

  // get the tracks from the vertex and build a new tracklist
  std::vector<reco::TransientTrack> mytracks;
  for ( reco::Vertex::trackRef_iterator tv=primaryVertex_.tracks_begin(); tv!=primaryVertex_.tracks_end(); tv++){
    const reco::Track & recoTrack=*(tv->get());

    if ( recoTrack.pt() == leptonH.track().pt() || recoTrack.pt() == leptonL.track().pt() ) continue;

    reco::TransientTrack ttrack=trackBuilder_->build(recoTrack);
    ttrack.setBeamSpot(beamSpot_);
    mytracks.push_back(ttrack);
  }

  // Do new fit
  AdaptiveVertexFitter* fitter = new AdaptiveVertexFitter();
  TransientVertex myVertex = fitter->vertex(mytracks,beamSpot_);
  return myVertex;
}

/// Convert to a transient track and assign the beamspot.
reco::TransientTrack LeptonAnalysis::leptonTrack(const PseudoLepton &track)
{
  reco::TransientTrack ttrack=trackBuilder_->build(track);
  ttrack.setBeamSpot(beamSpot_);
  return ttrack;
}

/// Convert to a transient track and assign the beamspot.
reco::TransientTrack LeptonAnalysis::leptonTrack(const pat::Electron &electron)
{
  if (!electron.gsfTrack().isNull()) {
    reco::TransientTrack ttrack=trackBuilder_->build(electron.gsfTrack());
    ttrack.setBeamSpot(beamSpot_);
    return ttrack;
  }
  // FIXME
  return reco::TransientTrack();
}

/// Convert to a transient track and assign the beamspot. Take innerTrack if available or outerTrack otherwise.
reco::TransientTrack LeptonAnalysis::leptonTrack(const pat::Muon &muon)
{
  if (!muon.innerTrack().isNull()) {
    reco::TransientTrack ttrack=trackBuilder_->build(muon.innerTrack());
    ttrack.setBeamSpot(beamSpot_);
    return ttrack;
  } else if (!muon.outerTrack().isNull()) {
    reco::TransientTrack ttrack=trackBuilder_->build(muon.outerTrack());
    ttrack.setBeamSpot(beamSpot_);
    return ttrack;
  }
  // FIXME
  return reco::TransientTrack();
}

/// Convert to a transient track and assign the beamspot.
reco::TransientTrack LeptonAnalysis::leptonTrack(const pat::Tau &tau)
{
  if (!tau.leadTrack().isNull()) {
    reco::TransientTrack ttrack=trackBuilder_->build(tau.leadTrack());
    ttrack.setBeamSpot(beamSpot_);
    return ttrack;
  }
  // FIXME
  return reco::TransientTrack();
}

// correct the impact parameter for a given track by a given deltaD0 and dz.
// the last boolean controls whether the IP is computed relative to the beamspot (false)
// or relative to the primary vertex (true).
reco::Track LeptonAnalysis::correctImpactParameter(const reco::Track &track, const float deltaD0,
						   const float deltaDZ, const bool usePV) {
  math::XYZPoint vtx;
  if (usePV)
    vtx = math::XYZPoint(primaryVertex_.x(), primaryVertex_.y(), primaryVertex_.z());
  else
    vtx = math::XYZPoint(beamSpot_.position(track.vz()));

  // Warning -- we use d0 which has the opposite sign of dxy (reco::Track also has a d0 method
  // but it only supports d0 to origin, not to a vertex), so be careful about signs here.
  double d0 = -track.dxy(vtx);
  double dz = track.dz(vtx);

  // express all distances relative to primary vertex/beamspot
  double vx = track.vx() - vtx.x();
  double vy = track.vy() - vtx.y();

  double vt = hypot(vx, vy);
  
  double d0new = d0 + deltaD0;

  // all distances are still relative to PV/beamspot; final conversion is in the creation below
  double vtnew = vt * d0new / d0;
  double vxnew = vtnew * (vx/vt);
  double vynew = vtnew * (vy/vt);
  double vznew = dz + deltaDZ + (track.pz()/track.pt()) * (vxnew*track.px() + vynew*track.py())/track.pt();

  reco::Track newTrack(track.chi2(),
		       track.ndof(),
		       math::XYZPoint(vxnew + vtx.x(), vynew + vtx.y(), vznew + vtx.z()),
		       track.momentum(),
		       track.charge(),
		       track.covariance(),
		       track.algo(),
		       (reco::TrackBase::TrackQuality)track.qualityMask());
  // copy hit pattern to new track as well
  newTrack.setHitPattern(track.hitPattern());
  newTrack.setTrackerExpectedHitsInner(track.trackerExpectedHitsInner());
  newTrack.setTrackerExpectedHitsOuter(track.trackerExpectedHitsOuter());

  return newTrack;
}

reco::TransientTrack LeptonAnalysis::CorrectTransientTrack(const reco::Track &track,
                           const float deltaD0, const float deltaDZ, const bool usePV)
{
  reco::Track newTrack = correctImpactParameter(track, deltaD0, deltaDZ, usePV);
  reco::TransientTrack tTrackCorrected = trackBuilder_->build(newTrack);
  return tTrackCorrected;
}

reco::TransientTrack LeptonAnalysis::CorrectTransientTrack(const reco::TransientTrack &tTrack,
                           const float deltaD0, const float deltaDZ, const bool usePV)
{
  reco::TransientTrack tTrackCorrected = CorrectTransientTrack(tTrack.track(), deltaD0, deltaDZ, usePV);
  return tTrackCorrected;
}

/// Default method, returns -999
double LeptonAnalysis::leptonTiming(const PseudoLepton &track)
{
  return -999;
}

/// Not implemented, returns -999
double LeptonAnalysis::leptonTiming(const pat::Electron &electron)
{
  //DetId seedDetID = electron->superCluster()->seed()->seed();
  return -999;
}

/// Muon timing. Assumes muon coming from inside the detector and has beta == 1
double LeptonAnalysis::leptonTiming(const pat::Muon &muon)
{
  if (muon.isTimeValid()) {
    // use time under the assumption the muon came from inside of the detector
    // and had beta==1.
    return muon.time().timeAtIpInOut;
  } else {
    return -999;
  }
}

/// Not implemented, returns -999
double LeptonAnalysis::leptonTiming(const pat::Tau &tau)
{
  // not implemented
  return -999;
}

void LeptonAnalysis::fillDipseudoleptonCandidates(const edm::Event& iEvent, const edm::EventSetup& iSetup,
						  const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles)
{
  // Find candidates
  // ---------------
  // first loop over the saved leptons
  for (unsigned ipart1=0; ipart1<candidates_.leptons_.size(); ++ipart1) {
    if( !candidates_.leptons_[ipart1].validTrack ) continue;
    if( !candidates_.leptons_[ipart1].isStandAloneMuon && !candidates_.leptons_[ipart1].isCentralTrack ) continue;
    // second loop over saved leptons
    for (unsigned ipart2=ipart1+1; ipart2<candidates_.leptons_.size(); ++ipart2) {
      TreeLepton highPtLepton = candidates_.leptons_[ipart1];
      TreeLepton lowPtLepton = candidates_.leptons_[ipart2];

      if( !lowPtLepton.validTrack ) continue;
      if( !lowPtLepton.isStandAloneMuon && !lowPtLepton.isCentralTrack ) continue;
      if( !(lowPtLepton.isStandAloneMuon && highPtLepton.isStandAloneMuon) && !(lowPtLepton.isCentralTrack && highPtLepton.isCentralTrack) ) continue;

      // Work out which is high/low pt lepton
      if (highPtLepton.pt<lowPtLepton.pt) {
        highPtLepton=candidates_.leptons_[ipart2];
        lowPtLepton=candidates_.leptons_[ipart1];
      }

      // For this use the same (higher) cut for all leptons
      if ( lowPtLepton.pt < leptonPtCut_ ) continue;

      // Make a candidate and fill info on this candidates
      candidates_.candidates_.push_back(TreeDipseudoLeptonCandidate());
      TreeDipseudoLeptonCandidate & candidate = candidates_.candidates_.back();
      fillCandidateInfo( candidate, highPtLepton, lowPtLepton, iEvent, iSetup, false, particles );
    }
  }

  // Loop on the candidates and find matches between RSA and track-based candidates
  findCandidateMatches( iEvent, iSetup, theMagField, particles );
}


const TreeLepton LeptonAnalysis::getLepton( unsigned int index )
{
  // Loop over TreeLeptons
  for (  unsigned int i = 0; i < candidates_.leptons_.size(); i++) {
    if ( candidates_.leptons_[i].index >=0 ) {
      if ( index == abs( candidates_.leptons_[i].index ) ) return candidates_.leptons_[i];
    }
  }
  // cout << "WARNING : Could not find this lepton in TreeLepton Candidate" << endl;
  return TreeLepton();
}


void LeptonAnalysis::findCandidateMatches( const edm::Event& iEvent, const edm::EventSetup& iSetup,
					   const edm::ESHandle<MagneticField> & theMagField, const edm::Handle<edm::View<PseudoLepton> > & particles )
{
  for( std::vector<TreeDipseudoLeptonCandidate>::iterator rsaCand = candidates_.candidates_.begin(); rsaCand != candidates_.candidates_.end(); ++rsaCand ) {

    TreeLepton rsaL = getLepton( rsaCand->leptonIndexL );
    TreeLepton rsaH = getLepton( rsaCand->leptonIndexH );
    if( !rsaL.isStandAloneMuon || !rsaH.isStandAloneMuon ) continue;
    PseudoLepton lowPtRSA = particles->at(rsaL.pseudoLeptonIndex);
    PseudoLepton highPtRSA = particles->at(rsaH.pseudoLeptonIndex);
    GlobalPoint positionL( lowPtRSA.innerPosition().x(), lowPtRSA.innerPosition().y(), lowPtRSA.innerPosition().z() );
    GlobalPoint positionH( highPtRSA.innerPosition().x(), highPtRSA.innerPosition().y(), highPtRSA.innerPosition().z() );

    int candIndex = 0;
    int minDRIndex = -999;
    float minDR = 10000.;
    for( std::vector<TreeDipseudoLeptonCandidate>::const_iterator tkCand = candidates_.candidates_.begin(); tkCand != candidates_.candidates_.end(); ++tkCand, ++candIndex ) {
      TreeLepton tkL = getLepton( tkCand->leptonIndexL );
      TreeLepton tkH = getLepton( tkCand->leptonIndexH );
      if( !tkL.isCentralTrack || !tkH.isCentralTrack ) continue;
      PseudoLepton lowPtTK = particles->at(tkL.pseudoLeptonIndex);
      PseudoLepton highPtTK = particles->at(tkH.pseudoLeptonIndex);
     
      // To avoid NaN stuff...
      float newDR;
      float a1 = extrapolateToMuon(lowPtTK, lowPtRSA, positionL, theMagField);
      float a2 = extrapolateToMuon(lowPtTK, highPtRSA, positionH, theMagField);
      float b1 = extrapolateToMuon(highPtTK, lowPtRSA, positionL, theMagField);
      float b2 = extrapolateToMuon(highPtTK, highPtRSA, positionH, theMagField);
      if ( a1 ==a1 && a2==a2 && b1==b1 && b2==b2 ) newDR = std::min(std::min(a1,a2), std::min(b1,b2));
      else {
        if ( a1!=a1 ) a1= 100000.0;
        if ( a2!=a2 ) a2= 10000.0;
        if ( b1!=b1 ) b1= 1000.0;
        if ( b2!=b2 ) b2= 100.0;
        newDR = std::min(std::min(a1,a2), std::min(b1,b2));
      }

      if( newDR < minDR ) {
	minDR = newDR;
	minDRIndex = candIndex;
      }
    }
    rsaCand->tkMatches.push_back(std::make_pair(minDRIndex, minDR));
  }
}


float LeptonAnalysis::extrapolateToMuon(const PseudoLepton & tk, const PseudoLepton & rsa,
					const GlobalPoint & position, const edm::ESHandle<MagneticField> & theMagField)
{
  FreeTrajectoryState fts(GlobalPoint(tk.vx(), tk.vy(), tk.vz()),
			  GlobalVector(tk.px(), tk.py(), tk.pz()),
			  tk.charge(),
			  0);//theMagField.product());
  FreeTrajectoryState ftsPCA(steppingHelixPropAlong_->propagate(fts, position));
  return deltaR(ftsPCA.momentum().eta(), ftsPCA.momentum().phi(), rsa.innerMomentum().eta(), rsa.innerMomentum().phi());
}


void LeptonAnalysis::fillCandidateInfo( TreeDipseudoLeptonCandidate & candidate, const TreeLepton & highPtLepton, const TreeLepton & lowPtLepton,
                                        const edm::Event& iEvent, const edm::EventSetup& iSetup, bool correctTipLip,
					const edm::Handle<edm::View<PseudoLepton> > & particles )
{
  double leptonMass=0.;
  // For electrons
  if (leptonName_=="etrack" || leptonName_=="electron") leptonMass=0.000511;
  // For muons
  if (leptonName_=="mutrack" || leptonName_=="muon") leptonMass=0.106;

  PseudoLepton highPtPseudoLepton = particles->at(highPtLepton.pseudoLeptonIndex);
  PseudoLepton lowPtPseudoLepton = particles->at(lowPtLepton.pseudoLeptonIndex);

  // Lepton index
  candidate.leptonIndexL = lowPtLepton.index;
  candidate.leptonIndexH = highPtLepton.index;

  // Different TO
  candidate.differentTO = ( lowPtLepton.triggerObjectIndex == highPtLepton.triggerObjectIndex ) ? 0 : 1;


  // Get original transient tracks
  reco::TransientTrack tTrackHighPtLepton = leptonTrack(highPtPseudoLepton);
  reco::TransientTrack tTrackLowPtLepton = leptonTrack(lowPtPseudoLepton);

  bool validTracks = (tTrackLowPtLepton.isValid() && tTrackHighPtLepton.isValid());
  if( !validTracks ) return;

  // Gather transient tracks
  std::vector<reco::TransientTrack> fitTracks;
  fitTracks.push_back(tTrackLowPtLepton);
  fitTracks.push_back(tTrackHighPtLepton);

  // Lepton isolation taking account of other lepton in candidate
  candidate.leptonIsoL = trackerIsolation(iEvent,tTrackLowPtLepton.track(),tTrackHighPtLepton.track());
  candidate.leptonIsoH = trackerIsolation(iEvent,tTrackHighPtLepton.track(),tTrackLowPtLepton.track());
  candidate.leptonIsoL4 = trackerIsolation(iEvent,tTrackLowPtLepton.track(),tTrackHighPtLepton.track(), 0.04);
  candidate.leptonIsoH4 = trackerIsolation(iEvent,tTrackHighPtLepton.track(),tTrackLowPtLepton.track(), 0.04);
  candidate.leptonIsoL5 = trackerIsolation(iEvent,tTrackLowPtLepton.track(),tTrackHighPtLepton.track(), 0.05);
  candidate.leptonIsoH5 = trackerIsolation(iEvent,tTrackHighPtLepton.track(),tTrackLowPtLepton.track(), 0.05);

  // ---------- //
  // Vertex fit //
  // ---------- //

  // Perform vertex fit if tracks are valid
  if (validTracks) {

    TransientVertex leptonVertex;
    try {
      leptonVertex = vertexFitter_->vertex(fitTracks);
      candidate.validVertex=leptonVertex.isValid();
    } catch(cms::Exception& e) {};

    // Original tracks p4
    ROOT::Math::PxPyPzMVector trackMomLowPt(tTrackLowPtLepton.track().px(),tTrackLowPtLepton.track().py(),
        tTrackLowPtLepton.track().pz(),leptonMass);
    ROOT::Math::PxPyPzMVector trackMomHighPt(tTrackHighPtLepton.track().px(),tTrackHighPtLepton.track().py(),
        tTrackHighPtLepton.track().pz(),leptonMass);
    ROOT::Math::PxPyPzMVector diLeptonMom = trackMomLowPt+trackMomHighPt;

    candidate.mass = (trackMomLowPt+trackMomHighPt).mass();

    // Refit primary vertex without these two leptons
    reco::Vertex refittedPV = refitPrimaryVertex( tTrackHighPtLepton, tTrackLowPtLepton );
    candidate.pvRefit_x = refittedPV.x();
    candidate.pvRefit_y = refittedPV.y();
    candidate.pvRefit_z = refittedPV.z();
    candidate.pvRefit_xError = refittedPV.xError();
    candidate.pvRefit_yError = refittedPV.yError();
    candidate.pvRefit_zError = refittedPV.zError();
    candidate.pvRefit_nTracks = refittedPV.nTracks();
    candidate.pvRefit_chi2 = refittedPV.chi2();
    candidate.pvRefit_ndof = refittedPV.ndof();

    // Save if vertex is valid
    if (leptonVertex.isValid()) {
      candidate.validVertex=1;

      // Vertex Chi^2
      candidate.vertexChi2 = leptonVertex.normalisedChiSquared();

      // Get refitted lepton tracks
      reco::TransientTrack refittedTrackLowPt(leptonVertex.refittedTrack(tTrackLowPtLepton));
      reco::TransientTrack refittedTrackHighPt(leptonVertex.refittedTrack(tTrackHighPtLepton));

      // Refitted lepton track quantites
      candidate.leptonPtL = refittedTrackLowPt.track().pt();
      candidate.leptonPtH = refittedTrackHighPt.track().pt();
      candidate.leptonEtaL = refittedTrackLowPt.track().eta();
      candidate.leptonEtaH = refittedTrackHighPt.track().eta();
      candidate.leptonChargeL = refittedTrackLowPt.track().charge();
      candidate.leptonChargeH = refittedTrackHighPt.track().charge();

      ROOT::Math::PxPyPzMVector caloCorrectedMom(0,0,0,0);
      // calculate p_t corrected invariant mass
      ROOT::Math::PxPyPzMVector totalMom(0,0,0,0);

      // Refitted tracks p4
      ROOT::Math::PxPyPzMVector refittedTrackMomLowPt(refittedTrackLowPt.track().px(),refittedTrackLowPt.track().py(),
          refittedTrackLowPt.track().pz(),leptonMass);
      ROOT::Math::PxPyPzMVector refittedTrackMomHighPt(refittedTrackHighPt.track().px(),refittedTrackHighPt.track().py(),
          refittedTrackHighPt.track().pz(),leptonMass);

      // Refitted momentum
      totalMom = refittedTrackMomLowPt + refittedTrackMomHighPt;
      // Calo corrected momentum
      if( lowPtLepton.hasCaloMatch != 0 ) caloCorrectedMom +=
          (lowPtLepton.photonEnergy/refittedTrackLowPt.track().p())*(refittedTrackMomLowPt);
      else caloCorrectedMom += refittedTrackMomLowPt;
      if( highPtLepton.hasCaloMatch != 0 ) caloCorrectedMom +=
          (highPtLepton.photonEnergy/refittedTrackHighPt.track().p())*(refittedTrackMomHighPt);
      else caloCorrectedMom += refittedTrackMomHighPt;

      candidate.corrDileptonMass = totalMom.M();
      candidate.caloCorrMass = caloCorrectedMom.M();

      // decay length and significance
      // FIXME: this could be not very appropriate for standAloneMuons with big displacements (>~ 1 m).
      VertexDistanceXY vertTool;
      // wrt PV
      Measurement1D vertexDist = vertTool.distance(leptonVertex.vertexState(),primaryVertexState_);
      candidate.decayLength_PV = vertexDist.value();
      candidate.decayLengthSignificance_PV = vertexDist.significance();

      // wrt Beamline
      VertexState beamSpotState(beamSpot_);
      vertexDist = vertTool.distance(leptonVertex.vertexState(),beamSpotState);
      candidate.decayLength_BS = vertexDist.value();
      candidate.decayLengthSignificance_BS = vertexDist.significance();

      // vertex flight direction vs dilepton momentum direction
      GlobalVector vertexDir = leptonVertex.position() - primaryVertexState_.position();
      candidate.dPhi= fabs(deltaPhi<GlobalVector, ROOT::Math::PxPyPzMVector>(vertexDir, diLeptonMom));
      candidate.dPhiCaloCorr = fabs(deltaPhi<GlobalVector, ROOT::Math::PxPyPzMVector>(vertexDir, caloCorrectedMom));
      candidate.dPhiCorr = fabs(deltaPhi<GlobalVector, ROOT::Math::PxPyPzMVector>(vertexDir, totalMom));
      candidate.dPhiCorrSigned = deltaPhi<GlobalVector, ROOT::Math::PxPyPzMVector>(vertexDir, totalMom);

      // Candidate poistion
      candidate.vx = leptonVertex.position().x();
      candidate.vy = leptonVertex.position().y();
      candidate.vz = leptonVertex.position().z();

      candidate.ptCorr = totalMom.pt();
      candidate.etaCorr = totalMom.eta();
      candidate.phiCorr = totalMom.phi();
      candidate.ptCaloCorr = caloCorrectedMom.pt();
      candidate.etaCaloCorr = caloCorrectedMom.eta();
      candidate.phiCaloCorr = caloCorrectedMom.phi();

      // Transverse mass calculation
      // For 3 body final states
      TLorentzVector p4SumReco( diLeptonMom.px(), diLeptonMom.py(), diLeptonMom.pz(), diLeptonMom.E() );
      TVector3 p3Exotic( vertexDir.x(), vertexDir.y(), vertexDir.z() );
      // This is the Pt of the dilepton w.r.t flight direction and hence also equal to Pt of neutrino
      float PtRelExoticDir = p4SumReco.Perp( p3Exotic );
      // Transverse energy of a particle is defined as sqrt(mass squared + pt squared)
      float sumEtRelExoticDir = sqrt(pow(p4SumReco.M(),2) + pow(PtRelExoticDir,2)) + PtRelExoticDir;
      float sumPt = 0.0; // Since dilepton and neutrino have opposite Pt relative to flight direction.
      // Transverse mass of particle pair is defined as sqrt(transverse energy squared - pt squared)
      float Mt = sqrt(pow(sumEtRelExoticDir, 2) - pow(sumPt, 2));
      candidate.transverseMass = Mt;

      int hitsBeforeVertex[2];
      int missedLayersAfterVertex[2];

      // Check hit pattern
      // This will not produce anything for vertices involving stand alone muons
      if ( !(lowPtLepton.isStandAloneMuon || highPtLepton.isStandAloneMuon) ) {
        for (unsigned i=0; i<fitTracks.size(); i++) {
          CheckHitPattern::Result hitPat = checkHitPattern_.analyze(iSetup,fitTracks[i].track(),leptonVertex.vertexState(),true);
          hitsBeforeVertex[i] = int(hitPat.hitsInFrontOfVert);
          missedLayersAfterVertex[i] = int(hitPat.missHitsAfterVert);
        }

        candidate.hitsBeforeVertexL = hitsBeforeVertex[0];
        candidate.hitsBeforeVertexH = hitsBeforeVertex[1];
        candidate.missedLayersAfterVertexL = missedLayersAfterVertex[0];
        candidate.missedLayersAfterVertexH = missedLayersAfterVertex[1];
      }

      try {
        candidate.leptonD0L_BS = refittedTrackLowPt.stateAtBeamLine().transverseImpactParameter().value();
        candidate.leptonD0SignificanceL_BS = refittedTrackLowPt.stateAtBeamLine().transverseImpactParameter().significance();
        candidate.leptonD0H_BS = refittedTrackHighPt.stateAtBeamLine().transverseImpactParameter().value();
        candidate.leptonD0SignificanceH_BS = refittedTrackHighPt.stateAtBeamLine().transverseImpactParameter().significance();
      } catch (cms::Exception& e) {
        candidate.leptonD0L_BS = -9999;
        candidate.leptonD0SignificanceL_BS = -9999;
        candidate.leptonD0H_BS = -9999;
        candidate.leptonD0SignificanceH_BS = -9999;
      };

      // Dilepton momentum vector
      GlobalVector dileptonDir( totalMom.px(), totalMom.py(), totalMom.pz() );

      // Vector perpendicular to dilepton momentum
      GlobalVector perpDileptonDir( dileptonDir.cross( GlobalVector( 0,0,1) ) );

      // Also get signed impact parameter of tracks
      // This is for unrefitted tracks
      // wrt PV including error on PV
      // sign is with respect to dilepton momentum vector

      GlobalVector refittedVertexDir = leptonVertex.position() - GlobalPoint(refittedPV.position().x(),refittedPV.position().y(),refittedPV.position().z());
      // Low pt lepton
      try {
        // Signed wrt dilepton momentum
        // Before refit of PV
        candidate.leptonD0L_PV = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dileptonDir, primaryVertex_).second.value();
        candidate.leptonD0SignificanceL_PV_includingPVError =
            candidate.leptonD0L_PV/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dileptonDir, primaryVertex_).second.error();

        // Signed wrt dilepton momentum
        // After refit of PV
        candidate.leptonD0L_PVrefit = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dileptonDir, refittedPV).second.value();
        candidate.leptonD0SignificanceL_PVrefit_includingPVError =
            candidate.leptonD0L_PVrefit/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dileptonDir, refittedPV).second.error();

        // Signed wrt vector perpendicular to dilepton momentum
        // For misalignment studies
        candidate.leptonD0L_PVrefit_sigWrtPerpDilepton = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, perpDileptonDir, refittedPV).second.value();
        candidate.leptonD0SignificanceL_PVrefit_sigWrtPerpDilepton_includingPVError =
            candidate.leptonD0L_PVrefit_sigWrtPerpDilepton/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, perpDileptonDir, refittedPV).second.error();

        // Signed wrt X direction taken from vector between PV and DV
        candidate.leptonD0L_PVrefit_signWrtX = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, refittedVertexDir, refittedPV).second.value();
        candidate.leptonD0SignificanceL_PVrefit_signWrtX_includingPVError =
            candidate.leptonD0L_PVrefit_signWrtX/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, refittedVertexDir, refittedPV).second.error();

        // Sign wrt vector perpendicular to lepton momentum (and z-axis)
        GlobalVector leptonMom(tTrackLowPtLepton.track().px(),tTrackLowPtLepton.track().py(),tTrackLowPtLepton.track().pz());
        // Get vector perpendicular to lepton mom and z-axis
        GlobalVector dirVector( leptonMom.cross( GlobalVector(0,0,1)) );
        candidate.leptonD0L_PVrefit_signWrtPerp = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dirVector, refittedPV).second.value();
        candidate.leptonD0SignificanceL_PVrefit_includingPVError_signWrtPerp =
            candidate.leptonD0L_PVrefit_signWrtPerp/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dirVector, refittedPV).second.error();

        // Store angle between dirVector and dilepton momentum vector
        // Can then apply d0 corrections later
        candidate.momPhi = dileptonDir.phi();
        candidate.dirPhiL = dirVector.phi();
        candidate.deltaPhiL = deltaPhi( dileptonDir.phi(), dirVector.phi() );

        // Z0 after PV refit
        candidate.leptonZ0L_PVRefit=tTrackLowPtLepton.trajectoryStateClosestToPoint(
              GlobalPoint(refittedPV.x(),refittedPV.y(),refittedPV.z())).perigeeParameters().longitudinalImpactParameter();

      } catch (cms::Exception& e) {
        candidate.leptonD0L_PV = -9999;
        candidate.leptonD0SignificanceL_PV_includingPVError = -99999;
        candidate.leptonD0L_PVrefit = -9999;
        candidate.leptonD0SignificanceL_PVrefit_includingPVError = -9999;
        candidate.leptonD0L_PVrefit_signWrtX = -9999;
        candidate.leptonD0SignificanceL_PVrefit_signWrtX_includingPVError = -9999;
        candidate.leptonD0L_PVrefit_signWrtPerp = -9999;
        candidate.leptonD0SignificanceL_PVrefit_includingPVError_signWrtPerp = -9999;
        candidate.dirPhiL = -99;
        candidate.deltaPhiL = -99;
      }

      // High pt lepton
      try {
        // Signed wrt dilepton momentum
        // Before refit of PV
        candidate.leptonD0H_PV = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dileptonDir, primaryVertex_).second.value();
        candidate.leptonD0SignificanceH_PV_includingPVError =
            candidate.leptonD0H_PV/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dileptonDir, primaryVertex_).second.error();

        // Signed wrt dilepton momentum
        // After refit of PV
        candidate.leptonD0H_PVrefit = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dileptonDir, refittedPV).second.value();
        candidate.leptonD0SignificanceH_PVrefit_includingPVError =
            candidate.leptonD0H_PVrefit/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dileptonDir, refittedPV).second.error();

        // Signed wrt vector perpendicular to dilepton momentum
        // For misalignment studies
        candidate.leptonD0H_PVrefit_sigWrtPerpDilepton = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, perpDileptonDir, refittedPV).second.value();
        candidate.leptonD0SignificanceH_PVrefit_sigWrtPerpDilepton_includingPVError =
            candidate.leptonD0H_PVrefit_sigWrtPerpDilepton/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, perpDileptonDir, refittedPV).second.error();

        // Signed wrt X direction taken from vector between PV and DV
        candidate.leptonD0H_PVrefit_signWrtX = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, refittedVertexDir, refittedPV).second.value();
        candidate.leptonD0SignificanceH_PVrefit_signWrtX_includingPVError =
            candidate.leptonD0H_PVrefit_signWrtX/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, refittedVertexDir, refittedPV).second.error();

        // Sign wrt vector perpendicular to lepton momentum (and z-axis)
        GlobalVector leptonMom(tTrackHighPtLepton.track().px(),tTrackHighPtLepton.track().py(),tTrackHighPtLepton.track().pz());
        // Get vector perpendicular to lepton mom and z-axis
        GlobalVector dirVector( leptonMom.cross( GlobalVector(0,0,1)) );
        candidate.leptonD0H_PVrefit_signWrtPerp = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dirVector, refittedPV).second.value();
        candidate.leptonD0SignificanceH_PVrefit_includingPVError_signWrtPerp =
            candidate.leptonD0H_PVrefit_signWrtPerp/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dirVector, refittedPV).second.error();

        // Store angle between dirVector and dilepton momentum vector
        // Can then apply d0 corrections later
        candidate.momPhi = dileptonDir.phi();
        candidate.dirPhiH = dirVector.phi();
        candidate.deltaPhiH = deltaPhi( dileptonDir.phi(), dirVector.phi() );

        // Z0 after PV refit
        candidate.leptonZ0H_PVRefit=tTrackHighPtLepton.trajectoryStateClosestToPoint(
              GlobalPoint(refittedPV.x(),refittedPV.y(),refittedPV.z())).perigeeParameters().longitudinalImpactParameter();

      } catch (cms::Exception& e) {
        candidate.leptonD0H_PV = -9999;
        candidate.leptonD0SignificanceH_PV_includingPVError = -99999;
        candidate.leptonD0H_PVrefit = -9999;
        candidate.leptonD0SignificanceH_PVrefit_includingPVError = -9999;
        candidate.leptonD0H_PVrefit_signWrtX = -9999;
        candidate.leptonD0SignificanceH_PVrefit_signWrtX_includingPVError = -9999;
        candidate.leptonD0H_PVrefit_signWrtPerp = -9999;
        candidate.leptonD0SignificanceH_PVrefit_includingPVError_signWrtPerp = -9999;
        candidate.dirPhiH = -99;
        candidate.deltaPhiH = -99;
      }
    }
    else {
      candidate.validVertex = 0;

      // Low pt lepton
      try {
        // Sign wrt vector perpendicular to lepton momentum (and z-axis)
        GlobalVector leptonMom(tTrackLowPtLepton.track().px(),tTrackLowPtLepton.track().py(),tTrackLowPtLepton.track().pz());
        // Get vector perpendicular to lepton mom and z-axis
        GlobalVector dirVector( leptonMom.cross( GlobalVector(0,0,1)) );
        candidate.leptonD0L_PVrefit_signWrtPerp = IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dirVector, refittedPV).second.value();
        candidate.leptonD0SignificanceL_PVrefit_includingPVError_signWrtPerp =
            candidate.leptonD0L_PVrefit_signWrtPerp/IPTools::signedTransverseImpactParameter(tTrackLowPtLepton, dirVector, refittedPV).second.error();
      } catch (cms::Exception& e) {
        candidate.leptonD0L_PVrefit_signWrtPerp = -9999;
        candidate.leptonD0SignificanceL_PVrefit_includingPVError_signWrtPerp = -9999;
      }

      // High pt lepton
      try {
        // Sign wrt vector perpendicular to lepton momentum (and z-axis)
        GlobalVector leptonMom(tTrackHighPtLepton.track().px(),tTrackHighPtLepton.track().py(),tTrackHighPtLepton.track().pz());
        // Get vector perpendicular to lepton mom and z-axis
        GlobalVector dirVector( leptonMom.cross( GlobalVector(0,0,1)) );
        candidate.leptonD0H_PVrefit_signWrtPerp = IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dirVector, refittedPV).second.value();
        candidate.leptonD0SignificanceH_PVrefit_includingPVError_signWrtPerp =
            candidate.leptonD0H_PVrefit_signWrtPerp/IPTools::signedTransverseImpactParameter(tTrackHighPtLepton, dirVector, refittedPV).second.error();
      } catch (cms::Exception& e) {
        candidate.leptonD0H_PVrefit_signWrtPerp = -9999;
        candidate.leptonD0SignificanceH_PVrefit_includingPVError_signWrtPerp = -9999;
      }

      ROOT::Math::PxPyPzMVector caloCorrectedMom(0,0,0,0);

      // Calo corrected momentum
      if( lowPtLepton.hasCaloMatch != 0 ) caloCorrectedMom +=
          (lowPtLepton.photonEnergy/tTrackLowPtLepton.track().p())*(trackMomLowPt);
      else caloCorrectedMom += trackMomLowPt;
      if( highPtLepton.hasCaloMatch != 0 ) caloCorrectedMom +=
          (highPtLepton.photonEnergy/tTrackHighPtLepton.track().p())*(trackMomHighPt);
      else caloCorrectedMom += trackMomHighPt;

      candidate.caloCorrMass = caloCorrectedMom.M();

      candidate.ptCaloCorr = caloCorrectedMom.pt();
      candidate.etaCaloCorr = caloCorrectedMom.eta();
      candidate.phiCaloCorr = caloCorrectedMom.phi();
    }


    // Angle between leptons
    // Use original unrefitted tracks
    reco::TrackBase::Vector mom1 = tTrackLowPtLepton.track().momentum();
    reco::TrackBase::Vector mom2 = tTrackHighPtLepton.track().momentum();
    candidate.cosine = mom1.Dot(mom2)/mom1.R()/mom2.R();
    candidate.deltaR = deltaR<reco::TrackBase::Vector,reco::TrackBase::Vector>(mom1,mom2);
    // general kinematic information about candidate
    candidate.pt=diLeptonMom.pt();
    candidate.eta=diLeptonMom.eta();
    candidate.phi=diLeptonMom.phi();
  }
}

void LeptonAnalysis::fillDiphotonCandidates(const edm::Event& iEvent)
{

  // Find diphoton candidates
  // -------------------------
  // first loop over the saved photons
  for (unsigned ipart1=0; ipart1<candidates_.photons_.size(); ++ipart1) {

    // second loop over saved leptons
    for (unsigned ipart2=ipart1+1; ipart2<candidates_.photons_.size(); ++ipart2) {

      // Get photons
      // Commented for now so we don't get build warnings
      // Will go away once they actually get used
      //      TreePhoton highPtPhoton = candidates_.photons_[ipart1];
      //      TreePhoton lowPtPhoton = candidates_.photons_[ipart2];

      // Do some vertex finding etc.

      // If you then decide to save this candidate...
      // Make a candidate
      candidates_.diphotonCandidates_.push_back(TreeDiphotonCandidate());
      TreeDiphotonCandidate & candidate = candidates_.diphotonCandidates_.back();

      // Fill with garbage for now
      candidate.mass=148;

      candidate.vertex_x=25;
      candidate.vertex_y=10;
      candidate.vertex_z=4;

      candidate.decayLength=26.9;
    }

  }
}

void LeptonAnalysis::fillDijetCandidates(const edm::Event& iEvent)
{

}

const reco::Candidate* LeptonAnalysis::signalOrigin(const reco::Candidate* part)
{
  const reco::Candidate* cand = part;
  const reco::Candidate* found2 = NULL;
  const reco::Candidate* found3 = NULL;

  // Whilst you still have a candidate but it's not status 3
  while (cand!=0 && !found3) {
    // Does this have the signal pdgid?
    if (find(signalPDGId_.begin(), signalPDGId_.end(), abs(cand->pdgId())) != signalPDGId_.end() ) {
      // Is it status 3?  If not, still found the status 2 particle
      if (cand->status()==3) found3=cand; else found2=cand;
    }
    // Move on to next mother
    cand=cand->mother();
  }

  if (found3) return found3; else return found2;
}

/*bool LeptonAnalysis::inBadRunRange(){

  // CHeck if run has been set in tree for this event
  if ( candidates_.run == -999 ) {
    std::cout << "WARNING : Run number has not been set in tree" << std::endl;
  }

  // Check if run is in bad run range
  if ( candidates_.run >= badRangeMin_ && candidates_.run < badRangeMax_ ) {
    // This is a bad run
    return true;
  }

  return false;
}
*/
void LeptonAnalysis::beginJob()
{
  vertexFitter_ = new KalmanVertexFitter(true);
}

void LeptonAnalysis::endJob() 
{
  // cut flow histograms
  std::string name=leptonName_;

  // print trigger summary information. use a stupid simple sort algorithm
  std::cout << "===========================================================" << std::endl;
  std::cout << "=== TRIGGER SUMMARY =======================================" << std::endl;
  std::cout << "===========================================================" << std::endl;
  unsigned highestRate=numProcessedEvents_;
  while(highestRate>0) {
    unsigned nextLowest=0;
    for (std::map<std::string,unsigned int>::iterator it=trigPathSummary_.begin();
        it!=trigPathSummary_.end(); it++) {
      if (it->second==highestRate) {
        std::cout << "PATH " << std::setw(6) << it->second << "  " << it->first << std::endl;
      } else if (it->second<highestRate && it->second>nextLowest) {
        nextLowest=it->second;
      }
    }
    highestRate=nextLowest;
  }
  std::cout << "===========================================================" << std::endl;
  highestRate=numProcessedEvents_;
  while(highestRate>0) {
    unsigned nextLowest=0;
    for (std::map<std::string,unsigned int>::iterator it=trigFilterSummary_.begin();
        it!=trigFilterSummary_.end(); it++) {
      if (it->second==highestRate) {
        std::cout << "FILTER " << std::setw(6) << it->second << "  " << it->first << std::endl;
      } else if (it->second<highestRate && it->second>nextLowest) {
        nextLowest=it->second;
      }
    }
    highestRate=nextLowest;
  }
  std::cout << "===========================================================" << std::endl;

  hTotalProcessedEvents_->SetBinContent(1, numProcessedEvents_);
  hEventsPassingEventsFilter_->SetBinContent(1, numEventsPassingEventFilters_);
  hEventsPassingTrigger_->SetBinContent(1, numEventsPassingTrigger_);
  hEventsPassingPreFilter_->SetBinContent(1, numEventsPassingPreFilter_ );
  fs_->cd();
  hTotalProcessedEvents_->Write();
  hEventsPassingEventsFilter_->Write();
  hEventsPassingTrigger_->Write();
  hEventsPassingPreFilter_->Write();
}

void LeptonAnalysis::initializeVars()
{
  candidates_.clear();
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(LeptonAnalysis);
