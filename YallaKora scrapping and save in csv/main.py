import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


date=input("please enter a date in form MM/DD/YYYY: \n")
sanitized_date = date.replace("/", "-")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}#")

def main(page) :
    src = page.content
    #print(src) # source code not parsed
    soup = BeautifulSoup(src, "lxml")
    ## printing source code html but parsed , note: lxml is fastest parser works with beautifulsoup , also soup is name convential 
    #print(soup) 
    matches_details = []
    # # note that matchCard is dev in the website that releated to the championship , in this day there are more than one like premier , laliga .....
    championships = soup.find_all("div", {'class':'matchCard'}) # find_all('class':'dev-name') looks in all the tag decendants that match my filters
    #print(championships)

    # div is a tag and all under it like <h2>---<h2> are childrens
    def get_match_info (championships):
        ## i tried championship.contents[0] but gives nothing so by trial and error got that it is championship.contents[1]
        ## .text.strip to remove spaces for the head you are searching # remove it and check the output you will see the diffrent
        championship_title = championships.contents[1].find("h2").text.strip() 
        all_matches = championships.contents[3].find_all("div", {"class": "liItem"})
        number_of_matches = len(all_matches)


        for i in range(number_of_matches):
            #get team names
            team_A = all_matches[i].find('div' , {'class':'teamA'}).text.strip() # first value in the list all_matches => [0] check first tag
            team_B = all_matches[i].find('div' , {'class':'teamB'}).text.strip() # first value in the list all_matches => [0] check first tag

            #Get score
            match_result = all_matches[i].find("div", {"class": "MResult"}).find_all('span',{'class':'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()} " # get the two scores in span and store it in string var store in form 0 - 0

            #get match time
            match_time = all_matches[i].find("div", {"class": "MResult"}).find('span',{'class':'time'}).text.strip()
            

            # add match info to list matches_details
            matches_details.append({"نوع البطولة" : championship_title, "الفريق الأول" : team_A , "الفريق الثاني" : team_B , "موعد المباراة" : match_time , "نتيجة المباراة" : score })

        #print (number_of_matches)
        #print(all_matches)
        #print(championship_title)
    

    for i in range(len(championships)):
        get_match_info(championships[i])
        matches_details.append({"نوع البطولة": "", "الفريق الأول": "", "الفريق الثاني": "", "موعد المباراة": "", "نتيجة المباراة": ""})


    keys = matches_details[0].keys() 

    file_name = f'C:\\Users\\Mahmo\\Downloads\\web_scraping\\Match_table_{sanitized_date}.csv'
    with open (file_name, 'w', newline='', encoding='utf-8') as output_file: 
        # get the header
        dict_writer = csv.DictWriter(output_file,fieldnames= keys)
        dict_writer.writeheader()
        # get values
        dict_writer.writerows(matches_details)

    # championships[0] for the first championship which here premier league



main(page)