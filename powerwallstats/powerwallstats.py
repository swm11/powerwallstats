# powerwallstats is (c) Simon Moore 2021
# but distributed under the BSD 2-Clause License

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class powerwallstats:
    def __init__(self, powerwall_ip_address, customer_email, customer_password):
        self.powerwallip = powerwall_ip_address
        self.email = customer_email
        self.password = customer_password
        self.__login__()

    def __login__(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.session = requests.Session()
        response = self.session.post('https://'+self.powerwallip+'/api/login/Basic',
                                     json={'username': 'customer',
                                           'email': self.email,
                                           'password': self.password},
                                     verify=False)
        if(response.status_code != 200):
            raise PowerwallstatsException("Loging into the Powerwall failed with response: {c}".format(c=response.status_code))

    def __get__(self, url):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = self.session.get(url,verify=False)
        if(response.status_code != 200):
            # Error, so try logging in again and retry
            self.__login__()
            response = self.session.get(url,verify=False)
        if(response.status_code == 200):
            return response.json()
        else:
            raise PowerwallstatsException("Powerwallstats failed with response: {c}".format(c=response.status_code))
                
    def battery_level(self):
        # get battery charge level
        energy = self.__get__("https://"+self.powerwallip+"/api/system_status/soe")
        return energy["percentage"]

    def meters(self):
        # get agrigated meter readings
        # returns a dict containing all of the meter information
        return self.__get__("https://"+self.powerwallip+"/api/meters/aggregates")


class PowerwallstatsException(Exception):
    pass
