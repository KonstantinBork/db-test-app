import graphene
import tokens

debug = True

def get_token():
    if debug:
        return tokens.DB_APP_TOKEN_SANDBOX
    else:
        return tokens.DB_APP_TOKEN_PRODUCTION

token = get_token()

def test_token():
    print(token)

def main():
    test_token()

main()
