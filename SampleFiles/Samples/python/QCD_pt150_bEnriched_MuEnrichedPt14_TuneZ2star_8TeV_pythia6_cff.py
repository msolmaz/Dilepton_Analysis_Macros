sampleDataSet = '/QCD_pt150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 5165598

sampleXSec = 579.1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="/store/user/lpcdve/DisplacedLeptons/QCD_pt150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20131211/demattia//QCD_pt150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV-pythia6/QCD_pt150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6_pat_20131211/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_146_1_QIN.root",
sampleBaseDir+"PATtuple_58_1_H71.root",
sampleBaseDir+"PATtuple_34_1_Oz4.root",
sampleBaseDir+"PATtuple_177_1_0hl.root",
sampleBaseDir+"PATtuple_1_1_lZu.root",
sampleBaseDir+"PATtuple_144_1_vzU.root",
sampleBaseDir+"PATtuple_26_1_AmX.root",
sampleBaseDir+"PATtuple_189_1_0OA.root",
sampleBaseDir+"PATtuple_153_1_lnT.root",
sampleBaseDir+"PATtuple_116_1_h9w.root",
sampleBaseDir+"PATtuple_38_1_sdo.root",
sampleBaseDir+"PATtuple_96_1_TTq.root",
sampleBaseDir+"PATtuple_107_1_6LV.root",
sampleBaseDir+"PATtuple_122_1_ZSk.root",
sampleBaseDir+"PATtuple_79_1_Dmb.root",
sampleBaseDir+"PATtuple_148_1_F7z.root",
sampleBaseDir+"PATtuple_30_1_3Hn.root",
sampleBaseDir+"PATtuple_170_1_FW0.root",
sampleBaseDir+"PATtuple_73_1_ADP.root",
sampleBaseDir+"PATtuple_192_1_5ET.root",
sampleBaseDir+"PATtuple_101_1_OrW.root",
sampleBaseDir+"PATtuple_22_1_4Mq.root",
sampleBaseDir+"PATtuple_17_1_k2C.root",
sampleBaseDir+"PATtuple_91_1_pxd.root",
sampleBaseDir+"PATtuple_2_1_bRO.root",
sampleBaseDir+"PATtuple_97_1_ZIb.root",
sampleBaseDir+"PATtuple_7_1_Rwl.root",
sampleBaseDir+"PATtuple_32_1_7ZO.root",
sampleBaseDir+"PATtuple_200_1_OFC.root",
sampleBaseDir+"PATtuple_68_1_saO.root",
sampleBaseDir+"PATtuple_39_1_vzn.root",
sampleBaseDir+"PATtuple_51_1_gNe.root",
sampleBaseDir+"PATtuple_82_1_rW1.root",
sampleBaseDir+"PATtuple_77_1_6SK.root",
sampleBaseDir+"PATtuple_136_1_U96.root",
sampleBaseDir+"PATtuple_156_1_uDJ.root",
sampleBaseDir+"PATtuple_70_1_CGi.root",
sampleBaseDir+"PATtuple_108_1_im4.root",
sampleBaseDir+"PATtuple_28_1_rRp.root",
sampleBaseDir+"PATtuple_114_1_QXx.root",
sampleBaseDir+"PATtuple_195_1_iaq.root",
sampleBaseDir+"PATtuple_191_1_ts7.root",
sampleBaseDir+"PATtuple_88_1_s1M.root",
sampleBaseDir+"PATtuple_69_1_6gj.root",
sampleBaseDir+"PATtuple_49_1_Da1.root",
sampleBaseDir+"PATtuple_199_1_R6N.root",
sampleBaseDir+"PATtuple_9_1_tVL.root",
sampleBaseDir+"PATtuple_111_1_sNE.root",
sampleBaseDir+"PATtuple_127_1_nnb.root",
sampleBaseDir+"PATtuple_12_1_1uB.root",
sampleBaseDir+"PATtuple_56_1_pmm.root",
sampleBaseDir+"PATtuple_55_1_osk.root",
sampleBaseDir+"PATtuple_13_1_bcp.root",
sampleBaseDir+"PATtuple_117_1_rkU.root",
sampleBaseDir+"PATtuple_154_1_XsY.root",
sampleBaseDir+"PATtuple_21_1_XSK.root",
sampleBaseDir+"PATtuple_76_1_58J.root",
sampleBaseDir+"PATtuple_104_1_aDy.root",
sampleBaseDir+"PATtuple_178_1_ftb.root",
sampleBaseDir+"PATtuple_86_1_pT8.root",
sampleBaseDir+"PATtuple_83_1_wVk.root",
sampleBaseDir+"PATtuple_50_1_y2o.root",
sampleBaseDir+"PATtuple_157_1_iRo.root",
sampleBaseDir+"PATtuple_198_1_BjI.root",
sampleBaseDir+"PATtuple_190_1_pk3.root",
sampleBaseDir+"PATtuple_129_1_dhv.root",
sampleBaseDir+"PATtuple_62_1_e00.root",
sampleBaseDir+"PATtuple_194_1_w1S.root",
sampleBaseDir+"PATtuple_23_1_gRT.root",
sampleBaseDir+"PATtuple_64_1_sIJ.root",
sampleBaseDir+"PATtuple_183_1_SMH.root",
sampleBaseDir+"PATtuple_80_1_iki.root",
sampleBaseDir+"PATtuple_120_1_nJy.root",
sampleBaseDir+"PATtuple_171_1_Ff8.root",
sampleBaseDir+"PATtuple_42_1_Rdl.root",
sampleBaseDir+"PATtuple_89_1_fUh.root",
sampleBaseDir+"PATtuple_54_1_ugF.root",
sampleBaseDir+"PATtuple_134_1_ewq.root",
sampleBaseDir+"PATtuple_186_1_Sf5.root",
sampleBaseDir+"PATtuple_61_1_ahU.root",
sampleBaseDir+"PATtuple_10_1_obj.root",
sampleBaseDir+"PATtuple_40_1_zyJ.root",
sampleBaseDir+"PATtuple_31_1_5uK.root",
sampleBaseDir+"PATtuple_143_1_Lda.root",
sampleBaseDir+"PATtuple_94_1_NjP.root",
sampleBaseDir+"PATtuple_53_1_fXJ.root",
sampleBaseDir+"PATtuple_24_1_0j5.root",
sampleBaseDir+"PATtuple_87_1_0lP.root",
sampleBaseDir+"PATtuple_59_1_4eL.root",
sampleBaseDir+"PATtuple_155_1_Hfh.root",
sampleBaseDir+"PATtuple_3_1_UBp.root",
sampleBaseDir+"PATtuple_15_1_Tth.root",
sampleBaseDir+"PATtuple_201_1_goU.root",
sampleBaseDir+"PATtuple_45_1_9Pq.root",
sampleBaseDir+"PATtuple_158_1_ami.root",
sampleBaseDir+"PATtuple_131_1_27j.root",
sampleBaseDir+"PATtuple_74_1_IA6.root",
sampleBaseDir+"PATtuple_57_1_NSz.root",
sampleBaseDir+"PATtuple_152_1_Mq0.root",
sampleBaseDir+"PATtuple_19_1_Eej.root",
sampleBaseDir+"PATtuple_27_1_zXe.root",
sampleBaseDir+"PATtuple_125_1_XY9.root",
sampleBaseDir+"PATtuple_162_1_kQJ.root",
sampleBaseDir+"PATtuple_67_1_sRe.root",
sampleBaseDir+"PATtuple_105_1_A8t.root",
sampleBaseDir+"PATtuple_93_1_UZJ.root",
sampleBaseDir+"PATtuple_124_1_Pa1.root",
sampleBaseDir+"PATtuple_150_1_fTs.root",
sampleBaseDir+"PATtuple_123_1_ryE.root",
]
