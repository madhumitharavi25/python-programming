import re
phonenumber = re.compile(r'\d\d\d-\d\d\d')
m0 = phonenumber.search("call me at 123-123")
m1 = phonenumber.findall("call me at 123-123")
phonenum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d)')
m3 = phonenum.search("call me at 123-123-12")
print(m0.group(),m1,m3.group())
batregex = re.compile(r'Bat(man|mobile)')
man = batregex.search("Batman is a good man")
print(man.group()) 
bat1regex = re.compile(r'bat(wo)?man')
m4 = bat1regex.search("batwoman is magestic")
print(m4.group())
bat2regex = re.compile(r'bat(wo)*man')
m5 = bat2regex.search("batwowowoman is magestic")
print(m5.group())
bat3regex = re.compile(r'bat(wo)+man')
m6 = bat2regex.search("batwowowoman is magestic")
print(m6.group())
bat4regex = re.compile(r'(wo){2,5}')
m7 = bat4regex.search("bat wowowo man is magestic")
print(m7.group())
digitregex = re.compile(r'(\d){2,5}?')
m8 = digitregex.search("bat 12345")
print(m8.group())
digit2regex = re.compile(r'(\d){2,5}')
m9 = digit2regex.search("bat 12345")
print(m9.group())
vowelregex = re.compile(r'[aeiou]')
m10 = vowelregex.findall("asfg hgsga")
print(m10)
words = re.compile(r'\d+\s\w+')
print(words.findall("12 asdddds hasjh"))
vowel1regex = re.compile(r'[^aeiou]')
m11 = vowel1regex.findall("asfg hgsga")
print(m11)
begin = re.compile(r'^gfa')
m12 =  begin.search("gfa hash")
print(m12.group())
end = re.compile(r'gfa$')
m13 =  end.search("gfa hash gfa")
print(m13.group())
dot1 = re.compile(r'.{1,3}gfa')
m14 =  dot1.search("fga sgfa hash gfa")
print(m14.group())
name = re.compile(r'first: (.*)')
print(name.findall("first: Madhu"))