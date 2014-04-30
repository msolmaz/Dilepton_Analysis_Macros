sampleDataSet = '/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 1740229

sampleXSec = 2.886e8 * 5.8e-4 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"



samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_Pt_20_30_BCtoE_pat_20140328/demattia//QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/QCD_Pt_20_30_BCtoE_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_PeH.root",
sampleBaseDir+"PATtuple_11_1_9kT.root",
sampleBaseDir+"PATtuple_12_1_9lU.root",
sampleBaseDir+"PATtuple_13_1_nNc.root",
sampleBaseDir+"PATtuple_14_1_Jv6.root",
sampleBaseDir+"PATtuple_15_1_P7C.root",
sampleBaseDir+"PATtuple_16_1_ZGg.root",
sampleBaseDir+"PATtuple_17_1_L3B.root",
sampleBaseDir+"PATtuple_18_1_wl6.root",
sampleBaseDir+"PATtuple_19_1_yvS.root",
sampleBaseDir+"PATtuple_1_1_wgB.root",
sampleBaseDir+"PATtuple_20_1_lj4.root",
sampleBaseDir+"PATtuple_21_1_fJJ.root",
sampleBaseDir+"PATtuple_22_1_yd6.root",
sampleBaseDir+"PATtuple_23_1_roQ.root",
sampleBaseDir+"PATtuple_24_1_vei.root",
sampleBaseDir+"PATtuple_25_1_7dB.root",
sampleBaseDir+"PATtuple_26_1_Fh9.root",
sampleBaseDir+"PATtuple_27_1_WnL.root",
sampleBaseDir+"PATtuple_28_1_bas.root",
sampleBaseDir+"PATtuple_29_1_hEp.root",
sampleBaseDir+"PATtuple_2_1_NdJ.root",
sampleBaseDir+"PATtuple_30_1_Rux.root",
sampleBaseDir+"PATtuple_31_1_Fny.root",
sampleBaseDir+"PATtuple_32_1_a7l.root",
sampleBaseDir+"PATtuple_33_1_POJ.root",
sampleBaseDir+"PATtuple_34_1_0fW.root",
sampleBaseDir+"PATtuple_35_1_UFh.root",
sampleBaseDir+"PATtuple_3_1_CAK.root",
sampleBaseDir+"PATtuple_4_1_5OU.root",
sampleBaseDir+"PATtuple_5_1_bBg.root",
sampleBaseDir+"PATtuple_6_1_MVg.root",
sampleBaseDir+"PATtuple_7_1_1FJ.root",
sampleBaseDir+"PATtuple_8_1_Zbe.root",
sampleBaseDir+"PATtuple_9_1_7JA.root",
]
