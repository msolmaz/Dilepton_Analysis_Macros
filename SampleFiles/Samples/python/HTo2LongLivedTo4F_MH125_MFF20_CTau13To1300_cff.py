sampleDataSet = '/HTo2LongLivedTo4F_MH-125_MFF-20_CTau13To1300_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/GEN-SIM-RECODEBUG'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_7" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_8" # release used to create new files with

sampleNumEvents = 100007

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7G::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_pat_20140502/zhenhu//HTo2LongLivedTo4F_MH-125_MFF-20_CTau13To1300_8TeV-pythia6/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_pat_20140502/45887e9793c49104ed53219bb94c3351/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_Yew.root",
sampleBaseDir+"PATtuple_11_1_KNL.root",
sampleBaseDir+"PATtuple_12_2_8nc.root",
sampleBaseDir+"PATtuple_13_1_f5U.root",
sampleBaseDir+"PATtuple_14_1_EXz.root",
sampleBaseDir+"PATtuple_15_1_9gG.root",
sampleBaseDir+"PATtuple_16_1_0LQ.root",
sampleBaseDir+"PATtuple_17_1_ARz.root",
sampleBaseDir+"PATtuple_18_1_jBe.root",
sampleBaseDir+"PATtuple_19_1_UvZ.root",
sampleBaseDir+"PATtuple_1_1_JvY.root",
sampleBaseDir+"PATtuple_20_1_X2n.root",
sampleBaseDir+"PATtuple_21_1_AyO.root",
sampleBaseDir+"PATtuple_22_1_OTl.root",
sampleBaseDir+"PATtuple_23_1_gdm.root",
sampleBaseDir+"PATtuple_24_1_V4X.root",
sampleBaseDir+"PATtuple_25_1_Rbk.root",
sampleBaseDir+"PATtuple_26_1_hQQ.root",
sampleBaseDir+"PATtuple_27_1_4yH.root",
sampleBaseDir+"PATtuple_28_1_oQJ.root",
sampleBaseDir+"PATtuple_2_2_tRg.root",
sampleBaseDir+"PATtuple_31_1_xAD.root",
sampleBaseDir+"PATtuple_32_1_Jkm.root",
sampleBaseDir+"PATtuple_33_1_W5D.root",
sampleBaseDir+"PATtuple_34_1_tbn.root",
sampleBaseDir+"PATtuple_35_1_HLr.root",
sampleBaseDir+"PATtuple_36_1_gTB.root",
sampleBaseDir+"PATtuple_37_1_WXr.root",
sampleBaseDir+"PATtuple_38_1_CUo.root",
sampleBaseDir+"PATtuple_39_1_v8Y.root",
sampleBaseDir+"PATtuple_3_2_m2g.root",
sampleBaseDir+"PATtuple_40_1_cWT.root",
sampleBaseDir+"PATtuple_41_1_9iU.root",
sampleBaseDir+"PATtuple_42_1_Bqx.root",
sampleBaseDir+"PATtuple_43_1_Qzi.root",
sampleBaseDir+"PATtuple_44_1_lKb.root",
sampleBaseDir+"PATtuple_45_1_cUw.root",
sampleBaseDir+"PATtuple_46_1_1vR.root",
sampleBaseDir+"PATtuple_47_1_8tb.root",
sampleBaseDir+"PATtuple_48_1_yQJ.root",
sampleBaseDir+"PATtuple_49_1_vL8.root",
sampleBaseDir+"PATtuple_4_1_7sH.root",
sampleBaseDir+"PATtuple_50_1_Wdy.root",
sampleBaseDir+"PATtuple_51_1_Nfx.root",
sampleBaseDir+"PATtuple_5_1_msp.root",
sampleBaseDir+"PATtuple_6_2_6Yl.root",
sampleBaseDir+"PATtuple_7_1_gAk.root",
]