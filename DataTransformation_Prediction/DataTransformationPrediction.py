

# =============================================================================
# # ---------------------------------------------------------------------------
# # Creation Date: 12-jan-2021
# # Author: Bibekananda Nayak
# # Version: 1.0
# #
# # ---------------------------------------------------------------------------#
# =============================================================================


from datetime import datetime
from os import listdir
import pandas
from application_logging.logger import App_Logger


class dataTransformPredict:



     def __init__(self):
          self.goodDataPath = "Prediction_Raw_Files_Validated/Good_Raw"
          self.logger = App_Logger()


     def addQuotesToStringValuesInColumn(self):


          try:
               log_file = open("Prediction_Logs/dataTransformLog.txt", 'a+')
               onlyfiles = [f for f in listdir(self.goodDataPath)]
               for file in onlyfiles:
                    data = pandas.read_csv(self.goodDataPath + "/" + file)

                    data['DATE'] = data["DATE"].apply(lambda x: "'" + str(x) + "'")


                    data.to_csv(self.goodDataPath + "/" + file, index=None, header=True)
                    self.logger.log(log_file, " %s: Quotes added successfully!!" % file)

          except Exception as e:
               log_file = open("Prediction_Logs/dataTransformLog.txt", 'a+')
               self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
               #log_file.write("Current Date :: %s" %date +"\t" +"Current time:: %s" % current_time + "\t \t" + "Data Transformation failed because:: %s" % e + "\n")
               log_file.close()
               raise e
          log_file.close()