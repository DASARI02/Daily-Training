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