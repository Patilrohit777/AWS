import boto3
from datetime import datetime
import pytz
from datetime import datetime
from dateutil import parser
print("")
print("")
print("")
print("========================================================")
print("--------------------------------------------------------")
print("========================================================")

client = boto3.client('iam')


list_of_users = client.list_users()

list_of_all_users_data = list_of_users["Users"]

for user_data_dict in list_of_all_users_data:
    UserName = user_data_dict["UserName"]
    UserId = user_data_dict["UserId"]
    
    print("UserName","-->",UserName, "====>","UserId","-->",UserId)
    print("========================================================")
    print("")