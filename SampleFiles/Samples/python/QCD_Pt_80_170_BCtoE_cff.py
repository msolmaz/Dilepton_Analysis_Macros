sampleDataSet = '/QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 1945525

sampleXSec = 0. # pb #### to be found

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"






samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_Pt_80_170_BCtoE_pat_20140328/demattia//QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/QCD_Pt_80_170_BCtoE_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_UDX.root",
sampleBaseDir+"PATtuple_11_1_CnT.root",
sampleBaseDir+"PATtuple_12_1_OIr.root",
sampleBaseDir+"PATtuple_13_1_LrS.root",
sampleBaseDir+"PATtuple_14_1_R8o.root",
sampleBaseDir+"PATtuple_15_1_UKm.root",
sampleBaseDir+"PATtuple_16_1_9Ri.root",
sampleBaseDir+"PATtuple_17_1_ny6.root",
sampleBaseDir+"PATtuple_18_1_Ksq.root",
sampleBaseDir+"PATtuple_19_1_Stl.root",
sampleBaseDir+"PATtuple_1_1_pN1.root",
sampleBaseDir+"PATtuple_20_1_3x1.root",
sampleBaseDir+"PATtuple_21_1_OrP.root",
sampleBaseDir+"PATtuple_22_1_qeP.root",
sampleBaseDir+"PATtuple_23_1_IBJ.root",
sampleBaseDir+"PATtuple_24_1_uOA.root",
sampleBaseDir+"PATtuple_25_1_d7F.root",
sampleBaseDir+"PATtuple_26_1_wZC.root",
sampleBaseDir+"PATtuple_27_1_Vya.root",
sampleBaseDir+"PATtuple_28_1_7fU.root",
sampleBaseDir+"PATtuple_29_1_jcb.root",
sampleBaseDir+"PATtuple_2_1_fxE.root",
sampleBaseDir+"PATtuple_30_1_Zbo.root",
sampleBaseDir+"PATtuple_31_1_qhH.root",
sampleBaseDir+"PATtuple_32_1_z5g.root",
sampleBaseDir+"PATtuple_33_1_cFB.root",
sampleBaseDir+"PATtuple_34_1_bAL.root",
sampleBaseDir+"PATtuple_35_1_8Hu.root",
sampleBaseDir+"PATtuple_36_1_QjR.root",
sampleBaseDir+"PATtuple_37_1_RaB.root",
sampleBaseDir+"PATtuple_38_1_AqE.root",
sampleBaseDir+"PATtuple_39_1_Ryq.root",
sampleBaseDir+"PATtuple_3_1_cJd.root",
sampleBaseDir+"PATtuple_4_1_hKZ.root",
sampleBaseDir+"PATtuple_5_1_Yzv.root",
sampleBaseDir+"PATtuple_6_1_Gl9.root",
sampleBaseDir+"PATtuple_7_1_yNV.root",
sampleBaseDir+"PATtuple_8_1_3zr.root",
sampleBaseDir+"PATtuple_9_1_4Cn.root",
]
