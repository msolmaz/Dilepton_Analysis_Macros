sampleDataSet = '/HTo2LongLivedTo4F_MH-125_MFF-20_CTau13To1300_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C-v1/GEN-SIM-RECODEBUG'  

sampleCMSEnergy = 8000

sampleRelease = "CMSSW_5_3_7" # original (i.e. RECO file) release, not the one we plan to process them with
sampleProcessRelease = "CMSSW_5_3_8" # release used to create new files with

sampleNumEvents = 100007

sampleXSec = 1 # pb

# global tag can be extracted from file using edmProvDump filename|grep globaltag
# note however that this is the tag for *further* processing, not the original tag
sampleGlobalTag = 'START53_V7G::All'

sampleDuplicateCheckMode = 'checkAllFilesOpened'

sampleType = "SIGNALMC"




samplePatDBSName=""

sampleBaseDir="file:/eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_pat_20140329/demattia//HTo2LongLivedTo4F_MH-125_MFF-20_CTau13To1300_8TeV-pythia6/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_pat_20140329/2683ba4974d65285b3ccbed96c537ee3/"
samplePatFiles = [
sampleBaseDir+"PATtuple_10_1_wnT.root",
sampleBaseDir+"PATtuple_11_1_aEs.root",
sampleBaseDir+"PATtuple_12_1_S0Q.root",
sampleBaseDir+"PATtuple_13_1_SF2.root",
sampleBaseDir+"PATtuple_14_2_Wor.root",
sampleBaseDir+"PATtuple_15_1_L8l.root",
sampleBaseDir+"PATtuple_16_1_rof.root",
sampleBaseDir+"PATtuple_17_1_fhf.root",
sampleBaseDir+"PATtuple_18_1_OKE.root",
sampleBaseDir+"PATtuple_19_1_Rcn.root",
sampleBaseDir+"PATtuple_1_1_G3x.root",
sampleBaseDir+"PATtuple_20_1_zya.root",
sampleBaseDir+"PATtuple_21_1_S3t.root",
sampleBaseDir+"PATtuple_22_1_PfJ.root",
sampleBaseDir+"PATtuple_23_2_UDh.root",
sampleBaseDir+"PATtuple_24_1_4ze.root",
sampleBaseDir+"PATtuple_25_1_Yd0.root",
sampleBaseDir+"PATtuple_26_1_Wcm.root",
sampleBaseDir+"PATtuple_27_1_9ox.root",
sampleBaseDir+"PATtuple_28_2_xFj.root",
sampleBaseDir+"PATtuple_29_1_yGT.root",
sampleBaseDir+"PATtuple_2_1_U3p.root",
sampleBaseDir+"PATtuple_30_1_H76.root",
sampleBaseDir+"PATtuple_31_1_Hls.root",
sampleBaseDir+"PATtuple_32_1_YWc.root",
sampleBaseDir+"PATtuple_33_1_OYh.root",
sampleBaseDir+"PATtuple_34_1_szC.root",
sampleBaseDir+"PATtuple_35_1_bZK.root",
sampleBaseDir+"PATtuple_36_1_hgW.root",
sampleBaseDir+"PATtuple_37_1_wVb.root",
sampleBaseDir+"PATtuple_38_1_C3w.root",
sampleBaseDir+"PATtuple_3_1_q56.root",
sampleBaseDir+"PATtuple_40_1_YwH.root",
sampleBaseDir+"PATtuple_41_1_JLv.root",
sampleBaseDir+"PATtuple_42_1_J6r.root",
sampleBaseDir+"PATtuple_43_1_9iH.root",
sampleBaseDir+"PATtuple_44_1_gaC.root",
sampleBaseDir+"PATtuple_45_1_btw.root",
sampleBaseDir+"PATtuple_46_1_vjA.root",
sampleBaseDir+"PATtuple_47_1_xrD.root",
sampleBaseDir+"PATtuple_48_1_kVK.root",
sampleBaseDir+"PATtuple_49_1_A7b.root",
sampleBaseDir+"PATtuple_4_1_s24.root",
sampleBaseDir+"PATtuple_50_1_KxU.root",
sampleBaseDir+"PATtuple_51_1_Rht.root",
sampleBaseDir+"PATtuple_5_1_ZUW.root",
sampleBaseDir+"PATtuple_6_1_a4W.root",
sampleBaseDir+"PATtuple_7_1_v9I.root",
sampleBaseDir+"PATtuple_8_2_Sw4.root",
sampleBaseDir+"PATtuple_9_1_Rcj.root",
]
