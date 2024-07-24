import sys 
import logging
from src.logger import logging

def error_msg_details(error, error_details:sys):
    error_details.exc_info() 
    '''The exc_info variable is a built-in Python object that contains information about the current exception being handled.return (type, vales, trackback)'''
    _,_,exc_trackback = error_details.exc_info()
    file_name = exc_trackback.tb_frame.f_code.co_filename
    line_number = exc_trackback.tb_lineno

    '''
    [exc_trackback] is the traceback object of the current exception, which is automatically passed to an exception handler.
    [tb_frame] is an attribute of the traceback object that contains a reference to the frame object where the exception occurred.
    [f_code] is an attribute of the frame object that contains the code object associated with the frame.
    [co_filename] is an attribute of the code object that contains the filename of the module that contains the code.
    '''
    error_msg = "oops... Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, str(error))

    return error_msg

class CustomException(Exception) :
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        '''
        This line calls the constructor of the parent class (Exception) and passes the error_message argument to it. This ensures that the error_message is stored in the exception instance.
        '''
        self.error_message = error_msg_details(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)