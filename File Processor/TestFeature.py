from FileProcessor import Processor

class TestFeature(Processor):
  """Each feature extractor should implement the class Processor and 
  particularly the abstract method "obtainFeaturesFromText". This kind of 
  class should contain a main method calling the run method of Processor
  """
  
  def main(self):
    self.configureFeatureSet()
    Processor.run(self)
  
  
  def configureFeatureSet(self):
    self.featureSetName = "Test Feature"


  def extractFeaturesFromText(self,fileText,fileName):
    """The principal method of a feature extractor. It receives the plain
    text of a virus file and returns a list with the values of the features.

    Keyword arguments:
    fileText -- the plain text of a virus file.
    fileName -- the name of the file containing the text.
    Return arguments:
    features -- a list with the values of the extracted features
    """
    featureList = list()
    
    """WRITE THE CODE HERE"""
    
    fileNameExtension = fileName.split(".")[1]
    if fileNameExtension=="asm":
      featureList.append(fileText.count("("))
      featureList.append(fileText.count(")"))
    else:
      featureList.append(0)
      featureList.append(0)
    return featureList

  
if __name__ == "__main__":
  testFeature = TestFeature()
  testFeature.main()