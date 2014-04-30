sampleDataSet = '/QCD_Pt_30_80_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 2048152

sampleXSec = 7.424e7 * 0.00225 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"





samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_Pt_30_80_BCtoE_pat_20140328/demattia//QCD_Pt_30_80_BCtoE_TuneZ2star_8TeV_pythia6/QCD_Pt_30_80_BCtoE_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_J73.root",
sampleBaseDir+"PATtuple_11_1_wfW.root",
sampleBaseDir+"PATtuple_12_1_OlN.root",
sampleBaseDir+"PATtuple_13_1_2N5.root",
sampleBaseDir+"PATtuple_14_1_HhQ.root",
sampleBaseDir+"PATtuple_15_1_QJ3.root",
sampleBaseDir+"PATtuple_16_1_4JI.root",
sampleBaseDir+"PATtuple_17_1_rjN.root",
sampleBaseDir+"PATtuple_18_1_Cmu.root",
sampleBaseDir+"PATtuple_19_1_UfD.root",
sampleBaseDir+"PATtuple_1_1_xjy.root",
sampleBaseDir+"PATtuple_20_1_EuJ.root",
sampleBaseDir+"PATtuple_21_1_Vm3.root",
sampleBaseDir+"PATtuple_22_1_Hxn.root",
sampleBaseDir+"PATtuple_23_1_sGg.root",
sampleBaseDir+"PATtuple_24_1_qbB.root",
sampleBaseDir+"PATtuple_25_1_D0z.root",
sampleBaseDir+"PATtuple_26_1_VbS.root",
sampleBaseDir+"PATtuple_27_1_YO3.root",
sampleBaseDir+"PATtuple_28_1_tGR.root",
sampleBaseDir+"PATtuple_29_1_pBi.root",
sampleBaseDir+"PATtuple_2_1_yA6.root",
sampleBaseDir+"PATtuple_30_1_wmd.root",
sampleBaseDir+"PATtuple_31_1_l1b.root",
sampleBaseDir+"PATtuple_32_1_HM1.root",
sampleBaseDir+"PATtuple_33_1_Iys.root",
sampleBaseDir+"PATtuple_34_1_ukB.root",
sampleBaseDir+"PATtuple_35_1_taK.root",
sampleBaseDir+"PATtuple_36_1_RKK.root",
sampleBaseDir+"PATtuple_37_1_cMj.root",
sampleBaseDir+"PATtuple_38_1_1Xj.root",
sampleBaseDir+"PATtuple_39_1_wPZ.root",
sampleBaseDir+"PATtuple_3_1_wKe.root",
sampleBaseDir+"PATtuple_40_1_zHs.root",
sampleBaseDir+"PATtuple_41_1_aCj.root",
sampleBaseDir+"PATtuple_4_1_clb.root",
sampleBaseDir+"PATtuple_5_1_y5v.root",
sampleBaseDir+"PATtuple_6_1_eDd.root",
sampleBaseDir+"PATtuple_7_1_ptW.root",
sampleBaseDir+"PATtuple_8_1_WEm.root",
sampleBaseDir+"PATtuple_9_1_fHf.root",
]
