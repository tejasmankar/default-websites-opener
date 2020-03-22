import webbrowser

#Enter the name of the browser to open
browser_name = 'chrome'

#Enter the URLs of the websites which should be opened by default in the file 'Websites_List.txt' 

#Enter the path containing the .exe file of the selected browser
browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

#Register the web browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))

#Open the URLs read from the input file in separate tabs in the selected browser
with open('Websites_List.txt') as file:
    for url in file:
        webbrowser.get(browser_name).open_new_tab(url)
