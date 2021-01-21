import json

import requests

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


text_file = open("sample.txt", "w", encoding='utf8')

headers = {'apikey': 'c6563080-7697-11ea-8b29-07792ee6451f'}

params = (
    ("q", "hunter io ceo"),
    ("device", "desktop"),
    ("location", "Manhattan,New York,United States"),
    ("num", "15"),
);

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);

text = response.text.replace("\/", "")
data = json.loads(text)
print(data)
n = text_file.write(json.dumps(data))

text_file.close()


# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

# Company, example, knowledge graph
# Description
# Phone number
# Address
# Type of business
# Foundation date
# Social Profiles


# def getCDesc(text):
# 	for key,value in text.items():
# 		if key=='organic':
# 			for i in value:
# 				if '| LinkedIn' in i['title']:
# 					ans=i['description']
# 					break

# def getCPhone(text):

# def getCAddress(text):


# def getCType(text):

# def foundDate(text):


# def socProf(text):


def getName(text):
    names_list = []
    for key, value in text.items():
        print(key)
        if key == "featured_snippet":
            value = value["title"].split()
            names_list.append([value[0], value[1]])
        if key == 'organic':
            value = str(value)
            value = value.split(",")
            for i in value:
                if "title" in i and "LinkedIn" in i:
                    i2 = i.split()
                    names_list.append([i2[1], i2[2]])
                if "title" in i and "Instagram" in i:
                    i = i.split()
                    names_list.append([i[1], i[2]])

    return names_list


def getEmail(text):
    email_list = []
    for key, value in text.items():
        value = str(value)
        value = value.split(",")
        for i in value:
            print(i)
            if "@" in i:
                i = i.split()
                for i2 in i:
                    if "@" in i2:
                        email_list.append(i2)
    return email_list


def getPosition(text):
    position_list = []
    for key, value in text.items():
        value = str(value)
        value = value.split(",")
        for i in value:
            if "title" in i and "LinkedIn" in i:
                i = i.split()
                position = [i[4]]

                position_list.append(position)

    return position_list


def getLinked(text):
    linked_list = []
    for key, value in text.items():
        value = str(value)
        value = value.split(",")
        for i in value:
            if "linkedin.comin" in i:
                i = i.split()

                linked_list.append(i[1])

    return linked_list


def getTwitter(text):
    twitter_list = []
    for key, value in text.items():
        value = str(value)
        value = value.split(",")
        for i in value:
            if "twitter.com" in i:
                print(i)
                i = i.split()
                print(i[0])
                twitter_list.append(i[0])
    return twitter_list


def getBio(text):
    bio_list = []
    for key, value in text.items():
        if key == "featured_snippet":
            bio_list.append(value['description'])

    return bio_list


text_file = open("sample.txt", "r", encoding='utf8')
text = text_file.read()
text = json.loads(text)
text_file.close()

name = getName(text)
email = getEmail(text)
link = getLinked(text)
twitter = getTwitter(text)
bio = getBio(text)
# position=getPosition(text)


print(name)
print(email)
print(link)
print(twitter)
print(bio)
# print(position)


# email_list=[]

# print(email_list)

# email_list=[]


# print(position)


# print(ans)
