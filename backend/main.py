import time
import requests as requests
from bs4 import BeautifulSoup
from supabase import create_client, Client
from datetime import datetime

if __name__ == '__main__':
    SUPABASE_URL = "your-url"
    SUPABASE_KEY = "your-key"
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    data = supabase.table("Snowday").select("*").execute();
    print(data)

    while True:
        # URl of my school where they post the snow delay
        URL = "https://www.trumbullps.org/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        getFirstDiv = soup.find('div', class_='leading-0')
        h2text = getFirstDiv.find('h2')
        print(h2text.text)

        # Variables that will be updated and send to supabase
        typeday = "";
        isHappy = False;
        inDepthtxt = "";

        if h2text.text.__contains__("School Closed"):
            # Terminal Output
            print("School is closed today!")
            print("Exact text: ", getFirstDiv.find('p'))

            # This is what the user will see in the front end
            typeday = "Congratulations: It is a snow day for Trumbull Public Schools 🙂"

            # Gets rid of the <p> tags from the data
            EditedStr = str(getFirstDiv.find('p')).replace("<p>", "");
            EditedStr = EditedStr.replace("</p>", "")
            inDepthtxt = EditedStr;

            # Sets this to true so that snowflakes activate on frontend
            isHappy = True;
            print("Modified", EditedStr)


        elif h2text.text.__contains__("Delay"):
            print("School is delayed!")
            typeday = "Congratulations: It is a delayed opening for Trumbull Public Schools 🙂"
            print("Exact text: ", getFirstDiv.find('p'))

            EditedStr = str(getFirstDiv.find('p')).replace("<p>", "");
            EditedStr = EditedStr.replace("</p>", "")
            inDepthtxt = EditedStr

            isHappy = True;

        else:
            print("No delay or closing :(")
            typeday = "It is Normal School Day for Trumbull Public Schools"
            isHappy = False;
            inDepthtxt = "";

        # Updated all the values in supabase
        data2 = supabase.table('Snowday').update({'typeDay': typeday}).execute()
        data3 = supabase.table('Snowday').update(
            {'created_at': str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))}).execute()
        data4 = supabase.table('Snowday').update({'isHappy': isHappy}).execute()
        data5 = supabase.table('Snowday').update({'websiteText': inDepthtxt}).execute()

        # Terminal Logging
        print("supabase updated!", str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

        # Suspends the program for 5 min
        mins = 5
        time.sleep(mins * 60)
