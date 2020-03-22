import webbrowser

#Enter the name of the browser to open
browser_name = 'chrome'

#Enter the URLs of websites which should be opened by default
website_url_list = ['www.google.com','https://www.geeksforgeeks.org/','https://leetcode.com/']

#Enter the path containing the .exe file of the selected browser
browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#Register the web browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))

#Open the selected websites in separate tabs in the browser
for url in website_url_list:
    webbrowser.get(browser_name).open_new_tab(url)
