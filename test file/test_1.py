import webbrowser
text = ("search youtube")
a = text.lower().split().index('search')
b = text.split()[a + 1:]
c = ' '.join([str(elem) for elem in b]) 
  
print(c)
print('searching as new tab in webbrowser')
url = "https://www.google.com.tr/search?q={}".format(c)
webbrowser.open_new_tab(url)
