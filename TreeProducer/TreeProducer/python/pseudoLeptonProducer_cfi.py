import FWCore.ParameterSet.Config as cms

pseudoLeptonProducer = cms.EDProducer("PseudoLeptonProducer",
                                      trackSrc = cms.InputTag("trackSel"),
                                      muonSrc = cms.InputTag("refittedStandAloneMuons"),
                                      patMuonSrc = cms.InputTag("selectedPatMuons"),
                                      minPt = cms.double(0),
                                      useStandAloneMuons = cms.bool(True))

