# M122-LB2 - Stockmarket report creator

## Description
This application creates a graph for a stock course over a specified time.

Afterwards these can be sent to an FTP Server or an Email address

## Prerequisites
- Install Python
- Install Packages
  - fpdf (PDF creation)
  - pandas (Data Analysis)
  - matplotlib (Creating stock plots)
  - pysftp (Upload to FTP server)

## Running the Application
Navigate into the src directory and run the following commands
### Windows
```python.exe main.py [args]```
### Linux
```python3 main.py [args]```

## Arguments
| Argument | Description             | Required |
|:---------|:------------------------|---------:|
| -t       | Time e.g. (20H or 10D)  |     True |
| -a       | Stock names(AAPL,GOOGL) |     True |
| -l       | Local Path              |    False |
| -u       | FTP username            |    False |
| -s       | FTP server address      |    False |
| -p       | FTP password            |    False |
| -P       | FTP server port         |    False |
| -e       | Email Address           |    False |
| -L       | FTP Path                |    False |