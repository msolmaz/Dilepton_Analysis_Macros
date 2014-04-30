import os,sys

# For each sample cff file, this script will remove any duplicate PATfiles
# e.g. if PATtuple_39_1_Sif.root and PATtuple_39_2_TQf.root exist on the storage element at the same directory
# This may mean that crab aborted/failed on job 39 but most of the output file made it back to the SE
# After resubmitting and succeeding it produced another (larger) PAT file on the SE
# Need to remove these from being inputted to the TreeProducer to avoid double counting
# Also messes up lumiCalc as crab is not aware of these extra jobs being put into Tree Producer!

# Note: Above is a guess, but removing these extra files improved the agreement between data and MC in control plots

dir="/uscms_data/d3/demattia/DisplacedLeptons/CMSSW_5_3_8/src/SampleFiles/Samples/python/"

sampleCffFiles=[# "Data_Photon_Run2012A1_cff.py"
    "DYJets10_cff.py",
    "DYJets50_cff.py",
    "QCDem170_cff.py",
    "QCDem20_cff.py",
    "QCDem250_cff.py",
    "QCDem30_cff.py",
    "QCDem350_cff.py",
    "QCDem80_cff.py",
    "QCDmu15_cff.py",
    "QCDmu20_cff.py",
    "TTJets_FullLept_cff.py",
    "WW_cff.py",
    "WZ_cff.py",
    "ZZ_cff.py",
    "WJetsToLNu_cff.py",
    "HTo2LongLivedTo4F_MH1000_MFF350_CTau35To3500_cff.py",
    "HTo2LongLivedTo4F_MH1000_MFF50_CTau4To400_cff.py",
    "Chi0ToNuLL_MSquark350_MChi148_cff.py",
    "Chi0ToNuLL_MSquark120_MChi48_cff.py",
    "Chi0ToNuLL_MSquark1000_MChi148_cff.py",
    "Chi0ToNuLL_MSquark1500_MChi494_cff.py",
    "HTo2LongLivedTo4F_MH400_MFF50_CTau8To800_cff.py",
    "HTo2LongLivedTo4F_MH400_MFF150_CTau40To4000_cff.py",
    "HTo2LongLivedTo4F_MH400_MFF20_CTau4To400_cff.py",
    "HTo2LongLivedTo4F_MH200_MFF50_CTau20To2000_cff.py",
    "HTo2LongLivedTo4F_MH200_MFF20_CTau7To700_cff.py",
    "HTo2LongLivedTo4F_MH1000_MFF20_CTau1p5To150_cff.py",
    "HTo2LongLivedTo4F_MH1000_MFF150_CTau10To1000_cff.py",
    "HTo2LongLivedTo4F_MH125_MFF50_CTau50To5000_cff.py",
    "HTo2LongLivedTo4F_MH125_MFF20_CTau13To1300_cff.py",
    "HTo2LongLivedTo4F_MH1000_MFF350_CTau3500To3500000_cff.py",
    "Data_Mu_Run2012A22Jan_cff.py",
    "Data_Mu_Run2012B22Jan_cff.py",
    "Data_Mu_Run2012C22Jan_cff.py",
    "Data_Mu_Run2012D22Jan_cff.py",
]

for sample in sampleCffFiles:
    
    sampleCffFile=dir+sample
    
    # Read original file
    originalCff=open(sampleCffFile,"r")
    originalCffLines=originalCff.readlines()
    originalCff.close()
    
    # New file for output
    newCff=open(sampleCffFile+".new","w")
    
    # List of PAT file numbers
    PATfileNumbers=[]
    
    seen=[]
    duplicates=[]
    
    cleanedPATList=[]
    
    # Get list of PAT files
    for line in originalCffLines:
        if line.find('sampleBaseDir+"PATtuple_')>=0:
            # Store number of PAT files
            n = line.split('"')[1].split('_')[1]
#            print line,n
            if n not in seen:
                seen.append(n)
                cleanedPATList.append(line)
                pass
            else : duplicates.append(int(n))
            pass
        elif( line.find(']') >= 0 ) : continue
        else:
            newCff.write(line)
        pass
    
    # Got list of PAT duplicate numbers
    duplicates.sort()
    seen.sort()
    print duplicates
    print len(duplicates)
    
    for line in cleanedPATList:
        newCff.write(line)
#        print line.strip()
        pass
    
    newCff.write("]")
    newCff.close()
    
    # Move files around
    os.system("mv "+sampleCffFile+" "+sampleCffFile+".old;")
    os.system("mv "+sampleCffFile+".new "+sampleCffFile+";")
    

