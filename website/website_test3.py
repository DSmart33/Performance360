# Import the discord library
import requests
import mechanicalsoup

# Create stateful browser
browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
)

# Use browser to open link
browser.open('https://clients.mindbodyonline.com/asp/su1.asp?fl=true&tabID=2')

# verify url
print(browser.get_url())

# get first form available
form = browser.select_form('form[name="frmLogon"]')

# print summary for review
#form.print_summary()

# enter username and password into form
browser['requiredtxtUserName'] = '***REMOVED***'
browser['requiredtxtPassword'] = 'K[kJ4cPacjx9J%N&J^(A'

# # print another summary to validate input
# form.print_summary()

# # submit form
browser.submit_selected()

# # check current url to see if we are logged in
print(browser.get_url())

# Create the session
# with requests.session() as s:

#     s.headers.update({'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})

#     loginPage = s.get('https://clients.mindbodyonline.com/asp/su1.asp?fl=true&tabID=2')

#     soup=BeautifulSoup(loginPage.content, features="html.parser")

#     print(soup)

    

    # payload = {
    #     'requiredtxtUserName': '***REMOVED***',
    #     'requiredtxtPassword': 'K[kJ4cPacjx9J%N&J^(A',
    #     'tg': '',
    #     'vt': '',
    #     'lvl': '',
    #     'stype': '',
    #     'qParam': '',
    #     'view': '',
    #     'trn': '0',
    #     'page': '',
    #     'catid': '',
    #     'prodid': '',
    #     'date': '2/9/2021',
    #     'classid': '0',
    #     'sSU': '',
    #     'optForwardingLink': '',
    #     'isAsync': 'false'
    # }

    # login = s.post('https://clients.mindbodyonline.com/Login?studioID=16575&isLibAsync=true&isJson=true', data = payload)
    # print(login)
    # print(login.content)

    # classes = s.get('https://clients.mindbodyonline.com/classic/mainclass?fl=true&tabID=7')

    # print(classes)
    #print(classes.content)