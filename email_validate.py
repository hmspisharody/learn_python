import re

def email_validate(email_id):
    pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w]+)+"
    valid_id = re.match(pattern, email_id)
    if valid_id:
        print("'" + email_id + "' is a valid e-mail id")
    else:
        print("'" + email_id + "' is not a valid e-mail id")

email_id = input("Enter your email id : ")
email_validate(email_id)
