1) Runs the script every 31 to 47 minutes to try to add courses from your cart. Note: You should already have some courses in your Quest cart
2) Add your Quest email and password to line 19 and 24 respectively..
3) Also provide the path to your Chrome driver binary at line 12 i.e. /users/...../

Requirnments:
1) Python version  > 3.*
2) BeautifulSoup
3) Chrome driver (https://chromedriver.chromium.org/)

Debug:
If you are getting error related to chrome not found then try changing line number 10 with Google Chrome.app (or any other chrome executable you have)
