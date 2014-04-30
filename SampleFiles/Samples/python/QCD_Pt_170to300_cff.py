sampleDataSet = '/QCD_Pt-170to300_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 5814398

sampleXSec = 1 # pb <- this needs to be found

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_Pt_170to300_pat_20140328/demattia//QCD_Pt-170to300_TuneZ2star_8TeV_pythia6/QCD_Pt_170to300_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_101_1_tmh.root",
sampleBaseDir+"PATtuple_102_1_YF5.root",
sampleBaseDir+"PATtuple_103_1_7BQ.root",
sampleBaseDir+"PATtuple_104_1_EIN.root",
sampleBaseDir+"PATtuple_105_1_FP5.root",
sampleBaseDir+"PATtuple_106_1_kWM.root",
sampleBaseDir+"PATtuple_108_1_3H2.root",
sampleBaseDir+"PATtuple_109_1_tyf.root",
sampleBaseDir+"PATtuple_110_1_oES.root",
sampleBaseDir+"PATtuple_111_1_Pn8.root",
sampleBaseDir+"PATtuple_112_1_NiV.root",
sampleBaseDir+"PATtuple_114_1_RK6.root",
sampleBaseDir+"PATtuple_115_1_jLn.root",
sampleBaseDir+"PATtuple_117_1_jjo.root",
sampleBaseDir+"PATtuple_118_1_qzJ.root",
sampleBaseDir+"PATtuple_11_1_g5R.root",
sampleBaseDir+"PATtuple_12_1_9vr.root",
sampleBaseDir+"PATtuple_13_1_yZH.root",
sampleBaseDir+"PATtuple_14_1_xtj.root",
sampleBaseDir+"PATtuple_15_1_kkI.root",
sampleBaseDir+"PATtuple_16_1_BSB.root",
sampleBaseDir+"PATtuple_17_1_804.root",
sampleBaseDir+"PATtuple_18_1_CTO.root",
sampleBaseDir+"PATtuple_19_1_SN9.root",
sampleBaseDir+"PATtuple_1_1_cFI.root",
sampleBaseDir+"PATtuple_20_1_fVy.root",
sampleBaseDir+"PATtuple_21_1_Jsx.root",
sampleBaseDir+"PATtuple_22_1_eSe.root",
sampleBaseDir+"PATtuple_23_1_8lr.root",
sampleBaseDir+"PATtuple_24_1_Igb.root",
sampleBaseDir+"PATtuple_25_1_M1J.root",
sampleBaseDir+"PATtuple_26_1_FpY.root",
sampleBaseDir+"PATtuple_27_1_9MB.root",
sampleBaseDir+"PATtuple_28_1_NYw.root",
sampleBaseDir+"PATtuple_29_1_V8W.root",
sampleBaseDir+"PATtuple_2_1_1Os.root",
sampleBaseDir+"PATtuple_30_1_63i.root",
sampleBaseDir+"PATtuple_31_1_F3U.root",
sampleBaseDir+"PATtuple_32_1_87d.root",
sampleBaseDir+"PATtuple_33_1_9ra.root",
sampleBaseDir+"PATtuple_34_1_Rz9.root",
sampleBaseDir+"PATtuple_35_1_nKv.root",
sampleBaseDir+"PATtuple_36_1_KlF.root",
sampleBaseDir+"PATtuple_37_1_4tk.root",
sampleBaseDir+"PATtuple_38_1_2Kk.root",
sampleBaseDir+"PATtuple_39_1_Fik.root",
sampleBaseDir+"PATtuple_3_1_5td.root",
sampleBaseDir+"PATtuple_40_1_sgN.root",
sampleBaseDir+"PATtuple_41_1_COv.root",
sampleBaseDir+"PATtuple_42_1_uqD.root",
sampleBaseDir+"PATtuple_43_1_3Fl.root",
sampleBaseDir+"PATtuple_44_1_bOV.root",
sampleBaseDir+"PATtuple_45_1_Q22.root",
sampleBaseDir+"PATtuple_46_1_Ul5.root",
sampleBaseDir+"PATtuple_48_1_WhG.root",
sampleBaseDir+"PATtuple_49_1_I6E.root",
sampleBaseDir+"PATtuple_4_1_4V8.root",
sampleBaseDir+"PATtuple_50_1_qsH.root",
sampleBaseDir+"PATtuple_51_1_IHt.root",
sampleBaseDir+"PATtuple_52_1_gAJ.root",
sampleBaseDir+"PATtuple_53_1_rTD.root",
sampleBaseDir+"PATtuple_54_1_NOo.root",
sampleBaseDir+"PATtuple_55_1_6QZ.root",
sampleBaseDir+"PATtuple_57_1_Fwg.root",
sampleBaseDir+"PATtuple_58_1_guB.root",
sampleBaseDir+"PATtuple_5_1_ARP.root",
sampleBaseDir+"PATtuple_60_1_wQ5.root",
sampleBaseDir+"PATtuple_61_1_sFl.root",
sampleBaseDir+"PATtuple_62_1_8JZ.root",
sampleBaseDir+"PATtuple_63_1_loG.root",
sampleBaseDir+"PATtuple_64_1_x2Y.root",
sampleBaseDir+"PATtuple_65_1_jLh.root",
sampleBaseDir+"PATtuple_66_1_whN.root",
sampleBaseDir+"PATtuple_67_1_mpw.root",
sampleBaseDir+"PATtuple_68_1_bWq.root",
sampleBaseDir+"PATtuple_69_1_3ES.root",
sampleBaseDir+"PATtuple_6_1_vjz.root",
sampleBaseDir+"PATtuple_70_1_gTK.root",
sampleBaseDir+"PATtuple_71_1_TbF.root",
sampleBaseDir+"PATtuple_72_1_tCj.root",
sampleBaseDir+"PATtuple_73_1_dLA.root",
sampleBaseDir+"PATtuple_74_1_zn7.root",
sampleBaseDir+"PATtuple_75_1_vzV.root",
sampleBaseDir+"PATtuple_76_1_Qos.root",
sampleBaseDir+"PATtuple_77_1_FMq.root",
sampleBaseDir+"PATtuple_78_1_ah0.root",
sampleBaseDir+"PATtuple_7_1_Dvj.root",
sampleBaseDir+"PATtuple_80_1_GpY.root",
sampleBaseDir+"PATtuple_81_1_Rf5.root",
sampleBaseDir+"PATtuple_82_1_YC7.root",
sampleBaseDir+"PATtuple_83_1_ey7.root",
sampleBaseDir+"PATtuple_85_1_zcm.root",
sampleBaseDir+"PATtuple_86_1_pHM.root",
sampleBaseDir+"PATtuple_87_1_rNK.root",
sampleBaseDir+"PATtuple_88_1_PT9.root",
sampleBaseDir+"PATtuple_89_1_ri2.root",
sampleBaseDir+"PATtuple_8_1_Dt3.root",
sampleBaseDir+"PATtuple_90_1_Hz0.root",
sampleBaseDir+"PATtuple_91_1_aCN.root",
sampleBaseDir+"PATtuple_92_1_YaM.root",
sampleBaseDir+"PATtuple_93_1_als.root",
sampleBaseDir+"PATtuple_94_1_X0t.root",
sampleBaseDir+"PATtuple_95_1_yT9.root",
sampleBaseDir+"PATtuple_96_1_QaC.root",
sampleBaseDir+"PATtuple_97_1_wCn.root",
sampleBaseDir+"PATtuple_98_1_PLm.root",
sampleBaseDir+"PATtuple_99_1_Q82.root",
sampleBaseDir+"PATtuple_9_1_Mee.root",
]
