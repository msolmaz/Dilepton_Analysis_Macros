sampleDataSet = '/DoubleMu/Run2012A-22Jan2013-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_7_patch5" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_8" 

sampleNumEvents = 5636274 # according to DBS, as of 13 October 2013

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
sampleGlobalTag = 'FT_53_V21_AN3::All'

# data quality run/lumi section selection
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON_MuonPhys.txt"
#sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"






samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Data_Mu_Run2012A22Jan_pat_20140501/demattia//DoubleMu/Data_Mu_Run2012A22Jan_pat_20140501/36c71b423fa00b459b44db94a37da1be/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_sqS.root",
sampleBaseDir+"PATtuple_101_1_OXp.root",
sampleBaseDir+"PATtuple_102_1_6un.root",
sampleBaseDir+"PATtuple_103_1_wEy.root",
sampleBaseDir+"PATtuple_104_1_ZWI.root",
sampleBaseDir+"PATtuple_105_1_SX2.root",
sampleBaseDir+"PATtuple_106_1_83f.root",
sampleBaseDir+"PATtuple_107_1_7Ae.root",
sampleBaseDir+"PATtuple_108_1_BCs.root",
sampleBaseDir+"PATtuple_109_1_IQW.root",
sampleBaseDir+"PATtuple_10_1_elX.root",
sampleBaseDir+"PATtuple_110_1_fcp.root",
sampleBaseDir+"PATtuple_111_1_V8j.root",
sampleBaseDir+"PATtuple_112_1_Y3j.root",
sampleBaseDir+"PATtuple_113_1_OyJ.root",
sampleBaseDir+"PATtuple_114_1_UhH.root",
sampleBaseDir+"PATtuple_115_1_D52.root",
sampleBaseDir+"PATtuple_116_1_Yja.root",
sampleBaseDir+"PATtuple_117_1_G80.root",
sampleBaseDir+"PATtuple_118_1_e91.root",
sampleBaseDir+"PATtuple_119_1_cpy.root",
sampleBaseDir+"PATtuple_11_1_JFF.root",
sampleBaseDir+"PATtuple_120_1_WFX.root",
sampleBaseDir+"PATtuple_121_1_m93.root",
sampleBaseDir+"PATtuple_122_1_oKw.root",
sampleBaseDir+"PATtuple_123_1_kbj.root",
sampleBaseDir+"PATtuple_124_1_SIi.root",
sampleBaseDir+"PATtuple_125_1_fVJ.root",
sampleBaseDir+"PATtuple_126_1_3Yn.root",
sampleBaseDir+"PATtuple_127_1_w1D.root",
sampleBaseDir+"PATtuple_128_1_2Dr.root",
sampleBaseDir+"PATtuple_129_1_Wac.root",
sampleBaseDir+"PATtuple_12_1_wFg.root",
sampleBaseDir+"PATtuple_130_1_th0.root",
sampleBaseDir+"PATtuple_131_1_M4q.root",
sampleBaseDir+"PATtuple_132_1_hY7.root",
sampleBaseDir+"PATtuple_133_1_CLf.root",
sampleBaseDir+"PATtuple_134_1_XLu.root",
sampleBaseDir+"PATtuple_135_1_6AN.root",
sampleBaseDir+"PATtuple_136_1_61L.root",
sampleBaseDir+"PATtuple_137_1_f5v.root",
sampleBaseDir+"PATtuple_138_1_mBl.root",
sampleBaseDir+"PATtuple_139_1_6xV.root",
sampleBaseDir+"PATtuple_13_1_N28.root",
sampleBaseDir+"PATtuple_140_1_q7v.root",
sampleBaseDir+"PATtuple_141_1_Hxk.root",
sampleBaseDir+"PATtuple_142_1_RH1.root",
sampleBaseDir+"PATtuple_143_1_dAI.root",
sampleBaseDir+"PATtuple_144_1_pcY.root",
sampleBaseDir+"PATtuple_145_1_T9J.root",
sampleBaseDir+"PATtuple_146_1_Abr.root",
sampleBaseDir+"PATtuple_147_1_RK4.root",
sampleBaseDir+"PATtuple_148_1_16X.root",
sampleBaseDir+"PATtuple_149_1_uaI.root",
sampleBaseDir+"PATtuple_14_1_RyI.root",
sampleBaseDir+"PATtuple_150_1_l5G.root",
sampleBaseDir+"PATtuple_151_1_4N6.root",
sampleBaseDir+"PATtuple_152_1_2RJ.root",
sampleBaseDir+"PATtuple_153_1_09N.root",
sampleBaseDir+"PATtuple_154_1_LYS.root",
sampleBaseDir+"PATtuple_155_1_9W5.root",
sampleBaseDir+"PATtuple_156_1_CrH.root",
sampleBaseDir+"PATtuple_157_1_JUC.root",
sampleBaseDir+"PATtuple_158_1_MEG.root",
sampleBaseDir+"PATtuple_159_1_c1f.root",
sampleBaseDir+"PATtuple_15_1_Yb4.root",
sampleBaseDir+"PATtuple_160_1_hvk.root",
sampleBaseDir+"PATtuple_161_1_rUU.root",
sampleBaseDir+"PATtuple_162_1_dlS.root",
sampleBaseDir+"PATtuple_163_1_nWR.root",
sampleBaseDir+"PATtuple_164_1_8ao.root",
sampleBaseDir+"PATtuple_165_1_yLg.root",
sampleBaseDir+"PATtuple_166_1_J2q.root",
sampleBaseDir+"PATtuple_167_1_wqB.root",
sampleBaseDir+"PATtuple_168_1_N7I.root",
sampleBaseDir+"PATtuple_169_1_VU5.root",
sampleBaseDir+"PATtuple_16_1_K86.root",
sampleBaseDir+"PATtuple_170_1_MzJ.root",
sampleBaseDir+"PATtuple_171_1_NQn.root",
sampleBaseDir+"PATtuple_172_1_wZt.root",
sampleBaseDir+"PATtuple_173_1_axi.root",
sampleBaseDir+"PATtuple_174_1_8B3.root",
sampleBaseDir+"PATtuple_175_1_Mrd.root",
sampleBaseDir+"PATtuple_176_1_eQI.root",
sampleBaseDir+"PATtuple_177_1_PY3.root",
sampleBaseDir+"PATtuple_178_1_wty.root",
sampleBaseDir+"PATtuple_179_1_gc1.root",
sampleBaseDir+"PATtuple_17_1_h6d.root",
sampleBaseDir+"PATtuple_180_1_Its.root",
sampleBaseDir+"PATtuple_181_1_8oW.root",
sampleBaseDir+"PATtuple_182_1_HiU.root",
sampleBaseDir+"PATtuple_183_1_4Ad.root",
sampleBaseDir+"PATtuple_184_1_DUL.root",
sampleBaseDir+"PATtuple_185_1_ChJ.root",
sampleBaseDir+"PATtuple_186_1_lXk.root",
sampleBaseDir+"PATtuple_187_1_Q9v.root",
sampleBaseDir+"PATtuple_188_1_OPK.root",
sampleBaseDir+"PATtuple_189_1_bRR.root",
sampleBaseDir+"PATtuple_18_1_J0W.root",
sampleBaseDir+"PATtuple_190_1_bmg.root",
sampleBaseDir+"PATtuple_191_1_xu5.root",
sampleBaseDir+"PATtuple_192_1_Exp.root",
sampleBaseDir+"PATtuple_193_1_LLe.root",
sampleBaseDir+"PATtuple_194_1_JV7.root",
sampleBaseDir+"PATtuple_195_1_Uzs.root",
sampleBaseDir+"PATtuple_196_1_TpM.root",
sampleBaseDir+"PATtuple_197_1_kbp.root",
sampleBaseDir+"PATtuple_198_1_m3U.root",
sampleBaseDir+"PATtuple_199_1_akV.root",
sampleBaseDir+"PATtuple_19_1_Jd0.root",
sampleBaseDir+"PATtuple_1_1_sab.root",
sampleBaseDir+"PATtuple_200_1_e7W.root",
sampleBaseDir+"PATtuple_201_1_tak.root",
sampleBaseDir+"PATtuple_202_1_T3B.root",
sampleBaseDir+"PATtuple_203_1_rZr.root",
sampleBaseDir+"PATtuple_204_1_VpG.root",
sampleBaseDir+"PATtuple_205_1_kOG.root",
sampleBaseDir+"PATtuple_206_1_Dru.root",
sampleBaseDir+"PATtuple_207_1_5ur.root",
sampleBaseDir+"PATtuple_208_1_C4U.root",
sampleBaseDir+"PATtuple_209_1_WhI.root",
sampleBaseDir+"PATtuple_20_1_0bv.root",
sampleBaseDir+"PATtuple_210_1_IQW.root",
sampleBaseDir+"PATtuple_211_1_DnU.root",
sampleBaseDir+"PATtuple_212_1_Ohe.root",
sampleBaseDir+"PATtuple_213_1_dUW.root",
sampleBaseDir+"PATtuple_214_1_nww.root",
sampleBaseDir+"PATtuple_215_1_Bxo.root",
sampleBaseDir+"PATtuple_216_1_5kN.root",
sampleBaseDir+"PATtuple_217_1_iUL.root",
sampleBaseDir+"PATtuple_218_1_Pxz.root",
sampleBaseDir+"PATtuple_219_1_6TP.root",
sampleBaseDir+"PATtuple_21_1_Bq2.root",
sampleBaseDir+"PATtuple_220_1_Dve.root",
sampleBaseDir+"PATtuple_221_1_iSV.root",
sampleBaseDir+"PATtuple_222_1_6ul.root",
sampleBaseDir+"PATtuple_223_1_V2e.root",
sampleBaseDir+"PATtuple_224_1_dsf.root",
sampleBaseDir+"PATtuple_225_1_xh7.root",
sampleBaseDir+"PATtuple_226_1_kEe.root",
sampleBaseDir+"PATtuple_227_1_hUO.root",
sampleBaseDir+"PATtuple_228_1_REX.root",
sampleBaseDir+"PATtuple_229_1_BGa.root",
sampleBaseDir+"PATtuple_22_1_TAW.root",
sampleBaseDir+"PATtuple_230_1_56k.root",
sampleBaseDir+"PATtuple_231_1_azx.root",
sampleBaseDir+"PATtuple_232_1_lKX.root",
sampleBaseDir+"PATtuple_233_1_Voy.root",
sampleBaseDir+"PATtuple_234_1_uwS.root",
sampleBaseDir+"PATtuple_235_1_6U8.root",
sampleBaseDir+"PATtuple_236_1_2kM.root",
sampleBaseDir+"PATtuple_237_1_Scz.root",
sampleBaseDir+"PATtuple_238_1_MdG.root",
sampleBaseDir+"PATtuple_239_1_wBW.root",
sampleBaseDir+"PATtuple_23_1_eVE.root",
sampleBaseDir+"PATtuple_240_1_VOT.root",
sampleBaseDir+"PATtuple_241_1_737.root",
sampleBaseDir+"PATtuple_242_1_WdU.root",
sampleBaseDir+"PATtuple_243_1_A7O.root",
sampleBaseDir+"PATtuple_244_1_BTz.root",
sampleBaseDir+"PATtuple_245_1_elC.root",
sampleBaseDir+"PATtuple_246_1_IJP.root",
sampleBaseDir+"PATtuple_247_1_UWz.root",
sampleBaseDir+"PATtuple_248_1_8Wt.root",
sampleBaseDir+"PATtuple_249_1_uq6.root",
sampleBaseDir+"PATtuple_24_1_icr.root",
sampleBaseDir+"PATtuple_250_1_2qQ.root",
sampleBaseDir+"PATtuple_251_1_dVd.root",
sampleBaseDir+"PATtuple_252_1_4mk.root",
sampleBaseDir+"PATtuple_253_1_D3r.root",
sampleBaseDir+"PATtuple_254_1_mcS.root",
sampleBaseDir+"PATtuple_255_1_BgB.root",
sampleBaseDir+"PATtuple_256_1_BNT.root",
sampleBaseDir+"PATtuple_257_1_TnR.root",
sampleBaseDir+"PATtuple_258_1_wb0.root",
sampleBaseDir+"PATtuple_259_1_4yJ.root",
sampleBaseDir+"PATtuple_25_1_5hj.root",
sampleBaseDir+"PATtuple_260_1_i4h.root",
sampleBaseDir+"PATtuple_261_1_OsQ.root",
sampleBaseDir+"PATtuple_262_1_5U0.root",
sampleBaseDir+"PATtuple_263_1_pul.root",
sampleBaseDir+"PATtuple_264_1_mNB.root",
sampleBaseDir+"PATtuple_265_1_ulA.root",
sampleBaseDir+"PATtuple_266_1_t7F.root",
sampleBaseDir+"PATtuple_267_1_To5.root",
sampleBaseDir+"PATtuple_268_1_OBm.root",
sampleBaseDir+"PATtuple_269_1_rCh.root",
sampleBaseDir+"PATtuple_26_1_LAf.root",
sampleBaseDir+"PATtuple_270_1_8Q2.root",
sampleBaseDir+"PATtuple_271_1_oYX.root",
sampleBaseDir+"PATtuple_272_1_YbU.root",
sampleBaseDir+"PATtuple_273_1_CEi.root",
sampleBaseDir+"PATtuple_274_1_g0B.root",
sampleBaseDir+"PATtuple_275_1_ipz.root",
sampleBaseDir+"PATtuple_276_1_Qkp.root",
sampleBaseDir+"PATtuple_277_1_BMd.root",
sampleBaseDir+"PATtuple_278_1_3If.root",
sampleBaseDir+"PATtuple_279_1_o6a.root",
sampleBaseDir+"PATtuple_27_1_M4v.root",
sampleBaseDir+"PATtuple_280_1_Z3y.root",
sampleBaseDir+"PATtuple_281_1_P1W.root",
sampleBaseDir+"PATtuple_282_1_JuM.root",
sampleBaseDir+"PATtuple_283_1_z3C.root",
sampleBaseDir+"PATtuple_284_1_xHY.root",
sampleBaseDir+"PATtuple_285_1_jYW.root",
sampleBaseDir+"PATtuple_286_1_nH1.root",
sampleBaseDir+"PATtuple_287_1_aR9.root",
sampleBaseDir+"PATtuple_288_1_S2t.root",
sampleBaseDir+"PATtuple_289_1_fDP.root",
sampleBaseDir+"PATtuple_28_1_PE7.root",
sampleBaseDir+"PATtuple_290_1_b6p.root",
sampleBaseDir+"PATtuple_291_1_VMJ.root",
sampleBaseDir+"PATtuple_292_1_zWO.root",
sampleBaseDir+"PATtuple_293_1_HZw.root",
sampleBaseDir+"PATtuple_294_1_Ua6.root",
sampleBaseDir+"PATtuple_295_1_cZT.root",
sampleBaseDir+"PATtuple_296_1_52M.root",
sampleBaseDir+"PATtuple_297_1_h4Z.root",
sampleBaseDir+"PATtuple_298_1_vQC.root",
sampleBaseDir+"PATtuple_299_1_uoN.root",
sampleBaseDir+"PATtuple_29_1_6H7.root",
sampleBaseDir+"PATtuple_2_1_qdJ.root",
sampleBaseDir+"PATtuple_300_1_BdQ.root",
sampleBaseDir+"PATtuple_301_1_0Mx.root",
sampleBaseDir+"PATtuple_302_1_ZYi.root",
sampleBaseDir+"PATtuple_303_1_2IY.root",
sampleBaseDir+"PATtuple_304_1_wdU.root",
sampleBaseDir+"PATtuple_305_1_PsP.root",
sampleBaseDir+"PATtuple_306_1_f3D.root",
sampleBaseDir+"PATtuple_307_1_xUG.root",
sampleBaseDir+"PATtuple_308_1_Xf0.root",
sampleBaseDir+"PATtuple_309_1_Rw0.root",
sampleBaseDir+"PATtuple_30_1_vQ6.root",
sampleBaseDir+"PATtuple_310_1_Xye.root",
sampleBaseDir+"PATtuple_311_1_uFI.root",
sampleBaseDir+"PATtuple_312_1_AzR.root",
sampleBaseDir+"PATtuple_313_1_082.root",
sampleBaseDir+"PATtuple_314_1_WnC.root",
sampleBaseDir+"PATtuple_315_1_xNj.root",
sampleBaseDir+"PATtuple_316_1_8ph.root",
sampleBaseDir+"PATtuple_317_1_VtA.root",
sampleBaseDir+"PATtuple_318_1_77L.root",
sampleBaseDir+"PATtuple_319_1_BW3.root",
sampleBaseDir+"PATtuple_31_1_VrE.root",
sampleBaseDir+"PATtuple_320_1_2tA.root",
sampleBaseDir+"PATtuple_321_1_mRa.root",
sampleBaseDir+"PATtuple_322_1_ctM.root",
sampleBaseDir+"PATtuple_323_1_nbA.root",
sampleBaseDir+"PATtuple_324_1_N7R.root",
sampleBaseDir+"PATtuple_325_1_Q6n.root",
sampleBaseDir+"PATtuple_326_1_grB.root",
sampleBaseDir+"PATtuple_327_1_S4x.root",
sampleBaseDir+"PATtuple_328_1_rg5.root",
sampleBaseDir+"PATtuple_329_1_vYg.root",
sampleBaseDir+"PATtuple_32_1_6wb.root",
sampleBaseDir+"PATtuple_33_1_U7B.root",
sampleBaseDir+"PATtuple_34_1_JbE.root",
sampleBaseDir+"PATtuple_35_1_oZp.root",
sampleBaseDir+"PATtuple_36_1_TdT.root",
sampleBaseDir+"PATtuple_37_1_GN3.root",
sampleBaseDir+"PATtuple_38_1_CmU.root",
sampleBaseDir+"PATtuple_39_1_g9J.root",
sampleBaseDir+"PATtuple_3_1_ikV.root",
sampleBaseDir+"PATtuple_40_1_D1B.root",
sampleBaseDir+"PATtuple_41_1_WOW.root",
sampleBaseDir+"PATtuple_42_1_Kef.root",
sampleBaseDir+"PATtuple_43_1_gHq.root",
sampleBaseDir+"PATtuple_44_1_xH5.root",
sampleBaseDir+"PATtuple_45_1_QF7.root",
sampleBaseDir+"PATtuple_46_1_x4K.root",
sampleBaseDir+"PATtuple_47_1_UGc.root",
sampleBaseDir+"PATtuple_48_1_aP0.root",
sampleBaseDir+"PATtuple_49_1_SYj.root",
sampleBaseDir+"PATtuple_4_1_5vN.root",
sampleBaseDir+"PATtuple_50_1_pbb.root",
sampleBaseDir+"PATtuple_51_1_gg6.root",
sampleBaseDir+"PATtuple_52_1_Hvk.root",
sampleBaseDir+"PATtuple_53_1_D5z.root",
sampleBaseDir+"PATtuple_54_1_F7e.root",
sampleBaseDir+"PATtuple_55_1_qSA.root",
sampleBaseDir+"PATtuple_56_1_oTx.root",
sampleBaseDir+"PATtuple_57_1_PlU.root",
sampleBaseDir+"PATtuple_58_1_Uzc.root",
sampleBaseDir+"PATtuple_59_1_K11.root",
sampleBaseDir+"PATtuple_5_1_muX.root",
sampleBaseDir+"PATtuple_60_1_izA.root",
sampleBaseDir+"PATtuple_61_1_QP5.root",
sampleBaseDir+"PATtuple_62_1_NQR.root",
sampleBaseDir+"PATtuple_63_1_vtJ.root",
sampleBaseDir+"PATtuple_64_1_t25.root",
sampleBaseDir+"PATtuple_65_1_KI0.root",
sampleBaseDir+"PATtuple_66_1_wxL.root",
sampleBaseDir+"PATtuple_67_1_hoP.root",
sampleBaseDir+"PATtuple_68_1_A4M.root",
sampleBaseDir+"PATtuple_69_1_JTM.root",
sampleBaseDir+"PATtuple_6_1_RF7.root",
sampleBaseDir+"PATtuple_70_1_HXE.root",
sampleBaseDir+"PATtuple_71_1_PVm.root",
sampleBaseDir+"PATtuple_72_1_aha.root",
sampleBaseDir+"PATtuple_73_1_cvx.root",
sampleBaseDir+"PATtuple_74_1_QUn.root",
sampleBaseDir+"PATtuple_75_1_QSz.root",
sampleBaseDir+"PATtuple_76_1_ubz.root",
sampleBaseDir+"PATtuple_77_1_hmG.root",
sampleBaseDir+"PATtuple_78_1_2c4.root",
sampleBaseDir+"PATtuple_79_1_bi3.root",
sampleBaseDir+"PATtuple_7_1_ScQ.root",
sampleBaseDir+"PATtuple_80_1_aAM.root",
sampleBaseDir+"PATtuple_81_1_2eD.root",
sampleBaseDir+"PATtuple_82_1_85q.root",
sampleBaseDir+"PATtuple_83_1_Axw.root",
sampleBaseDir+"PATtuple_84_1_dw7.root",
sampleBaseDir+"PATtuple_85_1_vWJ.root",
sampleBaseDir+"PATtuple_86_1_QPn.root",
sampleBaseDir+"PATtuple_87_1_KkM.root",
sampleBaseDir+"PATtuple_88_1_W8g.root",
sampleBaseDir+"PATtuple_89_1_Vdv.root",
sampleBaseDir+"PATtuple_8_1_2JF.root",
sampleBaseDir+"PATtuple_90_1_qR8.root",
sampleBaseDir+"PATtuple_91_1_T2u.root",
sampleBaseDir+"PATtuple_92_1_5b4.root",
sampleBaseDir+"PATtuple_93_1_ayK.root",
sampleBaseDir+"PATtuple_94_1_EIN.root",
sampleBaseDir+"PATtuple_95_1_tyg.root",
sampleBaseDir+"PATtuple_96_1_BiK.root",
sampleBaseDir+"PATtuple_97_1_9aR.root",
sampleBaseDir+"PATtuple_98_1_f1z.root",
sampleBaseDir+"PATtuple_99_1_vMM.root",
sampleBaseDir+"PATtuple_9_1_864.root",
]
