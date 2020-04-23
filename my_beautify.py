import os

 #prints start of execution of function
def fname_print(message):  # function name print
    print("===============================================")
    print("Executing {}:".format(message))


def log_print(message=None,variable_name=None,variable=None,log_flag=1):  # log print
	if log_flag ==1:
		if message ==None:	
			print("log: Variable output for {0}: {1}".format(variable_name,variable))
		elif variable_name == None:
			print("log: {0}".format(message))
		else:
			print("log: {0}: Variable output for {1}: {2}".format(message,variable_name,variable))

