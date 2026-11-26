# ==========================================
# 1. Dictionary methods
# ==========================================

user_details = {
    "user_id":"1234@abc",
    "user_name":"alex",
    "account_name":"self.__alex",
    "account_created":"20-12-2012",
    "account_based":"Washington",
    "is_active":True,
    "login_status":{
        "first_login":"20-12-2012",
        "last_login":"26-11-2026",
        "login_hour":8
    },
    "activity_status":{
        "content_posted":20,
        "reels":15,
        "photos":5,
        "changed_name":5,
        "links":1,
        "reshared":100,
        "tagged":6,
        "searched":15
    }
}

print(user_details.keys())                              # prints keys
print(user_details.values())                            # print values
print(user_details.get("login_hour"))                   # gets specific value of a key
print(user_details["login_status"].get("first_login"))  
user_details.update({                                   # updates the dictionary [ add new item[key:value]]
    "account_invalid":False
})
user_details.pop("activity_status")                     # removes specific key
print(user_details)                                     
user_details.popitem()                                  # removes the last key, value
print(user_details)                                     
print(user_details.items())                             # prints items
copied = user_details.copy()                            # copies the dictionary
print(copied)                                   
user_details.clear()                                    # clear all the key value inside the dictionary``