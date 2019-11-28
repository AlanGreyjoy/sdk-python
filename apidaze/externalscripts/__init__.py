from apidaze.http import Http, HttpMethodEnum


class Externalscripts(object):
    """
        Initializes the Externalscripts class

        Parameters
        ----------
        http: Http
            Apidaze Http object

        Returns
        -------
        object
            The Apidaze Externalscripts object
    """
    def __init__(self, http: Http):
        self.http = http
        self.endpoint = '/externalscripts'

    def list(self):
        """
            Shows external scripts list

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=self.endpoint,
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result

    def get(self, id: int):
        """
            Shows specific external script by id

            Parameters
            ----------
            id: int
                id of external script

            Returns
            -------
            dict
                JSON response
        """
        response = self.http.request(
            method=HttpMethodEnum.GET,
            endpoint=f'{self.endpoint}/{id}',
            payload={}
            )

        result = {
            'body': response.json(),
            'status_code': response.status_code
        }

        return result