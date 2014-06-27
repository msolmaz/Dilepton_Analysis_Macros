#ifndef FILESANDWEIGHTS_H
#define FILESANDWEIGHTS_H

#include <map>
#include <TString.h>

std::map<TString, double> filesAndWeightsMap( bool electrons )
{
  // The weights are the cross sections in pb. The number of processed events is read from a histograms in the tree root file.
  // Give data a weight of -1, so we know it is data

  // Files and weights map
  std::map<TString, double> fw;

  // Signal

  //  // mH = 1000 GeV

  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_analysis_20140618"] = 1.0 ;

  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_analysis_20140618"] = 1.0;

//
//  // mH = 400 GeV
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF50_CTau8To800_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH400_MFF20_CTau4To400_analysis_20140618"] = 1.0;
//
//  // mH = 200 GeV
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH200_MFF20_CTau7To700_analysis_20140618"] = 1.0;
//
//  // mH = 125 GeV
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_analysis_20140618"] = 1.0;

//
//  // Chi0
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1500_MChi494_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark1000_MChi148_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark350_MChi148_analysis_20140618"] = 1.0;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Chi0ToNuLL_MSquark120_MChi48_analysis_20140618"] = 1.0;



  // Vector bosons

  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/ZZ_analysis_20140618"] = 17.6;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/WZ_analysis_20140618"] = 33.2;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/WW_analysis_20140618"] = 54.8;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/WJetsToLNu_analysis_20140618"] = 36257.2;


  // TTbar

  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/TTJets_FullLept_analysis_20140618"] = 24.77;

  // DY JETS
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/DYJets10_analysis_20140618"] = 12471;
  fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/DYJets50_analysis_20140618"] = 3503.7;


  if (!electrons)
  {
    // QCD mu
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/QCDmu15_analysis_20140618"] = 2738580.0;
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/QCDmu20_analysis_20140618"] = 134680.0;


    // Data
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012A22Jan_analysis_20140618"] = -1;
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012B22Jan_analysis_20140618"] = -1;
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012C22Jan_analysis_20140618"] = -1;
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2012D22Jan_analysis_20140618"] = -1;
    // Data2011
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2011A12Oct_analysis_20140624"] = -1;
    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/Data_Mu_Run2011B12Oct_analysis_20140624"] = -1;
	
//Cosmics

//    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/cosmicsRunA_analysis_20140603"] = -1;
//    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/cosmicsRunB_analysis_20140603"] = -1;
//    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/cosmicsRunC_analysis_20140603"] = -1;

      
//    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_186785_186996_analysis_20140618"] = -1;
//    fw["/uscmst1b_scratch/lpc1/lpcmuon/zhenhu/RefittedStandAloneMuons/CMSSW_5_3_8/src/workdirs/cosmicsCRAFT_187461_187468_and_187469_189146_analysis_20140618"] = -1;

  }
  else
  {
  }
  return fw;
}

#endif
