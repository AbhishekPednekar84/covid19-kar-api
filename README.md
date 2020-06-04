## API for COVID 19 Tracker - Karnataka

[![Build Status](https://travis-ci.org/AbhishekPednekar84/covid19-kar-api.svg?branch=master)](https://travis-ci.org/AbhishekPednekar84/covid19-kar-api)

This is a Python API which pulls the COVID 19 **cases by gender** data for Karnataka from the [official COVID 19 dashboard](https://covid19.karnataka.gov.in/covid-dashboard/dashboard.html) maintained by the Govenment of Karnataka.

The API is currently used by the [https://kar.covid19-info.website](https://kar.covid19-info.website) website.

**Endpoint**: https://kar.covid19-info.website/gender.json

## Steps to create a local setup
1. Clone the repository - `git clone https://github.com/AbhishekPednekar84/covid19-kar-api`
2. Cretate a virtual environment - `python -m venv venv`
3. Activate the virtual environment - `venv\Scripts\activate` (Windows) or `source venv\bin\activate` (OS X)
4. Install dependences - `pip install -r requirements.txt`
5. Run the program - `python scrape_api.py`
6. Run tests - `pytest`
