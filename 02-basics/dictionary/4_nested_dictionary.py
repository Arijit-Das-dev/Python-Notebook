# ==========================================
# 1. Nested Dictionary
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
print(user_details)
print(user_details["login_status"]["login_hour"])
print(user_details["activity_status"]["content_posted"])