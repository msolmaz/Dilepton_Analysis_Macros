sampleDataSet = '/QCD_Pt-15to20_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 1722681

sampleXSec = 7.022E8 * 0.0039 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"










samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCDmu15_pat_20140502/zhenhu//QCD_Pt-15to20_MuEnrichedPt5_TuneZ2star_8TeV_pythia6/QCDmu15_pat_20140502/fdbd887910ea36180672aa763a206c5b/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_hBY.root",
sampleBaseDir+"PATtuple_11_1_qnO.root",
sampleBaseDir+"PATtuple_12_1_v9F.root",
sampleBaseDir+"PATtuple_13_1_YaA.root",
sampleBaseDir+"PATtuple_14_1_id1.root",
sampleBaseDir+"PATtuple_15_1_wHS.root",
sampleBaseDir+"PATtuple_16_1_Tpb.root",
sampleBaseDir+"PATtuple_17_1_Kni.root",
sampleBaseDir+"PATtuple_18_1_41j.root",
sampleBaseDir+"PATtuple_19_1_eE3.root",
sampleBaseDir+"PATtuple_1_1_J0C.root",
sampleBaseDir+"PATtuple_20_1_Udf.root",
sampleBaseDir+"PATtuple_21_1_cgi.root",
sampleBaseDir+"PATtuple_22_1_BX7.root",
sampleBaseDir+"PATtuple_23_1_M7d.root",
sampleBaseDir+"PATtuple_24_1_BEM.root",
sampleBaseDir+"PATtuple_25_1_4C2.root",
sampleBaseDir+"PATtuple_26_1_hpE.root",
sampleBaseDir+"PATtuple_27_1_n7a.root",
sampleBaseDir+"PATtuple_28_1_S21.root",
sampleBaseDir+"PATtuple_29_1_vhx.root",
sampleBaseDir+"PATtuple_2_1_r4m.root",
sampleBaseDir+"PATtuple_30_1_iXn.root",
sampleBaseDir+"PATtuple_31_1_8fO.root",
sampleBaseDir+"PATtuple_32_1_iv6.root",
sampleBaseDir+"PATtuple_33_1_TYs.root",
sampleBaseDir+"PATtuple_34_1_Qqv.root",
sampleBaseDir+"PATtuple_35_1_cuQ.root",
sampleBaseDir+"PATtuple_3_1_eY4.root",
sampleBaseDir+"PATtuple_4_1_Wht.root",
sampleBaseDir+"PATtuple_5_1_8kR.root",
sampleBaseDir+"PATtuple_6_1_dbc.root",
sampleBaseDir+"PATtuple_7_1_ina.root",
sampleBaseDir+"PATtuple_8_1_pUY.root",
sampleBaseDir+"PATtuple_9_1_ALR.root",
]