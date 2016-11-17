#!/bin/python3
# Hi, these Raspberry Pi courses by Prof Harris
# are supposed to be using Python3, at least
# that is what is stated at the start of the course
# and in the Coursera docuemtation.
#
# So my script below is in Python3, not Python 2.
#
# If you want to run this script you will first
# need install the Twython library for Python 3:
#
#   sudo pip3 install twython
#           ^
#           ^
# Thanks for reviewing my assgnment :)
#
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    # prepare counter (as a class variable)
    count = 0
    def on_success(self, data):
        if 'text' in data:
            # increment the counter
            self.count = self.count + 1
            # have 3 or more matching tweets been received?
            if self.count >= 3:
                print("Ian G. Harris is popular!")

# get the private key values
exec(open("./initkeys.py").read())

# set up the streamer
stream = MyStreamer(c_k, c_s, a_t, a_s)

# set up the filter
stream.statuses.filter(track="Ian G. Harris")

