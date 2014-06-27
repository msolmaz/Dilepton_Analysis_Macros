from Data_Mu_Run2012D22Jan_cff import samplePatFiles

totFiles = 700

def findFileNum(i):
    for rootFile in samplePatFiles:
        fileNum = int(rootFile.split('_')[9])
        if fileNum == i:
            return True
    return False


for i in range(1,totFiles+1):
    if not findFileNum(i):
        print "missing file:", i
