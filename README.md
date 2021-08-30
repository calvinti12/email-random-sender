# Email Random Sender
**python version: 3.9**

Send emails with random data, based from spreadsheet, in specific range of time.

# Install
## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

# Run

To **start** the program **in terminal**, **run** the **__main __.py** file with your **python 3.9** interpreter.

# Settings

All **configurations** are saved in the **config.json file**, **update** it with your **preferences and credentials**

## config.json

This is the **structure** of the **config.json** file, and a detailed description of each value.

``` json
{
 "from_email":"sample@mail.com",
 "password":"123456789",
 "to_email":"sample2@mail.com", 
 "sheet_link": "https://docs.google.com/spreadsheets/d/1A2pWKolXsfgsghsi_Uv_EOi7BWd19YkcIFi-Roqy5Q7buXg/edit#gid=0", 
 "english_header": "English",
 "japanese_header": "Japanese",
 "start_hour": 12,
 "end_hour": 16
}
```

* ### from_email
**Your** own **email**, for send the message. 
The program **support** the next email providers: 
1. **gmail**
2. **outlook**
3. **hotmail**
4. **live**
5. **Yahoo**
5. **Aol**

If you need to send the emails from other provider, [contact me](https://www.fiverr.com/darideveloper). 

* ### password
Password or application password. 

For **security**, the **most of the emails** services **don't allow you to send emails only with password**. 

You need an **alternative** or second **password**, named **"application key"**.

You can **generate a gmail application password** with this [tutorial](https://www.youtube.com/watch?v=QI2NM9Uy6R4&ab_channel=DariDeveloper). 

If you need help for generate an application password for other email, [contact me](https://www.fiverr.com/darideveloper).. 

* ### to_email
Email for **receive** the message

* ### sheet_link
**Google sheet link**. 

Important: for get data from google sheets, its necessary to do some configurations from google console, then, **if you create a new spreadsheet**, you need to **share me the file** or **give me access to your google account**, for configure it. 

* ### english_header
The **header** / first **row** of the **column** who have the sentences in **English**

* ### japanese_header
The **header** / first **row** of the **column** who have the sentences in **Japanese**

* ### start_hour
Reference **start hour** for random send message, with **24 format**

* ### end_hour
Reference **end hour** for random send message, with **24 format**