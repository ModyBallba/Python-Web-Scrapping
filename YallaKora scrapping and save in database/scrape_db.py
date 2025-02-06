import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

# Input date and sanitize it
date = input("Please enter a date in the form MM/DD/YYYY: \n")
sanitized_date = date.replace("/", "-")
page = requests.get(f"https://www.yallakora.com/match-center/?date={date}#")

# Create a connection to the SQLite database
conn = sqlite3.connect(f'Match_table_{sanitized_date}.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    championship_title TEXT,
    team_A TEXT,
    team_B TEXT,
    match_time TEXT,
    score TEXT
)''')
conn.commit()

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championship):
        championship_title = championship.contents[1].find("h2").text.strip()
        all_matches = championship.contents[3].find_all("div", {"class": "liItem"})

        for match in all_matches:
            team_A = match.find('div', {'class': 'teamA'}).text.strip()
            team_B = match.find('div', {'class': 'teamB'}).text.strip()
            match_result = match.find("div", {"class": "MResult"}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            match_time = match.find("div", {"class": "MResult"}).find('span', {'class': 'time'}).text.strip()

            matches_details.append({
                "championship_title": championship_title,
                "team_A": team_A,
                "team_B": team_B,
                "match_time": match_time,
                "score": score
            })

    for championship in championships:
        get_match_info(championship)

    # Insert data into the database
    for match in matches_details:
        cursor.execute('''INSERT INTO matches (championship_title, team_A, team_B, match_time, score)
                          VALUES (:championship_title, :team_A, :team_B, :match_time, :score)''', match)
    conn.commit()
    print("Data has been saved to the database.")

main(page)

# CRUD Operations


def read_matches():
    cursor.execute("SELECT * FROM matches")
    return cursor.fetchall()



# Read all matches
matches = read_matches()
for match in matches:
    print(match)

# Close the database connection
conn.close()
