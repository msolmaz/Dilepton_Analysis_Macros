sampleDataSet = '/HTo2LongLivedTo4F_MH-1000_MFF-350_CTau35To3500_8TeV-pythia6/Summer12_DR53X-DEBUG_PU_S10_START53_V7A-v1/AODSIM'  

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

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_pat_20140327/demattia//HTo2LongLivedTo4F_MH-1000_MFF-350_CTau35To3500_8TeV-pythia6/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_pat_20140327/44ed12438b36eeb4f61ccae26cc96d54/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_MJa.root",
sampleBaseDir+"PATtuple_11_1_BXJ.root",
sampleBaseDir+"PATtuple_12_2_E1v.root",
sampleBaseDir+"PATtuple_13_1_3hK.root",
sampleBaseDir+"PATtuple_14_1_Owm.root",
sampleBaseDir+"PATtuple_15_1_uXa.root",
sampleBaseDir+"PATtuple_16_1_GIi.root",
sampleBaseDir+"PATtuple_17_1_Hw8.root",
sampleBaseDir+"PATtuple_18_1_EtP.root",
sampleBaseDir+"PATtuple_19_1_DYH.root",
sampleBaseDir+"PATtuple_1_3_kqS.root",
sampleBaseDir+"PATtuple_20_1_VwL.root",
sampleBaseDir+"PATtuple_21_1_b4d.root",
sampleBaseDir+"PATtuple_22_1_pOT.root",
sampleBaseDir+"PATtuple_23_1_umG.root",
sampleBaseDir+"PATtuple_24_1_BbW.root",
sampleBaseDir+"PATtuple_25_1_9x2.root",
sampleBaseDir+"PATtuple_26_1_Go2.root",
sampleBaseDir+"PATtuple_27_1_bBL.root",
sampleBaseDir+"PATtuple_28_1_690.root",
sampleBaseDir+"PATtuple_29_1_kzs.root",
sampleBaseDir+"PATtuple_2_1_5gX.root",
sampleBaseDir+"PATtuple_30_1_tUI.root",
sampleBaseDir+"PATtuple_31_1_i3N.root",
sampleBaseDir+"PATtuple_32_2_MXl.root",
sampleBaseDir+"PATtuple_33_2_uiH.root",
sampleBaseDir+"PATtuple_34_1_nUP.root",
sampleBaseDir+"PATtuple_35_1_u29.root",
sampleBaseDir+"PATtuple_36_1_RZi.root",
sampleBaseDir+"PATtuple_37_1_YVF.root",
sampleBaseDir+"PATtuple_38_1_hih.root",
sampleBaseDir+"PATtuple_39_1_Glf.root",
sampleBaseDir+"PATtuple_3_1_3mx.root",
sampleBaseDir+"PATtuple_40_1_0Ni.root",
sampleBaseDir+"PATtuple_41_1_FLw.root",
sampleBaseDir+"PATtuple_42_1_fGU.root",
sampleBaseDir+"PATtuple_43_2_Q3Z.root",
sampleBaseDir+"PATtuple_44_1_pEI.root",
sampleBaseDir+"PATtuple_45_1_g53.root",
sampleBaseDir+"PATtuple_46_1_jfU.root",
sampleBaseDir+"PATtuple_47_2_qla.root",
sampleBaseDir+"PATtuple_48_1_K1e.root",
sampleBaseDir+"PATtuple_49_1_i46.root",
sampleBaseDir+"PATtuple_4_2_Fif.root",
sampleBaseDir+"PATtuple_50_1_c1o.root",
sampleBaseDir+"PATtuple_5_2_GmA.root",
sampleBaseDir+"PATtuple_6_2_CE1.root",
sampleBaseDir+"PATtuple_7_1_V31.root",
sampleBaseDir+"PATtuple_8_1_AYX.root",
sampleBaseDir+"PATtuple_9_1_P2v.root",
]
