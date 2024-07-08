from repositories import user as user_repositories
from repositories import account as account_repositories 

def fetch_all():
    users = user_repositories.fetch_users()
    # users = [user.obj_to_dict() for user in users]
    for user in users:
        print(user.email)
        for account in user.accounts:
            print(account.account_type)
    return users

def fetch_user_by_id():
    user_id = 1
    user = user_repositories.fetch_user(user_id)
    print("User: ", user.accounts)
    return None

def fetch_user_account():
    return True