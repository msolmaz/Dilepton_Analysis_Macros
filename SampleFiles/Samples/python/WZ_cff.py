sampleDataSet = '/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 10000283

sampleXSec = 32.3 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"





samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/WZ_pat_20140328/demattia//WZ_TuneZ2star_8TeV_pythia6_tauola/WZ_pat_20140328/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_100_1_frH.root",
sampleBaseDir+"PATtuple_101_1_V0f.root",
sampleBaseDir+"PATtuple_102_1_5yc.root",
sampleBaseDir+"PATtuple_103_1_YKB.root",
sampleBaseDir+"PATtuple_104_1_I2u.root",
sampleBaseDir+"PATtuple_105_1_X2h.root",
sampleBaseDir+"PATtuple_106_1_nvf.root",
sampleBaseDir+"PATtuple_107_1_7pk.root",
sampleBaseDir+"PATtuple_108_1_yN2.root",
sampleBaseDir+"PATtuple_109_1_Ypq.root",
sampleBaseDir+"PATtuple_10_1_sGk.root",
sampleBaseDir+"PATtuple_110_1_iu3.root",
sampleBaseDir+"PATtuple_111_1_0W5.root",
sampleBaseDir+"PATtuple_112_1_OGL.root",
sampleBaseDir+"PATtuple_113_1_J4M.root",
sampleBaseDir+"PATtuple_114_1_z7W.root",
sampleBaseDir+"PATtuple_115_1_pBa.root",
sampleBaseDir+"PATtuple_116_1_R3S.root",
sampleBaseDir+"PATtuple_117_1_MIq.root",
sampleBaseDir+"PATtuple_118_1_XB1.root",
sampleBaseDir+"PATtuple_119_1_0yR.root",
sampleBaseDir+"PATtuple_11_1_2uL.root",
sampleBaseDir+"PATtuple_120_1_0pB.root",
sampleBaseDir+"PATtuple_121_1_u4Q.root",
sampleBaseDir+"PATtuple_122_1_tzP.root",
sampleBaseDir+"PATtuple_123_1_Mit.root",
sampleBaseDir+"PATtuple_124_1_yYN.root",
sampleBaseDir+"PATtuple_125_1_MOU.root",
sampleBaseDir+"PATtuple_126_1_JhR.root",
sampleBaseDir+"PATtuple_127_1_Sm8.root",
sampleBaseDir+"PATtuple_128_1_j42.root",
sampleBaseDir+"PATtuple_129_1_mcf.root",
sampleBaseDir+"PATtuple_12_1_omS.root",
sampleBaseDir+"PATtuple_130_1_3Sg.root",
sampleBaseDir+"PATtuple_131_1_fSk.root",
sampleBaseDir+"PATtuple_132_1_XEV.root",
sampleBaseDir+"PATtuple_133_1_QcQ.root",
sampleBaseDir+"PATtuple_134_1_ylk.root",
sampleBaseDir+"PATtuple_135_1_Vek.root",
sampleBaseDir+"PATtuple_136_1_U5B.root",
sampleBaseDir+"PATtuple_137_1_Ns5.root",
sampleBaseDir+"PATtuple_138_1_EoM.root",
sampleBaseDir+"PATtuple_139_1_1b3.root",
sampleBaseDir+"PATtuple_13_1_Sph.root",
sampleBaseDir+"PATtuple_140_1_skQ.root",
sampleBaseDir+"PATtuple_141_1_mOK.root",
sampleBaseDir+"PATtuple_142_1_amX.root",
sampleBaseDir+"PATtuple_143_1_hNu.root",
sampleBaseDir+"PATtuple_144_1_Vcq.root",
sampleBaseDir+"PATtuple_145_1_Xmm.root",
sampleBaseDir+"PATtuple_146_1_CRq.root",
sampleBaseDir+"PATtuple_147_1_m8B.root",
sampleBaseDir+"PATtuple_148_1_rTI.root",
sampleBaseDir+"PATtuple_149_1_RV1.root",
sampleBaseDir+"PATtuple_14_1_Ssw.root",
sampleBaseDir+"PATtuple_150_1_Mn7.root",
sampleBaseDir+"PATtuple_151_1_Z8s.root",
sampleBaseDir+"PATtuple_152_1_9tY.root",
sampleBaseDir+"PATtuple_153_1_sgT.root",
sampleBaseDir+"PATtuple_154_1_hRD.root",
sampleBaseDir+"PATtuple_155_1_YdO.root",
sampleBaseDir+"PATtuple_156_1_HlT.root",
sampleBaseDir+"PATtuple_157_1_hcH.root",
sampleBaseDir+"PATtuple_158_1_SVs.root",
sampleBaseDir+"PATtuple_159_1_Ffl.root",
sampleBaseDir+"PATtuple_15_1_bBh.root",
sampleBaseDir+"PATtuple_160_1_K6J.root",
sampleBaseDir+"PATtuple_161_1_Yax.root",
sampleBaseDir+"PATtuple_162_1_aJP.root",
sampleBaseDir+"PATtuple_163_1_hi5.root",
sampleBaseDir+"PATtuple_164_1_x2Y.root",
sampleBaseDir+"PATtuple_165_1_paK.root",
sampleBaseDir+"PATtuple_166_1_InT.root",
sampleBaseDir+"PATtuple_167_1_znj.root",
sampleBaseDir+"PATtuple_168_1_aWO.root",
sampleBaseDir+"PATtuple_169_1_cci.root",
sampleBaseDir+"PATtuple_16_1_YoH.root",
sampleBaseDir+"PATtuple_170_1_9Gk.root",
sampleBaseDir+"PATtuple_171_1_AoO.root",
sampleBaseDir+"PATtuple_172_1_4qG.root",
sampleBaseDir+"PATtuple_173_1_gt3.root",
sampleBaseDir+"PATtuple_174_1_Ppr.root",
sampleBaseDir+"PATtuple_175_1_8bi.root",
sampleBaseDir+"PATtuple_176_1_RWJ.root",
sampleBaseDir+"PATtuple_177_1_bjz.root",
sampleBaseDir+"PATtuple_178_1_KjX.root",
sampleBaseDir+"PATtuple_179_1_dkW.root",
sampleBaseDir+"PATtuple_17_1_MEi.root",
sampleBaseDir+"PATtuple_180_1_kVX.root",
sampleBaseDir+"PATtuple_181_1_AjN.root",
sampleBaseDir+"PATtuple_182_1_6Hw.root",
sampleBaseDir+"PATtuple_183_1_hdx.root",
sampleBaseDir+"PATtuple_184_1_xma.root",
sampleBaseDir+"PATtuple_185_1_7d5.root",
sampleBaseDir+"PATtuple_186_1_iJy.root",
sampleBaseDir+"PATtuple_187_1_wdn.root",
sampleBaseDir+"PATtuple_188_1_ssY.root",
sampleBaseDir+"PATtuple_189_1_t4r.root",
sampleBaseDir+"PATtuple_18_1_c2l.root",
sampleBaseDir+"PATtuple_190_1_y9x.root",
sampleBaseDir+"PATtuple_191_1_p4B.root",
sampleBaseDir+"PATtuple_192_1_Tpv.root",
sampleBaseDir+"PATtuple_193_1_J1x.root",
sampleBaseDir+"PATtuple_194_1_Fpb.root",
sampleBaseDir+"PATtuple_195_1_fZJ.root",
sampleBaseDir+"PATtuple_196_1_7l3.root",
sampleBaseDir+"PATtuple_197_1_NhW.root",
sampleBaseDir+"PATtuple_198_1_qUf.root",
sampleBaseDir+"PATtuple_199_1_v9t.root",
sampleBaseDir+"PATtuple_19_1_pHN.root",
sampleBaseDir+"PATtuple_1_1_rua.root",
sampleBaseDir+"PATtuple_200_1_EBG.root",
sampleBaseDir+"PATtuple_201_1_t4x.root",
sampleBaseDir+"PATtuple_202_1_vc3.root",
sampleBaseDir+"PATtuple_203_1_M6W.root",
sampleBaseDir+"PATtuple_204_1_JvS.root",
sampleBaseDir+"PATtuple_205_1_6JV.root",
sampleBaseDir+"PATtuple_206_1_IOS.root",
sampleBaseDir+"PATtuple_207_1_SKQ.root",
sampleBaseDir+"PATtuple_208_1_cvk.root",
sampleBaseDir+"PATtuple_209_1_Pxb.root",
sampleBaseDir+"PATtuple_20_1_Ogr.root",
sampleBaseDir+"PATtuple_210_1_uTl.root",
sampleBaseDir+"PATtuple_211_1_fY0.root",
sampleBaseDir+"PATtuple_212_1_uMy.root",
sampleBaseDir+"PATtuple_213_1_7LS.root",
sampleBaseDir+"PATtuple_214_1_aim.root",
sampleBaseDir+"PATtuple_215_1_x0d.root",
sampleBaseDir+"PATtuple_216_1_ctn.root",
sampleBaseDir+"PATtuple_217_1_Z8B.root",
sampleBaseDir+"PATtuple_218_1_TRP.root",
sampleBaseDir+"PATtuple_219_1_04e.root",
sampleBaseDir+"PATtuple_21_1_YRn.root",
sampleBaseDir+"PATtuple_220_1_yPz.root",
sampleBaseDir+"PATtuple_221_1_dAa.root",
sampleBaseDir+"PATtuple_222_1_zuj.root",
sampleBaseDir+"PATtuple_223_1_QfX.root",
sampleBaseDir+"PATtuple_224_1_ixq.root",
sampleBaseDir+"PATtuple_225_1_Vlc.root",
sampleBaseDir+"PATtuple_226_1_yf3.root",
sampleBaseDir+"PATtuple_227_1_ogq.root",
sampleBaseDir+"PATtuple_228_1_zC8.root",
sampleBaseDir+"PATtuple_229_1_Hx1.root",
sampleBaseDir+"PATtuple_22_1_JmU.root",
sampleBaseDir+"PATtuple_230_1_JmR.root",
sampleBaseDir+"PATtuple_231_1_86q.root",
sampleBaseDir+"PATtuple_232_1_HVO.root",
sampleBaseDir+"PATtuple_233_1_S8m.root",
sampleBaseDir+"PATtuple_234_1_N6r.root",
sampleBaseDir+"PATtuple_235_1_IkG.root",
sampleBaseDir+"PATtuple_236_1_FT5.root",
sampleBaseDir+"PATtuple_237_1_0gQ.root",
sampleBaseDir+"PATtuple_238_1_m6O.root",
sampleBaseDir+"PATtuple_239_1_Vdt.root",
sampleBaseDir+"PATtuple_23_1_DKn.root",
sampleBaseDir+"PATtuple_240_1_3U5.root",
sampleBaseDir+"PATtuple_241_1_YF5.root",
sampleBaseDir+"PATtuple_242_1_lwn.root",
sampleBaseDir+"PATtuple_243_1_nVf.root",
sampleBaseDir+"PATtuple_244_1_pxw.root",
sampleBaseDir+"PATtuple_245_1_t5N.root",
sampleBaseDir+"PATtuple_246_1_L2V.root",
sampleBaseDir+"PATtuple_247_1_cul.root",
sampleBaseDir+"PATtuple_248_1_eE4.root",
sampleBaseDir+"PATtuple_249_1_w5I.root",
sampleBaseDir+"PATtuple_24_1_bD4.root",
sampleBaseDir+"PATtuple_250_1_SZW.root",
sampleBaseDir+"PATtuple_251_1_kYG.root",
sampleBaseDir+"PATtuple_252_1_UGM.root",
sampleBaseDir+"PATtuple_253_1_J82.root",
sampleBaseDir+"PATtuple_254_1_sbk.root",
sampleBaseDir+"PATtuple_255_1_Fc7.root",
sampleBaseDir+"PATtuple_256_1_1xJ.root",
sampleBaseDir+"PATtuple_257_1_w67.root",
sampleBaseDir+"PATtuple_258_1_kWa.root",
sampleBaseDir+"PATtuple_259_1_Z7t.root",
sampleBaseDir+"PATtuple_25_1_pYU.root",
sampleBaseDir+"PATtuple_260_1_VAL.root",
sampleBaseDir+"PATtuple_261_1_9NW.root",
sampleBaseDir+"PATtuple_262_1_WSJ.root",
sampleBaseDir+"PATtuple_263_1_Yax.root",
sampleBaseDir+"PATtuple_264_1_8rv.root",
sampleBaseDir+"PATtuple_265_1_1ay.root",
sampleBaseDir+"PATtuple_266_1_4v1.root",
sampleBaseDir+"PATtuple_267_1_M7U.root",
sampleBaseDir+"PATtuple_268_1_ATa.root",
sampleBaseDir+"PATtuple_269_1_C7M.root",
sampleBaseDir+"PATtuple_26_1_0XU.root",
sampleBaseDir+"PATtuple_270_1_thy.root",
sampleBaseDir+"PATtuple_271_1_duB.root",
sampleBaseDir+"PATtuple_272_1_YoL.root",
sampleBaseDir+"PATtuple_273_1_dUb.root",
sampleBaseDir+"PATtuple_274_1_BZe.root",
sampleBaseDir+"PATtuple_275_1_JJ1.root",
sampleBaseDir+"PATtuple_276_1_Ay7.root",
sampleBaseDir+"PATtuple_277_1_byg.root",
sampleBaseDir+"PATtuple_278_1_Zpk.root",
sampleBaseDir+"PATtuple_279_1_OjW.root",
sampleBaseDir+"PATtuple_27_1_JwX.root",
sampleBaseDir+"PATtuple_280_1_rHi.root",
sampleBaseDir+"PATtuple_281_1_3Lo.root",
sampleBaseDir+"PATtuple_282_1_UVR.root",
sampleBaseDir+"PATtuple_283_1_SI3.root",
sampleBaseDir+"PATtuple_284_1_aQg.root",
sampleBaseDir+"PATtuple_285_1_DUC.root",
sampleBaseDir+"PATtuple_286_1_vRJ.root",
sampleBaseDir+"PATtuple_287_1_YTS.root",
sampleBaseDir+"PATtuple_288_1_4Zt.root",
sampleBaseDir+"PATtuple_289_1_azW.root",
sampleBaseDir+"PATtuple_28_1_801.root",
sampleBaseDir+"PATtuple_290_1_79b.root",
sampleBaseDir+"PATtuple_291_1_lxk.root",
sampleBaseDir+"PATtuple_292_1_s0O.root",
sampleBaseDir+"PATtuple_293_1_mWk.root",
sampleBaseDir+"PATtuple_294_1_Nq1.root",
sampleBaseDir+"PATtuple_295_1_yNB.root",
sampleBaseDir+"PATtuple_296_1_8PT.root",
sampleBaseDir+"PATtuple_297_1_UNU.root",
sampleBaseDir+"PATtuple_298_1_xEs.root",
sampleBaseDir+"PATtuple_299_1_4zd.root",
sampleBaseDir+"PATtuple_29_1_s9S.root",
sampleBaseDir+"PATtuple_2_1_dPu.root",
sampleBaseDir+"PATtuple_300_1_VFG.root",
sampleBaseDir+"PATtuple_301_1_MRT.root",
sampleBaseDir+"PATtuple_302_1_dcG.root",
sampleBaseDir+"PATtuple_303_1_SbJ.root",
sampleBaseDir+"PATtuple_304_1_2MI.root",
sampleBaseDir+"PATtuple_305_1_CTi.root",
sampleBaseDir+"PATtuple_306_1_wrO.root",
sampleBaseDir+"PATtuple_307_1_Q6E.root",
sampleBaseDir+"PATtuple_308_1_FtZ.root",
sampleBaseDir+"PATtuple_309_1_II4.root",
sampleBaseDir+"PATtuple_30_1_5Do.root",
sampleBaseDir+"PATtuple_310_1_00T.root",
sampleBaseDir+"PATtuple_311_1_6BG.root",
sampleBaseDir+"PATtuple_312_1_ux7.root",
sampleBaseDir+"PATtuple_313_1_xOi.root",
sampleBaseDir+"PATtuple_314_1_Q0n.root",
sampleBaseDir+"PATtuple_315_1_JaU.root",
sampleBaseDir+"PATtuple_316_1_1No.root",
sampleBaseDir+"PATtuple_317_1_CNy.root",
sampleBaseDir+"PATtuple_318_1_6rW.root",
sampleBaseDir+"PATtuple_319_1_gsM.root",
sampleBaseDir+"PATtuple_31_1_vQB.root",
sampleBaseDir+"PATtuple_320_1_krE.root",
sampleBaseDir+"PATtuple_321_1_Y2t.root",
sampleBaseDir+"PATtuple_322_1_i1Z.root",
sampleBaseDir+"PATtuple_323_1_fhL.root",
sampleBaseDir+"PATtuple_324_1_sFz.root",
sampleBaseDir+"PATtuple_325_1_szf.root",
sampleBaseDir+"PATtuple_326_1_18O.root",
sampleBaseDir+"PATtuple_327_1_skO.root",
sampleBaseDir+"PATtuple_328_1_tyl.root",
sampleBaseDir+"PATtuple_329_1_zON.root",
sampleBaseDir+"PATtuple_32_1_zDM.root",
sampleBaseDir+"PATtuple_330_1_7Uv.root",
sampleBaseDir+"PATtuple_331_1_8iO.root",
sampleBaseDir+"PATtuple_332_1_oNP.root",
sampleBaseDir+"PATtuple_333_1_JUG.root",
sampleBaseDir+"PATtuple_334_1_GGs.root",
sampleBaseDir+"PATtuple_335_1_YeZ.root",
sampleBaseDir+"PATtuple_336_1_xTR.root",
sampleBaseDir+"PATtuple_337_1_wrd.root",
sampleBaseDir+"PATtuple_338_1_cqM.root",
sampleBaseDir+"PATtuple_339_1_gMK.root",
sampleBaseDir+"PATtuple_33_1_QpS.root",
sampleBaseDir+"PATtuple_340_1_oRc.root",
sampleBaseDir+"PATtuple_341_1_iDL.root",
sampleBaseDir+"PATtuple_342_1_jeE.root",
sampleBaseDir+"PATtuple_343_1_JL8.root",
sampleBaseDir+"PATtuple_344_1_UwA.root",
sampleBaseDir+"PATtuple_345_1_qjL.root",
sampleBaseDir+"PATtuple_346_1_QKK.root",
sampleBaseDir+"PATtuple_347_1_nNK.root",
sampleBaseDir+"PATtuple_348_1_k7N.root",
sampleBaseDir+"PATtuple_349_1_fN0.root",
sampleBaseDir+"PATtuple_34_1_IRd.root",
sampleBaseDir+"PATtuple_350_1_ScE.root",
sampleBaseDir+"PATtuple_351_1_MCG.root",
sampleBaseDir+"PATtuple_352_1_lnN.root",
sampleBaseDir+"PATtuple_353_1_qEQ.root",
sampleBaseDir+"PATtuple_354_1_pLb.root",
sampleBaseDir+"PATtuple_355_1_SYP.root",
sampleBaseDir+"PATtuple_356_1_kfy.root",
sampleBaseDir+"PATtuple_357_1_QtE.root",
sampleBaseDir+"PATtuple_358_1_i74.root",
sampleBaseDir+"PATtuple_359_1_bHk.root",
sampleBaseDir+"PATtuple_35_1_e9v.root",
sampleBaseDir+"PATtuple_360_1_eN6.root",
sampleBaseDir+"PATtuple_361_1_0kv.root",
sampleBaseDir+"PATtuple_362_1_MgR.root",
sampleBaseDir+"PATtuple_363_1_0d0.root",
sampleBaseDir+"PATtuple_364_1_8Ns.root",
sampleBaseDir+"PATtuple_365_1_DO0.root",
sampleBaseDir+"PATtuple_366_1_xv7.root",
sampleBaseDir+"PATtuple_367_1_PkG.root",
sampleBaseDir+"PATtuple_368_1_ksG.root",
sampleBaseDir+"PATtuple_369_1_X4T.root",
sampleBaseDir+"PATtuple_36_1_qBb.root",
sampleBaseDir+"PATtuple_370_1_NLM.root",
sampleBaseDir+"PATtuple_371_1_B6e.root",
sampleBaseDir+"PATtuple_372_1_7Mh.root",
sampleBaseDir+"PATtuple_373_1_ZvX.root",
sampleBaseDir+"PATtuple_374_1_NvD.root",
sampleBaseDir+"PATtuple_375_1_wuG.root",
sampleBaseDir+"PATtuple_376_1_Sng.root",
sampleBaseDir+"PATtuple_377_1_9tr.root",
sampleBaseDir+"PATtuple_378_1_2Ab.root",
sampleBaseDir+"PATtuple_379_1_BOQ.root",
sampleBaseDir+"PATtuple_37_1_rNv.root",
sampleBaseDir+"PATtuple_380_1_yCm.root",
sampleBaseDir+"PATtuple_381_1_tub.root",
sampleBaseDir+"PATtuple_382_1_Fto.root",
sampleBaseDir+"PATtuple_383_1_7u0.root",
sampleBaseDir+"PATtuple_384_1_Flv.root",
sampleBaseDir+"PATtuple_385_1_Rum.root",
sampleBaseDir+"PATtuple_386_1_4NC.root",
sampleBaseDir+"PATtuple_387_1_5Qt.root",
sampleBaseDir+"PATtuple_388_1_PNx.root",
sampleBaseDir+"PATtuple_389_1_QXB.root",
sampleBaseDir+"PATtuple_38_1_qvs.root",
sampleBaseDir+"PATtuple_390_1_jz3.root",
sampleBaseDir+"PATtuple_391_1_50J.root",
sampleBaseDir+"PATtuple_392_1_FW3.root",
sampleBaseDir+"PATtuple_393_1_DdQ.root",
sampleBaseDir+"PATtuple_394_1_DJf.root",
sampleBaseDir+"PATtuple_395_1_5DQ.root",
sampleBaseDir+"PATtuple_396_1_FM0.root",
sampleBaseDir+"PATtuple_397_1_VF1.root",
sampleBaseDir+"PATtuple_398_1_gD8.root",
sampleBaseDir+"PATtuple_399_1_vAn.root",
sampleBaseDir+"PATtuple_39_1_Fst.root",
sampleBaseDir+"PATtuple_3_1_PVY.root",
sampleBaseDir+"PATtuple_400_1_bZu.root",
sampleBaseDir+"PATtuple_401_1_qW9.root",
sampleBaseDir+"PATtuple_403_1_lN9.root",
sampleBaseDir+"PATtuple_404_1_fze.root",
sampleBaseDir+"PATtuple_405_1_51h.root",
sampleBaseDir+"PATtuple_406_1_LPq.root",
sampleBaseDir+"PATtuple_407_1_ODK.root",
sampleBaseDir+"PATtuple_408_1_2Ca.root",
sampleBaseDir+"PATtuple_409_1_vdp.root",
sampleBaseDir+"PATtuple_40_1_Seh.root",
sampleBaseDir+"PATtuple_410_1_UFT.root",
sampleBaseDir+"PATtuple_411_1_7XU.root",
sampleBaseDir+"PATtuple_412_1_x9m.root",
sampleBaseDir+"PATtuple_413_1_PmQ.root",
sampleBaseDir+"PATtuple_414_1_5LW.root",
sampleBaseDir+"PATtuple_415_1_2UB.root",
sampleBaseDir+"PATtuple_416_1_ON2.root",
sampleBaseDir+"PATtuple_417_1_fNU.root",
sampleBaseDir+"PATtuple_418_1_D7B.root",
sampleBaseDir+"PATtuple_419_1_346.root",
sampleBaseDir+"PATtuple_41_1_6KG.root",
sampleBaseDir+"PATtuple_420_1_Ei8.root",
sampleBaseDir+"PATtuple_421_1_VPn.root",
sampleBaseDir+"PATtuple_422_1_0rZ.root",
sampleBaseDir+"PATtuple_423_1_jhV.root",
sampleBaseDir+"PATtuple_424_1_pib.root",
sampleBaseDir+"PATtuple_425_1_bPI.root",
sampleBaseDir+"PATtuple_426_1_qlz.root",
sampleBaseDir+"PATtuple_427_1_B1d.root",
sampleBaseDir+"PATtuple_428_1_0P8.root",
sampleBaseDir+"PATtuple_429_1_25n.root",
sampleBaseDir+"PATtuple_42_1_jx2.root",
sampleBaseDir+"PATtuple_430_1_zre.root",
sampleBaseDir+"PATtuple_431_1_ET5.root",
sampleBaseDir+"PATtuple_432_1_jpR.root",
sampleBaseDir+"PATtuple_433_1_PA5.root",
sampleBaseDir+"PATtuple_434_1_6d0.root",
sampleBaseDir+"PATtuple_435_1_Nwr.root",
sampleBaseDir+"PATtuple_436_1_UMU.root",
sampleBaseDir+"PATtuple_437_1_Pxl.root",
sampleBaseDir+"PATtuple_438_1_Wcw.root",
sampleBaseDir+"PATtuple_439_1_A5M.root",
sampleBaseDir+"PATtuple_43_1_XgR.root",
sampleBaseDir+"PATtuple_440_1_M0E.root",
sampleBaseDir+"PATtuple_441_1_vMs.root",
sampleBaseDir+"PATtuple_442_1_4ba.root",
sampleBaseDir+"PATtuple_443_1_0C8.root",
sampleBaseDir+"PATtuple_444_1_cvn.root",
sampleBaseDir+"PATtuple_445_1_wIO.root",
sampleBaseDir+"PATtuple_446_1_Lh6.root",
sampleBaseDir+"PATtuple_447_1_2sk.root",
sampleBaseDir+"PATtuple_448_1_NPq.root",
sampleBaseDir+"PATtuple_449_1_l22.root",
sampleBaseDir+"PATtuple_44_1_nb0.root",
sampleBaseDir+"PATtuple_450_1_4TA.root",
sampleBaseDir+"PATtuple_451_1_1r8.root",
sampleBaseDir+"PATtuple_452_1_5GR.root",
sampleBaseDir+"PATtuple_453_1_wdJ.root",
sampleBaseDir+"PATtuple_454_1_osi.root",
sampleBaseDir+"PATtuple_455_1_We4.root",
sampleBaseDir+"PATtuple_456_1_maE.root",
sampleBaseDir+"PATtuple_457_1_457.root",
sampleBaseDir+"PATtuple_458_1_Iv0.root",
sampleBaseDir+"PATtuple_459_1_uOA.root",
sampleBaseDir+"PATtuple_45_1_MeG.root",
sampleBaseDir+"PATtuple_460_1_reU.root",
sampleBaseDir+"PATtuple_461_1_ibt.root",
sampleBaseDir+"PATtuple_462_1_655.root",
sampleBaseDir+"PATtuple_463_1_zKd.root",
sampleBaseDir+"PATtuple_464_1_gIN.root",
sampleBaseDir+"PATtuple_465_1_MMr.root",
sampleBaseDir+"PATtuple_466_1_nAo.root",
sampleBaseDir+"PATtuple_467_1_APy.root",
sampleBaseDir+"PATtuple_468_1_CPM.root",
sampleBaseDir+"PATtuple_469_1_uLy.root",
sampleBaseDir+"PATtuple_46_1_WzB.root",
sampleBaseDir+"PATtuple_470_1_Ty6.root",
sampleBaseDir+"PATtuple_471_1_qzH.root",
sampleBaseDir+"PATtuple_472_1_Ijv.root",
sampleBaseDir+"PATtuple_473_1_zVm.root",
sampleBaseDir+"PATtuple_474_1_1d0.root",
sampleBaseDir+"PATtuple_475_1_ZdC.root",
sampleBaseDir+"PATtuple_476_1_Qeg.root",
sampleBaseDir+"PATtuple_477_1_Ca9.root",
sampleBaseDir+"PATtuple_478_1_7wh.root",
sampleBaseDir+"PATtuple_479_1_yBw.root",
sampleBaseDir+"PATtuple_47_1_JNb.root",
sampleBaseDir+"PATtuple_480_1_2RQ.root",
sampleBaseDir+"PATtuple_481_1_Wc2.root",
sampleBaseDir+"PATtuple_482_1_soJ.root",
sampleBaseDir+"PATtuple_483_1_Z50.root",
sampleBaseDir+"PATtuple_484_1_lmP.root",
sampleBaseDir+"PATtuple_485_1_K6X.root",
sampleBaseDir+"PATtuple_486_1_8Ap.root",
sampleBaseDir+"PATtuple_487_1_VCi.root",
sampleBaseDir+"PATtuple_488_1_PKG.root",
sampleBaseDir+"PATtuple_489_1_53q.root",
sampleBaseDir+"PATtuple_48_1_9hG.root",
sampleBaseDir+"PATtuple_490_1_z8N.root",
sampleBaseDir+"PATtuple_491_1_yrQ.root",
sampleBaseDir+"PATtuple_492_1_6cW.root",
sampleBaseDir+"PATtuple_493_1_ZpN.root",
sampleBaseDir+"PATtuple_494_1_DJC.root",
sampleBaseDir+"PATtuple_495_1_orX.root",
sampleBaseDir+"PATtuple_496_1_f1c.root",
sampleBaseDir+"PATtuple_497_1_L6H.root",
sampleBaseDir+"PATtuple_498_1_gCg.root",
sampleBaseDir+"PATtuple_499_1_APp.root",
sampleBaseDir+"PATtuple_49_1_lSO.root",
sampleBaseDir+"PATtuple_4_1_O4H.root",
sampleBaseDir+"PATtuple_500_1_qRa.root",
sampleBaseDir+"PATtuple_501_1_riy.root",
sampleBaseDir+"PATtuple_502_1_6wy.root",
sampleBaseDir+"PATtuple_503_1_oYP.root",
sampleBaseDir+"PATtuple_504_1_Vsr.root",
sampleBaseDir+"PATtuple_505_1_P4r.root",
sampleBaseDir+"PATtuple_506_1_1N5.root",
sampleBaseDir+"PATtuple_507_1_pxg.root",
sampleBaseDir+"PATtuple_508_1_Njr.root",
sampleBaseDir+"PATtuple_509_1_uG2.root",
sampleBaseDir+"PATtuple_50_1_3iO.root",
sampleBaseDir+"PATtuple_510_1_X35.root",
sampleBaseDir+"PATtuple_511_1_V7Z.root",
sampleBaseDir+"PATtuple_512_1_ChF.root",
sampleBaseDir+"PATtuple_513_1_kRV.root",
sampleBaseDir+"PATtuple_514_1_ed7.root",
sampleBaseDir+"PATtuple_515_1_SCG.root",
sampleBaseDir+"PATtuple_516_1_2K4.root",
sampleBaseDir+"PATtuple_517_1_o5x.root",
sampleBaseDir+"PATtuple_518_1_SYj.root",
sampleBaseDir+"PATtuple_519_1_1N5.root",
sampleBaseDir+"PATtuple_51_1_N3a.root",
sampleBaseDir+"PATtuple_520_1_HgV.root",
sampleBaseDir+"PATtuple_521_1_ACr.root",
sampleBaseDir+"PATtuple_522_1_64T.root",
sampleBaseDir+"PATtuple_524_1_IFR.root",
sampleBaseDir+"PATtuple_525_1_6fh.root",
sampleBaseDir+"PATtuple_526_1_TMj.root",
sampleBaseDir+"PATtuple_527_1_vrl.root",
sampleBaseDir+"PATtuple_528_1_TNL.root",
sampleBaseDir+"PATtuple_529_1_YK2.root",
sampleBaseDir+"PATtuple_52_1_AWs.root",
sampleBaseDir+"PATtuple_530_1_8Tn.root",
sampleBaseDir+"PATtuple_531_1_tyI.root",
sampleBaseDir+"PATtuple_532_1_iAv.root",
sampleBaseDir+"PATtuple_533_1_KPI.root",
sampleBaseDir+"PATtuple_534_1_all.root",
sampleBaseDir+"PATtuple_535_1_jmD.root",
sampleBaseDir+"PATtuple_536_1_Urb.root",
sampleBaseDir+"PATtuple_537_1_R59.root",
sampleBaseDir+"PATtuple_538_1_IG3.root",
sampleBaseDir+"PATtuple_539_1_8r7.root",
sampleBaseDir+"PATtuple_53_1_VPp.root",
sampleBaseDir+"PATtuple_541_1_kqW.root",
sampleBaseDir+"PATtuple_542_1_T91.root",
sampleBaseDir+"PATtuple_543_1_XaA.root",
sampleBaseDir+"PATtuple_544_1_96g.root",
sampleBaseDir+"PATtuple_545_1_rEr.root",
sampleBaseDir+"PATtuple_546_1_Trl.root",
sampleBaseDir+"PATtuple_547_1_Gib.root",
sampleBaseDir+"PATtuple_548_1_UTx.root",
sampleBaseDir+"PATtuple_549_1_cko.root",
sampleBaseDir+"PATtuple_54_1_ZZn.root",
sampleBaseDir+"PATtuple_550_1_Df8.root",
sampleBaseDir+"PATtuple_551_1_fim.root",
sampleBaseDir+"PATtuple_552_1_b7Z.root",
sampleBaseDir+"PATtuple_553_1_XqV.root",
sampleBaseDir+"PATtuple_554_1_Ojr.root",
sampleBaseDir+"PATtuple_555_1_iIg.root",
sampleBaseDir+"PATtuple_557_1_3hi.root",
sampleBaseDir+"PATtuple_558_1_5jO.root",
sampleBaseDir+"PATtuple_559_1_0FY.root",
sampleBaseDir+"PATtuple_55_1_7wc.root",
sampleBaseDir+"PATtuple_560_1_AHe.root",
sampleBaseDir+"PATtuple_561_1_ADT.root",
sampleBaseDir+"PATtuple_562_1_ij5.root",
sampleBaseDir+"PATtuple_563_1_58m.root",
sampleBaseDir+"PATtuple_564_1_AZ0.root",
sampleBaseDir+"PATtuple_565_1_9Mp.root",
sampleBaseDir+"PATtuple_566_1_6dJ.root",
sampleBaseDir+"PATtuple_567_1_fa7.root",
sampleBaseDir+"PATtuple_568_1_o3Z.root",
sampleBaseDir+"PATtuple_569_1_Z8P.root",
sampleBaseDir+"PATtuple_56_1_zTo.root",
sampleBaseDir+"PATtuple_570_1_wjf.root",
sampleBaseDir+"PATtuple_571_1_eNR.root",
sampleBaseDir+"PATtuple_572_1_DPv.root",
sampleBaseDir+"PATtuple_573_1_CN5.root",
sampleBaseDir+"PATtuple_574_1_H1S.root",
sampleBaseDir+"PATtuple_575_1_IPe.root",
sampleBaseDir+"PATtuple_576_1_1j8.root",
sampleBaseDir+"PATtuple_577_1_2MY.root",
sampleBaseDir+"PATtuple_578_1_gDu.root",
sampleBaseDir+"PATtuple_579_1_BZs.root",
sampleBaseDir+"PATtuple_57_1_fHK.root",
sampleBaseDir+"PATtuple_580_1_JJ0.root",
sampleBaseDir+"PATtuple_581_1_Mkp.root",
sampleBaseDir+"PATtuple_582_1_mup.root",
sampleBaseDir+"PATtuple_583_1_My2.root",
sampleBaseDir+"PATtuple_584_1_9OR.root",
sampleBaseDir+"PATtuple_585_1_Ee2.root",
sampleBaseDir+"PATtuple_586_1_mOp.root",
sampleBaseDir+"PATtuple_588_1_f8Y.root",
sampleBaseDir+"PATtuple_589_1_Nsb.root",
sampleBaseDir+"PATtuple_58_1_LBw.root",
sampleBaseDir+"PATtuple_590_1_yl1.root",
sampleBaseDir+"PATtuple_591_1_SDr.root",
sampleBaseDir+"PATtuple_592_1_CK5.root",
sampleBaseDir+"PATtuple_593_1_CEM.root",
sampleBaseDir+"PATtuple_594_1_h0s.root",
sampleBaseDir+"PATtuple_595_1_lIe.root",
sampleBaseDir+"PATtuple_596_1_B7y.root",
sampleBaseDir+"PATtuple_597_1_wK9.root",
sampleBaseDir+"PATtuple_598_1_Nm9.root",
sampleBaseDir+"PATtuple_599_1_1BQ.root",
sampleBaseDir+"PATtuple_59_1_cFS.root",
sampleBaseDir+"PATtuple_5_1_vcM.root",
sampleBaseDir+"PATtuple_600_1_NoV.root",
sampleBaseDir+"PATtuple_601_1_Ssa.root",
sampleBaseDir+"PATtuple_602_1_a3S.root",
sampleBaseDir+"PATtuple_603_1_3Ux.root",
sampleBaseDir+"PATtuple_604_1_hgL.root",
sampleBaseDir+"PATtuple_605_1_jAT.root",
sampleBaseDir+"PATtuple_606_1_Iad.root",
sampleBaseDir+"PATtuple_607_1_DiP.root",
sampleBaseDir+"PATtuple_608_1_uuU.root",
sampleBaseDir+"PATtuple_609_1_gk6.root",
sampleBaseDir+"PATtuple_60_1_r7o.root",
sampleBaseDir+"PATtuple_610_1_xw8.root",
sampleBaseDir+"PATtuple_612_1_fNt.root",
sampleBaseDir+"PATtuple_613_1_3Gf.root",
sampleBaseDir+"PATtuple_614_1_HS6.root",
sampleBaseDir+"PATtuple_615_1_tZu.root",
sampleBaseDir+"PATtuple_616_1_LRL.root",
sampleBaseDir+"PATtuple_617_1_GCC.root",
sampleBaseDir+"PATtuple_619_1_DOO.root",
sampleBaseDir+"PATtuple_61_1_Epw.root",
sampleBaseDir+"PATtuple_620_1_yhv.root",
sampleBaseDir+"PATtuple_621_1_b5s.root",
sampleBaseDir+"PATtuple_622_1_sb5.root",
sampleBaseDir+"PATtuple_623_1_hkf.root",
sampleBaseDir+"PATtuple_624_1_kfj.root",
sampleBaseDir+"PATtuple_625_1_guh.root",
sampleBaseDir+"PATtuple_626_1_nKP.root",
sampleBaseDir+"PATtuple_627_1_YN2.root",
sampleBaseDir+"PATtuple_628_1_RfB.root",
sampleBaseDir+"PATtuple_629_1_tM8.root",
sampleBaseDir+"PATtuple_62_1_xWw.root",
sampleBaseDir+"PATtuple_630_1_dBp.root",
sampleBaseDir+"PATtuple_631_1_e6f.root",
sampleBaseDir+"PATtuple_632_1_w7r.root",
sampleBaseDir+"PATtuple_634_1_Efl.root",
sampleBaseDir+"PATtuple_635_1_fiK.root",
sampleBaseDir+"PATtuple_636_1_wKS.root",
sampleBaseDir+"PATtuple_637_1_ul2.root",
sampleBaseDir+"PATtuple_638_1_7Fg.root",
sampleBaseDir+"PATtuple_639_1_RKM.root",
sampleBaseDir+"PATtuple_63_1_hVg.root",
sampleBaseDir+"PATtuple_640_1_ukM.root",
sampleBaseDir+"PATtuple_641_1_V7U.root",
sampleBaseDir+"PATtuple_642_1_ON2.root",
sampleBaseDir+"PATtuple_643_1_GSw.root",
sampleBaseDir+"PATtuple_644_1_B7h.root",
sampleBaseDir+"PATtuple_646_1_Mnt.root",
sampleBaseDir+"PATtuple_647_1_cTo.root",
sampleBaseDir+"PATtuple_648_1_5fP.root",
sampleBaseDir+"PATtuple_649_1_JY9.root",
sampleBaseDir+"PATtuple_64_1_Zam.root",
sampleBaseDir+"PATtuple_650_1_jWI.root",
sampleBaseDir+"PATtuple_651_1_Jz9.root",
sampleBaseDir+"PATtuple_652_1_zdD.root",
sampleBaseDir+"PATtuple_653_1_7Ga.root",
sampleBaseDir+"PATtuple_654_1_amk.root",
sampleBaseDir+"PATtuple_655_1_fhL.root",
sampleBaseDir+"PATtuple_656_1_yMH.root",
sampleBaseDir+"PATtuple_657_1_CbX.root",
sampleBaseDir+"PATtuple_658_1_ApS.root",
sampleBaseDir+"PATtuple_659_1_fxk.root",
sampleBaseDir+"PATtuple_65_1_TYg.root",
sampleBaseDir+"PATtuple_660_1_hG3.root",
sampleBaseDir+"PATtuple_661_1_YuP.root",
sampleBaseDir+"PATtuple_662_1_oQX.root",
sampleBaseDir+"PATtuple_663_1_Fjy.root",
sampleBaseDir+"PATtuple_664_1_lfs.root",
sampleBaseDir+"PATtuple_665_1_th7.root",
sampleBaseDir+"PATtuple_666_1_k54.root",
sampleBaseDir+"PATtuple_667_1_3rm.root",
sampleBaseDir+"PATtuple_668_1_TTI.root",
sampleBaseDir+"PATtuple_669_1_mEA.root",
sampleBaseDir+"PATtuple_66_1_NAQ.root",
sampleBaseDir+"PATtuple_670_1_Rg1.root",
sampleBaseDir+"PATtuple_671_1_GzU.root",
sampleBaseDir+"PATtuple_672_1_Epb.root",
sampleBaseDir+"PATtuple_673_1_5EV.root",
sampleBaseDir+"PATtuple_675_1_Zu1.root",
sampleBaseDir+"PATtuple_676_1_d4i.root",
sampleBaseDir+"PATtuple_677_1_dMK.root",
sampleBaseDir+"PATtuple_679_1_3Qj.root",
sampleBaseDir+"PATtuple_67_1_goy.root",
sampleBaseDir+"PATtuple_681_1_EAY.root",
sampleBaseDir+"PATtuple_682_1_JAy.root",
sampleBaseDir+"PATtuple_683_1_2cA.root",
sampleBaseDir+"PATtuple_684_1_3Zs.root",
sampleBaseDir+"PATtuple_685_1_p5b.root",
sampleBaseDir+"PATtuple_686_1_Lui.root",
sampleBaseDir+"PATtuple_687_1_oPT.root",
sampleBaseDir+"PATtuple_688_1_gHW.root",
sampleBaseDir+"PATtuple_689_1_aY2.root",
sampleBaseDir+"PATtuple_68_1_R8Q.root",
sampleBaseDir+"PATtuple_691_1_SN9.root",
sampleBaseDir+"PATtuple_692_1_g4t.root",
sampleBaseDir+"PATtuple_693_1_gv1.root",
sampleBaseDir+"PATtuple_694_1_Qbh.root",
sampleBaseDir+"PATtuple_695_1_rUE.root",
sampleBaseDir+"PATtuple_696_1_hU2.root",
sampleBaseDir+"PATtuple_697_1_oZG.root",
sampleBaseDir+"PATtuple_698_1_PdU.root",
sampleBaseDir+"PATtuple_699_1_ufi.root",
sampleBaseDir+"PATtuple_69_1_peg.root",
sampleBaseDir+"PATtuple_6_1_71e.root",
sampleBaseDir+"PATtuple_700_1_x70.root",
sampleBaseDir+"PATtuple_701_1_wCE.root",
sampleBaseDir+"PATtuple_702_1_X0C.root",
sampleBaseDir+"PATtuple_703_1_out.root",
sampleBaseDir+"PATtuple_704_1_dtx.root",
sampleBaseDir+"PATtuple_705_1_77j.root",
sampleBaseDir+"PATtuple_706_1_0ju.root",
sampleBaseDir+"PATtuple_707_1_Gby.root",
sampleBaseDir+"PATtuple_708_1_VN7.root",
sampleBaseDir+"PATtuple_709_1_ALz.root",
sampleBaseDir+"PATtuple_70_1_v56.root",
sampleBaseDir+"PATtuple_710_1_zqJ.root",
sampleBaseDir+"PATtuple_711_1_nAj.root",
sampleBaseDir+"PATtuple_712_1_G8l.root",
sampleBaseDir+"PATtuple_714_1_NYN.root",
sampleBaseDir+"PATtuple_715_1_9br.root",
sampleBaseDir+"PATtuple_716_1_K3U.root",
sampleBaseDir+"PATtuple_717_1_Zd5.root",
sampleBaseDir+"PATtuple_718_1_yTf.root",
sampleBaseDir+"PATtuple_719_1_Y4c.root",
sampleBaseDir+"PATtuple_71_1_UI3.root",
sampleBaseDir+"PATtuple_720_1_qT3.root",
sampleBaseDir+"PATtuple_721_1_zd2.root",
sampleBaseDir+"PATtuple_722_1_ohl.root",
sampleBaseDir+"PATtuple_723_1_QsN.root",
sampleBaseDir+"PATtuple_724_1_2cL.root",
sampleBaseDir+"PATtuple_725_1_2Jh.root",
sampleBaseDir+"PATtuple_726_1_v7G.root",
sampleBaseDir+"PATtuple_727_1_oJj.root",
sampleBaseDir+"PATtuple_728_1_h1b.root",
sampleBaseDir+"PATtuple_729_1_Vif.root",
sampleBaseDir+"PATtuple_72_1_Fsz.root",
sampleBaseDir+"PATtuple_730_1_c9u.root",
sampleBaseDir+"PATtuple_731_1_hck.root",
sampleBaseDir+"PATtuple_732_1_CLv.root",
sampleBaseDir+"PATtuple_734_1_n58.root",
sampleBaseDir+"PATtuple_735_1_0pt.root",
sampleBaseDir+"PATtuple_736_1_gw1.root",
sampleBaseDir+"PATtuple_737_1_mnV.root",
sampleBaseDir+"PATtuple_738_1_Qoh.root",
sampleBaseDir+"PATtuple_739_1_7RL.root",
sampleBaseDir+"PATtuple_73_1_P8G.root",
sampleBaseDir+"PATtuple_740_1_zhH.root",
sampleBaseDir+"PATtuple_741_1_Hni.root",
sampleBaseDir+"PATtuple_742_1_us9.root",
sampleBaseDir+"PATtuple_744_1_mlE.root",
sampleBaseDir+"PATtuple_745_1_w3D.root",
sampleBaseDir+"PATtuple_746_1_ikq.root",
sampleBaseDir+"PATtuple_747_1_Vfb.root",
sampleBaseDir+"PATtuple_748_1_abG.root",
sampleBaseDir+"PATtuple_74_1_Ilz.root",
sampleBaseDir+"PATtuple_750_1_o5Z.root",
sampleBaseDir+"PATtuple_751_1_JEC.root",
sampleBaseDir+"PATtuple_752_1_dcd.root",
sampleBaseDir+"PATtuple_753_1_azw.root",
sampleBaseDir+"PATtuple_75_1_4Gz.root",
sampleBaseDir+"PATtuple_76_1_csZ.root",
sampleBaseDir+"PATtuple_77_1_lt1.root",
sampleBaseDir+"PATtuple_78_1_vc6.root",
sampleBaseDir+"PATtuple_79_1_qcV.root",
sampleBaseDir+"PATtuple_7_1_iYV.root",
sampleBaseDir+"PATtuple_80_1_C6Q.root",
sampleBaseDir+"PATtuple_81_1_0tH.root",
sampleBaseDir+"PATtuple_82_1_3Ib.root",
sampleBaseDir+"PATtuple_83_1_kyI.root",
sampleBaseDir+"PATtuple_84_1_dRc.root",
sampleBaseDir+"PATtuple_85_1_5Ft.root",
sampleBaseDir+"PATtuple_86_1_egN.root",
sampleBaseDir+"PATtuple_87_1_urU.root",
sampleBaseDir+"PATtuple_88_1_7tu.root",
sampleBaseDir+"PATtuple_89_1_3R0.root",
sampleBaseDir+"PATtuple_8_1_zy4.root",
sampleBaseDir+"PATtuple_90_1_wMU.root",
sampleBaseDir+"PATtuple_91_1_7xk.root",
sampleBaseDir+"PATtuple_92_1_zBg.root",
sampleBaseDir+"PATtuple_93_1_iWi.root",
sampleBaseDir+"PATtuple_94_1_Nr0.root",
sampleBaseDir+"PATtuple_95_1_BC7.root",
sampleBaseDir+"PATtuple_96_1_bNO.root",
sampleBaseDir+"PATtuple_97_1_n7M.root",
sampleBaseDir+"PATtuple_98_1_KWS.root",
sampleBaseDir+"PATtuple_99_1_UrD.root",
sampleBaseDir+"PATtuple_9_1_ZN0.root",
]