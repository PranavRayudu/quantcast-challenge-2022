[![Run Python Tests](https://github.com/PranavRayudu/quantcast-challenge-2022/actions/workflows/ci.yml/badge.svg)](https://github.com/PranavRayudu/quantcast-challenge-2022/actions/workflows/ci.yml)

# Most Active Cookie

Most Active Cookie is a command line application for the Quantcast 2022 Summer Internship coding challenge.

## Description

Mos Active Cookie processes the log file and return the most active cookie for specified day.

## Getting Started

1. This project requires [Python 3.7](https://www.python.org/download/releases/3.0/) or higher

2. Clone the repo
```bash
git clone https://github.com/PranavRayudu/quantcast-challenge-2022.git
```

### Executing program

* To execute on command line
```bash
python most_active_cookie.py <fillename> -d <date>
```

* Example program
```bash
python most_active_cookie.py most_active_cookie_log.csv -d 2018-12-09
```

* Command line help options
```bash
python most_active_cookie.py -h
```

* To run tests
```bash
python -m unittest
```

### Documentation 
Documentation is hosted on [Github pages](http://blog.pranavr.me/quantcast-challenge-2022/).