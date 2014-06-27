sampleDataSet = '/HTo2LongLivedTo4F_MH-200_MFF-50_CTau20To2000_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 99048

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7A::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"











samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_pat_20140502/zhenhu//HTo2LongLivedTo4F_MH-200_MFF-50_CTau20To2000_8TeV-pythia6/HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_pat_20140502/9a5984d39acb29a93d7b43a925b0ec93/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_VM7.root",
sampleBaseDir+"PATtuple_11_1_Hqo.root",
sampleBaseDir+"PATtuple_12_1_iPD.root",
sampleBaseDir+"PATtuple_13_1_t6a.root",
sampleBaseDir+"PATtuple_14_1_g8t.root",
sampleBaseDir+"PATtuple_15_1_sz7.root",
sampleBaseDir+"PATtuple_16_1_ddG.root",
sampleBaseDir+"PATtuple_17_1_yxK.root",
sampleBaseDir+"PATtuple_18_1_2KS.root",
sampleBaseDir+"PATtuple_19_1_UKk.root",
sampleBaseDir+"PATtuple_1_1_qBf.root",
sampleBaseDir+"PATtuple_20_1_k8D.root",
sampleBaseDir+"PATtuple_21_1_I1s.root",
sampleBaseDir+"PATtuple_22_1_m6V.root",
sampleBaseDir+"PATtuple_23_1_vro.root",
sampleBaseDir+"PATtuple_24_1_uZy.root",
sampleBaseDir+"PATtuple_25_1_dsx.root",
sampleBaseDir+"PATtuple_26_1_jOH.root",
sampleBaseDir+"PATtuple_27_1_KLS.root",
sampleBaseDir+"PATtuple_28_1_UYk.root",
sampleBaseDir+"PATtuple_29_1_MU5.root",
sampleBaseDir+"PATtuple_2_1_po9.root",
sampleBaseDir+"PATtuple_30_1_uK0.root",
sampleBaseDir+"PATtuple_31_1_jjd.root",
sampleBaseDir+"PATtuple_32_1_utg.root",
sampleBaseDir+"PATtuple_33_1_F1i.root",
sampleBaseDir+"PATtuple_34_1_fxv.root",
sampleBaseDir+"PATtuple_35_1_lG6.root",
sampleBaseDir+"PATtuple_36_1_85n.root",
sampleBaseDir+"PATtuple_37_1_fZF.root",
sampleBaseDir+"PATtuple_38_1_7hs.root",
sampleBaseDir+"PATtuple_39_1_f6r.root",
sampleBaseDir+"PATtuple_3_1_Abm.root",
sampleBaseDir+"PATtuple_40_1_8IW.root",
sampleBaseDir+"PATtuple_41_1_dn6.root",
sampleBaseDir+"PATtuple_42_1_EMS.root",
sampleBaseDir+"PATtuple_43_1_FUU.root",
sampleBaseDir+"PATtuple_44_1_xZD.root",
sampleBaseDir+"PATtuple_45_1_InH.root",
sampleBaseDir+"PATtuple_46_1_TZn.root",
sampleBaseDir+"PATtuple_47_1_C7e.root",
sampleBaseDir+"PATtuple_48_1_YGA.root",
sampleBaseDir+"PATtuple_49_1_A1a.root",
sampleBaseDir+"PATtuple_4_1_z6f.root",
sampleBaseDir+"PATtuple_50_1_Qeh.root",
sampleBaseDir+"PATtuple_5_1_CDm.root",
sampleBaseDir+"PATtuple_6_1_Epc.root",
sampleBaseDir+"PATtuple_7_1_Tc2.root",
sampleBaseDir+"PATtuple_8_1_TMJ.root",
sampleBaseDir+"PATtuple_9_1_ZYt.root",
]