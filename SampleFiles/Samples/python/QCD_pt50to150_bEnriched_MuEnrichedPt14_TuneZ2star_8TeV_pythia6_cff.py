sampleDataSet = '/QCD_pt50to150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 4865103

sampleXSec = 22450.0 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/QCD_pt50to150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20140328/demattia//QCD_pt50to150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/QCD_pt50to150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_8xY.root",
sampleBaseDir+"PATtuple_11_1_wYX.root",
sampleBaseDir+"PATtuple_12_1_th5.root",
sampleBaseDir+"PATtuple_13_1_LKp.root",
sampleBaseDir+"PATtuple_14_1_adS.root",
sampleBaseDir+"PATtuple_15_1_o96.root",
sampleBaseDir+"PATtuple_16_1_nX8.root",
sampleBaseDir+"PATtuple_17_1_VI3.root",
sampleBaseDir+"PATtuple_18_1_OhH.root",
sampleBaseDir+"PATtuple_19_1_Cy2.root",
sampleBaseDir+"PATtuple_1_1_DLL.root",
sampleBaseDir+"PATtuple_20_1_Oid.root",
sampleBaseDir+"PATtuple_21_1_v2I.root",
sampleBaseDir+"PATtuple_22_1_rBR.root",
sampleBaseDir+"PATtuple_23_1_exL.root",
sampleBaseDir+"PATtuple_24_1_u2p.root",
sampleBaseDir+"PATtuple_25_1_tr2.root",
sampleBaseDir+"PATtuple_26_1_v9W.root",
sampleBaseDir+"PATtuple_27_1_tQE.root",
sampleBaseDir+"PATtuple_28_1_rrt.root",
sampleBaseDir+"PATtuple_29_1_E8D.root",
sampleBaseDir+"PATtuple_2_1_AVj.root",
sampleBaseDir+"PATtuple_30_1_UkF.root",
sampleBaseDir+"PATtuple_31_1_VhD.root",
sampleBaseDir+"PATtuple_32_1_hgr.root",
sampleBaseDir+"PATtuple_33_1_aTj.root",
sampleBaseDir+"PATtuple_34_1_aqt.root",
sampleBaseDir+"PATtuple_35_1_n28.root",
sampleBaseDir+"PATtuple_36_1_Eu9.root",
sampleBaseDir+"PATtuple_37_1_fH9.root",
sampleBaseDir+"PATtuple_38_1_K1L.root",
sampleBaseDir+"PATtuple_39_1_1Rp.root",
sampleBaseDir+"PATtuple_3_1_e1m.root",
sampleBaseDir+"PATtuple_40_1_K5W.root",
sampleBaseDir+"PATtuple_41_1_P3h.root",
sampleBaseDir+"PATtuple_42_1_Otx.root",
sampleBaseDir+"PATtuple_44_1_V5H.root",
sampleBaseDir+"PATtuple_45_1_xbO.root",
sampleBaseDir+"PATtuple_46_1_k2I.root",
sampleBaseDir+"PATtuple_47_1_y3g.root",
sampleBaseDir+"PATtuple_48_1_dwT.root",
sampleBaseDir+"PATtuple_49_1_4Ke.root",
sampleBaseDir+"PATtuple_4_1_HWj.root",
sampleBaseDir+"PATtuple_50_1_L2U.root",
sampleBaseDir+"PATtuple_51_1_VHA.root",
sampleBaseDir+"PATtuple_52_1_bTA.root",
sampleBaseDir+"PATtuple_53_1_RzO.root",
sampleBaseDir+"PATtuple_54_1_t14.root",
sampleBaseDir+"PATtuple_55_1_eb7.root",
sampleBaseDir+"PATtuple_56_1_Z2e.root",
sampleBaseDir+"PATtuple_57_1_VTe.root",
sampleBaseDir+"PATtuple_58_1_scO.root",
sampleBaseDir+"PATtuple_59_1_WQb.root",
sampleBaseDir+"PATtuple_5_1_SnZ.root",
sampleBaseDir+"PATtuple_60_1_hhy.root",
sampleBaseDir+"PATtuple_61_1_Ex9.root",
sampleBaseDir+"PATtuple_62_1_sUK.root",
sampleBaseDir+"PATtuple_63_1_fjs.root",
sampleBaseDir+"PATtuple_64_1_Bm8.root",
sampleBaseDir+"PATtuple_65_1_dd6.root",
sampleBaseDir+"PATtuple_66_1_sES.root",
sampleBaseDir+"PATtuple_67_1_rWp.root",
sampleBaseDir+"PATtuple_68_1_006.root",
sampleBaseDir+"PATtuple_69_1_4wM.root",
sampleBaseDir+"PATtuple_6_1_k27.root",
sampleBaseDir+"PATtuple_70_1_G4A.root",
sampleBaseDir+"PATtuple_71_1_TGn.root",
sampleBaseDir+"PATtuple_72_1_7d8.root",
sampleBaseDir+"PATtuple_73_1_64N.root",
sampleBaseDir+"PATtuple_74_1_Vlc.root",
sampleBaseDir+"PATtuple_75_1_wUT.root",
sampleBaseDir+"PATtuple_76_1_H5j.root",
sampleBaseDir+"PATtuple_77_1_p48.root",
sampleBaseDir+"PATtuple_78_1_Hsq.root",
sampleBaseDir+"PATtuple_79_1_G7b.root",
sampleBaseDir+"PATtuple_7_1_TVj.root",
sampleBaseDir+"PATtuple_80_1_p7X.root",
sampleBaseDir+"PATtuple_81_1_hgb.root",
sampleBaseDir+"PATtuple_82_1_AKh.root",
sampleBaseDir+"PATtuple_83_1_u5g.root",
sampleBaseDir+"PATtuple_84_1_ayl.root",
sampleBaseDir+"PATtuple_85_1_HXg.root",
sampleBaseDir+"PATtuple_86_1_vlL.root",
sampleBaseDir+"PATtuple_87_1_xbW.root",
sampleBaseDir+"PATtuple_88_1_Iwd.root",
sampleBaseDir+"PATtuple_89_1_1ir.root",
sampleBaseDir+"PATtuple_8_1_LKm.root",
sampleBaseDir+"PATtuple_90_1_jJ6.root",
sampleBaseDir+"PATtuple_91_1_CxY.root",
sampleBaseDir+"PATtuple_92_1_YjI.root",
sampleBaseDir+"PATtuple_93_1_mmm.root",
sampleBaseDir+"PATtuple_94_1_MUo.root",
sampleBaseDir+"PATtuple_95_1_oqP.root",
sampleBaseDir+"PATtuple_96_1_PsP.root",
sampleBaseDir+"PATtuple_97_1_O2B.root",
sampleBaseDir+"PATtuple_98_1_o3C.root",
sampleBaseDir+"PATtuple_9_1_JGF.root",
]
