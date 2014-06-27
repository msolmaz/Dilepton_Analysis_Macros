sampleDataSet = '/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 9799908

sampleXSec = 8.3;

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"








samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/ZZ_pat_20140502/zhenhu//ZZ_TuneZ2star_8TeV_pythia6_tauola/ZZ_pat_20140502/fdbd887910ea36180672aa763a206c5b/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_lrI.root",
sampleBaseDir+"PATtuple_101_1_G7O.root",
sampleBaseDir+"PATtuple_102_1_fTR.root",
sampleBaseDir+"PATtuple_103_1_gMe.root",
sampleBaseDir+"PATtuple_104_1_PiL.root",
sampleBaseDir+"PATtuple_105_1_zFc.root",
sampleBaseDir+"PATtuple_106_1_luk.root",
sampleBaseDir+"PATtuple_107_1_nhW.root",
sampleBaseDir+"PATtuple_108_1_CYj.root",
sampleBaseDir+"PATtuple_109_1_P0J.root",
sampleBaseDir+"PATtuple_10_1_4A5.root",
sampleBaseDir+"PATtuple_110_1_iW2.root",
sampleBaseDir+"PATtuple_111_1_e9h.root",
sampleBaseDir+"PATtuple_112_1_TTE.root",
sampleBaseDir+"PATtuple_113_1_2Ho.root",
sampleBaseDir+"PATtuple_114_1_dLo.root",
sampleBaseDir+"PATtuple_115_1_261.root",
sampleBaseDir+"PATtuple_116_1_udo.root",
sampleBaseDir+"PATtuple_117_1_y9X.root",
sampleBaseDir+"PATtuple_118_1_QUd.root",
sampleBaseDir+"PATtuple_119_1_xmB.root",
sampleBaseDir+"PATtuple_11_1_oRO.root",
sampleBaseDir+"PATtuple_120_1_GnF.root",
sampleBaseDir+"PATtuple_121_1_wqx.root",
sampleBaseDir+"PATtuple_122_1_ta1.root",
sampleBaseDir+"PATtuple_123_1_YtO.root",
sampleBaseDir+"PATtuple_124_1_BZx.root",
sampleBaseDir+"PATtuple_125_1_8KI.root",
sampleBaseDir+"PATtuple_126_1_geW.root",
sampleBaseDir+"PATtuple_127_1_svN.root",
sampleBaseDir+"PATtuple_128_1_x6g.root",
sampleBaseDir+"PATtuple_129_1_Tle.root",
sampleBaseDir+"PATtuple_12_1_h2P.root",
sampleBaseDir+"PATtuple_130_1_5vy.root",
sampleBaseDir+"PATtuple_131_1_sYv.root",
sampleBaseDir+"PATtuple_132_1_gZK.root",
sampleBaseDir+"PATtuple_133_1_mXy.root",
sampleBaseDir+"PATtuple_134_1_yLU.root",
sampleBaseDir+"PATtuple_135_1_955.root",
sampleBaseDir+"PATtuple_136_1_6S7.root",
sampleBaseDir+"PATtuple_137_1_MVz.root",
sampleBaseDir+"PATtuple_138_1_M4X.root",
sampleBaseDir+"PATtuple_139_1_R3U.root",
sampleBaseDir+"PATtuple_13_1_iri.root",
sampleBaseDir+"PATtuple_140_1_Zlh.root",
sampleBaseDir+"PATtuple_141_1_cYv.root",
sampleBaseDir+"PATtuple_142_1_Hhk.root",
sampleBaseDir+"PATtuple_143_1_qaB.root",
sampleBaseDir+"PATtuple_144_1_JOq.root",
sampleBaseDir+"PATtuple_145_1_2lR.root",
sampleBaseDir+"PATtuple_146_1_aPd.root",
sampleBaseDir+"PATtuple_147_1_BBy.root",
sampleBaseDir+"PATtuple_148_1_Y10.root",
sampleBaseDir+"PATtuple_149_1_Bwl.root",
sampleBaseDir+"PATtuple_14_1_0uZ.root",
sampleBaseDir+"PATtuple_150_1_auo.root",
sampleBaseDir+"PATtuple_151_1_Z18.root",
sampleBaseDir+"PATtuple_152_1_qiR.root",
sampleBaseDir+"PATtuple_153_1_2bE.root",
sampleBaseDir+"PATtuple_154_1_Ia6.root",
sampleBaseDir+"PATtuple_155_1_Wuz.root",
sampleBaseDir+"PATtuple_156_1_0l8.root",
sampleBaseDir+"PATtuple_157_1_jCZ.root",
sampleBaseDir+"PATtuple_158_1_7aJ.root",
sampleBaseDir+"PATtuple_159_1_Ex3.root",
sampleBaseDir+"PATtuple_15_1_m6m.root",
sampleBaseDir+"PATtuple_160_1_2GR.root",
sampleBaseDir+"PATtuple_161_1_oaQ.root",
sampleBaseDir+"PATtuple_162_1_uQs.root",
sampleBaseDir+"PATtuple_163_1_XzC.root",
sampleBaseDir+"PATtuple_164_1_Xd1.root",
sampleBaseDir+"PATtuple_165_1_oic.root",
sampleBaseDir+"PATtuple_166_1_UzU.root",
sampleBaseDir+"PATtuple_167_1_Rk0.root",
sampleBaseDir+"PATtuple_168_1_3Lo.root",
sampleBaseDir+"PATtuple_169_1_rbY.root",
sampleBaseDir+"PATtuple_16_1_d1n.root",
sampleBaseDir+"PATtuple_170_1_7Km.root",
sampleBaseDir+"PATtuple_171_1_Ypa.root",
sampleBaseDir+"PATtuple_172_1_ssc.root",
sampleBaseDir+"PATtuple_173_1_mOg.root",
sampleBaseDir+"PATtuple_174_1_ZP7.root",
sampleBaseDir+"PATtuple_175_1_RQH.root",
sampleBaseDir+"PATtuple_176_1_Wh5.root",
sampleBaseDir+"PATtuple_177_1_onY.root",
sampleBaseDir+"PATtuple_178_1_IKF.root",
sampleBaseDir+"PATtuple_179_1_K1N.root",
sampleBaseDir+"PATtuple_17_1_eeK.root",
sampleBaseDir+"PATtuple_180_1_4W3.root",
sampleBaseDir+"PATtuple_181_1_Hc3.root",
sampleBaseDir+"PATtuple_182_1_a5k.root",
sampleBaseDir+"PATtuple_183_1_xZx.root",
sampleBaseDir+"PATtuple_184_1_vgH.root",
sampleBaseDir+"PATtuple_185_1_1Xw.root",
sampleBaseDir+"PATtuple_186_1_3fl.root",
sampleBaseDir+"PATtuple_187_1_825.root",
sampleBaseDir+"PATtuple_188_1_yp8.root",
sampleBaseDir+"PATtuple_189_1_KOQ.root",
sampleBaseDir+"PATtuple_18_1_2Dz.root",
sampleBaseDir+"PATtuple_190_1_SAg.root",
sampleBaseDir+"PATtuple_191_1_lcL.root",
sampleBaseDir+"PATtuple_192_1_liU.root",
sampleBaseDir+"PATtuple_193_1_x0l.root",
sampleBaseDir+"PATtuple_194_1_I68.root",
sampleBaseDir+"PATtuple_195_1_Tuu.root",
sampleBaseDir+"PATtuple_196_1_mrX.root",
sampleBaseDir+"PATtuple_197_1_oyb.root",
sampleBaseDir+"PATtuple_198_1_7Ls.root",
sampleBaseDir+"PATtuple_199_1_P5W.root",
sampleBaseDir+"PATtuple_19_1_Hh5.root",
sampleBaseDir+"PATtuple_1_1_nPv.root",
sampleBaseDir+"PATtuple_200_1_UZb.root",
sampleBaseDir+"PATtuple_201_1_W7X.root",
sampleBaseDir+"PATtuple_202_1_8u2.root",
sampleBaseDir+"PATtuple_203_1_ZoY.root",
sampleBaseDir+"PATtuple_204_1_WvU.root",
sampleBaseDir+"PATtuple_205_1_244.root",
sampleBaseDir+"PATtuple_206_1_Ltb.root",
sampleBaseDir+"PATtuple_207_1_cv3.root",
sampleBaseDir+"PATtuple_208_1_zf7.root",
sampleBaseDir+"PATtuple_209_1_gqU.root",
sampleBaseDir+"PATtuple_20_1_rgd.root",
sampleBaseDir+"PATtuple_210_1_LQ5.root",
sampleBaseDir+"PATtuple_211_1_196.root",
sampleBaseDir+"PATtuple_212_1_Evo.root",
sampleBaseDir+"PATtuple_213_1_kKt.root",
sampleBaseDir+"PATtuple_214_1_kUj.root",
sampleBaseDir+"PATtuple_215_1_x6F.root",
sampleBaseDir+"PATtuple_216_1_r4J.root",
sampleBaseDir+"PATtuple_217_1_pmd.root",
sampleBaseDir+"PATtuple_218_1_PvF.root",
sampleBaseDir+"PATtuple_219_1_wlq.root",
sampleBaseDir+"PATtuple_21_1_DyZ.root",
sampleBaseDir+"PATtuple_220_1_u1r.root",
sampleBaseDir+"PATtuple_221_1_yM4.root",
sampleBaseDir+"PATtuple_222_1_Ixg.root",
sampleBaseDir+"PATtuple_223_1_oeF.root",
sampleBaseDir+"PATtuple_224_1_NQa.root",
sampleBaseDir+"PATtuple_225_1_URC.root",
sampleBaseDir+"PATtuple_226_1_e9D.root",
sampleBaseDir+"PATtuple_227_1_UMD.root",
sampleBaseDir+"PATtuple_228_1_J4X.root",
sampleBaseDir+"PATtuple_22_1_ycl.root",
sampleBaseDir+"PATtuple_230_1_MWg.root",
sampleBaseDir+"PATtuple_231_1_kvl.root",
sampleBaseDir+"PATtuple_232_1_KTV.root",
sampleBaseDir+"PATtuple_233_1_EaD.root",
sampleBaseDir+"PATtuple_234_1_HC7.root",
sampleBaseDir+"PATtuple_235_1_ORp.root",
sampleBaseDir+"PATtuple_236_1_mNZ.root",
sampleBaseDir+"PATtuple_237_1_BNT.root",
sampleBaseDir+"PATtuple_238_1_EDR.root",
sampleBaseDir+"PATtuple_239_1_3do.root",
sampleBaseDir+"PATtuple_23_1_4eB.root",
sampleBaseDir+"PATtuple_240_1_EiK.root",
sampleBaseDir+"PATtuple_241_1_EiR.root",
sampleBaseDir+"PATtuple_242_1_3RI.root",
sampleBaseDir+"PATtuple_243_1_OiN.root",
sampleBaseDir+"PATtuple_244_1_7rX.root",
sampleBaseDir+"PATtuple_245_1_Kjt.root",
sampleBaseDir+"PATtuple_246_1_xkW.root",
sampleBaseDir+"PATtuple_247_1_Soi.root",
sampleBaseDir+"PATtuple_248_1_X4I.root",
sampleBaseDir+"PATtuple_249_1_n7z.root",
sampleBaseDir+"PATtuple_24_1_N9S.root",
sampleBaseDir+"PATtuple_250_1_wGL.root",
sampleBaseDir+"PATtuple_251_1_ufR.root",
sampleBaseDir+"PATtuple_252_1_bLj.root",
sampleBaseDir+"PATtuple_253_1_s8R.root",
sampleBaseDir+"PATtuple_254_1_dKq.root",
sampleBaseDir+"PATtuple_255_1_WsQ.root",
sampleBaseDir+"PATtuple_256_1_gD2.root",
sampleBaseDir+"PATtuple_257_1_MsW.root",
sampleBaseDir+"PATtuple_258_1_J34.root",
sampleBaseDir+"PATtuple_259_1_67l.root",
sampleBaseDir+"PATtuple_25_1_H4Y.root",
sampleBaseDir+"PATtuple_260_1_gVi.root",
sampleBaseDir+"PATtuple_261_1_Q7N.root",
sampleBaseDir+"PATtuple_262_1_X00.root",
sampleBaseDir+"PATtuple_263_1_hfm.root",
sampleBaseDir+"PATtuple_264_1_lBN.root",
sampleBaseDir+"PATtuple_265_1_ggN.root",
sampleBaseDir+"PATtuple_266_1_CGc.root",
sampleBaseDir+"PATtuple_267_1_rTx.root",
sampleBaseDir+"PATtuple_268_1_w8M.root",
sampleBaseDir+"PATtuple_269_1_U2J.root",
sampleBaseDir+"PATtuple_26_1_Tbo.root",
sampleBaseDir+"PATtuple_270_1_r8s.root",
sampleBaseDir+"PATtuple_271_1_yB4.root",
sampleBaseDir+"PATtuple_272_1_TPP.root",
sampleBaseDir+"PATtuple_273_1_X7y.root",
sampleBaseDir+"PATtuple_274_1_OIu.root",
sampleBaseDir+"PATtuple_275_1_YHj.root",
sampleBaseDir+"PATtuple_276_1_iLd.root",
sampleBaseDir+"PATtuple_277_1_DPA.root",
sampleBaseDir+"PATtuple_278_1_mNb.root",
sampleBaseDir+"PATtuple_279_1_2QX.root",
sampleBaseDir+"PATtuple_27_1_LfM.root",
sampleBaseDir+"PATtuple_280_1_bE7.root",
sampleBaseDir+"PATtuple_281_1_bdr.root",
sampleBaseDir+"PATtuple_282_1_XH7.root",
sampleBaseDir+"PATtuple_283_1_H7b.root",
sampleBaseDir+"PATtuple_284_1_JtM.root",
sampleBaseDir+"PATtuple_285_1_5ue.root",
sampleBaseDir+"PATtuple_286_1_ZOF.root",
sampleBaseDir+"PATtuple_287_1_KiV.root",
sampleBaseDir+"PATtuple_288_1_aAD.root",
sampleBaseDir+"PATtuple_289_1_apc.root",
sampleBaseDir+"PATtuple_28_1_eS3.root",
sampleBaseDir+"PATtuple_290_1_hOf.root",
sampleBaseDir+"PATtuple_291_1_25Z.root",
sampleBaseDir+"PATtuple_292_1_Y90.root",
sampleBaseDir+"PATtuple_293_1_zid.root",
sampleBaseDir+"PATtuple_294_1_yKr.root",
sampleBaseDir+"PATtuple_295_1_7IM.root",
sampleBaseDir+"PATtuple_296_1_FfJ.root",
sampleBaseDir+"PATtuple_297_1_Gcu.root",
sampleBaseDir+"PATtuple_298_1_F14.root",
sampleBaseDir+"PATtuple_299_1_x2q.root",
sampleBaseDir+"PATtuple_29_1_twM.root",
sampleBaseDir+"PATtuple_2_1_7HJ.root",
sampleBaseDir+"PATtuple_300_1_mMQ.root",
sampleBaseDir+"PATtuple_301_1_4Hq.root",
sampleBaseDir+"PATtuple_302_1_Whk.root",
sampleBaseDir+"PATtuple_303_1_2Ng.root",
sampleBaseDir+"PATtuple_304_1_xi6.root",
sampleBaseDir+"PATtuple_305_1_xjA.root",
sampleBaseDir+"PATtuple_306_1_7vD.root",
sampleBaseDir+"PATtuple_307_1_lFh.root",
sampleBaseDir+"PATtuple_308_1_znk.root",
sampleBaseDir+"PATtuple_309_1_rSX.root",
sampleBaseDir+"PATtuple_30_1_Qgz.root",
sampleBaseDir+"PATtuple_310_1_ZkU.root",
sampleBaseDir+"PATtuple_311_1_y59.root",
sampleBaseDir+"PATtuple_312_1_hNe.root",
sampleBaseDir+"PATtuple_313_1_CoC.root",
sampleBaseDir+"PATtuple_314_1_nBQ.root",
sampleBaseDir+"PATtuple_315_1_bnF.root",
sampleBaseDir+"PATtuple_316_1_da4.root",
sampleBaseDir+"PATtuple_317_1_mmd.root",
sampleBaseDir+"PATtuple_318_1_qgF.root",
sampleBaseDir+"PATtuple_319_1_sLv.root",
sampleBaseDir+"PATtuple_31_1_lbs.root",
sampleBaseDir+"PATtuple_320_1_0w2.root",
sampleBaseDir+"PATtuple_321_1_Pf3.root",
sampleBaseDir+"PATtuple_322_1_SLd.root",
sampleBaseDir+"PATtuple_323_1_pVS.root",
sampleBaseDir+"PATtuple_324_1_EWI.root",
sampleBaseDir+"PATtuple_325_1_3g0.root",
sampleBaseDir+"PATtuple_326_1_qio.root",
sampleBaseDir+"PATtuple_327_1_mBB.root",
sampleBaseDir+"PATtuple_328_1_7g8.root",
sampleBaseDir+"PATtuple_329_1_Ydw.root",
sampleBaseDir+"PATtuple_32_1_o7Y.root",
sampleBaseDir+"PATtuple_330_1_GKi.root",
sampleBaseDir+"PATtuple_331_1_7eU.root",
sampleBaseDir+"PATtuple_332_1_tBx.root",
sampleBaseDir+"PATtuple_333_1_Lq3.root",
sampleBaseDir+"PATtuple_334_1_sfY.root",
sampleBaseDir+"PATtuple_335_1_66U.root",
sampleBaseDir+"PATtuple_336_1_j8u.root",
sampleBaseDir+"PATtuple_337_1_I2d.root",
sampleBaseDir+"PATtuple_338_1_XcP.root",
sampleBaseDir+"PATtuple_339_1_IPC.root",
sampleBaseDir+"PATtuple_33_1_dFR.root",
sampleBaseDir+"PATtuple_340_1_eTD.root",
sampleBaseDir+"PATtuple_341_1_Dgp.root",
sampleBaseDir+"PATtuple_342_1_kcl.root",
sampleBaseDir+"PATtuple_343_1_bpT.root",
sampleBaseDir+"PATtuple_344_1_EmP.root",
sampleBaseDir+"PATtuple_345_1_Ijh.root",
sampleBaseDir+"PATtuple_346_1_9PO.root",
sampleBaseDir+"PATtuple_347_1_p0o.root",
sampleBaseDir+"PATtuple_348_1_ubW.root",
sampleBaseDir+"PATtuple_349_1_P2P.root",
sampleBaseDir+"PATtuple_34_1_x3X.root",
sampleBaseDir+"PATtuple_350_1_XoB.root",
sampleBaseDir+"PATtuple_351_1_RU9.root",
sampleBaseDir+"PATtuple_352_1_UY6.root",
sampleBaseDir+"PATtuple_353_1_FKZ.root",
sampleBaseDir+"PATtuple_354_1_dYt.root",
sampleBaseDir+"PATtuple_355_1_tIK.root",
sampleBaseDir+"PATtuple_356_1_GDb.root",
sampleBaseDir+"PATtuple_357_1_tNZ.root",
sampleBaseDir+"PATtuple_358_1_1IZ.root",
sampleBaseDir+"PATtuple_359_1_u0D.root",
sampleBaseDir+"PATtuple_35_1_sWs.root",
sampleBaseDir+"PATtuple_360_1_P7X.root",
sampleBaseDir+"PATtuple_361_1_auy.root",
sampleBaseDir+"PATtuple_362_1_77f.root",
sampleBaseDir+"PATtuple_363_1_OfO.root",
sampleBaseDir+"PATtuple_364_1_54g.root",
sampleBaseDir+"PATtuple_365_1_NHb.root",
sampleBaseDir+"PATtuple_366_1_Fh2.root",
sampleBaseDir+"PATtuple_367_1_vBx.root",
sampleBaseDir+"PATtuple_368_1_eq4.root",
sampleBaseDir+"PATtuple_369_1_Dkz.root",
sampleBaseDir+"PATtuple_36_1_fte.root",
sampleBaseDir+"PATtuple_370_1_Y90.root",
sampleBaseDir+"PATtuple_371_1_iZv.root",
sampleBaseDir+"PATtuple_372_1_rG4.root",
sampleBaseDir+"PATtuple_373_1_98n.root",
sampleBaseDir+"PATtuple_374_1_eUV.root",
sampleBaseDir+"PATtuple_375_1_Lwj.root",
sampleBaseDir+"PATtuple_376_1_6LM.root",
sampleBaseDir+"PATtuple_377_1_17O.root",
sampleBaseDir+"PATtuple_378_1_woS.root",
sampleBaseDir+"PATtuple_379_1_wei.root",
sampleBaseDir+"PATtuple_37_1_9nH.root",
sampleBaseDir+"PATtuple_380_1_vkJ.root",
sampleBaseDir+"PATtuple_381_1_bH1.root",
sampleBaseDir+"PATtuple_382_1_lvc.root",
sampleBaseDir+"PATtuple_383_1_0cx.root",
sampleBaseDir+"PATtuple_384_1_ib9.root",
sampleBaseDir+"PATtuple_385_1_3D2.root",
sampleBaseDir+"PATtuple_386_1_TQi.root",
sampleBaseDir+"PATtuple_387_1_B0H.root",
sampleBaseDir+"PATtuple_388_1_Dk2.root",
sampleBaseDir+"PATtuple_389_1_rdW.root",
sampleBaseDir+"PATtuple_38_1_bpg.root",
sampleBaseDir+"PATtuple_390_1_w3n.root",
sampleBaseDir+"PATtuple_391_1_wFJ.root",
sampleBaseDir+"PATtuple_392_1_xC9.root",
sampleBaseDir+"PATtuple_393_1_f3C.root",
sampleBaseDir+"PATtuple_394_1_jOb.root",
sampleBaseDir+"PATtuple_395_1_yJT.root",
sampleBaseDir+"PATtuple_396_1_iye.root",
sampleBaseDir+"PATtuple_397_1_1Mo.root",
sampleBaseDir+"PATtuple_398_1_Pys.root",
sampleBaseDir+"PATtuple_399_1_hvR.root",
sampleBaseDir+"PATtuple_39_1_oRh.root",
sampleBaseDir+"PATtuple_3_1_TRi.root",
sampleBaseDir+"PATtuple_400_1_4S0.root",
sampleBaseDir+"PATtuple_401_1_Ilk.root",
sampleBaseDir+"PATtuple_402_1_zJd.root",
sampleBaseDir+"PATtuple_403_1_o1d.root",
sampleBaseDir+"PATtuple_404_1_7b2.root",
sampleBaseDir+"PATtuple_405_1_VVz.root",
sampleBaseDir+"PATtuple_406_1_drF.root",
sampleBaseDir+"PATtuple_407_1_ZWc.root",
sampleBaseDir+"PATtuple_408_1_Q85.root",
sampleBaseDir+"PATtuple_409_1_O9y.root",
sampleBaseDir+"PATtuple_40_1_USm.root",
sampleBaseDir+"PATtuple_410_1_XY4.root",
sampleBaseDir+"PATtuple_411_1_ZkQ.root",
sampleBaseDir+"PATtuple_412_1_ntg.root",
sampleBaseDir+"PATtuple_413_1_vyE.root",
sampleBaseDir+"PATtuple_414_1_k8q.root",
sampleBaseDir+"PATtuple_415_1_UGr.root",
sampleBaseDir+"PATtuple_416_1_VGZ.root",
sampleBaseDir+"PATtuple_417_1_D0k.root",
sampleBaseDir+"PATtuple_418_1_hqh.root",
sampleBaseDir+"PATtuple_419_1_6Rt.root",
sampleBaseDir+"PATtuple_41_1_R44.root",
sampleBaseDir+"PATtuple_420_1_YEU.root",
sampleBaseDir+"PATtuple_421_1_OoM.root",
sampleBaseDir+"PATtuple_422_1_FdF.root",
sampleBaseDir+"PATtuple_423_1_DIW.root",
sampleBaseDir+"PATtuple_424_1_6Xe.root",
sampleBaseDir+"PATtuple_425_1_bsV.root",
sampleBaseDir+"PATtuple_426_1_7Uf.root",
sampleBaseDir+"PATtuple_427_1_bH5.root",
sampleBaseDir+"PATtuple_428_1_0NQ.root",
sampleBaseDir+"PATtuple_429_1_owC.root",
sampleBaseDir+"PATtuple_42_1_Dx8.root",
sampleBaseDir+"PATtuple_430_1_bgs.root",
sampleBaseDir+"PATtuple_431_1_Idg.root",
sampleBaseDir+"PATtuple_432_1_Jsg.root",
sampleBaseDir+"PATtuple_433_1_OmQ.root",
sampleBaseDir+"PATtuple_434_1_CI6.root",
sampleBaseDir+"PATtuple_435_1_Htd.root",
sampleBaseDir+"PATtuple_436_1_0Zf.root",
sampleBaseDir+"PATtuple_437_1_RnQ.root",
sampleBaseDir+"PATtuple_438_1_tLW.root",
sampleBaseDir+"PATtuple_439_1_yII.root",
sampleBaseDir+"PATtuple_43_1_H7h.root",
sampleBaseDir+"PATtuple_440_1_sVr.root",
sampleBaseDir+"PATtuple_441_1_eHY.root",
sampleBaseDir+"PATtuple_442_1_vaW.root",
sampleBaseDir+"PATtuple_443_1_oKV.root",
sampleBaseDir+"PATtuple_444_1_hSC.root",
sampleBaseDir+"PATtuple_445_1_T0Y.root",
sampleBaseDir+"PATtuple_446_1_53x.root",
sampleBaseDir+"PATtuple_447_1_yKj.root",
sampleBaseDir+"PATtuple_448_1_GNq.root",
sampleBaseDir+"PATtuple_449_1_Qfm.root",
sampleBaseDir+"PATtuple_44_1_mWG.root",
sampleBaseDir+"PATtuple_450_1_lMf.root",
sampleBaseDir+"PATtuple_451_1_1LT.root",
sampleBaseDir+"PATtuple_452_1_OUN.root",
sampleBaseDir+"PATtuple_453_1_gr7.root",
sampleBaseDir+"PATtuple_454_1_LEi.root",
sampleBaseDir+"PATtuple_455_1_3Pe.root",
sampleBaseDir+"PATtuple_456_1_oIJ.root",
sampleBaseDir+"PATtuple_457_1_be3.root",
sampleBaseDir+"PATtuple_458_1_J05.root",
sampleBaseDir+"PATtuple_459_1_WGH.root",
sampleBaseDir+"PATtuple_45_1_PTN.root",
sampleBaseDir+"PATtuple_460_1_9Xd.root",
sampleBaseDir+"PATtuple_461_1_DZu.root",
sampleBaseDir+"PATtuple_462_1_GQC.root",
sampleBaseDir+"PATtuple_463_1_i8l.root",
sampleBaseDir+"PATtuple_464_1_poO.root",
sampleBaseDir+"PATtuple_465_1_AyE.root",
sampleBaseDir+"PATtuple_466_1_vvy.root",
sampleBaseDir+"PATtuple_467_1_DkP.root",
sampleBaseDir+"PATtuple_468_1_76M.root",
sampleBaseDir+"PATtuple_469_1_AKt.root",
sampleBaseDir+"PATtuple_46_1_bN4.root",
sampleBaseDir+"PATtuple_470_1_M8T.root",
sampleBaseDir+"PATtuple_471_1_mXg.root",
sampleBaseDir+"PATtuple_472_1_lys.root",
sampleBaseDir+"PATtuple_473_1_VNM.root",
sampleBaseDir+"PATtuple_474_1_Qb6.root",
sampleBaseDir+"PATtuple_475_1_u8a.root",
sampleBaseDir+"PATtuple_476_1_6z8.root",
sampleBaseDir+"PATtuple_477_1_EAu.root",
sampleBaseDir+"PATtuple_478_1_qsg.root",
sampleBaseDir+"PATtuple_479_1_PSF.root",
sampleBaseDir+"PATtuple_47_1_G8u.root",
sampleBaseDir+"PATtuple_480_1_XrZ.root",
sampleBaseDir+"PATtuple_481_1_Io3.root",
sampleBaseDir+"PATtuple_482_1_OTy.root",
sampleBaseDir+"PATtuple_483_1_bjc.root",
sampleBaseDir+"PATtuple_484_1_1bd.root",
sampleBaseDir+"PATtuple_485_1_Tls.root",
sampleBaseDir+"PATtuple_486_1_RF6.root",
sampleBaseDir+"PATtuple_487_1_0XM.root",
sampleBaseDir+"PATtuple_488_1_5pD.root",
sampleBaseDir+"PATtuple_489_1_5aX.root",
sampleBaseDir+"PATtuple_48_1_JDq.root",
sampleBaseDir+"PATtuple_490_1_KPB.root",
sampleBaseDir+"PATtuple_491_1_7WP.root",
sampleBaseDir+"PATtuple_492_1_ub3.root",
sampleBaseDir+"PATtuple_493_1_LAE.root",
sampleBaseDir+"PATtuple_494_1_55B.root",
sampleBaseDir+"PATtuple_495_1_i10.root",
sampleBaseDir+"PATtuple_496_1_PuV.root",
sampleBaseDir+"PATtuple_497_1_v6h.root",
sampleBaseDir+"PATtuple_498_1_Wuo.root",
sampleBaseDir+"PATtuple_499_1_lnY.root",
sampleBaseDir+"PATtuple_49_1_Si5.root",
sampleBaseDir+"PATtuple_4_1_ttr.root",
sampleBaseDir+"PATtuple_500_1_MzZ.root",
sampleBaseDir+"PATtuple_501_1_j4o.root",
sampleBaseDir+"PATtuple_502_1_l8k.root",
sampleBaseDir+"PATtuple_504_1_MrL.root",
sampleBaseDir+"PATtuple_505_1_O3M.root",
sampleBaseDir+"PATtuple_506_1_AvW.root",
sampleBaseDir+"PATtuple_507_1_JFF.root",
sampleBaseDir+"PATtuple_508_1_BCF.root",
sampleBaseDir+"PATtuple_509_1_wuA.root",
sampleBaseDir+"PATtuple_50_1_B7b.root",
sampleBaseDir+"PATtuple_510_1_SAG.root",
sampleBaseDir+"PATtuple_511_1_YAg.root",
sampleBaseDir+"PATtuple_512_1_0KC.root",
sampleBaseDir+"PATtuple_513_1_DpL.root",
sampleBaseDir+"PATtuple_514_1_nqc.root",
sampleBaseDir+"PATtuple_515_1_NNd.root",
sampleBaseDir+"PATtuple_516_1_4qL.root",
sampleBaseDir+"PATtuple_517_1_ieC.root",
sampleBaseDir+"PATtuple_518_1_eMv.root",
sampleBaseDir+"PATtuple_519_1_hb9.root",
sampleBaseDir+"PATtuple_51_1_9vE.root",
sampleBaseDir+"PATtuple_520_1_7ka.root",
sampleBaseDir+"PATtuple_521_1_PQ5.root",
sampleBaseDir+"PATtuple_522_1_C2b.root",
sampleBaseDir+"PATtuple_523_1_0H7.root",
sampleBaseDir+"PATtuple_524_1_5px.root",
sampleBaseDir+"PATtuple_525_1_Oje.root",
sampleBaseDir+"PATtuple_526_1_Csw.root",
sampleBaseDir+"PATtuple_527_1_lY7.root",
sampleBaseDir+"PATtuple_528_1_UZk.root",
sampleBaseDir+"PATtuple_529_1_jAc.root",
sampleBaseDir+"PATtuple_52_1_ldn.root",
sampleBaseDir+"PATtuple_530_1_QfL.root",
sampleBaseDir+"PATtuple_531_1_ZMF.root",
sampleBaseDir+"PATtuple_532_1_Buj.root",
sampleBaseDir+"PATtuple_533_1_iTY.root",
sampleBaseDir+"PATtuple_534_1_ZhU.root",
sampleBaseDir+"PATtuple_535_1_nmZ.root",
sampleBaseDir+"PATtuple_536_1_jRv.root",
sampleBaseDir+"PATtuple_537_1_uym.root",
sampleBaseDir+"PATtuple_538_1_5Wp.root",
sampleBaseDir+"PATtuple_539_1_jsQ.root",
sampleBaseDir+"PATtuple_53_1_o6b.root",
sampleBaseDir+"PATtuple_540_1_5hs.root",
sampleBaseDir+"PATtuple_541_1_iSW.root",
sampleBaseDir+"PATtuple_542_1_gak.root",
sampleBaseDir+"PATtuple_543_1_hHK.root",
sampleBaseDir+"PATtuple_544_1_d5r.root",
sampleBaseDir+"PATtuple_545_1_i1j.root",
sampleBaseDir+"PATtuple_546_1_bnR.root",
sampleBaseDir+"PATtuple_547_1_Ys7.root",
sampleBaseDir+"PATtuple_548_1_Pjo.root",
sampleBaseDir+"PATtuple_549_1_udp.root",
sampleBaseDir+"PATtuple_54_1_I8A.root",
sampleBaseDir+"PATtuple_550_1_MQD.root",
sampleBaseDir+"PATtuple_551_1_qMF.root",
sampleBaseDir+"PATtuple_552_1_flB.root",
sampleBaseDir+"PATtuple_553_1_j8n.root",
sampleBaseDir+"PATtuple_554_1_uyp.root",
sampleBaseDir+"PATtuple_555_1_ayp.root",
sampleBaseDir+"PATtuple_556_1_1PS.root",
sampleBaseDir+"PATtuple_557_1_jUf.root",
sampleBaseDir+"PATtuple_558_1_C23.root",
sampleBaseDir+"PATtuple_55_1_RO7.root",
sampleBaseDir+"PATtuple_560_1_cKH.root",
sampleBaseDir+"PATtuple_561_1_QOz.root",
sampleBaseDir+"PATtuple_562_1_07c.root",
sampleBaseDir+"PATtuple_563_1_mAW.root",
sampleBaseDir+"PATtuple_564_1_AEk.root",
sampleBaseDir+"PATtuple_565_1_00r.root",
sampleBaseDir+"PATtuple_566_1_sZg.root",
sampleBaseDir+"PATtuple_567_1_DHg.root",
sampleBaseDir+"PATtuple_568_1_smd.root",
sampleBaseDir+"PATtuple_569_1_vOH.root",
sampleBaseDir+"PATtuple_56_1_3q4.root",
sampleBaseDir+"PATtuple_570_1_4N2.root",
sampleBaseDir+"PATtuple_571_1_7dn.root",
sampleBaseDir+"PATtuple_572_1_o92.root",
sampleBaseDir+"PATtuple_573_1_OTu.root",
sampleBaseDir+"PATtuple_574_1_eEy.root",
sampleBaseDir+"PATtuple_575_1_UcB.root",
sampleBaseDir+"PATtuple_576_1_JCV.root",
sampleBaseDir+"PATtuple_577_1_cYT.root",
sampleBaseDir+"PATtuple_578_1_fLf.root",
sampleBaseDir+"PATtuple_579_1_1dd.root",
sampleBaseDir+"PATtuple_57_1_GcY.root",
sampleBaseDir+"PATtuple_580_1_b31.root",
sampleBaseDir+"PATtuple_581_1_cQs.root",
sampleBaseDir+"PATtuple_582_1_Dch.root",
sampleBaseDir+"PATtuple_583_1_4Ir.root",
sampleBaseDir+"PATtuple_584_1_Xze.root",
sampleBaseDir+"PATtuple_585_1_OXp.root",
sampleBaseDir+"PATtuple_586_1_UxA.root",
sampleBaseDir+"PATtuple_587_1_RQk.root",
sampleBaseDir+"PATtuple_588_1_VsE.root",
sampleBaseDir+"PATtuple_589_1_TuT.root",
sampleBaseDir+"PATtuple_58_1_Nla.root",
sampleBaseDir+"PATtuple_590_1_XIh.root",
sampleBaseDir+"PATtuple_591_1_lsX.root",
sampleBaseDir+"PATtuple_592_1_VrD.root",
sampleBaseDir+"PATtuple_593_1_aUv.root",
sampleBaseDir+"PATtuple_594_1_Of4.root",
sampleBaseDir+"PATtuple_595_1_1hF.root",
sampleBaseDir+"PATtuple_596_1_Ol5.root",
sampleBaseDir+"PATtuple_597_1_toZ.root",
sampleBaseDir+"PATtuple_598_1_nkL.root",
sampleBaseDir+"PATtuple_599_1_bAl.root",
sampleBaseDir+"PATtuple_59_1_4uv.root",
sampleBaseDir+"PATtuple_5_1_Ryy.root",
sampleBaseDir+"PATtuple_600_1_uPn.root",
sampleBaseDir+"PATtuple_601_1_JhF.root",
sampleBaseDir+"PATtuple_602_1_eG3.root",
sampleBaseDir+"PATtuple_603_1_cwh.root",
sampleBaseDir+"PATtuple_604_1_Q1N.root",
sampleBaseDir+"PATtuple_605_1_ptM.root",
sampleBaseDir+"PATtuple_606_1_V4B.root",
sampleBaseDir+"PATtuple_607_1_QNK.root",
sampleBaseDir+"PATtuple_608_1_qhp.root",
sampleBaseDir+"PATtuple_609_1_b0l.root",
sampleBaseDir+"PATtuple_60_1_5F5.root",
sampleBaseDir+"PATtuple_610_1_76q.root",
sampleBaseDir+"PATtuple_611_1_Uz2.root",
sampleBaseDir+"PATtuple_612_1_GSk.root",
sampleBaseDir+"PATtuple_613_1_sOe.root",
sampleBaseDir+"PATtuple_614_1_B0v.root",
sampleBaseDir+"PATtuple_615_1_SnO.root",
sampleBaseDir+"PATtuple_616_1_ZoY.root",
sampleBaseDir+"PATtuple_617_1_qpB.root",
sampleBaseDir+"PATtuple_618_1_6uP.root",
sampleBaseDir+"PATtuple_619_1_KXr.root",
sampleBaseDir+"PATtuple_61_1_gVr.root",
sampleBaseDir+"PATtuple_620_1_ib7.root",
sampleBaseDir+"PATtuple_621_1_ApI.root",
sampleBaseDir+"PATtuple_622_1_vJw.root",
sampleBaseDir+"PATtuple_623_1_W7f.root",
sampleBaseDir+"PATtuple_624_1_dB0.root",
sampleBaseDir+"PATtuple_625_1_pNY.root",
sampleBaseDir+"PATtuple_626_1_oEH.root",
sampleBaseDir+"PATtuple_627_1_2r5.root",
sampleBaseDir+"PATtuple_628_1_VyB.root",
sampleBaseDir+"PATtuple_629_1_SCY.root",
sampleBaseDir+"PATtuple_62_1_VSC.root",
sampleBaseDir+"PATtuple_630_1_1M0.root",
sampleBaseDir+"PATtuple_631_1_LcM.root",
sampleBaseDir+"PATtuple_632_1_RuX.root",
sampleBaseDir+"PATtuple_633_1_d9K.root",
sampleBaseDir+"PATtuple_634_1_UQi.root",
sampleBaseDir+"PATtuple_635_1_uus.root",
sampleBaseDir+"PATtuple_636_1_7Ba.root",
sampleBaseDir+"PATtuple_637_1_NUi.root",
sampleBaseDir+"PATtuple_638_1_6jt.root",
sampleBaseDir+"PATtuple_639_1_ZKa.root",
sampleBaseDir+"PATtuple_63_1_K5C.root",
sampleBaseDir+"PATtuple_640_1_pOH.root",
sampleBaseDir+"PATtuple_641_1_f0a.root",
sampleBaseDir+"PATtuple_643_1_30o.root",
sampleBaseDir+"PATtuple_644_1_J8d.root",
sampleBaseDir+"PATtuple_645_1_peU.root",
sampleBaseDir+"PATtuple_647_1_NYt.root",
sampleBaseDir+"PATtuple_648_1_brr.root",
sampleBaseDir+"PATtuple_649_1_yeJ.root",
sampleBaseDir+"PATtuple_64_1_4YE.root",
sampleBaseDir+"PATtuple_650_1_3jf.root",
sampleBaseDir+"PATtuple_651_1_BcI.root",
sampleBaseDir+"PATtuple_652_1_xXv.root",
sampleBaseDir+"PATtuple_653_1_sZw.root",
sampleBaseDir+"PATtuple_654_1_faW.root",
sampleBaseDir+"PATtuple_655_1_0Fm.root",
sampleBaseDir+"PATtuple_656_1_OYm.root",
sampleBaseDir+"PATtuple_657_1_dWa.root",
sampleBaseDir+"PATtuple_658_1_Kp3.root",
sampleBaseDir+"PATtuple_659_1_T6G.root",
sampleBaseDir+"PATtuple_65_1_lzf.root",
sampleBaseDir+"PATtuple_660_1_omL.root",
sampleBaseDir+"PATtuple_661_1_jyK.root",
sampleBaseDir+"PATtuple_662_1_HrO.root",
sampleBaseDir+"PATtuple_663_1_MHi.root",
sampleBaseDir+"PATtuple_664_1_zFB.root",
sampleBaseDir+"PATtuple_665_1_rAw.root",
sampleBaseDir+"PATtuple_666_1_n3S.root",
sampleBaseDir+"PATtuple_667_1_Ybf.root",
sampleBaseDir+"PATtuple_668_1_4OK.root",
sampleBaseDir+"PATtuple_669_1_ni7.root",
sampleBaseDir+"PATtuple_66_1_H3I.root",
sampleBaseDir+"PATtuple_670_1_0k4.root",
sampleBaseDir+"PATtuple_671_1_yk2.root",
sampleBaseDir+"PATtuple_672_1_7mB.root",
sampleBaseDir+"PATtuple_673_1_Sm9.root",
sampleBaseDir+"PATtuple_674_1_qDc.root",
sampleBaseDir+"PATtuple_675_1_8Zu.root",
sampleBaseDir+"PATtuple_676_1_6U6.root",
sampleBaseDir+"PATtuple_677_1_YuG.root",
sampleBaseDir+"PATtuple_678_1_G6v.root",
sampleBaseDir+"PATtuple_679_1_I0h.root",
sampleBaseDir+"PATtuple_67_1_VXx.root",
sampleBaseDir+"PATtuple_680_1_iFm.root",
sampleBaseDir+"PATtuple_682_1_v4T.root",
sampleBaseDir+"PATtuple_683_1_yHM.root",
sampleBaseDir+"PATtuple_684_1_jXb.root",
sampleBaseDir+"PATtuple_685_1_DS5.root",
sampleBaseDir+"PATtuple_686_1_yUH.root",
sampleBaseDir+"PATtuple_687_1_6Ln.root",
sampleBaseDir+"PATtuple_688_1_Ing.root",
sampleBaseDir+"PATtuple_689_1_pDk.root",
sampleBaseDir+"PATtuple_68_1_77N.root",
sampleBaseDir+"PATtuple_690_1_vv6.root",
sampleBaseDir+"PATtuple_691_1_x6K.root",
sampleBaseDir+"PATtuple_692_1_dpw.root",
sampleBaseDir+"PATtuple_693_1_fF5.root",
sampleBaseDir+"PATtuple_694_1_UXH.root",
sampleBaseDir+"PATtuple_695_1_oJ5.root",
sampleBaseDir+"PATtuple_696_1_wWx.root",
sampleBaseDir+"PATtuple_697_1_77m.root",
sampleBaseDir+"PATtuple_698_1_J3M.root",
sampleBaseDir+"PATtuple_699_1_thK.root",
sampleBaseDir+"PATtuple_69_1_XeV.root",
sampleBaseDir+"PATtuple_6_1_6iX.root",
sampleBaseDir+"PATtuple_700_1_a7Z.root",
sampleBaseDir+"PATtuple_701_1_P1V.root",
sampleBaseDir+"PATtuple_702_1_fkv.root",
sampleBaseDir+"PATtuple_704_1_VLe.root",
sampleBaseDir+"PATtuple_705_1_QIO.root",
sampleBaseDir+"PATtuple_706_1_og8.root",
sampleBaseDir+"PATtuple_707_1_4bG.root",
sampleBaseDir+"PATtuple_708_1_Yv9.root",
sampleBaseDir+"PATtuple_709_1_Hnx.root",
sampleBaseDir+"PATtuple_70_1_9NF.root",
sampleBaseDir+"PATtuple_710_1_BHY.root",
sampleBaseDir+"PATtuple_711_1_Qg7.root",
sampleBaseDir+"PATtuple_712_1_zmc.root",
sampleBaseDir+"PATtuple_713_1_OVH.root",
sampleBaseDir+"PATtuple_714_1_ctI.root",
sampleBaseDir+"PATtuple_715_1_UMV.root",
sampleBaseDir+"PATtuple_716_1_suf.root",
sampleBaseDir+"PATtuple_717_1_51D.root",
sampleBaseDir+"PATtuple_718_1_9EO.root",
sampleBaseDir+"PATtuple_719_1_uxC.root",
sampleBaseDir+"PATtuple_71_1_q6W.root",
sampleBaseDir+"PATtuple_720_1_ZDK.root",
sampleBaseDir+"PATtuple_721_1_2hP.root",
sampleBaseDir+"PATtuple_722_1_QiZ.root",
sampleBaseDir+"PATtuple_723_1_V8Q.root",
sampleBaseDir+"PATtuple_724_1_WvI.root",
sampleBaseDir+"PATtuple_725_1_tjw.root",
sampleBaseDir+"PATtuple_726_1_lwZ.root",
sampleBaseDir+"PATtuple_727_1_X5Z.root",
sampleBaseDir+"PATtuple_728_1_SeZ.root",
sampleBaseDir+"PATtuple_729_1_G6h.root",
sampleBaseDir+"PATtuple_72_1_m3x.root",
sampleBaseDir+"PATtuple_730_1_nPC.root",
sampleBaseDir+"PATtuple_731_1_x77.root",
sampleBaseDir+"PATtuple_732_1_3XV.root",
sampleBaseDir+"PATtuple_733_1_6gy.root",
sampleBaseDir+"PATtuple_734_1_I7g.root",
sampleBaseDir+"PATtuple_735_1_GfP.root",
sampleBaseDir+"PATtuple_736_1_Y3R.root",
sampleBaseDir+"PATtuple_737_1_6bz.root",
sampleBaseDir+"PATtuple_738_1_RkY.root",
sampleBaseDir+"PATtuple_739_1_zLS.root",
sampleBaseDir+"PATtuple_73_1_nu7.root",
sampleBaseDir+"PATtuple_740_1_J4h.root",
sampleBaseDir+"PATtuple_741_1_YCE.root",
sampleBaseDir+"PATtuple_742_1_gat.root",
sampleBaseDir+"PATtuple_743_1_InX.root",
sampleBaseDir+"PATtuple_744_1_Sdv.root",
sampleBaseDir+"PATtuple_745_1_aC7.root",
sampleBaseDir+"PATtuple_746_1_MQe.root",
sampleBaseDir+"PATtuple_747_1_5hK.root",
sampleBaseDir+"PATtuple_748_1_I4E.root",
sampleBaseDir+"PATtuple_749_1_dvZ.root",
sampleBaseDir+"PATtuple_74_1_vUN.root",
sampleBaseDir+"PATtuple_750_1_1FP.root",
sampleBaseDir+"PATtuple_751_1_fuk.root",
sampleBaseDir+"PATtuple_752_1_cal.root",
sampleBaseDir+"PATtuple_753_1_vkr.root",
sampleBaseDir+"PATtuple_754_1_wEF.root",
sampleBaseDir+"PATtuple_755_1_3Ga.root",
sampleBaseDir+"PATtuple_756_1_z3I.root",
sampleBaseDir+"PATtuple_75_1_3Bx.root",
sampleBaseDir+"PATtuple_76_1_k0J.root",
sampleBaseDir+"PATtuple_77_1_rt3.root",
sampleBaseDir+"PATtuple_78_1_yP9.root",
sampleBaseDir+"PATtuple_79_1_hos.root",
sampleBaseDir+"PATtuple_7_1_K00.root",
sampleBaseDir+"PATtuple_80_1_gHs.root",
sampleBaseDir+"PATtuple_81_1_K2U.root",
sampleBaseDir+"PATtuple_82_1_OHO.root",
sampleBaseDir+"PATtuple_83_1_SJ2.root",
sampleBaseDir+"PATtuple_84_1_yU4.root",
sampleBaseDir+"PATtuple_85_1_fsk.root",
sampleBaseDir+"PATtuple_86_1_3kr.root",
sampleBaseDir+"PATtuple_87_1_UDD.root",
sampleBaseDir+"PATtuple_88_1_aIG.root",
sampleBaseDir+"PATtuple_89_1_wcL.root",
sampleBaseDir+"PATtuple_8_1_LuL.root",
sampleBaseDir+"PATtuple_90_1_vJ0.root",
sampleBaseDir+"PATtuple_91_1_IPu.root",
sampleBaseDir+"PATtuple_92_1_knc.root",
sampleBaseDir+"PATtuple_93_1_08M.root",
sampleBaseDir+"PATtuple_94_1_sjW.root",
sampleBaseDir+"PATtuple_95_1_RtB.root",
sampleBaseDir+"PATtuple_96_1_eZE.root",
sampleBaseDir+"PATtuple_97_1_E5G.root",
sampleBaseDir+"PATtuple_98_1_hzK.root",
sampleBaseDir+"PATtuple_99_1_4si.root",
sampleBaseDir+"PATtuple_9_1_awO.root",
]