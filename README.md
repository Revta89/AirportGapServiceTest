# AirportGap API & SauceDemo UI Automated Tests (Python)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![pytest](https://img.shields.io/badge/pytest-8.0%2B-green)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![GitHub](https://img.shields.io/github/license/Revta89/AirportGapServiceTest)

Automated test suite covering:
- API Tests: [Airport Gap](https://airportgap.com/) endpoints (airports, distances, favorites).
- UI Tests: [SauceDemo](https://www.saucedemo.com/) online store (login, cart interactions).

## Technologies
- Python 3.9+
- pytest (test framework)
- Requests (HTTP for API tests)
- Selenium WebDriver (UI automation)
- jsonschema (JSON validation)


## Installation
1. Clone the repository:
  
   git clone https://github.com/Revta89/AirportGapServiceTest.git
   cd AirportGapServiceTest
   
2. Install dependencies:
  
   pip install -r requirements.txt
   
3. For UI tests, download the appropriate [ChromeDriver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) 

## Running Tests
### API Tests (AirportGap)
```bash
pytest -m api
```

### UI Tests (SauceDemo)
```bash
pytest -m ui
```