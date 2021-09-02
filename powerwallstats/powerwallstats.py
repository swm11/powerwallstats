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
                
    def meters(self):
        # get agrigated meter readings
        # returns a dict containing all of the meter information
        return self.__get__("https://"+self.powerwallip+"/api/meters/aggregates")

    def battery_level(self):
        # get battery charge level
        energy = self.__get__("https://"+self.powerwallip+"/api/system_status/soe")
        return energy["percentage"]

    def operation(self):
        # get the operating mode and battery precentage as a dict.  Example:
        # {'real_mode': 'self_consumption', 'backup_reserve_percent': 14.5, 'freq_shift_load_shed_soe': 75, 'freq_shift_load_shed_delta_f': -0.32}
        # note: backup_reserve_percent:
        #  On APP    On Powerwall
        #    5%  
        #   10%      14.5%
        #   20%      24%
        #   30%      33.5%
        #   40%      
        return self.__get__("https://"+self.powerwallip+"/api/operation")

    def grid_faults(self):
        # get grid fault information
        return self.__get__("https://"+self.powerwallip+"/api/system_status/grid_faults")

class PowerwallstatsException(Exception):
    pass
