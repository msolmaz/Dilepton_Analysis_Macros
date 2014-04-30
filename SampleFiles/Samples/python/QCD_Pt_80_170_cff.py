sampleDataSet = '/QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 1945525

sampleXSec = 1191000.0 * 0.0109 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_Pt_80_170_pat_20140328/demattia//QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/QCD_Pt_80_170_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_MEI.root",
sampleBaseDir+"PATtuple_11_1_hNk.root",
sampleBaseDir+"PATtuple_12_1_wum.root",
sampleBaseDir+"PATtuple_13_1_lte.root",
sampleBaseDir+"PATtuple_14_1_X7G.root",
sampleBaseDir+"PATtuple_15_1_svX.root",
sampleBaseDir+"PATtuple_16_1_aGu.root",
sampleBaseDir+"PATtuple_17_1_gJB.root",
sampleBaseDir+"PATtuple_18_1_mWk.root",
sampleBaseDir+"PATtuple_19_1_Adj.root",
sampleBaseDir+"PATtuple_1_1_1Yt.root",
sampleBaseDir+"PATtuple_20_1_jk5.root",
sampleBaseDir+"PATtuple_21_1_YaG.root",
sampleBaseDir+"PATtuple_22_1_ou5.root",
sampleBaseDir+"PATtuple_23_1_fbu.root",
sampleBaseDir+"PATtuple_24_1_JJw.root",
sampleBaseDir+"PATtuple_25_1_LVx.root",
sampleBaseDir+"PATtuple_26_1_znH.root",
sampleBaseDir+"PATtuple_27_1_hmx.root",
sampleBaseDir+"PATtuple_28_1_hgZ.root",
sampleBaseDir+"PATtuple_29_1_ECY.root",
sampleBaseDir+"PATtuple_2_1_KB4.root",
sampleBaseDir+"PATtuple_30_1_KUo.root",
sampleBaseDir+"PATtuple_31_1_mfr.root",
sampleBaseDir+"PATtuple_32_1_rIV.root",
sampleBaseDir+"PATtuple_33_1_m8E.root",
sampleBaseDir+"PATtuple_34_1_P9d.root",
sampleBaseDir+"PATtuple_35_1_FmX.root",
sampleBaseDir+"PATtuple_36_1_Pxd.root",
sampleBaseDir+"PATtuple_37_1_qk8.root",
sampleBaseDir+"PATtuple_38_1_57c.root",
sampleBaseDir+"PATtuple_39_1_kWa.root",
sampleBaseDir+"PATtuple_3_1_6at.root",
sampleBaseDir+"PATtuple_4_1_O8C.root",
sampleBaseDir+"PATtuple_5_1_vr1.root",
sampleBaseDir+"PATtuple_6_1_YQv.root",
sampleBaseDir+"PATtuple_7_1_APY.root",
sampleBaseDir+"PATtuple_8_1_NDY.root",
sampleBaseDir+"PATtuple_9_1_CGc.root",
]
