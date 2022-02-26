import pandas as pd
# =============================================================================
# # ---------------------------------------------------------------------------
# # Creation Date: 12-jan-2021
# # Author: Bibekananda Nayak
# # Version: 1.0
# # This class shall  be used for obtaining the data from the source for prediction.
# # ---------------------------------------------------------------------------#
# =============================================================================
class Data_Getter_Pred:

    def __init__(self, file_object, logger_object):
        self.prediction_file='Prediction_FileFromDB/InputFile.csv'
        self.file_object=file_object
        self.logger_object=logger_object

    def get_data(self):
        self.logger_object.log(self.file_object,'Entered the get_data method of the Data_Getter class')
        try:
            self.data= pd.read_csv(self.prediction_file) # reading the data file
            self.logger_object.log(self.file_object,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()


