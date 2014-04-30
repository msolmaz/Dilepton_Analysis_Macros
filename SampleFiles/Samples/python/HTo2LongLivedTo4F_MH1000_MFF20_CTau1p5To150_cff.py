sampleDataSet = '/HTo2LongLivedTo4F_MH-1000_MFF-20_CTau1p5To150_8TeV-pythia6/Summer12_DR53X-DEBUG_PU_S10_START53_V7A-v2/AODSIM'  

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

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_pat_20140328/demattia//HTo2LongLivedTo4F_MH-1000_MFF-20_CTau1p5To150_8TeV-pythia6/HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_pat_20140328/44ed12438b36eeb4f61ccae26cc96d54/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_bBe.root",
sampleBaseDir+"PATtuple_11_2_tSK.root",
sampleBaseDir+"PATtuple_12_1_l3K.root",
sampleBaseDir+"PATtuple_13_1_6bi.root",
sampleBaseDir+"PATtuple_14_1_shX.root",
sampleBaseDir+"PATtuple_15_1_pF3.root",
sampleBaseDir+"PATtuple_16_1_umJ.root",
sampleBaseDir+"PATtuple_17_1_gLz.root",
sampleBaseDir+"PATtuple_18_1_Sg3.root",
sampleBaseDir+"PATtuple_19_2_Szy.root",
sampleBaseDir+"PATtuple_1_2_YRd.root",
sampleBaseDir+"PATtuple_20_2_LEx.root",
sampleBaseDir+"PATtuple_21_1_N68.root",
sampleBaseDir+"PATtuple_22_1_PYb.root",
sampleBaseDir+"PATtuple_23_1_eQO.root",
sampleBaseDir+"PATtuple_24_1_550.root",
sampleBaseDir+"PATtuple_25_1_WkR.root",
sampleBaseDir+"PATtuple_26_1_XWV.root",
sampleBaseDir+"PATtuple_27_1_1uf.root",
sampleBaseDir+"PATtuple_28_1_uBi.root",
sampleBaseDir+"PATtuple_29_1_l68.root",
sampleBaseDir+"PATtuple_2_2_q9y.root",
sampleBaseDir+"PATtuple_30_1_2i3.root",
sampleBaseDir+"PATtuple_31_2_6IR.root",
sampleBaseDir+"PATtuple_32_1_BuQ.root",
sampleBaseDir+"PATtuple_33_1_g6q.root",
sampleBaseDir+"PATtuple_34_1_Ldx.root",
sampleBaseDir+"PATtuple_35_1_ItH.root",
sampleBaseDir+"PATtuple_36_1_KkH.root",
sampleBaseDir+"PATtuple_37_1_HcB.root",
sampleBaseDir+"PATtuple_38_1_QL7.root",
sampleBaseDir+"PATtuple_39_1_M6L.root",
sampleBaseDir+"PATtuple_3_1_iAs.root",
sampleBaseDir+"PATtuple_40_1_tn2.root",
sampleBaseDir+"PATtuple_41_1_OUY.root",
sampleBaseDir+"PATtuple_42_1_XO4.root",
sampleBaseDir+"PATtuple_43_1_aIt.root",
sampleBaseDir+"PATtuple_44_1_Quo.root",
sampleBaseDir+"PATtuple_45_1_0rI.root",
sampleBaseDir+"PATtuple_46_1_8lz.root",
sampleBaseDir+"PATtuple_47_1_7Zv.root",
sampleBaseDir+"PATtuple_48_1_c7J.root",
sampleBaseDir+"PATtuple_49_1_unQ.root",
sampleBaseDir+"PATtuple_4_1_s6e.root",
sampleBaseDir+"PATtuple_50_1_qpm.root",
sampleBaseDir+"PATtuple_5_1_xkG.root",
sampleBaseDir+"PATtuple_6_1_XVY.root",
sampleBaseDir+"PATtuple_7_1_YOn.root",
sampleBaseDir+"PATtuple_8_1_OLX.root",
sampleBaseDir+"PATtuple_9_1_KoF.root",
]
