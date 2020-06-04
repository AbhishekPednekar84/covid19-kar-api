import requests
import json
from bs4 import BeautifulSoup


r = requests.get(
    "https://covid19.karnataka.gov.in/covid-dashboard/dashboard.html"
)

soup = BeautifulSoup(r.text, "lxml")

percent_men_dict = {}
percent_women_dict = {}
percent_list = []

for subheader in soup.find_all("div", class_="card-body"):
    try:
        # Get the gender percentage and values
        title = subheader.div.div.text
        percentage = subheader.find(
            "div", class_="d-flex align-items-baseline"
        ).text

        if title == "%Men in Total":
            title = "Male"
            value = float(str.strip(percentage).rstrip("%"))

            percent_men_dict["gender"] = title
            percent_men_dict["percentage"] = value
            percent_list.append(percent_men_dict)

        if title == "%Women in Total":
            title = "Female"
            value = float(str.strip(percentage).rstrip("%"))

            percent_women_dict["gender"] = title
            percent_women_dict["percentage"] = value
            percent_list.append(percent_women_dict)

    except AttributeError:
        break


with open("gender.json", "w") as f:
    json.dump(percent_list, f)
