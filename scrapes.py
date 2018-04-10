import requests #to load page
import time #need time tools to delay requests
import smtplib #email stuff....to paging?

#set an initial variable to empty, load the current data into the variable
#on each iteration, compare new request data to the variable
#if it's new....send a page
foo = ""
# while this is true (it is true by default),
while True:
    # set the url 
    url = "http://electionresults.stlouisco.com/el180403/EL45.HTM"
    # set some headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    # retrieve the url
    response = requests.get(url, headers=headers)

    #text at the beginning of your data block to search
    seekme = "MAYOR WEBSTER GROVES"
    bar = response.text.index(seekme)
    
    #I used 300 because I needed 300 characters beyond my index string set above
    if response.text[bar:bar+300] != foo:
        print(response.text[bar:bar+300])
        foo = response.text[bar:bar+300]
    
        # create a message 
        msg = " ".join(foo.split())
        # set the 'from' address
        fromaddr = 'user@host.com'
        # set the 'to' addresses, I used the email to SMS address for my cell
        toaddrs  = ['anotheruser@host.net']
        # set the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # credentials go here...
        server.login("yourcreds@host.com", "Passwords")
        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

    time.sleep(30) #however long you want to wait
    print("Script ran...")

