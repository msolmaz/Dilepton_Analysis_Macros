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

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_pat_20140502/zhenhu//HTo2LongLivedTo4F_MH-1000_MFF-350_CTau35To3500_8TeV-pythia6/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_pat_20140502/9a5984d39acb29a93d7b43a925b0ec93/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_kSA.root",
sampleBaseDir+"PATtuple_11_1_BpV.root",
sampleBaseDir+"PATtuple_12_1_VLV.root",
sampleBaseDir+"PATtuple_13_1_n3g.root",
sampleBaseDir+"PATtuple_14_1_9Do.root",
sampleBaseDir+"PATtuple_15_1_AWM.root",
sampleBaseDir+"PATtuple_16_1_9kc.root",
sampleBaseDir+"PATtuple_17_1_tca.root",
sampleBaseDir+"PATtuple_18_1_oM3.root",
sampleBaseDir+"PATtuple_19_1_VuW.root",
sampleBaseDir+"PATtuple_1_1_5Sb.root",
sampleBaseDir+"PATtuple_20_1_qsK.root",
sampleBaseDir+"PATtuple_21_1_x5W.root",
sampleBaseDir+"PATtuple_22_1_ZcC.root",
sampleBaseDir+"PATtuple_23_1_6Zv.root",
sampleBaseDir+"PATtuple_24_1_BEX.root",
sampleBaseDir+"PATtuple_25_1_jm9.root",
sampleBaseDir+"PATtuple_26_1_Ieq.root",
sampleBaseDir+"PATtuple_27_1_peD.root",
sampleBaseDir+"PATtuple_28_1_Icf.root",
sampleBaseDir+"PATtuple_29_1_zJT.root",
sampleBaseDir+"PATtuple_2_1_gMG.root",
sampleBaseDir+"PATtuple_30_1_qZX.root",
sampleBaseDir+"PATtuple_31_1_0OF.root",
sampleBaseDir+"PATtuple_32_1_4aP.root",
sampleBaseDir+"PATtuple_33_1_660.root",
sampleBaseDir+"PATtuple_34_1_Ugl.root",
sampleBaseDir+"PATtuple_35_1_THP.root",
sampleBaseDir+"PATtuple_36_1_WRj.root",
sampleBaseDir+"PATtuple_37_1_Kug.root",
sampleBaseDir+"PATtuple_38_1_MXz.root",
sampleBaseDir+"PATtuple_39_1_cGn.root",
sampleBaseDir+"PATtuple_3_1_9j4.root",
sampleBaseDir+"PATtuple_40_1_ACm.root",
sampleBaseDir+"PATtuple_41_1_E3B.root",
sampleBaseDir+"PATtuple_42_1_0Cz.root",
sampleBaseDir+"PATtuple_43_1_GSw.root",
sampleBaseDir+"PATtuple_44_1_GIt.root",
sampleBaseDir+"PATtuple_45_1_W6a.root",
sampleBaseDir+"PATtuple_46_1_7qV.root",
sampleBaseDir+"PATtuple_47_1_GAO.root",
sampleBaseDir+"PATtuple_48_1_GpX.root",
sampleBaseDir+"PATtuple_49_1_2Si.root",
sampleBaseDir+"PATtuple_4_1_MvL.root",
sampleBaseDir+"PATtuple_50_1_5IB.root",
sampleBaseDir+"PATtuple_5_1_07O.root",
sampleBaseDir+"PATtuple_6_1_Jlu.root",
sampleBaseDir+"PATtuple_7_1_7Xl.root",
sampleBaseDir+"PATtuple_8_1_6Be.root",
sampleBaseDir+"PATtuple_9_1_m0N.root",
]