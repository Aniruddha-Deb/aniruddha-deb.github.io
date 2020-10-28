Title: IIT Department Finder Launch (plus personal website domain)
Date: 2020-10-28 20:39
Category: Programming
Tags: Programming, Python, Web Development
Slug: iit-dep-finder

For IIT admissions, I had created a small command line tool called `iit_dep_finder.py` 
to check the departments I would get, given a particular rank. Once the round 
one allocation results came out, I decided to create a web version, for others 
to use as well. This article chronicles the steps I took, and while I did get 
the department finder up and running, I also did a lot of other stuff in the 
process (including changing the domain name, in case you haven't noticed :). 
It's a long and uncensored article, so be warned.

## Index:

1. [Flask App Development](#flask-app-development)
2. [NGINX and GUnicorn local setup](#nginx-and-gunicorn-local-setup)
3. [Lightsail (VPS) setup and deployment](#lightsail-vps-setup-and-deployment)
4. [Domain acquisition and Setup](#domain-acquisition-and-setup)
5. [Domain routing and site setup](#domain-routing-and-site-setup)
6. [Enabling SSL and Security](#enabling-ssl-and-security)

## Flask App Development
Developing the Flask app was probably the most rewarding part of the process, 
considering that the rest of it was DevOps, which is not exactly my cup of 
tea. I started out by downloading the data from 
[https://josaa.nic.in/Result/Result/currentorcr.aspx](https://josaa.nic.in/Result/Result/currentorcr.aspx)
as a set of HTML files, to retain their tabular format. The data was then 
scraped with BeautifulSoup and LXML into a CSV intermediate using the following
snippet of code:

```python
main_table = soup.find("table", {"class":"border_table_at"})
table_rows = main_table.find_all("tr")

for row in table_rows:
	cells = row.find_all("td")
	for cell in cells:
		field = cell.text.strip()
		if field == "Female-only (including Supernumerary)":
			field = field.replace(" (including Supernumerary)", "")
		outfile.write(field.replace(",", "") + ",")
	outfile.write("\n")
```

The CSV file was then cleaned up a bit manually, such as removing commas at the
end of the line and changing a few typos and values. After this, I created the 
SQLite database and added a table, whose schema was as follows:

```sql
	CREATE TABLE IF NOT EXISTS "orcr_2020_r3"(
	institute varchar(256),
	department varchar(256),
	quota varchar(4),
	category varchar(32),
	gender varchar(32),
	OPR integer,
	OPR_prep integer,
	CPR integer,
	CPR_prep integer
	);
```

This was enough to store the required data. Notice the `OPR\_prep` and `CPR\_prep` 
fields, which are there for [Preparatory Course ranklists](https://www.iitism.ac.in/assets/pdfs/rules/pcr.pdf).
The ranks for these ranklists have a 'P' appended to the number. Since we want 
to store the number as an integer for sorting purposes, the 'P' needs to be 
abstracted into this boolean-esque field. 

## NGINX and GUnicorn local setup

## Lightsail (VPS) Setup and Deployment

## Domain Acquisition and Setup

## Domain routing and Site Setup

## Enabling SSL and Security
