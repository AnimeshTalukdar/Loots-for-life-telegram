import os
import re
import time
CHANNEL = "Offerzone_Deals_Loots"

first_time = True
new_links = []
while True:
    arr = os.popen("curl https://t.me/s/" + CHANNEL).read()
    # print(arr)
    # find the regex ("https://amzn.to/*<a>")
    # amznlinks = re.findall("https://amzn.to/<a>", arr)
    # print(re.findall("<a[^>]*>https://amzn.to([^<]+)<\/a>", arr, re.DOTALL))

    amznlinks = re.findall("<b>Loot(?:(?!</a>).)*", arr)
    for link in amznlinks:
        actual_link = re.search(">https://amzn.to([^<]+)", link).group(0)[1:]
        if actual_link not in new_links:
            if not first_time:
                os.system("open " + actual_link)
            print("linkAdded " + actual_link)
            new_links.append(actual_link)
        # sleep for 30 seconds
    while len(new_links) > len(amznlinks):
        print("linkRemoved ")
        new_links.pop(0)
    first_time = False
    time.sleep(30)
