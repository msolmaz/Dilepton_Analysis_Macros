import os

samples = [
           # Standard Background MC
           "DYJets10",
           "DYJets50",
           "TTJets_FullLept",
           "WZ",
           "WW",
           "ZZ",
           "QCDmu15",
           "QCDmu20",
           "WJetsToLNu",
	   # "QCD_Pt_50to80",
	   # "QCD_Pt_80_170",
	   # "QCD_Pt_170to300",
           # Extra Background MC
           # "QCD_Pt_20_30_BCtoE",
	   # "QCD_Pt_30_80_BCtoE",
	   # "QCD_Pt_80_170_BCtoE",
	   # "QCD_Pt_170_250_BCtoE",
	   # "QCD_Pt_250_350_BCtoE",
	   # "QCD_Pt_350_BCtoE",
	   # "QCD_Pt_1000to1400",
           # "QCD_pt15to30_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6",
           # "QCD_pt30to50_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6",
           # "QCD_pt50to150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6",
           # "QCD_pt150_bEnriched_MuEnrichedPt14_TuneZ2star_8TeV_pythia6",
           # Signal MC
           # "LongLivedTo2F_M_50_CTau350",
           "HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500",
           "HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000",
           "HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150",
           "HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400",
           "HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000",
           "HTo2LongLivedTo4F_MH200_MFF20_CTau7To700",
           "HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000",
           "HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000",
           "HTo2LongLivedTo4F_MH400_MFF20_CTau4To400",
           "HTo2LongLivedTo4F_MH400_MFF50_CTau8To800",
           "HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300",
           "Chi0ToNuLL_MSquark120_MChi48",
           "Chi0ToNuLL_MSquark1000_MChi148",
           "Chi0ToNuLL_MSquark1500_MChi494",
           "Chi0ToNuLL_MSquark350_MChi148",
           # "Data_Photon_Run2012A22Jan",
           # "Data_Photon_Run2012B22Jan",
           # "Data_Photon_Run2012C22Jan",
           # "Data_Photon_Run2012D22Jan",
           "Data_Mu_Run2012A22Jan",
           "Data_Mu_Run2012B22Jan",
           "Data_Mu_Run2012C22Jan",
           "Data_Mu_Run2012D22Jan",
           "HTo2LongLivedTo4F_MH1000_MFF350_CTau3500To3500000"
#           "Data_Mu_Run2011A12Oct",
#           "Data_Mu_Run2011B12Oct"
           ]

for sample in samples:
    os.system("python MakePatTuple/MakePatTuple/test/run_pat.py SampleFiles/Samples/python/"+sample+"_cff.py 0")
    # os.system("crab -create -cfg /uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/"+sample+"_pat_20140624/crab.cfg")
    # os.system("crab -submit 1-499 -c /uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/"+sample+"_pat_20140624/crabDir/")
    # os.system("crab -submit 500-999 -c /uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/"+sample+"_pat_20140624/crabDir/")
    # os.system("crab -submit 1000-1499 -c /uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/"+sample+"_pat_20140624/crabDir/")
    # os.system("crab -status -c /uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/"+sample+"_pat_20140624/crabDir/")
    # os.system("python MakePatTuple/MakePatTuple/test/run_postGrid.py workdirs/"+sample+"_pat_20140624/ /eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/"+sample+"_pat_20140624/zhenhu/ 0")
    # print "python MakePatTuple/MakePatTuple/test/run_postGrid.py workdirs/"+sample+"_pat_20140327/ /eos/uscms/store/user/lpcdve/noreplica/DisplacedLeptons/"+sample+"_pat_20140327/demattia/ 0"
