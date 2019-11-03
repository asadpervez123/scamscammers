"""Python script to spam a phishing scam with realistic looking fake form submissions. 
Phishing website is http://rewardspointsredem.com/"""

import requests
import random
import string
import time

#phone number funtion
def phone_number():
    """Generate 10 digit phone number that starts with 9"""
    number = '9'
    for _ in range(0,9):
        number += str(random.randint(0,9))
    return number


#card number function
def card_number():
    """Generate a 16 digit debit card number that resembles VISA and MasterCard"""
    card_start = ['50','51','52','53','54','55','40']
    ccnumber = random.choice(card_start)
    for _ in range(0,14):
        ccnumber += str(random.randint(0,9))
    return ccnumber

#CVV number
import random
def cvv ():
    """Generate a 3 digit CVV number"""
    cvv_number = ''
    for _ in range (0,3):
        cvv_number += str(random.randint(0,9))
    return cvv_number


#mpin
import random
def mpin():
    """Generate a 4 digit MPIN number"""
    m_pin = ''
    for _ in range (0,4):
        m_pin += str(random.randint(0,9))
    return m_pin

#exp
def exp():
    """Generate the exp date on card"""

    month_list = ['01','02','03','04','05','06','07','08','09','10','11','12']
    year_list = ['20','21','22','23','24']
    monthnumber = random.choice(month_list)
    yearnumber = random.choice(year_list)

    card_exp = monthnumber + '/' + yearnumber

    return card_exp


#dateofbirth
def date_of_birth():
    """Generate DOB for someone born between 1960 to 2001"""

    birth_year = list(range(1960,2001))
    birth_day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
    birth_month = ['01','02','03','04','05','06','07','08','09','10','11','12']

    birthyearnumber = str(random.choice (birth_year))
    birthdaynumber = random.choice (birth_day)
    birthmonthnumber = random.choice(birth_month)

    date_of_birth = birthyearnumber + '-' + birthmonthnumber + '-' + birthdaynumber
    return date_of_birth




#creating passwords
def password(stringLength=8):
    """Generate an eight character password"""

    special_char = ['!','@','#','$']
    password_characters = string.ascii_letters + string.digits + random.choice(special_char)
    password =  ''.join(random.choice(password_characters) for i in range(stringLength))
    return password



#Submission URL
url = 'http://rewardspointsredem.com/send.php'


#Submitting the form
def runfunc():
    """Submitting on the request URL"""

    first_name =[
        "Saanvi",
        "Anya",
        "Aadhya",
        "Aaradhya",
        "Ananya",
        "Pari",
        "Anika",
        "Navya",
        "Angel",
        "Diya",
        "Myra",
        "Sara",
        "Iraa",
        "Ahana",
        "Anvi",
        "Prisha",
        "Riya",
        "Aarohi",
        "Anaya",
        "Akshara",
        "Eva",
        "Shanaya",
        "Kyra",
        "Siya",
        "Aarav",
        "Vihaan",
        "Vivaan",
        "Ananya",
        "Diya",
        "Advik",
        "Kabir",
        "Anaya",
        "Aarav",
        "Vivaan",
        "Aditya",
        "Vivaan",
        "Vihaan",
        "Arjun",
        "Vivaan",
        "Reyansh",
        "Mohammed",
        "Sai",
        "Arnav",
        "Aayan",
        "Krishna",
        "Ishaan",
        "Shaurya",
        "Atharva",
        "Advik",
        "Pranav",
        "Advaith",
        "Aaryan",
        "Dhruv",
        "Kabir",
        "Ritvik",
        "Aarush",
        "Kian",
        "Darsh",
        "Veer"
    ]

    surnames = [
        "Bedi",
        "Gandhi",
        "Parekh",
        "Kohli",
        "Ahluwalia",
        "Chandra",
        "Jha",
        "Khanna",
        "Bajwa",
        "Chawla",
        "Lal",
        "Anand",
        "Gill",
        "Chakrabarti",
        "Dubey",
        "Kapoor",
        "Khurana",
        "Modi",
        "Kulkarni",
        "Khatri",
        "Kaur",
        "Dhillon",
        "Kumar",
        "Gupta",
        "Naidu",
        "Das",
        "Jain",
        "Chowdhury",
        "Dalal",
        "Thakur",
        "Gokhale",
        "Apte",
        "Sachdev",
        "Mehta",
        "Ganguly",
        "Bhasin",
        "Mannan",
        "Ahuja",
        "Singh",
        "Bakshi",
        "Basu",
        "Ray",
        "Mani",
        "Datta",
        "Balakrishna",
        "Biswas",
        "Laghari",
        "Malhotra",
        "Dewan",
        "Purohit"
    ]

    random_first_name = random.choice(first_name)
    random_surname = random.choice(surnames)

    def full_name():
        """ Generate random fullname"""
        full_name = random_first_name + ' ' + random_surname
        return full_name
    
    #create Email Domains
    email_domain_list = ['@hotmail.com','@gmail.com','@yahoo.co.in','@yahoo.com','@rediffmail.com','@aol.com','@outlook.com']
    random_email_domain = random.choice(email_domain_list)

    number_list_email = list(range(1,9999))
    random_email_number = str(random.choice(number_list_email))


    email_address = random_first_name.lower()+ '.' + random_surname.lower() + random_email_number + random_email_domain

    requests.post(url, allow_redirects=False, data= {
		
        'name': full_name(),
        'phone': phone_number(),
        'email': email_address,
        'pwd': password(),
        'dob': date_of_birth(),
        'cno': card_number(),
        'exp': exp(),
        'cvv': cvv(),
        'mpin': mpin(),
	    })

    print(f"""Submitting the following details: 
    {full_name()}    
    {phone_number()}    
    {email_address}    
    {password()}    
    {date_of_birth()}    
    {card_number()}    
    {exp()}    
    {cvv()}    
    {mpin()}    """) 

for j in range(2000): #Loop for 2000 submissions

    for i in range(45): #Loop for submitting 45 submissions at a time
        runfunc()
    time.sleep(60)
