from apidaze.http import Http
from apidaze.messages import Messages
from apidaze.misc import Miscellaneous
from apidaze.calls import Calls
from apidaze.recordings import Recordings
from apidaze.cdrhandlers import Cdrhandlers


class Client(object):
    """
        Initializes the Apidaze Client class

        Parameters
        ----------
        api_key: str
            API key to use with
        api_secret: str
            API secret to authenticate with

        Returns
        -------
        object
            Apidaze Client object
    """
    def __init__(self, api_key: str = None, api_secret: str = None):
        self.api_key = api_key
        self.api_secret = api_secret

        if not self.api_key or not self.api_secret:
            raise ValueError('api_key and api_secret must be provided')

        # Http request
        self.http = Http(api_key=self.api_key, api_secret=self.api_secret)

        # Domains
        self.messages = Messages(http=self.http)
        self.external_scripts = None
        self.calls = Calls(http=self.http)
        self.cdr_handlers = Cdrhandlers(http=self.http)
        self.recordings = Recordings(http=self.http)
        self.misc = Miscellaneous(http=self.http)
