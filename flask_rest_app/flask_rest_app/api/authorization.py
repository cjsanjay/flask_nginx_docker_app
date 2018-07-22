from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "password"
}

@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
