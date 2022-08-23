from token_manager import *

session, token_info = get_oauth_session(gen_token=False)
print(session)
print(token_info)