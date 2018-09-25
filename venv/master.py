# Colin Goodman - 2018
# Information propagation in social media networks

import tweepy

# tweepy stuff
auth = tweepy.OAuthHandler('0oG3gXlR17hHDfrmK5ICkR6nV', '2oOe6SxCaBgNz7PTtwriSTVj5Vx6lkZdoAkb4nM0BpEtZl0BOz')
auth.set_access_token('247468435-MM16zZOkuNPIL7qE7aNRfWDs3YRx3VSmV0xWKSed', '5Bx6AbxFUdv6zh0xMU9BAwKhBuhOq0fR8inNme6MK7bVx')
api = tweepy.API(auth)