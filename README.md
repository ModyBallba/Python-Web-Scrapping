# Python Webscrapping Project for YallaKora

## Overview

This project is designed to scrape match data from the Yallakora website for a specific date and store it in an SQLite database. The database can then be queried to retrieve match details, such as championship titles, teams, match times, and scores.

## Files

1. **`scrape_and_store.py`**:  
   This script scrapes match data from the Yallakora website for a given date, stores it in an SQLite database, and provides basic CRUD (Create, Read, Update, Delete) operations.

2. **`database.py`**:  
   This script connects to the SQLite database and retrieves all match data stored in the database.
   
4. **`CSV file contain football table scrapped`**:  

---

## How It Works

### Step 1: Scraping Data
- The `scrape_and_store.py` script prompts the user to input a date in the format `MM/DD/YYYY`.
- It then scrapes match data from the Yallakora website for the specified date.
- The scraped data includes:
  - Championship title
  - Team A
  - Team B
  - Match time
  - Score

### Step 2: Storing Data
- The scraped data is stored in an SQLite database named `Match_table_<date>.db`.
- A table named `matches` is created with the following columns:
  - `id` (Primary Key)
  - `championship_title`
  - `team_A`
  - `team_B`
  - `match_time`
  - `score`


### Step 3: Querying Data
- The `database.py` script connects to the SQLite database and retrieves all match data stored in the `matches` table.
- It prints the retrieved data to the console.

---
## The second code store in .csv file as shown`.
## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `sqlite3`
  - `csv`

Install the required libraries using pip:
```bash
pip install requests beautifulsoup4
