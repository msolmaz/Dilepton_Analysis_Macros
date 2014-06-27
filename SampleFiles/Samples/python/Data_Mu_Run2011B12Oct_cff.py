sampleDataSet = '/DoubleMu/Run2011B-12Oct2013-v1/AOD'

# original (i.e. RECO file) release,
# not the one we plan to process them with
sampleRelease = "CMSSW_5_3_7_patch5" 
# release used to create new files with
sampleProcessRelease = "CMSSW_5_3_8" 

sampleNumEvents = 39668813 # according to DBS, as of 13 October 2013

# global tag needs to be chosen to match release, trigger menu and alignment conditions.
# see https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrontierConditions
#sampleGlobalTag = 'FT_53_V21_AN3::All'
sampleGlobalTag = 'FT_53_LV5_AN1::All'

# data quality run/lumi section selection
#sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON_MuonPhys.txt"
#sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt"
sampleJSON = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions11/7TeV/Reprocessing/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON_v2.txt"

# restrict run range (mainly to get a sample with consistent trigger configuration)

# use checkAllFilesOpened whenever possible, and noDuplicateCheck when necessary
sampleDuplicateCheckMode = "checkAllFilesOpened"

# "DATA" or "MC"
sampleType = "DATA"










samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/Data_Mu_Run2011B12Oct_pat_20140624/zhenhu//DoubleMu/Data_Mu_Run2011B12Oct_pat_20140624/702dc91834f3a02ee06566a4974241f2/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_lCl.root",
sampleBaseDir+"PATtuple_101_1_Zt4.root",
sampleBaseDir+"PATtuple_102_1_e7n.root",
sampleBaseDir+"PATtuple_103_1_YB5.root",
sampleBaseDir+"PATtuple_104_1_k5z.root",
sampleBaseDir+"PATtuple_105_1_PEc.root",
sampleBaseDir+"PATtuple_106_1_u8B.root",
sampleBaseDir+"PATtuple_107_1_4CA.root",
sampleBaseDir+"PATtuple_108_1_Vxk.root",
sampleBaseDir+"PATtuple_109_1_8zW.root",
sampleBaseDir+"PATtuple_10_1_46s.root",
sampleBaseDir+"PATtuple_110_1_9sb.root",
sampleBaseDir+"PATtuple_111_1_8sR.root",
sampleBaseDir+"PATtuple_112_1_6Qu.root",
sampleBaseDir+"PATtuple_113_1_QHT.root",
sampleBaseDir+"PATtuple_114_1_HFg.root",
sampleBaseDir+"PATtuple_115_1_43s.root",
sampleBaseDir+"PATtuple_116_1_0ij.root",
sampleBaseDir+"PATtuple_117_1_2bQ.root",
sampleBaseDir+"PATtuple_118_1_MGH.root",
sampleBaseDir+"PATtuple_119_1_Dyl.root",
sampleBaseDir+"PATtuple_11_1_sJR.root",
sampleBaseDir+"PATtuple_120_1_Wtc.root",
sampleBaseDir+"PATtuple_121_1_rc9.root",
sampleBaseDir+"PATtuple_122_1_WVc.root",
sampleBaseDir+"PATtuple_123_1_0bV.root",
sampleBaseDir+"PATtuple_124_1_JfG.root",
sampleBaseDir+"PATtuple_125_1_hAj.root",
sampleBaseDir+"PATtuple_126_1_aHW.root",
sampleBaseDir+"PATtuple_127_1_MQM.root",
sampleBaseDir+"PATtuple_128_1_B3q.root",
sampleBaseDir+"PATtuple_129_1_Nqh.root",
sampleBaseDir+"PATtuple_12_1_Wb2.root",
sampleBaseDir+"PATtuple_130_1_gYq.root",
sampleBaseDir+"PATtuple_131_1_uqG.root",
sampleBaseDir+"PATtuple_132_1_w5q.root",
sampleBaseDir+"PATtuple_133_1_tF4.root",
sampleBaseDir+"PATtuple_134_1_VOA.root",
sampleBaseDir+"PATtuple_135_1_McI.root",
sampleBaseDir+"PATtuple_136_1_6CH.root",
sampleBaseDir+"PATtuple_137_1_Uvj.root",
sampleBaseDir+"PATtuple_138_1_Ytn.root",
sampleBaseDir+"PATtuple_139_1_Wwf.root",
sampleBaseDir+"PATtuple_13_1_cMy.root",
sampleBaseDir+"PATtuple_140_1_jML.root",
sampleBaseDir+"PATtuple_141_1_f5a.root",
sampleBaseDir+"PATtuple_142_1_xf5.root",
sampleBaseDir+"PATtuple_143_1_5w8.root",
sampleBaseDir+"PATtuple_144_1_7px.root",
sampleBaseDir+"PATtuple_145_1_eOV.root",
sampleBaseDir+"PATtuple_146_1_WV5.root",
sampleBaseDir+"PATtuple_147_1_Wkz.root",
sampleBaseDir+"PATtuple_148_1_sH4.root",
sampleBaseDir+"PATtuple_149_1_NU9.root",
sampleBaseDir+"PATtuple_14_1_CHR.root",
sampleBaseDir+"PATtuple_150_1_pTz.root",
sampleBaseDir+"PATtuple_151_1_bkE.root",
sampleBaseDir+"PATtuple_152_1_2oP.root",
sampleBaseDir+"PATtuple_153_1_WfO.root",
sampleBaseDir+"PATtuple_154_1_lEi.root",
sampleBaseDir+"PATtuple_155_1_ZGB.root",
sampleBaseDir+"PATtuple_156_1_HOZ.root",
sampleBaseDir+"PATtuple_157_1_mng.root",
sampleBaseDir+"PATtuple_158_1_Hcb.root",
sampleBaseDir+"PATtuple_159_1_ZYW.root",
sampleBaseDir+"PATtuple_15_1_lRj.root",
sampleBaseDir+"PATtuple_160_1_VcN.root",
sampleBaseDir+"PATtuple_161_1_suI.root",
sampleBaseDir+"PATtuple_162_1_b53.root",
sampleBaseDir+"PATtuple_163_1_yP6.root",
sampleBaseDir+"PATtuple_164_1_QVe.root",
sampleBaseDir+"PATtuple_165_1_87p.root",
sampleBaseDir+"PATtuple_166_1_VNQ.root",
sampleBaseDir+"PATtuple_167_1_jie.root",
sampleBaseDir+"PATtuple_168_1_CxF.root",
sampleBaseDir+"PATtuple_169_1_MCF.root",
sampleBaseDir+"PATtuple_16_1_6Fr.root",
sampleBaseDir+"PATtuple_170_1_2ib.root",
sampleBaseDir+"PATtuple_171_1_w3b.root",
sampleBaseDir+"PATtuple_172_1_hjA.root",
sampleBaseDir+"PATtuple_173_1_Dj9.root",
sampleBaseDir+"PATtuple_174_1_O3v.root",
sampleBaseDir+"PATtuple_175_1_05G.root",
sampleBaseDir+"PATtuple_176_1_5bV.root",
sampleBaseDir+"PATtuple_177_1_bm6.root",
sampleBaseDir+"PATtuple_178_1_Hyu.root",
sampleBaseDir+"PATtuple_179_1_aIi.root",
sampleBaseDir+"PATtuple_17_1_rvm.root",
sampleBaseDir+"PATtuple_180_1_bKR.root",
sampleBaseDir+"PATtuple_181_1_hL6.root",
sampleBaseDir+"PATtuple_182_1_9E1.root",
sampleBaseDir+"PATtuple_183_1_xRt.root",
sampleBaseDir+"PATtuple_184_1_ZCu.root",
sampleBaseDir+"PATtuple_185_1_pWt.root",
sampleBaseDir+"PATtuple_186_1_0NO.root",
sampleBaseDir+"PATtuple_187_1_oz5.root",
sampleBaseDir+"PATtuple_188_1_I8v.root",
sampleBaseDir+"PATtuple_189_1_hcb.root",
sampleBaseDir+"PATtuple_18_1_JBd.root",
sampleBaseDir+"PATtuple_190_1_Qz8.root",
sampleBaseDir+"PATtuple_191_1_07v.root",
sampleBaseDir+"PATtuple_192_1_zih.root",
sampleBaseDir+"PATtuple_193_1_tLb.root",
sampleBaseDir+"PATtuple_194_1_c8B.root",
sampleBaseDir+"PATtuple_195_1_eD5.root",
sampleBaseDir+"PATtuple_196_1_6rh.root",
sampleBaseDir+"PATtuple_197_1_EBv.root",
sampleBaseDir+"PATtuple_198_1_EFt.root",
sampleBaseDir+"PATtuple_199_1_2on.root",
sampleBaseDir+"PATtuple_19_1_2BY.root",
sampleBaseDir+"PATtuple_1_1_VyZ.root",
sampleBaseDir+"PATtuple_200_1_G1P.root",
sampleBaseDir+"PATtuple_201_1_1k4.root",
sampleBaseDir+"PATtuple_202_1_1qi.root",
sampleBaseDir+"PATtuple_203_1_ZaX.root",
sampleBaseDir+"PATtuple_204_1_DhO.root",
sampleBaseDir+"PATtuple_205_1_S0U.root",
sampleBaseDir+"PATtuple_206_1_pkv.root",
sampleBaseDir+"PATtuple_207_1_VQ5.root",
sampleBaseDir+"PATtuple_208_1_ixg.root",
sampleBaseDir+"PATtuple_209_1_zZ5.root",
sampleBaseDir+"PATtuple_20_1_em9.root",
sampleBaseDir+"PATtuple_210_1_TYT.root",
sampleBaseDir+"PATtuple_211_1_yZY.root",
sampleBaseDir+"PATtuple_212_1_62P.root",
sampleBaseDir+"PATtuple_213_1_Tkk.root",
sampleBaseDir+"PATtuple_214_1_lJK.root",
sampleBaseDir+"PATtuple_215_1_NfV.root",
sampleBaseDir+"PATtuple_216_1_bMy.root",
sampleBaseDir+"PATtuple_217_1_272.root",
sampleBaseDir+"PATtuple_218_1_wRw.root",
sampleBaseDir+"PATtuple_219_1_Md6.root",
sampleBaseDir+"PATtuple_21_1_vi8.root",
sampleBaseDir+"PATtuple_220_1_RtZ.root",
sampleBaseDir+"PATtuple_221_1_fxL.root",
sampleBaseDir+"PATtuple_222_1_VcW.root",
sampleBaseDir+"PATtuple_223_1_5Xd.root",
sampleBaseDir+"PATtuple_224_1_ddn.root",
sampleBaseDir+"PATtuple_225_1_Kt4.root",
sampleBaseDir+"PATtuple_226_1_eKP.root",
sampleBaseDir+"PATtuple_227_1_GWI.root",
sampleBaseDir+"PATtuple_228_1_d8T.root",
sampleBaseDir+"PATtuple_229_1_NFK.root",
sampleBaseDir+"PATtuple_22_1_omr.root",
sampleBaseDir+"PATtuple_230_1_kyA.root",
sampleBaseDir+"PATtuple_231_1_3Vi.root",
sampleBaseDir+"PATtuple_232_1_aJ6.root",
sampleBaseDir+"PATtuple_233_1_rhE.root",
sampleBaseDir+"PATtuple_234_1_QFx.root",
sampleBaseDir+"PATtuple_235_1_6Q7.root",
sampleBaseDir+"PATtuple_236_1_6Pd.root",
sampleBaseDir+"PATtuple_237_1_grK.root",
sampleBaseDir+"PATtuple_238_1_1YW.root",
sampleBaseDir+"PATtuple_239_1_qFD.root",
sampleBaseDir+"PATtuple_23_1_7Tv.root",
sampleBaseDir+"PATtuple_240_1_Scx.root",
sampleBaseDir+"PATtuple_241_1_rVv.root",
sampleBaseDir+"PATtuple_242_1_SFj.root",
sampleBaseDir+"PATtuple_243_1_uzh.root",
sampleBaseDir+"PATtuple_244_1_TlG.root",
sampleBaseDir+"PATtuple_245_1_rTC.root",
sampleBaseDir+"PATtuple_246_1_cl8.root",
sampleBaseDir+"PATtuple_247_1_FBu.root",
sampleBaseDir+"PATtuple_248_1_wAn.root",
sampleBaseDir+"PATtuple_249_1_K8s.root",
sampleBaseDir+"PATtuple_24_1_hdl.root",
sampleBaseDir+"PATtuple_250_1_NY4.root",
sampleBaseDir+"PATtuple_251_1_43i.root",
sampleBaseDir+"PATtuple_252_1_61K.root",
sampleBaseDir+"PATtuple_253_1_UuU.root",
sampleBaseDir+"PATtuple_254_1_vUz.root",
sampleBaseDir+"PATtuple_255_1_2jh.root",
sampleBaseDir+"PATtuple_256_1_eE6.root",
sampleBaseDir+"PATtuple_257_1_SSy.root",
sampleBaseDir+"PATtuple_258_1_VBI.root",
sampleBaseDir+"PATtuple_259_1_pWj.root",
sampleBaseDir+"PATtuple_25_1_o1i.root",
sampleBaseDir+"PATtuple_260_1_LMc.root",
sampleBaseDir+"PATtuple_261_1_fPb.root",
sampleBaseDir+"PATtuple_262_1_mPy.root",
sampleBaseDir+"PATtuple_263_1_YJb.root",
sampleBaseDir+"PATtuple_264_1_o6j.root",
sampleBaseDir+"PATtuple_265_1_3ZK.root",
sampleBaseDir+"PATtuple_266_1_g6x.root",
sampleBaseDir+"PATtuple_267_1_1xv.root",
sampleBaseDir+"PATtuple_268_1_sPi.root",
sampleBaseDir+"PATtuple_269_1_Rdh.root",
sampleBaseDir+"PATtuple_26_1_eaA.root",
sampleBaseDir+"PATtuple_270_1_BgS.root",
sampleBaseDir+"PATtuple_271_1_7gn.root",
sampleBaseDir+"PATtuple_272_1_L1l.root",
sampleBaseDir+"PATtuple_273_1_oqF.root",
sampleBaseDir+"PATtuple_274_1_d23.root",
sampleBaseDir+"PATtuple_275_1_HQv.root",
sampleBaseDir+"PATtuple_276_1_rw3.root",
sampleBaseDir+"PATtuple_277_1_G2C.root",
sampleBaseDir+"PATtuple_278_1_GWa.root",
sampleBaseDir+"PATtuple_279_1_myr.root",
sampleBaseDir+"PATtuple_27_1_ls6.root",
sampleBaseDir+"PATtuple_280_1_GXU.root",
sampleBaseDir+"PATtuple_281_1_nlw.root",
sampleBaseDir+"PATtuple_282_1_joa.root",
sampleBaseDir+"PATtuple_283_1_ZGq.root",
sampleBaseDir+"PATtuple_284_1_A9a.root",
sampleBaseDir+"PATtuple_285_1_8eN.root",
sampleBaseDir+"PATtuple_286_1_Ju1.root",
sampleBaseDir+"PATtuple_287_1_4IH.root",
sampleBaseDir+"PATtuple_288_1_dFx.root",
sampleBaseDir+"PATtuple_289_1_OV7.root",
sampleBaseDir+"PATtuple_28_1_Kj1.root",
sampleBaseDir+"PATtuple_290_1_koa.root",
sampleBaseDir+"PATtuple_291_1_3r1.root",
sampleBaseDir+"PATtuple_292_1_Rwe.root",
sampleBaseDir+"PATtuple_293_1_7Vd.root",
sampleBaseDir+"PATtuple_294_1_YNC.root",
sampleBaseDir+"PATtuple_295_1_24w.root",
sampleBaseDir+"PATtuple_296_1_hmU.root",
sampleBaseDir+"PATtuple_297_1_6ix.root",
sampleBaseDir+"PATtuple_298_1_YfH.root",
sampleBaseDir+"PATtuple_299_1_LlJ.root",
sampleBaseDir+"PATtuple_29_1_yJL.root",
sampleBaseDir+"PATtuple_2_1_yFs.root",
sampleBaseDir+"PATtuple_300_1_5OK.root",
sampleBaseDir+"PATtuple_301_1_sLO.root",
sampleBaseDir+"PATtuple_302_1_efy.root",
sampleBaseDir+"PATtuple_303_1_flV.root",
sampleBaseDir+"PATtuple_304_1_ODh.root",
sampleBaseDir+"PATtuple_305_1_FGk.root",
sampleBaseDir+"PATtuple_306_1_iJc.root",
sampleBaseDir+"PATtuple_307_1_aQJ.root",
sampleBaseDir+"PATtuple_308_1_FtR.root",
sampleBaseDir+"PATtuple_309_1_oeW.root",
sampleBaseDir+"PATtuple_30_1_hm5.root",
sampleBaseDir+"PATtuple_310_1_HK9.root",
sampleBaseDir+"PATtuple_311_1_SOc.root",
sampleBaseDir+"PATtuple_312_1_YSv.root",
sampleBaseDir+"PATtuple_313_1_4y3.root",
sampleBaseDir+"PATtuple_314_1_DZc.root",
sampleBaseDir+"PATtuple_315_1_2jn.root",
sampleBaseDir+"PATtuple_316_1_OIy.root",
sampleBaseDir+"PATtuple_317_1_rmd.root",
sampleBaseDir+"PATtuple_318_1_O9f.root",
sampleBaseDir+"PATtuple_319_1_F52.root",
sampleBaseDir+"PATtuple_31_1_kwt.root",
sampleBaseDir+"PATtuple_320_1_kDQ.root",
sampleBaseDir+"PATtuple_321_1_xAT.root",
sampleBaseDir+"PATtuple_322_1_8wi.root",
sampleBaseDir+"PATtuple_323_1_ev8.root",
sampleBaseDir+"PATtuple_324_1_b1V.root",
sampleBaseDir+"PATtuple_325_1_730.root",
sampleBaseDir+"PATtuple_326_1_wOl.root",
sampleBaseDir+"PATtuple_327_1_oZJ.root",
sampleBaseDir+"PATtuple_328_1_sr7.root",
sampleBaseDir+"PATtuple_329_1_ZoA.root",
sampleBaseDir+"PATtuple_32_1_eng.root",
sampleBaseDir+"PATtuple_330_1_iyj.root",
sampleBaseDir+"PATtuple_331_1_shw.root",
sampleBaseDir+"PATtuple_332_1_4d6.root",
sampleBaseDir+"PATtuple_333_1_5kO.root",
sampleBaseDir+"PATtuple_334_1_Hi3.root",
sampleBaseDir+"PATtuple_335_1_6WZ.root",
sampleBaseDir+"PATtuple_336_1_139.root",
sampleBaseDir+"PATtuple_337_1_TsI.root",
sampleBaseDir+"PATtuple_338_1_T4u.root",
sampleBaseDir+"PATtuple_339_1_eae.root",
sampleBaseDir+"PATtuple_33_1_NNw.root",
sampleBaseDir+"PATtuple_340_1_iog.root",
sampleBaseDir+"PATtuple_341_1_8fc.root",
sampleBaseDir+"PATtuple_342_1_Fj9.root",
sampleBaseDir+"PATtuple_343_1_FPZ.root",
sampleBaseDir+"PATtuple_344_1_Uaw.root",
sampleBaseDir+"PATtuple_345_1_jr2.root",
sampleBaseDir+"PATtuple_346_1_CMI.root",
sampleBaseDir+"PATtuple_347_1_dsN.root",
sampleBaseDir+"PATtuple_348_1_FLB.root",
sampleBaseDir+"PATtuple_349_1_xCf.root",
sampleBaseDir+"PATtuple_34_1_OLo.root",
sampleBaseDir+"PATtuple_350_1_cK1.root",
sampleBaseDir+"PATtuple_351_1_9jT.root",
sampleBaseDir+"PATtuple_352_1_iE5.root",
sampleBaseDir+"PATtuple_353_1_mQ4.root",
sampleBaseDir+"PATtuple_354_1_T6b.root",
sampleBaseDir+"PATtuple_355_1_xXZ.root",
sampleBaseDir+"PATtuple_356_1_GxT.root",
sampleBaseDir+"PATtuple_357_1_Gly.root",
sampleBaseDir+"PATtuple_358_1_US2.root",
sampleBaseDir+"PATtuple_359_1_qjv.root",
sampleBaseDir+"PATtuple_35_1_zQ3.root",
sampleBaseDir+"PATtuple_360_1_7YG.root",
sampleBaseDir+"PATtuple_361_1_pXF.root",
sampleBaseDir+"PATtuple_362_1_jo6.root",
sampleBaseDir+"PATtuple_363_1_9Ug.root",
sampleBaseDir+"PATtuple_364_1_Y3x.root",
sampleBaseDir+"PATtuple_365_1_yah.root",
sampleBaseDir+"PATtuple_366_1_zQ1.root",
sampleBaseDir+"PATtuple_367_1_BYU.root",
sampleBaseDir+"PATtuple_368_1_n2f.root",
sampleBaseDir+"PATtuple_369_1_pje.root",
sampleBaseDir+"PATtuple_36_1_PrE.root",
sampleBaseDir+"PATtuple_370_1_mNQ.root",
sampleBaseDir+"PATtuple_371_1_X3A.root",
sampleBaseDir+"PATtuple_372_1_vDW.root",
sampleBaseDir+"PATtuple_373_1_dXt.root",
sampleBaseDir+"PATtuple_374_1_w60.root",
sampleBaseDir+"PATtuple_375_1_6P8.root",
sampleBaseDir+"PATtuple_376_1_Qzb.root",
sampleBaseDir+"PATtuple_377_1_OKs.root",
sampleBaseDir+"PATtuple_378_1_yHi.root",
sampleBaseDir+"PATtuple_379_1_5yZ.root",
sampleBaseDir+"PATtuple_37_1_1Uq.root",
sampleBaseDir+"PATtuple_380_1_HXr.root",
sampleBaseDir+"PATtuple_381_1_ync.root",
sampleBaseDir+"PATtuple_382_1_u8z.root",
sampleBaseDir+"PATtuple_383_1_jjG.root",
sampleBaseDir+"PATtuple_384_1_SBg.root",
sampleBaseDir+"PATtuple_385_1_iUQ.root",
sampleBaseDir+"PATtuple_386_1_2V4.root",
sampleBaseDir+"PATtuple_387_1_1hH.root",
sampleBaseDir+"PATtuple_388_1_9EM.root",
sampleBaseDir+"PATtuple_389_1_GB6.root",
sampleBaseDir+"PATtuple_38_1_mWW.root",
sampleBaseDir+"PATtuple_390_1_fTK.root",
sampleBaseDir+"PATtuple_391_1_Gd8.root",
sampleBaseDir+"PATtuple_392_1_aqn.root",
sampleBaseDir+"PATtuple_393_1_SXM.root",
sampleBaseDir+"PATtuple_394_1_qQy.root",
sampleBaseDir+"PATtuple_395_1_Dov.root",
sampleBaseDir+"PATtuple_396_1_IlQ.root",
sampleBaseDir+"PATtuple_397_1_NRh.root",
sampleBaseDir+"PATtuple_398_1_EUz.root",
sampleBaseDir+"PATtuple_399_1_MMv.root",
sampleBaseDir+"PATtuple_39_1_OKQ.root",
sampleBaseDir+"PATtuple_3_1_O39.root",
sampleBaseDir+"PATtuple_400_1_L6J.root",
sampleBaseDir+"PATtuple_401_1_m4S.root",
sampleBaseDir+"PATtuple_402_1_xEs.root",
sampleBaseDir+"PATtuple_403_1_TMu.root",
sampleBaseDir+"PATtuple_404_1_ZBz.root",
sampleBaseDir+"PATtuple_405_1_5c1.root",
sampleBaseDir+"PATtuple_406_1_WSe.root",
sampleBaseDir+"PATtuple_407_1_TA7.root",
sampleBaseDir+"PATtuple_408_1_rsi.root",
sampleBaseDir+"PATtuple_409_1_1cK.root",
sampleBaseDir+"PATtuple_40_1_DGW.root",
sampleBaseDir+"PATtuple_410_1_diS.root",
sampleBaseDir+"PATtuple_411_1_OYh.root",
sampleBaseDir+"PATtuple_412_1_kw2.root",
sampleBaseDir+"PATtuple_413_1_Res.root",
sampleBaseDir+"PATtuple_414_1_LrW.root",
sampleBaseDir+"PATtuple_415_1_bHl.root",
sampleBaseDir+"PATtuple_416_1_zjQ.root",
sampleBaseDir+"PATtuple_417_1_sHU.root",
sampleBaseDir+"PATtuple_418_1_kpJ.root",
sampleBaseDir+"PATtuple_419_1_c1s.root",
sampleBaseDir+"PATtuple_41_1_wAW.root",
sampleBaseDir+"PATtuple_420_1_uEi.root",
sampleBaseDir+"PATtuple_421_1_LNj.root",
sampleBaseDir+"PATtuple_422_1_K6o.root",
sampleBaseDir+"PATtuple_423_1_p43.root",
sampleBaseDir+"PATtuple_424_1_VFM.root",
sampleBaseDir+"PATtuple_425_1_e3Q.root",
sampleBaseDir+"PATtuple_426_1_xoK.root",
sampleBaseDir+"PATtuple_427_1_Jzi.root",
sampleBaseDir+"PATtuple_428_1_Hx8.root",
sampleBaseDir+"PATtuple_429_1_pml.root",
sampleBaseDir+"PATtuple_42_1_cKI.root",
sampleBaseDir+"PATtuple_430_1_qeA.root",
sampleBaseDir+"PATtuple_431_1_PTH.root",
sampleBaseDir+"PATtuple_432_1_rn0.root",
sampleBaseDir+"PATtuple_433_1_6Y4.root",
sampleBaseDir+"PATtuple_434_1_uTi.root",
sampleBaseDir+"PATtuple_435_1_WbU.root",
sampleBaseDir+"PATtuple_436_1_jHz.root",
sampleBaseDir+"PATtuple_437_1_VnB.root",
sampleBaseDir+"PATtuple_438_1_H7R.root",
sampleBaseDir+"PATtuple_439_1_6aE.root",
sampleBaseDir+"PATtuple_43_1_WLy.root",
sampleBaseDir+"PATtuple_440_1_1Bx.root",
sampleBaseDir+"PATtuple_441_1_6uI.root",
sampleBaseDir+"PATtuple_442_1_6N7.root",
sampleBaseDir+"PATtuple_443_1_qqi.root",
sampleBaseDir+"PATtuple_444_1_DYo.root",
sampleBaseDir+"PATtuple_445_1_pk3.root",
sampleBaseDir+"PATtuple_446_1_QuS.root",
sampleBaseDir+"PATtuple_447_1_YrS.root",
sampleBaseDir+"PATtuple_448_1_V8I.root",
sampleBaseDir+"PATtuple_449_1_qOU.root",
sampleBaseDir+"PATtuple_44_1_sLQ.root",
sampleBaseDir+"PATtuple_450_1_CEU.root",
sampleBaseDir+"PATtuple_451_1_UXZ.root",
sampleBaseDir+"PATtuple_452_1_s75.root",
sampleBaseDir+"PATtuple_453_1_aIP.root",
sampleBaseDir+"PATtuple_454_1_Kqc.root",
sampleBaseDir+"PATtuple_455_1_2kb.root",
sampleBaseDir+"PATtuple_456_1_ZBC.root",
sampleBaseDir+"PATtuple_457_1_w3J.root",
sampleBaseDir+"PATtuple_458_1_Bn7.root",
sampleBaseDir+"PATtuple_459_1_H5B.root",
sampleBaseDir+"PATtuple_45_1_3Ef.root",
sampleBaseDir+"PATtuple_460_1_0DK.root",
sampleBaseDir+"PATtuple_461_1_kiG.root",
sampleBaseDir+"PATtuple_462_1_xMC.root",
sampleBaseDir+"PATtuple_463_1_OHl.root",
sampleBaseDir+"PATtuple_464_1_y4W.root",
sampleBaseDir+"PATtuple_465_1_xrG.root",
sampleBaseDir+"PATtuple_466_1_FHT.root",
sampleBaseDir+"PATtuple_467_1_diN.root",
sampleBaseDir+"PATtuple_468_1_PIP.root",
sampleBaseDir+"PATtuple_469_1_VY1.root",
sampleBaseDir+"PATtuple_46_1_prM.root",
sampleBaseDir+"PATtuple_470_1_oxe.root",
sampleBaseDir+"PATtuple_471_1_c2F.root",
sampleBaseDir+"PATtuple_472_1_Ns1.root",
sampleBaseDir+"PATtuple_473_1_8Bq.root",
sampleBaseDir+"PATtuple_474_1_mW1.root",
sampleBaseDir+"PATtuple_475_1_Sw3.root",
sampleBaseDir+"PATtuple_476_1_0A0.root",
sampleBaseDir+"PATtuple_477_1_yWZ.root",
sampleBaseDir+"PATtuple_478_1_khR.root",
sampleBaseDir+"PATtuple_479_1_LSr.root",
sampleBaseDir+"PATtuple_47_1_Huc.root",
sampleBaseDir+"PATtuple_480_1_7nU.root",
sampleBaseDir+"PATtuple_481_1_Ay7.root",
sampleBaseDir+"PATtuple_482_1_L9q.root",
sampleBaseDir+"PATtuple_483_1_rIq.root",
sampleBaseDir+"PATtuple_484_1_esZ.root",
sampleBaseDir+"PATtuple_485_1_hP2.root",
sampleBaseDir+"PATtuple_486_1_GME.root",
sampleBaseDir+"PATtuple_487_1_KIy.root",
sampleBaseDir+"PATtuple_488_1_uiq.root",
sampleBaseDir+"PATtuple_489_1_Wtt.root",
sampleBaseDir+"PATtuple_48_1_QgR.root",
sampleBaseDir+"PATtuple_490_1_FWi.root",
sampleBaseDir+"PATtuple_491_1_Jdj.root",
sampleBaseDir+"PATtuple_492_1_Wsa.root",
sampleBaseDir+"PATtuple_493_1_WQi.root",
sampleBaseDir+"PATtuple_494_1_20s.root",
sampleBaseDir+"PATtuple_495_1_SEQ.root",
sampleBaseDir+"PATtuple_496_1_Hne.root",
sampleBaseDir+"PATtuple_497_1_M75.root",
sampleBaseDir+"PATtuple_498_1_IX7.root",
sampleBaseDir+"PATtuple_499_1_Kvu.root",
sampleBaseDir+"PATtuple_49_1_bDk.root",
sampleBaseDir+"PATtuple_4_1_LiM.root",
sampleBaseDir+"PATtuple_500_1_jdN.root",
sampleBaseDir+"PATtuple_501_1_Lu9.root",
sampleBaseDir+"PATtuple_502_1_IQD.root",
sampleBaseDir+"PATtuple_503_1_aKJ.root",
sampleBaseDir+"PATtuple_504_1_yeO.root",
sampleBaseDir+"PATtuple_505_1_1iv.root",
sampleBaseDir+"PATtuple_506_1_z4R.root",
sampleBaseDir+"PATtuple_507_1_XRa.root",
sampleBaseDir+"PATtuple_508_1_7qV.root",
sampleBaseDir+"PATtuple_509_1_PhX.root",
sampleBaseDir+"PATtuple_50_1_FXZ.root",
sampleBaseDir+"PATtuple_510_1_SAl.root",
sampleBaseDir+"PATtuple_511_1_Vr9.root",
sampleBaseDir+"PATtuple_512_1_GID.root",
sampleBaseDir+"PATtuple_513_1_y6r.root",
sampleBaseDir+"PATtuple_514_1_b3d.root",
sampleBaseDir+"PATtuple_515_1_Vxm.root",
sampleBaseDir+"PATtuple_516_1_hOP.root",
sampleBaseDir+"PATtuple_517_1_4zo.root",
sampleBaseDir+"PATtuple_518_1_FCK.root",
sampleBaseDir+"PATtuple_519_1_uya.root",
sampleBaseDir+"PATtuple_51_1_rVM.root",
sampleBaseDir+"PATtuple_520_1_fkk.root",
sampleBaseDir+"PATtuple_521_1_W9t.root",
sampleBaseDir+"PATtuple_522_1_ft9.root",
sampleBaseDir+"PATtuple_523_1_lmu.root",
sampleBaseDir+"PATtuple_524_1_6MP.root",
sampleBaseDir+"PATtuple_525_1_Fz5.root",
sampleBaseDir+"PATtuple_526_1_ZVg.root",
sampleBaseDir+"PATtuple_527_1_4wn.root",
sampleBaseDir+"PATtuple_528_1_4IO.root",
sampleBaseDir+"PATtuple_529_1_tzx.root",
sampleBaseDir+"PATtuple_52_1_f07.root",
sampleBaseDir+"PATtuple_530_1_xOA.root",
sampleBaseDir+"PATtuple_531_1_KDu.root",
sampleBaseDir+"PATtuple_532_1_tFr.root",
sampleBaseDir+"PATtuple_533_1_qJ5.root",
sampleBaseDir+"PATtuple_534_1_EFH.root",
sampleBaseDir+"PATtuple_535_1_Ex1.root",
sampleBaseDir+"PATtuple_536_1_kGh.root",
sampleBaseDir+"PATtuple_537_1_uyc.root",
sampleBaseDir+"PATtuple_538_1_1hw.root",
sampleBaseDir+"PATtuple_539_1_o6P.root",
sampleBaseDir+"PATtuple_53_1_7zE.root",
sampleBaseDir+"PATtuple_540_1_Xnt.root",
sampleBaseDir+"PATtuple_541_1_SXp.root",
sampleBaseDir+"PATtuple_542_1_R8Q.root",
sampleBaseDir+"PATtuple_543_1_O2E.root",
sampleBaseDir+"PATtuple_544_1_3Oh.root",
sampleBaseDir+"PATtuple_545_1_XFg.root",
sampleBaseDir+"PATtuple_546_1_2ti.root",
sampleBaseDir+"PATtuple_547_1_yru.root",
sampleBaseDir+"PATtuple_548_1_gCc.root",
sampleBaseDir+"PATtuple_549_1_jQl.root",
sampleBaseDir+"PATtuple_54_1_P8A.root",
sampleBaseDir+"PATtuple_550_1_Qvj.root",
sampleBaseDir+"PATtuple_551_1_E9f.root",
sampleBaseDir+"PATtuple_552_1_r4e.root",
sampleBaseDir+"PATtuple_553_1_HKY.root",
sampleBaseDir+"PATtuple_554_1_jEt.root",
sampleBaseDir+"PATtuple_555_1_e4K.root",
sampleBaseDir+"PATtuple_556_1_P8p.root",
sampleBaseDir+"PATtuple_55_1_LSt.root",
sampleBaseDir+"PATtuple_56_1_EiC.root",
sampleBaseDir+"PATtuple_57_1_G92.root",
sampleBaseDir+"PATtuple_58_1_ME4.root",
sampleBaseDir+"PATtuple_59_1_M0O.root",
sampleBaseDir+"PATtuple_5_1_tAr.root",
sampleBaseDir+"PATtuple_60_1_r7z.root",
sampleBaseDir+"PATtuple_61_1_KLJ.root",
sampleBaseDir+"PATtuple_62_1_exw.root",
sampleBaseDir+"PATtuple_63_1_sUy.root",
sampleBaseDir+"PATtuple_64_1_xlE.root",
sampleBaseDir+"PATtuple_65_1_Bo5.root",
sampleBaseDir+"PATtuple_66_1_RZw.root",
sampleBaseDir+"PATtuple_67_1_l2p.root",
sampleBaseDir+"PATtuple_68_1_zcT.root",
sampleBaseDir+"PATtuple_69_1_0Hm.root",
sampleBaseDir+"PATtuple_6_1_4mG.root",
sampleBaseDir+"PATtuple_70_1_odc.root",
sampleBaseDir+"PATtuple_71_1_Xfr.root",
sampleBaseDir+"PATtuple_72_1_Crs.root",
sampleBaseDir+"PATtuple_73_1_q12.root",
sampleBaseDir+"PATtuple_74_1_usW.root",
sampleBaseDir+"PATtuple_75_1_BHy.root",
sampleBaseDir+"PATtuple_76_1_F5l.root",
sampleBaseDir+"PATtuple_77_1_nK5.root",
sampleBaseDir+"PATtuple_78_1_otU.root",
sampleBaseDir+"PATtuple_79_1_B3e.root",
sampleBaseDir+"PATtuple_7_1_YoH.root",
sampleBaseDir+"PATtuple_80_1_msS.root",
sampleBaseDir+"PATtuple_81_1_GG5.root",
sampleBaseDir+"PATtuple_82_1_s6U.root",
sampleBaseDir+"PATtuple_83_1_V16.root",
sampleBaseDir+"PATtuple_84_1_d79.root",
sampleBaseDir+"PATtuple_85_1_wE0.root",
sampleBaseDir+"PATtuple_86_1_Bcs.root",
sampleBaseDir+"PATtuple_87_1_tVX.root",
sampleBaseDir+"PATtuple_88_1_3Zi.root",
sampleBaseDir+"PATtuple_89_1_IAs.root",
sampleBaseDir+"PATtuple_8_1_g5E.root",
sampleBaseDir+"PATtuple_90_1_YP4.root",
sampleBaseDir+"PATtuple_91_1_Oaq.root",
sampleBaseDir+"PATtuple_92_1_rzb.root",
sampleBaseDir+"PATtuple_93_1_a3H.root",
sampleBaseDir+"PATtuple_94_1_APM.root",
sampleBaseDir+"PATtuple_95_1_naY.root",
sampleBaseDir+"PATtuple_96_1_DAs.root",
sampleBaseDir+"PATtuple_97_1_mzu.root",
sampleBaseDir+"PATtuple_98_1_R0L.root",
sampleBaseDir+"PATtuple_99_1_JYd.root",
sampleBaseDir+"PATtuple_9_1_kmn.root",
]
