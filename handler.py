import requests
import msal
import constants
import logging

log=logging.getLogger(__name__)
log.setLevel(logging.INFO)

def post(url,headers,data):
    try:
        response=requests.post(url=url,headers=headers,data=data)
        response.raise_for_status
        return response
    except Exception as e:
        log.error(f"error in Http post request : {e}") 

def get_embed_url(filter_str=""):
    try:
        if filter_str:
            embed_url = f'{constants.BASE_URL}?reportId={constants.REPORT_ID}&groupId={constants.GROUP_ID}&filter={filter_str}'
        else:
            embed_url = f'{constants.BASE_URL}?reportId={constants.REPORT_ID}&groupId={constants.GROUP_ID}'
        return embed_url
    except Exception as e:
        log.error(f"error generating embed url: {e}")


def get_access_token():
    try:
        client = msal.PublicClientApplication(constants.APP_ID, authority=constants.AUTHORITY_URL)
        response= client.acquire_token_by_username_password(username=constants.USERNAME, password=constants.PASSWORD,scopes=constants.SCOPE)
        access_token= response.get("access_token")
        log.info(f"get_access_token: {response}")
        return access_token
    except Exception as e:
        log.error(f"error generating access token: {e}")
