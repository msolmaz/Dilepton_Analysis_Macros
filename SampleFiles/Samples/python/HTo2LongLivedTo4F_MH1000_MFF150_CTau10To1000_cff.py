sampleDataSet = '/HTo2LongLivedTo4F_MH-1000_MFF-150_CTau10To1000_8TeV-pythia6/Summer12_DR53X-DEBUG_PU_S10_START53_V7A-v2/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 99016

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7A::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"











samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_pat_20140502/zhenhu//HTo2LongLivedTo4F_MH-1000_MFF-150_CTau10To1000_8TeV-pythia6/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_pat_20140502/9a5984d39acb29a93d7b43a925b0ec93/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_RjV.root",
sampleBaseDir+"PATtuple_11_1_g3l.root",
sampleBaseDir+"PATtuple_12_1_Z8s.root",
sampleBaseDir+"PATtuple_13_1_0ie.root",
sampleBaseDir+"PATtuple_14_1_bB9.root",
sampleBaseDir+"PATtuple_15_1_q4q.root",
sampleBaseDir+"PATtuple_16_1_B84.root",
sampleBaseDir+"PATtuple_17_1_gpc.root",
sampleBaseDir+"PATtuple_18_1_TsM.root",
sampleBaseDir+"PATtuple_19_1_5Dv.root",
sampleBaseDir+"PATtuple_1_1_z5f.root",
sampleBaseDir+"PATtuple_20_1_12o.root",
sampleBaseDir+"PATtuple_21_1_1yQ.root",
sampleBaseDir+"PATtuple_22_1_TyW.root",
sampleBaseDir+"PATtuple_23_1_zBT.root",
sampleBaseDir+"PATtuple_24_1_05X.root",
sampleBaseDir+"PATtuple_25_1_XLU.root",
sampleBaseDir+"PATtuple_26_1_eLh.root",
sampleBaseDir+"PATtuple_27_1_92s.root",
sampleBaseDir+"PATtuple_28_1_aIY.root",
sampleBaseDir+"PATtuple_29_1_Y7W.root",
sampleBaseDir+"PATtuple_2_1_3kX.root",
sampleBaseDir+"PATtuple_30_1_Y3y.root",
sampleBaseDir+"PATtuple_31_1_E4H.root",
sampleBaseDir+"PATtuple_32_1_0jY.root",
sampleBaseDir+"PATtuple_33_1_oH2.root",
sampleBaseDir+"PATtuple_34_1_cw1.root",
sampleBaseDir+"PATtuple_35_1_sWJ.root",
sampleBaseDir+"PATtuple_36_1_9Ca.root",
sampleBaseDir+"PATtuple_37_1_9YZ.root",
sampleBaseDir+"PATtuple_38_1_aWZ.root",
sampleBaseDir+"PATtuple_39_1_m4F.root",
sampleBaseDir+"PATtuple_3_1_vUr.root",
sampleBaseDir+"PATtuple_40_1_9Je.root",
sampleBaseDir+"PATtuple_41_1_PGr.root",
sampleBaseDir+"PATtuple_42_1_D2x.root",
sampleBaseDir+"PATtuple_43_1_zLI.root",
sampleBaseDir+"PATtuple_44_1_oNB.root",
sampleBaseDir+"PATtuple_45_1_T56.root",
sampleBaseDir+"PATtuple_46_1_swY.root",
sampleBaseDir+"PATtuple_47_1_0YS.root",
sampleBaseDir+"PATtuple_48_1_WEs.root",
sampleBaseDir+"PATtuple_49_1_mWh.root",
sampleBaseDir+"PATtuple_4_1_3ux.root",
sampleBaseDir+"PATtuple_50_1_pCZ.root",
sampleBaseDir+"PATtuple_5_1_lrb.root",
sampleBaseDir+"PATtuple_6_1_5CJ.root",
sampleBaseDir+"PATtuple_7_1_MNG.root",
sampleBaseDir+"PATtuple_8_1_gTg.root",
sampleBaseDir+"PATtuple_9_1_Pqm.root",
]