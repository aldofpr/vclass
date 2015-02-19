import py7zlib
from abc import ABCMeta, abstractmethod


class Processor:
  
  
  def deleteContent(self,pfile):
    pfile.seek(0)
    pfile.truncate()
  
  @abstractmethod
  def extractFeaturesFromText(self,fileText,fileName):
    pass
  
  def getFeaturesFromFile(self,archive,fileName,reportFile):
    fileText = archive.getmember(fileName).read()
    reportFile.write(fileName + " ")
    features = self.extractFeaturesFromText(fileText,fileName)
    for feature in features:
      reportFile.write(str(feature) + " ")
    reportFile.write("\n")
    
  def processAllFiles(self,firstFileName,archive):
    """Process all files of the 7z starting by the file with name 
    firstFileName, this is convenient if we want to resume a process that 
    was interrupted from the last file processed

    Keyword arguments:
    firstFileName -- the name of the file from where we start processing.
    If this is "" we start from the beginning
    archive -- the object representing the set of files
    """
    fileNames = archive.getnames()
    reportFile = open(self.featureSetName.replace(" ", "")+".txt", "a")
    self.deleteContent(reportFile)
    if firstFileName=="":
      firstFileIndex = 0
    else:
      firstFileIndex = archive.index(firstFileName)
    for i in range (firstFileIndex,len(fileNames)):
      fileName = archive.getnames()[i]
      self.getFeaturesFromFile(archive,fileName,reportFile)
      
  def run(self):
    filepath= "dataSample.7z"
    fp = open(filepath, 'rb')
    archive = py7zlib.Archive7z(fp)
    self.processAllFiles("",archive)
  
    
    