from models.account import Account

def fetch_accounts():
    accounts = Account.query.all()
    return accounts