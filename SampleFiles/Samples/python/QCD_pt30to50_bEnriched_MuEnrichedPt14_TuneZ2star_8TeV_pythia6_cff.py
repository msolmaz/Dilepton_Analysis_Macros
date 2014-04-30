sampleDataSet = '/QCD_pt30to50_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 5004553

sampleXSec = 41400.0 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_pt30to50_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20140328/demattia//QCD_pt30to50_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/QCD_pt30to50_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_RPk.root",
sampleBaseDir+"PATtuple_101_1_Pl6.root",
sampleBaseDir+"PATtuple_102_1_tF0.root",
sampleBaseDir+"PATtuple_10_1_0Xa.root",
sampleBaseDir+"PATtuple_11_1_rJL.root",
sampleBaseDir+"PATtuple_12_1_EWf.root",
sampleBaseDir+"PATtuple_13_1_J0D.root",
sampleBaseDir+"PATtuple_14_1_52B.root",
sampleBaseDir+"PATtuple_15_1_oUJ.root",
sampleBaseDir+"PATtuple_16_1_Qw4.root",
sampleBaseDir+"PATtuple_17_1_40G.root",
sampleBaseDir+"PATtuple_18_1_2Of.root",
sampleBaseDir+"PATtuple_19_1_vlm.root",
sampleBaseDir+"PATtuple_1_1_OAI.root",
sampleBaseDir+"PATtuple_20_1_Nt9.root",
sampleBaseDir+"PATtuple_21_1_gRv.root",
sampleBaseDir+"PATtuple_22_1_Zdv.root",
sampleBaseDir+"PATtuple_23_1_Z9u.root",
sampleBaseDir+"PATtuple_24_1_duj.root",
sampleBaseDir+"PATtuple_25_1_eWs.root",
sampleBaseDir+"PATtuple_26_1_eZY.root",
sampleBaseDir+"PATtuple_27_1_qPX.root",
sampleBaseDir+"PATtuple_28_1_Z5m.root",
sampleBaseDir+"PATtuple_29_1_65D.root",
sampleBaseDir+"PATtuple_2_1_aOi.root",
sampleBaseDir+"PATtuple_30_1_N68.root",
sampleBaseDir+"PATtuple_31_1_qQA.root",
sampleBaseDir+"PATtuple_32_1_zN6.root",
sampleBaseDir+"PATtuple_33_1_xEz.root",
sampleBaseDir+"PATtuple_34_1_MrL.root",
sampleBaseDir+"PATtuple_35_1_d3N.root",
sampleBaseDir+"PATtuple_36_1_40h.root",
sampleBaseDir+"PATtuple_37_1_5Lr.root",
sampleBaseDir+"PATtuple_38_1_tuQ.root",
sampleBaseDir+"PATtuple_39_1_zAw.root",
sampleBaseDir+"PATtuple_3_1_NBN.root",
sampleBaseDir+"PATtuple_40_1_7RJ.root",
sampleBaseDir+"PATtuple_41_1_LeH.root",
sampleBaseDir+"PATtuple_42_1_aEe.root",
sampleBaseDir+"PATtuple_43_1_Vue.root",
sampleBaseDir+"PATtuple_44_1_IZA.root",
sampleBaseDir+"PATtuple_45_1_oaQ.root",
sampleBaseDir+"PATtuple_46_1_R8w.root",
sampleBaseDir+"PATtuple_47_1_XUo.root",
sampleBaseDir+"PATtuple_48_1_lIL.root",
sampleBaseDir+"PATtuple_49_1_8os.root",
sampleBaseDir+"PATtuple_4_1_m53.root",
sampleBaseDir+"PATtuple_50_1_M3l.root",
sampleBaseDir+"PATtuple_51_1_su0.root",
sampleBaseDir+"PATtuple_52_1_bk4.root",
sampleBaseDir+"PATtuple_53_1_B0O.root",
sampleBaseDir+"PATtuple_54_1_Lk7.root",
sampleBaseDir+"PATtuple_55_1_42D.root",
sampleBaseDir+"PATtuple_56_1_0tC.root",
sampleBaseDir+"PATtuple_57_1_BDW.root",
sampleBaseDir+"PATtuple_58_1_WMJ.root",
sampleBaseDir+"PATtuple_59_1_JPe.root",
sampleBaseDir+"PATtuple_5_1_BGy.root",
sampleBaseDir+"PATtuple_60_1_uWW.root",
sampleBaseDir+"PATtuple_61_1_RJa.root",
sampleBaseDir+"PATtuple_62_1_TZx.root",
sampleBaseDir+"PATtuple_63_1_GL7.root",
sampleBaseDir+"PATtuple_64_1_0rX.root",
sampleBaseDir+"PATtuple_65_1_4aI.root",
sampleBaseDir+"PATtuple_66_1_jus.root",
sampleBaseDir+"PATtuple_67_1_i70.root",
sampleBaseDir+"PATtuple_68_1_Rdv.root",
sampleBaseDir+"PATtuple_69_1_si7.root",
sampleBaseDir+"PATtuple_6_1_ym4.root",
sampleBaseDir+"PATtuple_70_1_nLk.root",
sampleBaseDir+"PATtuple_71_1_TcX.root",
sampleBaseDir+"PATtuple_72_1_tLn.root",
sampleBaseDir+"PATtuple_73_1_Jhr.root",
sampleBaseDir+"PATtuple_74_1_XTK.root",
sampleBaseDir+"PATtuple_75_1_hLc.root",
sampleBaseDir+"PATtuple_76_1_dR4.root",
sampleBaseDir+"PATtuple_77_1_IuR.root",
sampleBaseDir+"PATtuple_78_1_wtL.root",
sampleBaseDir+"PATtuple_79_1_eE3.root",
sampleBaseDir+"PATtuple_7_1_Qog.root",
sampleBaseDir+"PATtuple_80_1_ffP.root",
sampleBaseDir+"PATtuple_81_1_5Hr.root",
sampleBaseDir+"PATtuple_82_1_la7.root",
sampleBaseDir+"PATtuple_83_1_kti.root",
sampleBaseDir+"PATtuple_84_1_Ck7.root",
sampleBaseDir+"PATtuple_85_1_CNy.root",
sampleBaseDir+"PATtuple_86_1_svu.root",
sampleBaseDir+"PATtuple_87_1_YlH.root",
sampleBaseDir+"PATtuple_88_1_J5O.root",
sampleBaseDir+"PATtuple_89_1_ykW.root",
sampleBaseDir+"PATtuple_8_1_jCy.root",
sampleBaseDir+"PATtuple_90_1_NNE.root",
sampleBaseDir+"PATtuple_91_1_n8L.root",
sampleBaseDir+"PATtuple_92_1_IiX.root",
sampleBaseDir+"PATtuple_93_1_qlm.root",
sampleBaseDir+"PATtuple_94_1_JbP.root",
sampleBaseDir+"PATtuple_95_1_fUZ.root",
sampleBaseDir+"PATtuple_96_1_txR.root",
sampleBaseDir+"PATtuple_97_1_rNq.root",
sampleBaseDir+"PATtuple_98_1_Git.root",
sampleBaseDir+"PATtuple_99_1_2kt.root",
sampleBaseDir+"PATtuple_9_1_9bD.root",
]
