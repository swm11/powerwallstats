#!/usr/bin/env python3

from powerwallstats import powerwallstats
import time

powerwallip = 'Your Powerwall IP address goes here'
customer_email = 'Your customer email address goes here (the one to login to your powerwall)'
customer_password = 'Your customer password goes here (the one to login to your powerwall)'

def main():
	# instantiate a powerwallstats object and provide credentails:
	pw = powerwallstats(powerwallip, customer_email, customer_password)

	# power source names:
	source_names = ['battery', # battery power, where positive is discharging
					'site',    # grid power, where positive is import
					'load',    # house power consumption, always positive
					'solar']   # solar power, where positive is solar energy provided  

	# read some values
	while True:
		print("battery level: %d%%" % (pw.battery_level()))
		meters = pw.meters()
		for src in source_names:
			print("%s %5.3f kW" % (src, float(meters[src]['instant_power'])/1000.0))
		print()
		time.sleep(1)

if __name__ == "__main__":
    main()

