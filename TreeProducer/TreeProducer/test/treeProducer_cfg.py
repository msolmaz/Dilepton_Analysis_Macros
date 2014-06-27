import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")

process.load('FWCore.MessageService.MessageLogger_cfi')

# Suppress messages from vertex fitter
process.MessageLogger.categories.append( 'TwoTrackMinimumDistance' )
process.MessageLogger.cerr.TwoTrackMinimumDistance = cms.untracked.PSet( limit =cms.untracked.int32( 0 ) )
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load('Configuration/Geometry/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('RecoTracker.Configuration.RecoTracker_cff')

process.load('TreeProducer.TreeProducer.leptonAnalysis_cfi')


# SteppingHelixPropagator
process.MaterialPropagator = cms.ESProducer("PropagatorWithMaterialESProducer",
                                            MaxDPhi = cms.double(1.6),
                                            ComponentName = cms.string('PropagatorWithMaterial'),
                                            Mass = cms.double(0.105),
                                            PropagationDirection = cms.string('alongMomentum'),
                                            useRungeKutta = cms.bool(False),
                                            # If ptMin > 0, uncertainty in reconstructed momentum will be taken into account when estimating rms scattering angle.
                                            # (By default, it is neglected). However, it will also be assumed that the track pt can't be below specified value,
                                            # to prevent this scattering angle becoming too big.
                                            ptMin = cms.double(-1.)
                                            )

process.SteppingHelixPropagatorAny = cms.ESProducer("SteppingHelixPropagatorESProducer",
                                                    ComponentName = cms.string('SteppingHelixPropagatorAny'),
                                                    NoErrorPropagation = cms.bool(False),
                                                    PropagationDirection = cms.string('anyDirection'),
                                                    useTuningForL2Speed = cms.bool(False),
                                                    useIsYokeFlag = cms.bool(True),
                                                    endcapShiftInZNeg = cms.double(0.0),
                                                    SetVBFPointer = cms.bool(False),
                                                    AssumeNoMaterial = cms.bool(False),
                                                    endcapShiftInZPos = cms.double(0.0),
                                                    useInTeslaFromMagField = cms.bool(False),
                                                    VBFName = cms.string('VolumeBasedMagneticField'),
                                                    useEndcapShiftsInZ = cms.bool(False),
                                                    sendLogWarning = cms.bool(False),
                                                    useMatVolumes = cms.bool(True),
                                                    debug = cms.bool(False),
                                                    #This sort of works but assumes a measurement at propagation origin
                                                    ApplyRadX0Correction = cms.bool(True),
                                                    useMagVolumes = cms.bool(True),
                                                    returnTangentPlane = cms.bool(True)
                                                    )



# data sample and sample-specific settings
sampleSignalPID=[6001113,6002113,6003113,6001114,6002114,6003114,1000022,15,-15,23]
sampleRequireCollision=1
sampleRunE=1
sampleRunMu=1

from SampleFiles.Samples.Debug_sample_cff import *

# Electron - pseudo lepton
process.eTrackAnalysis = process.analyzeLeptons.clone()
process.eTrackAnalysis.signalPDGId = sampleSignalPID
process.eTrackAnalysis.leptonPDGId = -11
process.eTrackAnalysis.leptonPtCut = 10
process.eTrackAnalysis.leptonRSAPtCut = 0
process.eTrackAnalysis.leptonSCEtCut = 22
process.eTrackAnalysis.hltPaths = cms.vstring(
#                                         # Original trigger
#                                        "HLT_DoublePhoton48_HEVT_v3",
#                                        "HLT_DoublePhoton48_HEVT_v4",
#                                        "HLT_DoublePhoton48_HEVT_v5",
#                                        "HLT_DoublePhoton48_HEVT_v6",
#                                        "HLT_DoublePhoton48_HEVT_v7",
#                                        "HLT_DoublePhoton48_HEVT_v7",
#                                        "HLT_DoublePhoton48_HEVT_v8",

                                        # New higgs trigger
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v1",
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v2",
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v3",
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v4",
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v5",
                                        "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_R9Id85_OR_CaloId10_Iso50_v6",

                                        # For testing
#                                         "HLT_Photon36_R9Id85_OR_CaloId10_Iso50_Photon22_v4"
                                         )
# Add "*" if we are looking at signal MC so we don't filter on triggers, but we still have trigger objects to match to
if ( sampleType == "SIGNALMC" ) : process.eTrackAnalysis.hltPaths.append("*")
if sampleType == "DATA" : 
    process.eTrackAnalysis.UseMCTruth = False
    process.eTrackAnalysis.isData = True
    pass
    
# Muon - pseudo lepton
process.muTrackAnalysis = process.analyzeLeptons.clone()
process.muTrackAnalysis.signalPDGId = sampleSignalPID
process.muTrackAnalysis.leptonPDGId = -13
process.muTrackAnalysis.leptonPtCut = 25
process.muTrackAnalysis.leptonRSAPtCut = 0
process.muTrackAnalysis.leptonSCEtCut = 0
process.muTrackAnalysis.hltPaths = cms.vstring(
                                          #"HLT_L2Mu11",  # Run2010A1 (136035-141881)
                                          #"HLT_L2Mu15",  # Run2010A2 (141956-144114)
                                          #"HLT_L2Mu25",                   # Run2010B1 (146428-147120)
                                          #"HLT_L2DoubleMu20_NoVertex_v1", # Run2010B2 (147121-150000)
                                          #"HLT_L2DoubleMu23_NoVertex_v1",
                                          #"HLT_L2DoubleMu23_NoVertex_v2",
                                          #"HLT_L2DoubleMu23_NoVertex_v3",
                                          #"HLT_L2DoubleMu23_NoVertex_v4",
                                          #"HLT_L2DoubleMu23_NoVertex_v5",
                                          #"HLT_L2DoubleMu23_NoVertex_v6",
                                          #"HLT_L2DoubleMu23_NoVertex_v7",
                                          #"HLT_L2DoubleMu30_NoVertex_v1",
                                          #"HLT_L2DoubleMu30_NoVertex_v2",
                                          #"HLT_L2DoubleMu30_NoVertex_v3",
                                          #"HLT_L2DoubleMu30_NoVertex_v4",
                                          #"HLT_MET120_v1",
                                          #"HLT_MET120_v2",
                                          #"HLT_MET120_v3",
                                          #"HLT_MET120_v4",
                                          #"HLT_MET120_v5",
                                          #"HLT_MET120_v6",
                                          #"HLT_MET120_v7"
                                            "HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v1",
                                            "HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v2",
                                            "HLT_L2DoubleMu23_NoVertex_2Cha_Angle2p5_v3",
											"HLT_PFMET150_v1",
											"HLT_PFMET150_v2",
											"HLT_PFMET150_v3",
											"HLT_PFMET150_v4",
											"HLT_PFMET150_v5",
											"HLT_PFMET150_v6",
											"HLT_PFMET150_v7",
										    "HLT_PFMET150_v8",
											"HLT_PFMET150_v9",
											"HLT_MET120_HBHENoiseCleaned_v1",
											"HLT_MET120_HBHENoiseCleaned_v2",
											"HLT_MET120_HBHENoiseCleaned_v3",
											"HLT_MET120_HBHENoiseCleaned_v4",
											"HLT_MET120_HBHENoiseCleaned_v5",
											"HLT_MET120_HBHENoiseCleaned_v6",
											"HLT_MET120_HBHENoiseCleaned_v7",
											"HLT_MET120_HBHENoiseCleaned_v8",
											"HLT_MET120_HBHENoiseCleaned_v9",
)
if ( sampleType == "SIGNALMC" ) : process.muTrackAnalysis.hltPaths.append("*")
if sampleType == "DATA" : 
    process.muTrackAnalysis.UseMCTruth = False
    process.muTrackAnalysis.isData = True
    pass

# create pseudo-leptons for all lepton channels
process.load("TreeProducer.TreeProducer.pseudoLeptonProducer_cfi")

# Set input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string(sampleDuplicateCheckMode),
    fileNames = cms.untracked.vstring(samplePatFiles),
    # Useful for debugging and jumping to a particular event
#     skipEvents = cms.untracked.uint32(920)
)

# Set global tag
process.GlobalTag.globaltag = sampleGlobalTag
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

# Output TFileService
process.TFileService = cms.Service("TFileService", 
    fileName = cms.string('histograms.root')
)

process.load("TreeProducer.TreeProducer.goodCollFilter_cff")

# # Configure tip and lip corrections
# # For data only
# if sampleType is 'DATA' :
#     from TreeProducer.TreeProducer.configureTipLipCorrections_cfi import *
#     configureTipLipCorrections( process.muTrackAnalysis, sampleBaseDir, '2muTrack' )
#     configureTipLipCorrections( process.eTrackAnalysis, sampleBaseDir, '2eTrack' )
#     pass

process.p = cms.Path()

# Only apply filter if not signal MC
if ( sampleType != "SIGNALMC" ):
    # Filter on good collisions
    if sampleRequireCollision: process.p+=process.goodcollFilter
    pass
# Require pseudoleptons of sufficent pt/Et
process.p+=process.pseudoLeptonProducer

# Add electron pseudolepton analysis
# if sampleRunE: process.p+=process.eTrackAnalysis
# Add muon psuedolepton analysis
if sampleRunMu: process.p+=process.muTrackAnalysis
