#location_box = ['Canary Islands', 'Chiba Prefecture', 'Egypt',  'Ho Chi Minh City', 
#                'Hokkaido', 'Hong Kong', 'Hubei', 'Illinois', 'Ishikawa', 'Japan', 'Johor', 'Kanagawa', 
#                'Kathmandu', 'Kowloon', 'Langkawi', 'London', 'Malaysia', 'Mallorca', 'Manila', 
#                'Nagoya City', 'NSW', 'Paris', 'Qom', 'Sagamihara', 'Saitama Prefecture', 'Seoul', 
#                'Shandong', 'Singapore', 'South Korea', 'Sri Lanka', 'Taiwan', 'Thailand', 'Tokyo', 
#                'Toronto', 'Tyumen', 'UAE', 'Vinh Phuc', 'Washington', 'Wuhan, Hubei', 'Zabaikalsky']

location_box = [ 'Afghanistan', 'Aichi Prefecture', 'Alappuzha', 'Algeria', 'Amiens', 'Andalusia', 
                'Annecy', 'Araq', 'Arizona', 'Baden-Wuerttemberg', 'Bahrain', 'Barcelona', 
                'Bavaria', 'Beijing', 'Belgium', 'Bern', 'Bois-Guillaume', 'Bordeaux', 'Brest', 
                'California', 'Canary Islands', 'Castellon', 'Castile and Leon', 'Chiba Prefecture', 
                'Chongqing', 'Croatia', 'Dijon', 'Egypt', 'Fo Tan', 'France', 'Frankfurt', 
                'Fujian', 'Fukuoka Prefecture', 'Gansu', 'Gifu Prefecture', 'Guangxi', 'Guilan', 
                'Guizhou', 'Hamburg', 'Haneda', 'Hanoi', 'Hebei', 'Hechi, Guangxi', 'Heilongjiang', 
                'Henan', 'Hesse', 'Ho Chi Minh City', 'Hokkaido', 'Hong Kong', 'Hubei', 'Hunan', 
                'Illinois', 'Inner Mongolia', 'Innsbruck', 'Ishikawa', 'Israel', 'Japan', 'Jiangsu', 
                'Jiangxi', 'Jilin', 'Johor', 'Jonkoping', 'Kanagawa', 'Kathmandu', 'Kerala', 'Kowloon', 
                'Kumamoto City', 'Kumamoto Prefecture', 'Kuwait', 'Kwai Chung', 'Kwun Tong', 'Kyoto', 
                'Langkawi', 'Lapland', 'Lebanon', 'Liaoning', 'Lile', 'London', 'Lyon', 'Macau', 
                'Madrid', 'Malaysia', 'Mallorca', 'Manila', 'Massachusetts', 'Mie', 'Montpellier', 
                'Nagano Prefecture', 'Nagoya City', 'Nantes', 'Nara Prefecture', 'Ngau Chi Wan', 
                'Nice', 'Ningxia', 'Nortern Ireland', 'North Rhine-Westphalia', 'NSW', 
                'Okinawa Prefecture', 'Osaka Prefecture', 'Paris', 'Phillipines', 
                'Preah Sihanouk Province', 'Qom', 'Queensland', 'Rhineland-Palatinate', 
                'Rome', 'Sagamihara', 'Saint-Mande', 'Saitama Prefecture', 'Sapporo', 'Seoul', 
                'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Shanxi (陕西)', 'Shenzhen, Guangdong', 
                'Sichuan', 'Singapore', 'South Australia', 'South Korea', 'Sri Lanka', 'Strasbourg', 
                'Taiwan', 'Tehran', 'Tenerife', 'Texas', 'Thailand', 'Thanh Hoa', 'Tianjin', 'Tokyo', 
                'Toronto', 'Tsing Yi', 'Tubingen', 'Tyumen', 'UAE', 'UK', 'Valencia', 'Vancouver', 
                'Victoria', 'Vietnam', 'Vinh Phuc', 'Wakayama Prefecture', 'Wales', 'Wan Chai', 
                'Washington', 'Wisconsin', 'Wuhan, Hubei', 'Xinjiang', 'Yau Ma Tei', 'York', 
                'Yunnan', 'Zabaikalsky', 'Zaragoza', 'Zhejiang', 'Zhuhai'] 
location_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
                59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,
                87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,
                111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,
                132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,
                153,154,155]
location_len = len(location_num)

#country_box = [ 'Australia', 'Canada', 'China', 'Egypt', 'France', 'Hong Kong', 'Iran', 'Japan', 
#               'Malaysia', 'Nepal', 'Phillipines', 'Russia', 'Singapore', 'South Korea', 'Spain', 
#               'Sri Lanka', 'Taiwan', 'Thailand', 'UAE', 'UK', 'USA', 'Vietnam']

country_box = [ 'Afghanistan', 'Algeria', 'Australia', 'Austria', 'Bahrain', 'Belgium', 'Cambodia', 
               'Canada', 'China', 'Croatia', 'Egypt', 'Finland', 'France', 'Germany', 'Hong Kong', 
               'India', 'Iran', 'Israel', 'Italy', 'Japan', 'Kuwait', 'Lebanon', 'Malaysia', 'Nepal', 
               'Phillipines', 'Russia', 'Singapore', 'South Korea', 'Spain', 'Sri Lanka', 'Sweden', 
               'Switzerland', 'Taiwan', 'Thailand', 'UAE', 'UK', 'USA', 'Vietnam'] 
country_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
country_len = len(country_num)


symptom1_box = [ 'chest discomfort', 'chills', 'cold', 'cough', 'cough with sputum', 
                'difficulty breathing', 'fatigue', 'fever', 'flu symptoms', 'headache', 
                'high fever', 'joint pain', 'malaise', 'mild cough', 'mild fever', 'myalgia', 
                'NA', 'nausea', 'physical discomfort', 'reflux', 'runny nose', 'sore body', 
                'sore throat', 'throat discomfort', 'throat pain', 'tired', 'vomiting']
symptom1_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
symptom1_len = len(symptom1_num)

symptom2_box = [ 'abdominal pain', ' aching muscles', ' breathlessness', ' chest pain', ' chill', 
                ' chills', ' cold', ' cough', ' coughing', ' diarrhea', ' difficulty breathing', 
                ' fatigue', ' fever', ' headache', ' itchy throat', ' joint pain', ' loss of appetite',
                ' malaise', ' muscle aches', ' muscle pain', ' myalgia', 'NA', ' nasal discharge', 
                ' pneumonia', ' respiratory distress', ' runny nose', ' shortness of breath', 
                ' sneeze', ' sore throat', ' sputum', ' thirst', ' vomiting']
symptom2_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
symptom2_len = len(symptom2_num)

symptom3_box = [ 'breathlessness', 'chest pain', 'chills', 'cough', 'diarrhea', 
                'difficult in breathing', 'dyspnea', 'fever', 'flu', 'headache', 'joint pain', 
                'malaise', 'muscle aches', 'muscle cramps', 'muscle pain', 'myalgias', 'NA', 
                'pneumonia', 'runny nose', 'shortness of breath', 'sore throat', 'sputum', 
                'throat discomfort', 'vomiting']
symptom3_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
symptom3_len = len(symptom3_num)

symptom4_box = [ 'cough', 'diarrhea', 'dyspnea', 'fever', 'headache', 'heavy head', 'joint pain',
                'malaise', 'NA', 'nausea', 'runny nose', 'sore throat', 'vomiting']
symptom4_num = [0,1,2,3,4,5,6,7,8,9,10,11,12]
symptom4_len = len(symptom4_num)
