import os,sys

def combineFiles( type, puFiles ):
    
    command = "hadd -f ../PileupFiles/pileup_"+type+".root "
    
    for file in puFiles:
        command += file+" "
        pass
    
    print "Running command :",command
    os.system(command)
    pass

def checkFileExists( file ):
    if not os.path.exists(file) :
        print "File :",file,"does not exist"
        sys.exit(1)
        pass

def getLumi( lumiFile ):
    openFile = open(lumiFile, "r")
    lumiLines = openFile.readlines()
    openFile.close()
    for line in lumiLines:
        if line.find("Recorded Lumi")>=0 :
            return float( line.split(":")[-1].strip() ) / 1000000
            pass
        pass
    
    print "ERROR : did not find recorded lumi in",lumiFile
    sys.exit(1)
    
def writeLumi( type, lumi ):
    outputFile = open("../LumiFiles/lumi_"+type+".txt","w")
    outputFile.write(str(lumi))
    outputFile.close()
    pass


#===============================================================================
# Read FilesAndWeights.h and work out which data periods I am running on
#===============================================================================
# Find original FilesAndWeights.h
originalFile=open("../CommonMacros/FilesAndWeights.h","r")
originalFileLines=originalFile.readlines()
originalFile.close()

muonFiles = []
muonP5Files = []
muonM5Files = []
electronFiles = []
electronP5Files = []
electronM5Files = []

muonFiles_12Oct = []
muonP5Files_12Oct = []
muonM5Files_12Oct = []
electronFiles_12Oct = []
electronP5Files_12Oct = []
electronM5Files_12Oct = []

muonLumi = 0
electronLumi = 0
muonLumi_12Oct = 0
electronLumi_12Oct = 0

for line in originalFileLines:
    # Look for data lines
    if line.find("Data")>=0:
        # Not interested if commented out
        firstPart=line.split("fw")[0]
        if firstPart.find("//")>=0: continue
     
        sampleName = ( line.split("_analysis")[0] ).split("/")[-1]
        puFile = "../PileupFiles/pileup_"+sampleName+".root"
        puP5File = "../PileupFiles/pileup_p5_"+sampleName+".root"
        puM5File = "../PileupFiles/pileup_m5_"+sampleName+".root"
        lumiFile = "../LumiFiles/lumi_"+sampleName+".txt"

        # Check files exist
        checkFileExists(puFile)
        checkFileExists(puP5File)
        checkFileExists(puM5File)
        checkFileExists(lumiFile)
        
        # Is this electrons or muons?
        if sampleName.find("Mu")>=0:
            # Muons
            print "Found muon data sample being considered :",sampleName
            if sampleName.find('12Oct')>=0:
                muonFiles_12Oct.append(puFile)
                muonP5Files_12Oct.append(puP5File)
                muonM5Files_12Oct.append(puM5File)
                muonLumi_12Oct += getLumi(lumiFile)
                pass
            else :
                muonFiles.append(puFile)
                muonP5Files.append(puP5File)
                muonM5Files.append(puM5File)
                # get lumi
                muonLumi += getLumi( lumiFile )
            pass
        elif sampleName.find("Photon")>=0:
            # Photons
            print "Found photon data sample being considered :",sampleName
            if sampleName.find('12Oct')>=0:
                electronFiles_12Oct.append(puFile)
                electronP5Files_12Oct.append(puP5File)
                electronM5Files_12Oct.append(puM5File)
                electronLumi_12Oct += getLumi( lumiFile )
                pass
            else:
                electronFiles.append(puFile)
                electronP5Files.append(puP5File)
                electronM5Files.append(puM5File)
                
                # get lumi
                electronLumi += getLumi( lumiFile )
                pass
            pass
        else : 
            print "Unkown Data type ??? ",sampleName
            pass
        pass
    pass

#===============================================================================
# Combine pileup files so I have one pileup.root file for electrons/muons
#===============================================================================

combineFiles( "muon", muonFiles )
combineFiles( "muon_p5", muonP5Files )
combineFiles( "muon_m5", muonM5Files )
combineFiles( "electron", electronFiles )
combineFiles( "electron_p5", electronP5Files )
combineFiles( "electron_m5", electronM5Files )

combineFiles( "muon_12Oct", muonFiles_12Oct )
combineFiles( "muon_p5_12Oct", muonP5Files_12Oct )
combineFiles( "muon_m5_12Oct", muonM5Files_12Oct )
combineFiles( "electron_12Oct", electronFiles_12Oct )
combineFiles( "electron_p5_12Oct", electronP5Files_12Oct )
combineFiles( "electron_m5_12Oct", electronM5Files_12Oct )

#===============================================================================
# Record total lumi for each channel
#===============================================================================

writeLumi( "muon", muonLumi )
writeLumi( "electron", electronLumi )

writeLumi( "muon_12Oct", muonLumi_12Oct )
writeLumi( "electron_12Oct", electronLumi_12Oct )

print "Total muon lumi :",muonLumi,"/pb"
print "Total electron lumi :",electronLumi,"/pb"
print "---- 12Oct"
print "Total muon lumi :",muonLumi_12Oct,"/pb"
print "Total electron lumi :",electronLumi_12Oct,"/pb"
