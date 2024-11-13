#Take input from the user and print the dictionary for Task and their Data. If user input is 0, then it will print a different dictionary that has a failed status.
#If the number is other than 0, then print the dictionary having its data as the multiples of the user input





def presentation(number):
    temp_dict ={
            "statuscode" : -1,
            "statusmessage" : "Failed",
            "data" : None
        }
    if number :
        temp_dict["statuscode"] = 1
        temp_dict["statusmessage"] = "Sussessfull"
        temp_dict["data"] = [number*i for i in range(1,6)]
 
    return temp_dict
       
       
def start():
    result = presentation(1)
    if result["statuscode"]:
        print(f"statusCode : {result["statuscode"]}, status_message : {result["statusmessage"]}, data : {result["data"]}")
    else :
        print(f"statusCode : {result["statuscode"]}, status_message : {result["statusmessage"]}, data : {result["data"]}")
   
start()