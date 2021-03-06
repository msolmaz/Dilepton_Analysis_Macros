#include "TreeProducer/TreeProducer/interface/PseudoLepton.h"

/// default constructor
PseudoLepton::PseudoLepton() :
  reco::Track(),
  genPartSize_(0),
  isStandAloneMuon_(false),
  isGlobalMuon_(false),
  isTrackerMuon_(false),
  isLooseMuon_(false),
  isCentralTrack_(false)
//   innerPositionX(-999), innerPositionY(-999), innerPositionZ(-999),
//   outerPositionX(-999), outerPositionY(-999), outerPositionZ(-999)
{
}


/// constructor from reco::Track
PseudoLepton::PseudoLepton(const reco::Track & aTrack) :
  reco::Track(aTrack),
  genPartSize_(0),
  isStandAloneMuon_(false),
  isGlobalMuon_(false),
  isTrackerMuon_(false),
  isLooseMuon_(false),
  isCentralTrack_(false)
//   innerPositionX(-999), innerPositionY(-999), innerPositionZ(-999),
//   outerPositionX(-999), outerPositionY(-999), outerPositionZ(-999)
{
  p4_.SetCoordinates(aTrack.momentum().x(),aTrack.momentum().y(),
                     aTrack.momentum().z(),sqrt(aTrack.momentum().mag2()+0.14*0.14));
}


//void PseudoLepton::muonTime(const reco::MuonTime & muonTime)
//{
//  std::cout << "pseudoLeptonProducer: nDof = " << muonTime.nDof << std::endl;

//  muonTime_.nDof = muonTime.nDof;
//  muonTime_.timeAtIpInOut = muonTime.timeAtIpInOut;
//  muonTime_.timeAtIpInOutErr = muonTime.timeAtIpInOutErr;
//  muonTime_.timeAtIpOutIn = muonTime.timeAtIpOutIn;
//  muonTime_.timeAtIpOutInErr = muonTime.timeAtIpOutInErr;
//}


//void PseudoLepton::muonEnergy(const reco::MuonEnergy & muonE)
//{
//  // std::cout << "muonE.ecal_time = " << muonE.ecal_time << std::endl;
//  muonE_.emMax = muonE.emMax;
//  muonE_.ecal_time = muonE.ecal_time;
//  muonE_.ecal_timeError = muonE.ecal_timeError;
//  muonE_.hadMax = muonE.hadMax;
//  muonE_.hcal_time = muonE.hcal_time;
//  muonE_.hcal_timeError = muonE.hcal_timeError;
//}


//void PseudoLepton::fillMuonExtraTime(reco::MuonTimeExtra & muonExtraTime_, const reco::MuonTimeExtra & muonExtraTime)
//{
//  muonExtraTime_.setNDof(muonExtraTime.nDof());
//  muonExtraTime_.setTimeAtIpInOut(muonExtraTime.timeAtIpInOut());
//  muonExtraTime_.setTimeAtIpInOutErr(muonExtraTime.timeAtIpInOutErr());
//  muonExtraTime_.setTimeAtIpOutIn(muonExtraTime.timeAtIpOutIn());
//  muonExtraTime_.setTimeAtIpOutInErr(muonExtraTime.timeAtIpOutInErr());
//  muonExtraTime_.setInverseBeta(muonExtraTime.inverseBeta());
//  muonExtraTime_.setInverseBetaErr(muonExtraTime.inverseBetaErr());
//  muonExtraTime_.setFreeInverseBeta(muonExtraTime.freeInverseBeta());
//  muonExtraTime_.setFreeInverseBetaErr(muonExtraTime.freeInverseBetaErr());
//}


/// destructor
PseudoLepton::~PseudoLepton() {
}


