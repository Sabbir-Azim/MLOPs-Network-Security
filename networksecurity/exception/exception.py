import sys
import traceback
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys): # type: ignore
        super().__init__(str(error_message))
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno # type: ignore
        self.file_name=exc_tb.tb_frame.f_code.co_filename  # type: ignore
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        

        
