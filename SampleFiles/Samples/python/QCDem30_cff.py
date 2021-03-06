sampleDataSet = '/QCD_Pt_30_80_EMEnriched_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_2_patch4" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_5" # release used to create new files with

sampleNumEvents = 33088888

sampleXSec = 7.433E7 * 0.0621 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7F::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "BKGMC"




samplePatDBSName=""

sampleBaseDir="/store/user/lpcdve/DisplacedLeptons/QCDem30_pat_20130203/demattia//QCD_Pt_30_80_EMEnriched_TuneZ2star_8TeV_pythia6/QCDem30_pat_20130203/5fe3dadd93bf8608b396f970098158ed/"
samplePatFiles = [
sampleBaseDir+"PATtuple_125_1_cd9.root",
sampleBaseDir+"PATtuple_325_1_d44.root",
sampleBaseDir+"PATtuple_330_1_ux0.root",
sampleBaseDir+"PATtuple_379_1_fvQ.root",
sampleBaseDir+"PATtuple_407_1_A9A.root",
sampleBaseDir+"PATtuple_358_1_F61.root",
sampleBaseDir+"PATtuple_313_1_oFe.root",
sampleBaseDir+"PATtuple_481_1_cah.root",
sampleBaseDir+"PATtuple_393_1_Jbh.root",
sampleBaseDir+"PATtuple_582_1_CGK.root",
sampleBaseDir+"PATtuple_394_1_LsC.root",
sampleBaseDir+"PATtuple_321_1_Nus.root",
sampleBaseDir+"PATtuple_574_1_lBE.root",
sampleBaseDir+"PATtuple_622_1_c5s.root",
sampleBaseDir+"PATtuple_310_1_i4h.root",
sampleBaseDir+"PATtuple_39_1_Vlu.root",
sampleBaseDir+"PATtuple_102_1_dYT.root",
sampleBaseDir+"PATtuple_205_1_9Zm.root",
sampleBaseDir+"PATtuple_372_1_BZJ.root",
sampleBaseDir+"PATtuple_509_1_8iF.root",
sampleBaseDir+"PATtuple_650_1_6qN.root",
sampleBaseDir+"PATtuple_18_1_8NC.root",
sampleBaseDir+"PATtuple_59_1_4k5.root",
sampleBaseDir+"PATtuple_217_1_Dgi.root",
sampleBaseDir+"PATtuple_215_1_B3G.root",
sampleBaseDir+"PATtuple_549_1_ENK.root",
sampleBaseDir+"PATtuple_552_1_5M7.root",
sampleBaseDir+"PATtuple_395_1_ywA.root",
sampleBaseDir+"PATtuple_2_1_Uzt.root",
sampleBaseDir+"PATtuple_134_1_ZdT.root",
sampleBaseDir+"PATtuple_626_1_WMJ.root",
sampleBaseDir+"PATtuple_526_1_htA.root",
sampleBaseDir+"PATtuple_634_1_YRx.root",
sampleBaseDir+"PATtuple_161_1_UJW.root",
sampleBaseDir+"PATtuple_486_1_AXn.root",
sampleBaseDir+"PATtuple_520_1_alc.root",
sampleBaseDir+"PATtuple_378_1_KJn.root",
sampleBaseDir+"PATtuple_7_1_8NV.root",
sampleBaseDir+"PATtuple_34_1_UaP.root",
sampleBaseDir+"PATtuple_20_1_7Lj.root",
sampleBaseDir+"PATtuple_234_1_21H.root",
sampleBaseDir+"PATtuple_42_1_2eb.root",
sampleBaseDir+"PATtuple_275_1_xDA.root",
sampleBaseDir+"PATtuple_70_1_lOq.root",
sampleBaseDir+"PATtuple_455_1_Fab.root",
sampleBaseDir+"PATtuple_540_1_JVa.root",
sampleBaseDir+"PATtuple_52_1_60m.root",
sampleBaseDir+"PATtuple_174_1_uBl.root",
sampleBaseDir+"PATtuple_216_1_97h.root",
sampleBaseDir+"PATtuple_245_1_QCY.root",
sampleBaseDir+"PATtuple_211_1_3ar.root",
sampleBaseDir+"PATtuple_91_1_xkV.root",
sampleBaseDir+"PATtuple_499_1_R4u.root",
sampleBaseDir+"PATtuple_476_1_yNj.root",
sampleBaseDir+"PATtuple_506_1_fT9.root",
sampleBaseDir+"PATtuple_502_1_tuj.root",
sampleBaseDir+"PATtuple_133_1_jxw.root",
sampleBaseDir+"PATtuple_158_1_Wcq.root",
sampleBaseDir+"PATtuple_419_1_Njl.root",
sampleBaseDir+"PATtuple_517_1_O0Z.root",
sampleBaseDir+"PATtuple_577_1_ykC.root",
sampleBaseDir+"PATtuple_435_1_XEY.root",
sampleBaseDir+"PATtuple_664_1_Pr3.root",
sampleBaseDir+"PATtuple_113_1_f4f.root",
sampleBaseDir+"PATtuple_242_1_Kox.root",
sampleBaseDir+"PATtuple_368_1_ZfQ.root",
sampleBaseDir+"PATtuple_637_1_dro.root",
sampleBaseDir+"PATtuple_401_1_0lL.root",
sampleBaseDir+"PATtuple_558_1_MVU.root",
sampleBaseDir+"PATtuple_17_1_9yf.root",
sampleBaseDir+"PATtuple_167_1_PJx.root",
sampleBaseDir+"PATtuple_200_1_2fq.root",
sampleBaseDir+"PATtuple_300_1_NYI.root",
sampleBaseDir+"PATtuple_495_1_PEy.root",
sampleBaseDir+"PATtuple_65_1_ULc.root",
sampleBaseDir+"PATtuple_548_1_iJN.root",
sampleBaseDir+"PATtuple_505_1_OHh.root",
sampleBaseDir+"PATtuple_312_1_lbx.root",
sampleBaseDir+"PATtuple_97_1_XKM.root",
sampleBaseDir+"PATtuple_239_1_g4g.root",
sampleBaseDir+"PATtuple_74_1_TaR.root",
sampleBaseDir+"PATtuple_271_1_soY.root",
sampleBaseDir+"PATtuple_602_1_4oq.root",
sampleBaseDir+"PATtuple_444_1_RKu.root",
sampleBaseDir+"PATtuple_654_1_7KE.root",
sampleBaseDir+"PATtuple_544_1_6nE.root",
sampleBaseDir+"PATtuple_259_1_amx.root",
sampleBaseDir+"PATtuple_417_1_KDu.root",
sampleBaseDir+"PATtuple_456_1_xAS.root",
sampleBaseDir+"PATtuple_457_1_978.root",
sampleBaseDir+"PATtuple_657_1_Z1Q.root",
sampleBaseDir+"PATtuple_4_1_31E.root",
sampleBaseDir+"PATtuple_570_1_axw.root",
sampleBaseDir+"PATtuple_345_1_sp6.root",
sampleBaseDir+"PATtuple_226_1_Scx.root",
sampleBaseDir+"PATtuple_223_1_wPJ.root",
sampleBaseDir+"PATtuple_293_1_25w.root",
sampleBaseDir+"PATtuple_341_1_fDJ.root",
sampleBaseDir+"PATtuple_138_1_3IU.root",
sampleBaseDir+"PATtuple_354_1_A6r.root",
sampleBaseDir+"PATtuple_30_1_6AU.root",
sampleBaseDir+"PATtuple_316_1_LGe.root",
sampleBaseDir+"PATtuple_460_1_fFx.root",
sampleBaseDir+"PATtuple_494_1_Q80.root",
sampleBaseDir+"PATtuple_438_1_Cta.root",
sampleBaseDir+"PATtuple_480_1_kj0.root",
sampleBaseDir+"PATtuple_281_1_yKQ.root",
sampleBaseDir+"PATtuple_150_1_U6K.root",
sampleBaseDir+"PATtuple_592_1_EOR.root",
sampleBaseDir+"PATtuple_197_1_WHR.root",
sampleBaseDir+"PATtuple_251_1_0Fd.root",
sampleBaseDir+"PATtuple_270_1_EOL.root",
sampleBaseDir+"PATtuple_415_1_yqL.root",
sampleBaseDir+"PATtuple_535_1_LnW.root",
sampleBaseDir+"PATtuple_254_1_rp7.root",
sampleBaseDir+"PATtuple_326_1_QWc.root",
sampleBaseDir+"PATtuple_530_1_7eN.root",
sampleBaseDir+"PATtuple_227_1_xC5.root",
sampleBaseDir+"PATtuple_352_1_Yyl.root",
sampleBaseDir+"PATtuple_14_1_ge5.root",
sampleBaseDir+"PATtuple_187_1_atY.root",
sampleBaseDir+"PATtuple_329_1_IqT.root",
sampleBaseDir+"PATtuple_305_1_Evu.root",
sampleBaseDir+"PATtuple_561_1_Xlj.root",
sampleBaseDir+"PATtuple_587_1_cav.root",
sampleBaseDir+"PATtuple_611_1_A7V.root",
sampleBaseDir+"PATtuple_661_1_gzr.root",
sampleBaseDir+"PATtuple_61_1_CKx.root",
sampleBaseDir+"PATtuple_191_1_qCd.root",
sampleBaseDir+"PATtuple_68_1_DGt.root",
sampleBaseDir+"PATtuple_421_1_cEF.root",
sampleBaseDir+"PATtuple_258_1_ITP.root",
sampleBaseDir+"PATtuple_357_1_Q1d.root",
sampleBaseDir+"PATtuple_247_1_MD6.root",
sampleBaseDir+"PATtuple_248_1_Lr9.root",
sampleBaseDir+"PATtuple_308_1_0TB.root",
sampleBaseDir+"PATtuple_431_1_Nik.root",
sampleBaseDir+"PATtuple_437_1_vaO.root",
sampleBaseDir+"PATtuple_382_1_zGa.root",
sampleBaseDir+"PATtuple_126_1_N9x.root",
sampleBaseDir+"PATtuple_127_1_Hwr.root",
sampleBaseDir+"PATtuple_180_1_0Te.root",
sampleBaseDir+"PATtuple_429_1_eRI.root",
sampleBaseDir+"PATtuple_451_1_ccu.root",
sampleBaseDir+"PATtuple_467_1_9FQ.root",
sampleBaseDir+"PATtuple_639_1_UZH.root",
sampleBaseDir+"PATtuple_443_1_jTv.root",
sampleBaseDir+"PATtuple_261_1_721.root",
sampleBaseDir+"PATtuple_38_1_CNX.root",
sampleBaseDir+"PATtuple_299_1_ZNh.root",
sampleBaseDir+"PATtuple_267_1_pXv.root",
sampleBaseDir+"PATtuple_331_1_B79.root",
sampleBaseDir+"PATtuple_618_1_J8m.root",
sampleBaseDir+"PATtuple_596_1_iTU.root",
sampleBaseDir+"PATtuple_589_1_hyh.root",
sampleBaseDir+"PATtuple_445_1_yVE.root",
sampleBaseDir+"PATtuple_233_1_I76.root",
sampleBaseDir+"PATtuple_319_1_2mJ.root",
sampleBaseDir+"PATtuple_390_1_ffs.root",
sampleBaseDir+"PATtuple_597_1_h8k.root",
sampleBaseDir+"PATtuple_646_1_3hR.root",
sampleBaseDir+"PATtuple_484_1_NlX.root",
sampleBaseDir+"PATtuple_8_1_j2h.root",
sampleBaseDir+"PATtuple_302_1_5W6.root",
sampleBaseDir+"PATtuple_511_1_w66.root",
sampleBaseDir+"PATtuple_344_1_tJj.root",
sampleBaseDir+"PATtuple_571_1_PJ5.root",
sampleBaseDir+"PATtuple_508_1_N4D.root",
sampleBaseDir+"PATtuple_63_1_50a.root",
sampleBaseDir+"PATtuple_273_1_kVT.root",
sampleBaseDir+"PATtuple_453_1_Rgn.root",
sampleBaseDir+"PATtuple_521_1_EOI.root",
sampleBaseDir+"PATtuple_624_1_IT9.root",
sampleBaseDir+"PATtuple_363_1_NWH.root",
sampleBaseDir+"PATtuple_388_1_Egc.root",
sampleBaseDir+"PATtuple_441_1_vWe.root",
sampleBaseDir+"PATtuple_655_1_R21.root",
sampleBaseDir+"PATtuple_124_1_ypo.root",
sampleBaseDir+"PATtuple_487_1_nqt.root",
sampleBaseDir+"PATtuple_399_1_Qam.root",
sampleBaseDir+"PATtuple_627_1_4Lc.root",
sampleBaseDir+"PATtuple_306_1_6r7.root",
sampleBaseDir+"PATtuple_386_1_a00.root",
sampleBaseDir+"PATtuple_403_1_deO.root",
sampleBaseDir+"PATtuple_439_1_LfA.root",
sampleBaseDir+"PATtuple_409_1_ao2.root",
sampleBaseDir+"PATtuple_69_1_C9u.root",
sampleBaseDir+"PATtuple_384_1_IEl.root",
sampleBaseDir+"PATtuple_557_1_Hxm.root",
sampleBaseDir+"PATtuple_410_1_oH7.root",
sampleBaseDir+"PATtuple_21_1_1cF.root",
sampleBaseDir+"PATtuple_182_1_5iC.root",
sampleBaseDir+"PATtuple_206_1_74Q.root",
sampleBaseDir+"PATtuple_214_1_5h8.root",
sampleBaseDir+"PATtuple_423_1_sxw.root",
sampleBaseDir+"PATtuple_562_1_zn5.root",
sampleBaseDir+"PATtuple_448_1_Umx.root",
sampleBaseDir+"PATtuple_408_1_RGS.root",
sampleBaseDir+"PATtuple_195_1_paN.root",
sampleBaseDir+"PATtuple_160_1_gvw.root",
sampleBaseDir+"PATtuple_468_1_5F6.root",
sampleBaseDir+"PATtuple_524_1_qPw.root",
sampleBaseDir+"PATtuple_633_1_0WM.root",
sampleBaseDir+"PATtuple_581_1_H6H.root",
sampleBaseDir+"PATtuple_141_1_9NF.root",
sampleBaseDir+"PATtuple_527_1_P85.root",
sampleBaseDir+"PATtuple_43_1_GtT.root",
sampleBaseDir+"PATtuple_98_1_gw3.root",
sampleBaseDir+"PATtuple_22_1_Yp7.root",
sampleBaseDir+"PATtuple_218_1_3Q4.root",
sampleBaseDir+"PATtuple_566_1_aUX.root",
sampleBaseDir+"PATtuple_404_1_MXh.root",
sampleBaseDir+"PATtuple_49_1_4xt.root",
sampleBaseDir+"PATtuple_414_1_7aW.root",
sampleBaseDir+"PATtuple_153_1_mL3.root",
sampleBaseDir+"PATtuple_41_1_lgP.root",
sampleBaseDir+"PATtuple_82_1_4wi.root",
sampleBaseDir+"PATtuple_208_1_W8n.root",
sampleBaseDir+"PATtuple_322_1_jyQ.root",
sampleBaseDir+"PATtuple_556_1_KPl.root",
sampleBaseDir+"PATtuple_342_1_myb.root",
sampleBaseDir+"PATtuple_327_1_4Xv.root",
sampleBaseDir+"PATtuple_418_1_cOW.root",
sampleBaseDir+"PATtuple_465_1_dO7.root",
sampleBaseDir+"PATtuple_640_1_nm1.root",
sampleBaseDir+"PATtuple_473_1_awU.root",
sampleBaseDir+"PATtuple_482_1_kqh.root",
sampleBaseDir+"PATtuple_96_1_m5Y.root",
sampleBaseDir+"PATtuple_224_1_ioy.root",
sampleBaseDir+"PATtuple_185_1_X6j.root",
sampleBaseDir+"PATtuple_220_1_AyW.root",
sampleBaseDir+"PATtuple_332_1_gEy.root",
sampleBaseDir+"PATtuple_594_1_cNH.root",
sampleBaseDir+"PATtuple_192_1_JuX.root",
sampleBaseDir+"PATtuple_272_1_6zE.root",
sampleBaseDir+"PATtuple_297_1_JtO.root",
sampleBaseDir+"PATtuple_99_1_f1c.root",
sampleBaseDir+"PATtuple_307_1_01O.root",
sampleBaseDir+"PATtuple_512_1_LbO.root",
sampleBaseDir+"PATtuple_522_1_A7H.root",
sampleBaseDir+"PATtuple_24_1_eTD.root",
sampleBaseDir+"PATtuple_237_1_lof.root",
sampleBaseDir+"PATtuple_278_1_arz.root",
sampleBaseDir+"PATtuple_337_1_noc.root",
sampleBaseDir+"PATtuple_446_1_wjG.root",
sampleBaseDir+"PATtuple_301_1_kKa.root",
sampleBaseDir+"PATtuple_26_1_U2Q.root",
sampleBaseDir+"PATtuple_76_1_uzd.root",
sampleBaseDir+"PATtuple_89_1_O35.root",
sampleBaseDir+"PATtuple_324_1_4Uy.root",
sampleBaseDir+"PATtuple_545_1_VEY.root",
sampleBaseDir+"PATtuple_635_1_F35.root",
sampleBaseDir+"PATtuple_625_1_Tw6.root",
sampleBaseDir+"PATtuple_209_1_Fvh.root",
sampleBaseDir+"PATtuple_311_1_9Ql.root",
sampleBaseDir+"PATtuple_117_1_CHB.root",
sampleBaseDir+"PATtuple_6_1_gmb.root",
sampleBaseDir+"PATtuple_304_1_EHG.root",
sampleBaseDir+"PATtuple_356_1_wS3.root",
sampleBaseDir+"PATtuple_605_1_Q7G.root",
sampleBaseDir+"PATtuple_609_1_Im9.root",
sampleBaseDir+"PATtuple_45_1_jID.root",
sampleBaseDir+"PATtuple_212_1_gIG.root",
sampleBaseDir+"PATtuple_424_1_afs.root",
sampleBaseDir+"PATtuple_615_1_WWG.root",
sampleBaseDir+"PATtuple_148_1_U7k.root",
sampleBaseDir+"PATtuple_81_1_0fi.root",
sampleBaseDir+"PATtuple_204_1_1df.root",
sampleBaseDir+"PATtuple_430_1_mTC.root",
sampleBaseDir+"PATtuple_371_1_j7l.root",
sampleBaseDir+"PATtuple_601_1_sqI.root",
sampleBaseDir+"PATtuple_16_1_6IG.root",
sampleBaseDir+"PATtuple_252_1_DKd.root",
sampleBaseDir+"PATtuple_462_1_hWs.root",
sampleBaseDir+"PATtuple_35_1_nnj.root",
sampleBaseDir+"PATtuple_47_1_Opr.root",
sampleBaseDir+"PATtuple_54_1_O9C.root",
sampleBaseDir+"PATtuple_165_1_4Iw.root",
sampleBaseDir+"PATtuple_235_1_L7y.root",
sampleBaseDir+"PATtuple_257_1_iG8.root",
sampleBaseDir+"PATtuple_53_1_IvZ.root",
sampleBaseDir+"PATtuple_90_1_bWe.root",
sampleBaseDir+"PATtuple_110_1_8EE.root",
sampleBaseDir+"PATtuple_383_1_TIT.root",
sampleBaseDir+"PATtuple_198_1_eBu.root",
sampleBaseDir+"PATtuple_243_1_Fwa.root",
sampleBaseDir+"PATtuple_78_1_PwE.root",
sampleBaseDir+"PATtuple_19_1_Nxd.root",
sampleBaseDir+"PATtuple_149_1_cRU.root",
sampleBaseDir+"PATtuple_240_1_6ve.root",
sampleBaseDir+"PATtuple_335_1_8AH.root",
sampleBaseDir+"PATtuple_351_1_tne.root",
sampleBaseDir+"PATtuple_55_1_fJk.root",
sampleBaseDir+"PATtuple_551_1_Xia.root",
sampleBaseDir+"PATtuple_493_1_cZX.root",
sampleBaseDir+"PATtuple_31_1_2F6.root",
sampleBaseDir+"PATtuple_219_1_GFG.root",
sampleBaseDir+"PATtuple_565_1_MPy.root",
sampleBaseDir+"PATtuple_46_1_E6z.root",
sampleBaseDir+"PATtuple_292_1_FVy.root",
sampleBaseDir+"PATtuple_598_1_1St.root",
sampleBaseDir+"PATtuple_604_1_jND.root",
sampleBaseDir+"PATtuple_662_1_Oty.root",
sampleBaseDir+"PATtuple_92_1_YN2.root",
sampleBaseDir+"PATtuple_119_1_tUd.root",
sampleBaseDir+"PATtuple_364_1_RbF.root",
sampleBaseDir+"PATtuple_309_1_xum.root",
sampleBaseDir+"PATtuple_27_1_4Ee.root",
sampleBaseDir+"PATtuple_23_1_DWC.root",
sampleBaseDir+"PATtuple_449_1_45A.root",
sampleBaseDir+"PATtuple_108_1_oF1.root",
sampleBaseDir+"PATtuple_56_1_c8p.root",
sampleBaseDir+"PATtuple_377_1_TrM.root",
sampleBaseDir+"PATtuple_339_1_my7.root",
sampleBaseDir+"PATtuple_459_1_jj0.root",
sampleBaseDir+"PATtuple_534_1_A9k.root",
sampleBaseDir+"PATtuple_398_1_urR.root",
sampleBaseDir+"PATtuple_647_1_b29.root",
sampleBaseDir+"PATtuple_629_1_0zq.root",
sampleBaseDir+"PATtuple_658_1_zy5.root",
sampleBaseDir+"PATtuple_496_1_enm.root",
sampleBaseDir+"PATtuple_33_1_QVl.root",
sampleBaseDir+"PATtuple_114_1_ud3.root",
sampleBaseDir+"PATtuple_181_1_zSV.root",
sampleBaseDir+"PATtuple_184_1_wPx.root",
sampleBaseDir+"PATtuple_131_1_NwQ.root",
sampleBaseDir+"PATtuple_416_1_sfD.root",
sampleBaseDir+"PATtuple_93_1_Yd1.root",
sampleBaseDir+"PATtuple_60_1_CG2.root",
sampleBaseDir+"PATtuple_485_1_Ekw.root",
sampleBaseDir+"PATtuple_610_1_FT0.root",
sampleBaseDir+"PATtuple_630_1_UlE.root",
sampleBaseDir+"PATtuple_40_1_yeE.root",
sampleBaseDir+"PATtuple_84_1_Hqt.root",
sampleBaseDir+"PATtuple_488_1_eeP.root",
sampleBaseDir+"PATtuple_531_1_nYE.root",
sampleBaseDir+"PATtuple_380_1_Dj7.root",
sampleBaseDir+"PATtuple_120_1_Vds.root",
sampleBaseDir+"PATtuple_154_1_Hs6.root",
sampleBaseDir+"PATtuple_11_1_Ksj.root",
sampleBaseDir+"PATtuple_595_1_xSt.root",
sampleBaseDir+"PATtuple_590_1_gk1.root",
sampleBaseDir+"PATtuple_616_1_m9X.root",
sampleBaseDir+"PATtuple_87_1_OT3.root",
sampleBaseDir+"PATtuple_255_1_yRj.root",
sampleBaseDir+"PATtuple_623_1_UXe.root",
sampleBaseDir+"PATtuple_83_1_lRV.root",
sampleBaseDir+"PATtuple_614_1_Adr.root",
sampleBaseDir+"PATtuple_554_1_ycI.root",
sampleBaseDir+"PATtuple_440_1_Wzh.root",
sampleBaseDir+"PATtuple_188_1_VRW.root",
sampleBaseDir+"PATtuple_336_1_DTX.root",
sampleBaseDir+"PATtuple_579_1_pdh.root",
sampleBaseDir+"PATtuple_497_1_Gzp.root",
sampleBaseDir+"PATtuple_405_1_xeq.root",
sampleBaseDir+"PATtuple_201_1_n8K.root",
sampleBaseDir+"PATtuple_221_1_9MC.root",
sampleBaseDir+"PATtuple_230_1_Zpd.root",
sampleBaseDir+"PATtuple_121_1_Ljf.root",
sampleBaseDir+"PATtuple_362_1_Ddt.root",
sampleBaseDir+"PATtuple_367_1_JqO.root",
sampleBaseDir+"PATtuple_397_1_6mR.root",
sampleBaseDir+"PATtuple_1_1_PVP.root",
sampleBaseDir+"PATtuple_66_1_Rls.root",
sampleBaseDir+"PATtuple_50_1_M2K.root",
sampleBaseDir+"PATtuple_159_1_hjF.root",
sampleBaseDir+"PATtuple_162_1_HxO.root",
sampleBaseDir+"PATtuple_318_1_ZlJ.root",
sampleBaseDir+"PATtuple_452_1_uMW.root",
sampleBaseDir+"PATtuple_369_1_A3u.root",
sampleBaseDir+"PATtuple_504_1_lCF.root",
sampleBaseDir+"PATtuple_317_1_sf7.root",
sampleBaseDir+"PATtuple_51_1_75R.root",
sampleBaseDir+"PATtuple_112_1_8mz.root",
sampleBaseDir+"PATtuple_232_1_pom.root",
sampleBaseDir+"PATtuple_413_1_6Ac.root",
sampleBaseDir+"PATtuple_498_1_uu8.root",
sampleBaseDir+"PATtuple_483_1_Gw1.root",
sampleBaseDir+"PATtuple_194_1_5e7.root",
sampleBaseDir+"PATtuple_320_1_4c4.root",
sampleBaseDir+"PATtuple_334_1_KeV.root",
sampleBaseDir+"PATtuple_608_1_Ljh.root",
sampleBaseDir+"PATtuple_584_1_cr0.root",
sampleBaseDir+"PATtuple_475_1_Ugc.root",
sampleBaseDir+"PATtuple_12_1_1Mo.root",
sampleBaseDir+"PATtuple_115_1_Zs2.root",
sampleBaseDir+"PATtuple_569_1_rY5.root",
sampleBaseDir+"PATtuple_207_1_qJY.root",
sampleBaseDir+"PATtuple_250_1_NUn.root",
sampleBaseDir+"PATtuple_279_1_pCR.root",
sampleBaseDir+"PATtuple_621_1_9MD.root",
sampleBaseDir+"PATtuple_492_1_3GC.root",
sampleBaseDir+"PATtuple_64_1_FEG.root",
sampleBaseDir+"PATtuple_333_1_Iuq.root",
sampleBaseDir+"PATtuple_519_1_EsO.root",
sampleBaseDir+"PATtuple_222_1_bg3.root",
sampleBaseDir+"PATtuple_638_1_iFd.root",
sampleBaseDir+"PATtuple_28_1_obS.root",
sampleBaseDir+"PATtuple_210_1_UZO.root",
sampleBaseDir+"PATtuple_236_1_451.root",
sampleBaseDir+"PATtuple_264_1_rBE.root",
sampleBaseDir+"PATtuple_420_1_rKJ.root",
sampleBaseDir+"PATtuple_518_1_yBD.root",
sampleBaseDir+"PATtuple_355_1_Hl1.root",
sampleBaseDir+"PATtuple_588_1_R7w.root",
sampleBaseDir+"PATtuple_656_1_PXT.root",
sampleBaseDir+"PATtuple_15_1_8ta.root",
sampleBaseDir+"PATtuple_88_1_0mr.root",
sampleBaseDir+"PATtuple_376_1_x60.root",
sampleBaseDir+"PATtuple_77_1_TbO.root",
sampleBaseDir+"PATtuple_229_1_8Ci.root",
sampleBaseDir+"PATtuple_101_1_HNF.root",
sampleBaseDir+"PATtuple_422_1_LTE.root",
sampleBaseDir+"PATtuple_425_1_eoM.root",
sampleBaseDir+"PATtuple_541_1_58U.root",
sampleBaseDir+"PATtuple_177_1_Esb.root",
sampleBaseDir+"PATtuple_374_1_2yA.root",
sampleBaseDir+"PATtuple_442_1_vl2.root",
sampleBaseDir+"PATtuple_373_1_2gm.root",
sampleBaseDir+"PATtuple_10_1_Jsx.root",
sampleBaseDir+"PATtuple_128_1_LIa.root",
sampleBaseDir+"PATtuple_280_1_oBD.root",
sampleBaseDir+"PATtuple_73_1_RFT.root",
sampleBaseDir+"PATtuple_573_1_3gi.root",
sampleBaseDir+"PATtuple_560_1_EJA.root",
sampleBaseDir+"PATtuple_436_1_888.root",
sampleBaseDir+"PATtuple_203_1_kUl.root",
sampleBaseDir+"PATtuple_168_1_5Wm.root",
sampleBaseDir+"PATtuple_353_1_671.root",
sampleBaseDir+"PATtuple_536_1_FUy.root",
sampleBaseDir+"PATtuple_501_1_5oI.root",
sampleBaseDir+"PATtuple_542_1_5Yi.root",
sampleBaseDir+"PATtuple_298_1_K9X.root",
sampleBaseDir+"PATtuple_450_1_O0C.root",
sampleBaseDir+"PATtuple_25_1_ASE.root",
sampleBaseDir+"PATtuple_123_1_LJa.root",
sampleBaseDir+"PATtuple_328_1_X8c.root",
sampleBaseDir+"PATtuple_163_1_qMG.root",
sampleBaseDir+"PATtuple_151_1_beH.root",
sampleBaseDir+"PATtuple_170_1_NFK.root",
sampleBaseDir+"PATtuple_568_1_yQN.root",
sampleBaseDir+"PATtuple_649_1_p3V.root",
sampleBaseDir+"PATtuple_400_1_MA9.root",
sampleBaseDir+"PATtuple_479_1_epC.root",
sampleBaseDir+"PATtuple_434_1_O35.root",
sampleBaseDir+"PATtuple_253_1_84C.root",
sampleBaseDir+"PATtuple_85_1_beR.root",
sampleBaseDir+"PATtuple_146_1_J7m.root",
sampleBaseDir+"PATtuple_617_1_FFp.root",
sampleBaseDir+"PATtuple_643_1_xKt.root",
sampleBaseDir+"PATtuple_175_1_VNt.root",
sampleBaseDir+"PATtuple_282_1_0jt.root",
sampleBaseDir+"PATtuple_641_1_QPU.root",
sampleBaseDir+"PATtuple_166_1_cha.root",
sampleBaseDir+"PATtuple_559_1_pcH.root",
sampleBaseDir+"PATtuple_523_1_iED.root",
sampleBaseDir+"PATtuple_48_1_77W.root",
sampleBaseDir+"PATtuple_72_1_0vr.root",
sampleBaseDir+"PATtuple_130_1_zdr.root",
sampleBaseDir+"PATtuple_225_1_V7o.root",
sampleBaseDir+"PATtuple_631_1_3SY.root",
sampleBaseDir+"PATtuple_118_1_4Tr.root",
sampleBaseDir+"PATtuple_644_1_fOW.root",
sampleBaseDir+"PATtuple_62_1_0eo.root",
sampleBaseDir+"PATtuple_144_1_AZQ.root",
sampleBaseDir+"PATtuple_147_1_Sho.root",
sampleBaseDir+"PATtuple_539_1_giM.root",
sampleBaseDir+"PATtuple_599_1_KGA.root",
sampleBaseDir+"PATtuple_652_1_uPK.root",
sampleBaseDir+"PATtuple_458_1_aKf.root",
sampleBaseDir+"PATtuple_284_1_1Iv.root",
sampleBaseDir+"PATtuple_277_1_KyQ.root",
sampleBaseDir+"PATtuple_349_1_DbE.root",
sampleBaseDir+"PATtuple_350_1_W27.root",
sampleBaseDir+"PATtuple_94_1_YA1.root",
sampleBaseDir+"PATtuple_145_1_hTb.root",
sampleBaseDir+"PATtuple_620_1_1jx.root",
sampleBaseDir+"PATtuple_231_1_3Wl.root",
sampleBaseDir+"PATtuple_290_1_jr8.root",
sampleBaseDir+"PATtuple_186_1_mNk.root",
sampleBaseDir+"PATtuple_58_1_Pai.root",
sampleBaseDir+"PATtuple_132_1_IsJ.root",
sampleBaseDir+"PATtuple_241_1_TBt.root",
sampleBaseDir+"PATtuple_461_1_GRK.root",
sampleBaseDir+"PATtuple_510_1_mmZ.root",
sampleBaseDir+"PATtuple_111_1_rAa.root",
sampleBaseDir+"PATtuple_666_1_1Ub.root",
sampleBaseDir+"PATtuple_447_1_Wju.root",
sampleBaseDir+"PATtuple_387_1_sGi.root",
sampleBaseDir+"PATtuple_262_1_qJn.root",
sampleBaseDir+"PATtuple_464_1_4r7.root",
sampleBaseDir+"PATtuple_515_1_N0o.root",
sampleBaseDir+"PATtuple_346_1_xSU.root",
sampleBaseDir+"PATtuple_613_1_iSv.root",
sampleBaseDir+"PATtuple_564_1_tET.root",
sampleBaseDir+"PATtuple_179_1_KvF.root",
sampleBaseDir+"PATtuple_283_1_rgL.root",
sampleBaseDir+"PATtuple_567_1_0dh.root",
sampleBaseDir+"PATtuple_628_1_UZ0.root",
sampleBaseDir+"PATtuple_659_1_HKs.root",
sampleBaseDir+"PATtuple_44_1_zQl.root",
sampleBaseDir+"PATtuple_294_1_0OZ.root",
sampleBaseDir+"PATtuple_137_1_ISD.root",
sampleBaseDir+"PATtuple_199_1_kyB.root",
sampleBaseDir+"PATtuple_75_1_aJO.root",
sampleBaseDir+"PATtuple_578_1_DTm.root",
sampleBaseDir+"PATtuple_238_1_pvR.root",
sampleBaseDir+"PATtuple_660_1_uis.root",
sampleBaseDir+"PATtuple_642_1_xNk.root",
sampleBaseDir+"PATtuple_135_1_BWs.root",
sampleBaseDir+"PATtuple_80_1_cV0.root",
sampleBaseDir+"PATtuple_172_1_W8I.root",
sampleBaseDir+"PATtuple_466_1_12y.root",
sampleBaseDir+"PATtuple_469_1_q1P.root",
sampleBaseDir+"PATtuple_381_1_iwy.root",
sampleBaseDir+"PATtuple_585_1_OB6.root",
sampleBaseDir+"PATtuple_173_1_78G.root",
sampleBaseDir+"PATtuple_612_1_Ou1.root",
sampleBaseDir+"PATtuple_406_1_VAY.root",
sampleBaseDir+"PATtuple_171_1_tFw.root",
sampleBaseDir+"PATtuple_289_1_nQn.root",
sampleBaseDir+"PATtuple_586_1_VlF.root",
sampleBaseDir+"PATtuple_607_1_UbL.root",
sampleBaseDir+"PATtuple_338_1_IF4.root",
sampleBaseDir+"PATtuple_103_1_WZx.root",
sampleBaseDir+"PATtuple_507_1_JOz.root",
sampleBaseDir+"PATtuple_580_1_SRF.root",
sampleBaseDir+"PATtuple_359_1_Vku.root",
sampleBaseDir+"PATtuple_600_1_ZTz.root",
sampleBaseDir+"PATtuple_340_1_JCb.root",
sampleBaseDir+"PATtuple_246_1_4pm.root",
sampleBaseDir+"PATtuple_606_1_zg8.root",
sampleBaseDir+"PATtuple_474_1_HDj.root",
sampleBaseDir+"PATtuple_9_1_fMQ.root",
sampleBaseDir+"PATtuple_513_1_Ev1.root",
sampleBaseDir+"PATtuple_472_1_SCs.root",
sampleBaseDir+"PATtuple_651_1_vFq.root",
sampleBaseDir+"PATtuple_95_1_AeY.root",
sampleBaseDir+"PATtuple_67_1_3G7.root",
sampleBaseDir+"PATtuple_176_1_5LH.root",
sampleBaseDir+"PATtuple_291_1_vy3.root",
sampleBaseDir+"PATtuple_426_1_SR4.root",
sampleBaseDir+"PATtuple_365_1_ujY.root",
sampleBaseDir+"PATtuple_537_1_QfH.root",
sampleBaseDir+"PATtuple_619_1_z6r.root",
sampleBaseDir+"PATtuple_5_1_IW4.root",
sampleBaseDir+"PATtuple_260_1_I9R.root",
sampleBaseDir+"PATtuple_263_1_nYe.root",
sampleBaseDir+"PATtuple_533_1_5DO.root",
sampleBaseDir+"PATtuple_576_1_J4F.root",
sampleBaseDir+"PATtuple_550_1_ny3.root",
sampleBaseDir+"PATtuple_392_1_PGa.root",
sampleBaseDir+"PATtuple_385_1_9WG.root",
sampleBaseDir+"PATtuple_13_1_UvC.root",
sampleBaseDir+"PATtuple_105_1_mDU.root",
sampleBaseDir+"PATtuple_268_1_KlV.root",
sampleBaseDir+"PATtuple_347_1_qBI.root",
sampleBaseDir+"PATtuple_529_1_qPs.root",
sampleBaseDir+"PATtuple_632_1_lh4.root",
sampleBaseDir+"PATtuple_228_1_znT.root",
sampleBaseDir+"PATtuple_249_1_mVk.root",
sampleBaseDir+"PATtuple_463_1_XwY.root",
sampleBaseDir+"PATtuple_36_1_CWy.root",
sampleBaseDir+"PATtuple_143_1_CNK.root",
sampleBaseDir+"PATtuple_169_1_5lu.root",
sampleBaseDir+"PATtuple_183_1_ecx.root",
sampleBaseDir+"PATtuple_532_1_tIn.root",
sampleBaseDir+"PATtuple_593_1_vwF.root",
sampleBaseDir+"PATtuple_427_1_9sw.root",
sampleBaseDir+"PATtuple_296_1_ZVI.root",
sampleBaseDir+"PATtuple_428_1_CRU.root",
sampleBaseDir+"PATtuple_470_1_zHO.root",
sampleBaseDir+"PATtuple_603_1_0c7.root",
sampleBaseDir+"PATtuple_546_1_sXp.root",
sampleBaseDir+"PATtuple_575_1_w50.root",
sampleBaseDir+"PATtuple_29_1_Q4Y.root",
sampleBaseDir+"PATtuple_315_1_z1G.root",
sampleBaseDir+"PATtuple_295_1_PoD.root",
sampleBaseDir+"PATtuple_122_1_89W.root",
sampleBaseDir+"PATtuple_636_1_590.root",
sampleBaseDir+"PATtuple_490_1_Ikv.root",
sampleBaseDir+"PATtuple_653_1_y7F.root",
sampleBaseDir+"PATtuple_287_1_NSs.root",
sampleBaseDir+"PATtuple_648_1_MIV.root",
sampleBaseDir+"PATtuple_274_1_QnH.root",
sampleBaseDir+"PATtuple_140_1_2vG.root",
sampleBaseDir+"PATtuple_164_1_GFZ.root",
sampleBaseDir+"PATtuple_136_1_IO9.root",
sampleBaseDir+"PATtuple_193_1_FbO.root",
sampleBaseDir+"PATtuple_366_1_Zss.root",
sampleBaseDir+"PATtuple_213_1_40J.root",
sampleBaseDir+"PATtuple_391_1_Yvt.root",
sampleBaseDir+"PATtuple_202_1_wzY.root",
sampleBaseDir+"PATtuple_286_1_mJW.root",
sampleBaseDir+"PATtuple_516_1_t9I.root",
sampleBaseDir+"PATtuple_129_1_hB8.root",
sampleBaseDir+"PATtuple_157_1_AUE.root",
sampleBaseDir+"PATtuple_190_1_k5i.root",
sampleBaseDir+"PATtuple_489_1_Czw.root",
sampleBaseDir+"PATtuple_547_1_NJ1.root",
sampleBaseDir+"PATtuple_543_1_NxC.root",
sampleBaseDir+"PATtuple_412_1_7i0.root",
sampleBaseDir+"PATtuple_348_1_vKe.root",
sampleBaseDir+"PATtuple_514_1_ujX.root",
sampleBaseDir+"PATtuple_360_1_uRG.root",
sampleBaseDir+"PATtuple_178_1_23G.root",
sampleBaseDir+"PATtuple_196_1_rtp.root",
sampleBaseDir+"PATtuple_389_1_GgA.root",
sampleBaseDir+"PATtuple_266_1_KBw.root",
sampleBaseDir+"PATtuple_503_1_ZED.root",
sampleBaseDir+"PATtuple_71_1_dXt.root",
sampleBaseDir+"PATtuple_285_1_j1t.root",
sampleBaseDir+"PATtuple_109_1_JR4.root",
sampleBaseDir+"PATtuple_411_1_p0F.root",
sampleBaseDir+"PATtuple_86_1_sNz.root",
sampleBaseDir+"PATtuple_57_1_2y8.root",
sampleBaseDir+"PATtuple_269_1_wx1.root",
sampleBaseDir+"PATtuple_265_1_GH9.root",
sampleBaseDir+"PATtuple_491_1_3H6.root",
sampleBaseDir+"PATtuple_665_1_kcJ.root",
sampleBaseDir+"PATtuple_500_1_A1s.root",
sampleBaseDir+"PATtuple_525_1_Kui.root",
sampleBaseDir+"PATtuple_370_1_eE4.root",
sampleBaseDir+"PATtuple_142_1_qk6.root",
sampleBaseDir+"PATtuple_156_1_jYF.root",
sampleBaseDir+"PATtuple_189_1_1SD.root",
sampleBaseDir+"PATtuple_375_1_1bN.root",
sampleBaseDir+"PATtuple_433_1_O6S.root",
sampleBaseDir+"PATtuple_361_1_rbj.root",
sampleBaseDir+"PATtuple_572_1_Un2.root",
sampleBaseDir+"PATtuple_591_1_ZE4.root",
sampleBaseDir+"PATtuple_402_1_01x.root",
sampleBaseDir+"PATtuple_314_1_ell.root",
sampleBaseDir+"PATtuple_32_1_Dk7.root",
sampleBaseDir+"PATtuple_106_1_3cM.root",
sampleBaseDir+"PATtuple_288_1_sHs.root",
sampleBaseDir+"PATtuple_478_1_dlI.root",
sampleBaseDir+"PATtuple_583_1_oNt.root",
sampleBaseDir+"PATtuple_471_1_XTs.root",
sampleBaseDir+"PATtuple_555_1_EXI.root",
sampleBaseDir+"PATtuple_107_1_PbJ.root",
sampleBaseDir+"PATtuple_100_1_eIv.root",
sampleBaseDir+"PATtuple_244_1_CAc.root",
sampleBaseDir+"PATtuple_303_1_Y9J.root",
sampleBaseDir+"PATtuple_432_1_qPO.root",
sampleBaseDir+"PATtuple_454_1_bw7.root",
sampleBaseDir+"PATtuple_663_1_7Pd.root",
sampleBaseDir+"PATtuple_477_1_0RJ.root",
sampleBaseDir+"PATtuple_528_1_K1J.root",
sampleBaseDir+"PATtuple_645_1_pz9.root",
sampleBaseDir+"PATtuple_37_1_lJY.root",
sampleBaseDir+"PATtuple_116_1_uwF.root",
sampleBaseDir+"PATtuple_538_1_uyv.root",
sampleBaseDir+"PATtuple_563_1_JW6.root",
sampleBaseDir+"PATtuple_3_1_0JC.root",
sampleBaseDir+"PATtuple_155_1_5Tt.root",
sampleBaseDir+"PATtuple_256_1_A9p.root",
sampleBaseDir+"PATtuple_276_1_8ma.root",
sampleBaseDir+"PATtuple_396_1_0xo.root",
sampleBaseDir+"PATtuple_553_1_TDO.root",
sampleBaseDir+"PATtuple_343_1_b2h.root",
sampleBaseDir+"PATtuple_139_1_Mbl.root",
sampleBaseDir+"PATtuple_79_1_fAj.root",
sampleBaseDir+"PATtuple_104_1_J2U.root",
sampleBaseDir+"PATtuple_152_1_uc8.root",
sampleBaseDir+"PATtuple_323_1_Qm3.root",
]