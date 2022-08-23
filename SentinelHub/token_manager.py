from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os
import pickle

# TODO: Check expiry and refresh, when reusing token

CLIENT_NAME = "satvision-test"
CLIENT_PATH = f".client_{CLIENT_NAME}"

SECRET_FILEPATH = os.path.join(CLIENT_PATH, '.secret')
ID_FILEPATH = os.path.join(CLIENT_PATH, '.id')
TOKEN_FILEPATH = os.path.join(CLIENT_PATH, '.token')
TOKENOBJ_FILEPATH = os.path.join(CLIENT_PATH, '.tokenobj')


def get_oauth_session(gen_token=False):

    def sentinelhub_compliance_hook(response):
        response.raise_for_status()
        return response

    # client credentials
    client_id = open(ID_FILEPATH, 'r').read()
    client_secret = open(SECRET_FILEPATH, 'r').read()

    # Create a session
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)

    # Get token for the session
    if gen_token:
        token = oauth.fetch_token(token_url='https://services.sentinel-hub.com/oauth/token',
                                client_secret=client_secret)
        # save token to file
        if token.get('access_token'):
            open(TOKEN_FILEPATH, "w").write(token.get('access_token'))
            pickle.dump(token, open(TOKENOBJ_FILEPATH, "wb")) 

    else:
        oauth = OAuth2Session(
            client = client,
            token = pickle.load(open(TOKENOBJ_FILEPATH, 'rb'))
        )

    # All requests using this session will have an access token automatically added
    resp = oauth.get("https://services.sentinel-hub.com/oauth/tokeninfo")
    token_info = resp.content

    oauth.register_compliance_hook("access_token_response", sentinelhub_compliance_hook)
    return oauth, token_info