import requests
import getpass

import github_login
import github_observe
import facebook_message


if __name__ == '__main__':
    with requests.session() as session:
        github_login.signin(session, id=input('id: '), pw=getpass.getpass('password: '))
        facebook_client = facebook_message.login()
        print("Put 'quit' to quit the loop.")
        github_observe.get_new(session, facebook_client)