from requests import Session
from uuid import uuid4

# Register is a mess, they using Email/Number verification and Captcha, so this module only for login purpose.
# They tracking user analytic data on login, so I added a function to simulate that behavior.
# All for educational purpose only.
# Please don't use it for illegal activities and respect Paysafe's terms of service.

# -> Its using Paysafe Latest Mobile Api, reversed and ssl bypassed recently.


class Paysafe:
    """
    Paysafe class for handling authentication with the Paysafe payment platform.
    This class manages login credentials and provides methods for authenticating
    with the Paysafe API and sending analytics data.
    Attributes:
        __email__ (str): The user's email address for authentication.
        __password__ (str): The user's password for authentication.
        request (Session): A requests Session object for managing HTTP connections.
        api_url (str): The Paysafe login API endpoint URL.
        headers (dict): Default HTTP headers for API requests including authentication
                        credentials and device information.
    Methods:
        __init__(email: str, password: str) -> None:
            Initializes the Paysafe instance with user credentials and sets up
            the HTTP session with appropriate headers.
        __analytic__() -> dict:
            Sends analytics data to the Paysafe Marketing Cloud APIs and returns
            the response as a dictionary.
        login() -> str:
            Attempts to authenticate the user with the Paysafe API and returns
            either the response message or an error message.
    """

    def __init__(self, email: str, password: str):
        self.__email__ = email
        self.__password__ = password
        self.request = Session()
        self.api_url = "https://login.paysafecard.com/auth/rest/login?client_id=mobileApp&clientApplicationKey=D4hqzBREaa349sIlNvtipsD2MoYkzXeF"
        self.headers = {
            "threatmetrixidentifier": "tib42vd0lu36dcfw0fi9d9chesk9vsjk",
            "username": self.__email__,
            "password": self.__password__,
            "devicepublicid": "a17b83b2-3eac-46af-9ae1-b7d9612e1c9a",
            "user-agent": "paysafecard/25.24.2 (SM-N975F; Android 9; okhttp/5.3.2)",
            "accept": "application/json",
            "accept-language": "en-DE",
            "content-type": "application/json; charset=UTF-8",
            "accept-encoding": "gzip",
        }

    def __analytic__(self) -> dict:
        "Ignore this function"
        payload = [
            {
                "etAppId": "0b47822b-379c-4d2b-be8f-42fd7f4472f7",
                "deviceId": "3f825a59-4b63-4f0c-b943-91249945797e",
                "eventDate": "2026-01-15T15:27:59.067Z",
                "value": 37,
                "analyticTypes": [4],
                "objectIds": [],
                "uuid": str(uuid4()),
                "propertyBag": {"platform": "Android"},
            }
        ]

        headers = {
            "user-agent": "MarketingCloudSdk/9.0.3 (Android 9; en_DE; samsung/SM-N975F) at.paysafecard.android/25.24.2",
            "authorization": "Bearer d7wnry345g76s562kn6pnjhw",
            "accept": "application/json",
            "x-sdk-version": "9.0.3",
            "content-type": "application/json",
            "host": "mcffg48yszjybhmnhttcmf9b-jl4.device.marketingcloudapis.com",
            "connection": "Keep-Alive",
            "accept-encoding": "gzip",
        }

        return self.request.post(
            "https://mcffg48yszjybhmnhttcmf9b-jl4.device.marketingcloudapis.com/device/v1/event/analytic",
            json=payload,
            headers=headers,
        ).json()

    def login(self) -> str:
        for _ in range(2):
            return self.__analytic__()
        try:
            response = self.request.post(
                self.api_url,
                json={},
                headers=self.headers,
            ).json()
            return response["message"]
        except Exception as e:
            return f"An error occurred: {e}"


if __name__ == "__main__":
    email = input("Enter your Paysafe email: ")
    password = input("Enter your Paysafe password: ")
    paysafe = Paysafe(email, password)
    result = paysafe.login()
    print(result)
