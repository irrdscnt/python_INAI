# flags={"kg":{"red","yellow"},"russia":{"white","red","blue"},"china":{"red","yellow"}}
# inp=str(input("Please select color "))
# listByAge = {}
# for country, colors in dict.items():
#     if colors==inp:
#         print(country)

# dict((v,k) for k,v in flags.items()).get(inp)

# # while inp:
# for inp in dict.items():
#     print(list(dict.keys())[list(dict.values(inp)).index(inp)])
# time='morning'
# if time=='morning':
#     print(f'Good {time}')
# elif time=='night':
#     print(f'Good {time}')

# day=int(input('Your birth day '))
# month=int(input('Your month of birth '))
# if day:
#     print(f'Your day of birh is {day}')
# if day>=21 and month==3 or day<=20 and month==4:
#     print('You are aries')
# else:
#     print('you are not an aries')
# apple=5
# good=0
# bad=0
# while apple:
#     stroka=str(input('Good or bad? '))
#     if stroka =='good':
#         good +=1
#     if stroka =='bad':
#         bad +=1
#     apple-=1
# print(f'good {good}')
# print(f'bad {bad}')


glasnye=0
soglasnye=0
vowels='aAeEuUiIoOyY'
consonants='WwSsRrTtPpQqDdFfGgHhJjKkLlZzXxCcVvBbNnMm'
# while True:
#     name=str(input('Please write your name? '))
#     print(len(name))
#     # print(list(name))
#     for i in name:
#         if i in vowels:
#             glasnye += 1
#         elif i in consonants:
#             soglasnye +=1
#         else:
#             print(('Please write only words'))
#     print(f'glasnye {glasnye} ,soglasnye {soglasnye}')
#     print(f'Glasnye/soglasnye {glasnye*100/len(name)}%,{soglasnye*100/len(name)}%')
#     break
# num1=11111
# num2=1111111
# print(num1*num2)
# a=int(input('Tell me num '))
# while True:
#     g=random.randint(0, 100)
#     s=str(input(f'Is this your number? {g} '))
#     if s=='yes':
#         print(f'Your number is {g}')
#         break
#     if s=='no':
#         print('Let me try again')
#         v=str(input(' is your number smaller or bigger??'))
#         if v=='smaller':
#             sm=random.randint(0,g)
#             print(sm)
#         if v=='bigger':
#             bg=random.randint(g,100)
#             print(bg)
# lesson=["I","L","O","V","E",True,False,2,13,5,4,11,13,12.12,33.222,True,False]
# word=[]
# number=[]
# boolean=[]
# for i in lesson:
#     if type(i) == str:
#         word.append(i)
#         word.reverse()
#     elif type(i) == int:
#         number.append(i)
#     elif type(i) == float:
#         number.append(i)
#     else:
#         boolean.append(i)
# number.sort()
# word[1]='V'
# word[2]='O'
# word.append('E')
# print(word)
# print(boolean)
# print(number)
# tuple1=tuple(word)+tuple(boolean)+tuple(number)
# print(tuple1)

# INAI={
#     'address':'Toktogula 175',
#     'courses':['Android','Backend','Frontend'],
#     'bag':['fails','errors','stack'],
# }
# INAI.__delitem__('bag')
# INAI['address']='Sovetskaya 65'
# INAI['courses']=['Android','Backend','Frontend','UX/UI design']
# for keys, values in INAI.items():
#     print(f'{keys}:{values}')
# print(INAI)

# sport_car=[]
# modern_car=[]
# old_car=[]

# europe_car=[]
# asian_car=[]
# american_car=[]
# russian_car=[]

# cars=[
#     {'title':'BMW','country':'europe','volume':3.0,'type':'sport'},
#     {'title':'Kia','country':'asia','volume':3.0,'type':'modern'},
#     {'title':'Lada','country':'russia','volume':3.0,'type':'old'},
#     {'title':'Ford','country':'america','volume':3.0,'type':'modern'},
#     {'title':'Ferrari','country':'europe','volume':3.0,'type':'sport'},
# ]
# def all_cars(lst):
#     for i in lst:
#         for key, value in i.items():
#             print(f'{key}-{value}')
# def sort_cars(lst, sport_car:list,modern_car:list, old_car:list,russian_car:list,american_car:list,europe_car:list,asian_car:list):
#     for i in lst:
#         if i['country']=='europe' :
#             europe_car.append(i)
#         elif i['country']=='asia':
#             asian_car.append(i)
#         elif i['country']=='russia':
#             russian_car.append(i)
#         elif i['country']=='america':
#             american_car.append(i)
#     for i in lst:
#         if i['type']=='old':
#             old_car.append(i)
#         if i['type']=='sport':
#             sport_car.append(i)
#         if i['type']=='modern':
#             modern_car.append(i)

# sort_cars(cars, sport_car, modern_car, old_car, russian_car,american_car,europe_car,asian_car)
# print(f'European - {europe_car}\n'
#       f'America - {american_car}\n'
#       f'Asian - {asian_car}\n'
#       f'Russian - {russian_car}\n'
#       f'old car - {old_car}\n'
#       f'modern car -{modern_car}\n'
#       f'sport car -{sport_car}')

# contacts = [
#     {'name': 'Inai', 'phone': '0507052078'},
#     {'name': 'Служба спасения', 'phone': '911'},
#     {'name': 'Пожарная служба', 'phone': '101'},
# ]

# def create(name,phone):

#  contacts.append({'name':name,'phone':phone})

# # create('INAI','0556784512')

# def edit(index,name,phone):
#         contacts[index]['name'] =name
#         contacts[index]['phone']=phone
# # edit(3,'Dexter','0555666777')
# # edit(2,'Hannibal','0777888999')
# create('Hannibal','0556784512')
# create('INAI','0556784512')
# edit(0,'Cronos','0999888666')

# def delete(namedel):
#     for name in contacts:
#         if name['name'] == namedel:
#             del name
# delete('Hannibal')

# print(contacts)


#Дан словарь в списке нужно создать следующие функции

# Создать функцию create - добавление контакта

# Создать функцию edit - изменение контакта

# Создать функцию delete - удаление контакта
# a= int('26')
# b=12
# print(a+b)
# def fun():
#     print('fun')
# print(fun())
# def plus(a,b):
#     return a+b
# print(plus(1,13))
# a=4
# b=9
# print(f'{a}+{b}')
# a=12
# b='56'
# print(a+b)
# if a>=12:
#     print('dfkjhf')
# else:
#     print('fsagf')

# class Person:
#     def __init__(self,name,age,height,hobby,number):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.hobby=hobby
#         self.number=number
#     def speak(self,language):
#         if language=='russian':
#             return f' My name is {self.name} i can speak {language}'
#         elif language=='deutsch':
#             return f' My name is {self.name} i can speak {language}'
#         else:
#             return f'I dont speak'

#     def __str__(self):
#         return  f'Name {self.name}\n' \
#                 f'Age {self.age}\n' \
#                 f'height {self.height}\n' \
#                 f'hobby {self.hobby}\n' \
#                 f'number {self.number}\n' \

# human1=Person('Aikanysh',20,171,'Reading','05555555555')
# print(human1.speak('japan'))
# class Film:
#     def __init__(self,name,year,length,producer,director,rate,actresses,actors,description,):
#         self.name=name
#         self.year=year
#         self.length=length
#         self.producer=producer
#         self.director=director
#         self.rate=rate
#         self.actresses=actresses
#         self.actors=actors
#         self.description=description
#     def opininon(self,opinion):
#         if opinion=='interesting':
#             return f' This movie {self.name} seemed {opinion} to me'
#         elif opinion=='amazing':
#             return f' This movie {self.name} seemed {opinion} to me'
#         else:
#             return f'I didnt like that movie'
#     def wantToWatch(self,yesno):
#         if yesno=='yes':
#             return f'I really want to watch {self.name}'
#         if yesno=='no':
#             return f'I dont want to watch {self.name}'

#     def __str__(self):
#         return  f'Name {self.name}\n' \
#                 f'Year {self.year}\n' \
#                 f'Length {self.length}\n' \
#                 f'producer {self.producer}\n' \
#                 f'director {self.director}\n' \
#                 f'Rate {self.rate}\n' \
#                 f'Actresses {self.actresses}\n' \
#                 f'Actors {self.actors}\n' \
#                 f'Description {self.description}\n' \

# sherlock=Film('Sherlock Holmes',2009,'2.50','Michael Robert Johnson','Guy Ritchie',7.6,'Rachel McAddams','Robert Downey Jr','Detective Sherlock Holmes and his partner, Dr Watson, send Blackwood, a serial killer, to the gallows. However, they are shocked to learn that he is back from the dead and must pursue him again.')
# print(sherlock)

# class Series(Film):
#     def __init__(self,name,year,length,producer,director,rate,actresses,actors,description,numberOfSeasons,numberOfseries):
#         super().__init__(name,year,length,producer,director,rate,actresses,actors,description)
#         self.numSeasons = numberOfSeasons
#         self.numSeries = numberOfseries
    
#     def isAmerican(self,yesno):
#         if yesno=='yes':
#             return f'The series {self.name} are american'
#         if yesno=='no':
#             return f'The series {self.name} are not american'


#     def __str__(self):
#         return super(Series, self).__str__()+ f'Number of seasons {self.numSeasons}\n' \
#                                               f'Number of series {self.numSeries}'

# hannibal= Series('Hannibal',2013,length=False,producer='Bryan Fuller',
#         director='Michael Rymer,Guillermo Navarro,Vincenzo Natali',rate=8.5,actresses='Caroline Dhavernas',
#          actors='Hugh Dancy,Mads Mikkelsen',
#          description='Will, a criminal profiler with a unique ability, slowly sees his sanity taking a hit. The FBI advises he see Hannibal Lecter, a forensic psychiatrist who is secretly a cannibalistic serial killer.',
#          numberOfSeasons=3,numberOfseries=39)
# print(hannibal.isAmerican('yes'))

# class Book(Film):
#     def __init__(self,name,year,length,producer,director,rate,actresses,actors,description,writer,form):
#         super().__init__(name,year,length,producer,director,rate,actresses,actors,description)
#         self.writer=writer
#         self.form=form

#     def wantToRead(self,yesno):
#         if yesno=='yes':
#             return f'I really want to read {self.name}'
#         if yesno=='no':
#             return f'I dont want to read {self.name}'

#     def __str__(self):
#         return super(Book, self).__str__()+ f'Writer of book {self.writer}\n' \
#                                               f'Form of book {self.form}'
# redDragon= Book('Red Dragon',1981,length=432,producer=False,
#         director=False,rate='4/5',actresses=False,
#          actors=False,
#          description='The plot follows former FBI profiler Will Graham, who comes out of retirement to find and apprehend an enigmatic serial killer nicknamed the Tooth Fairy',
#          writer='Tomas Harris',form='paper')
# print(redDragon.wantToRead('yes'))

# class JunDev:
#     def __init__(self,name,lang,):
#         self.name=name
#         self.lang=lang
#     def selfexp(self,name):
#         if name:
#             return f'My name is {self.name} i am junior {self.lang} dev '
#     def isWorking(self,yesno):
#         if yesno=='yes':
#             return f'{self.name} is working right now'
#         if yesno=='no':
#             return f'{self.name} isnt working right now'
#     def __str__(self):
#         return  f'Name {self.name}\n' \
#                 f'Language {self.lang}\n' \

# junior=JunDev('Alana','Java')
# print(junior.selfexp(junior.name))
# print(junior.isWorking('no'))
# print(junior)

# class MidDev(JunDev):
#     def __init__(self,name,lang,experience,company,otherlang):
#         super().__init__(name,lang)
#         self.experience = experience
#         self.company = company
#         self.otherlang=otherlang
#     def __str__(self):
#         return super(MidDev, self).__str__()+ f'Experience {self.experience}\n' \
#                                               f'knowledge of other prog.lang {self.otherlang}'
#     def other(self,company):
#         if company:
#             return f'{self.name} works in {self.company}'

# middle=MidDev('Lacey','Python','5 years','Atlassoft','Java')
# print(middle)
# print(middle.other(middle.company))

# class SenDev(MidDev):
#     def __init__(self,name,lang,experience,company,otherlang,skills,previousjobs,salary):
#         super().__init__(name,lang,experience,company,otherlang,)
#         self.skills = skills
#         self.previousjobs = previousjobs
#         self.salary=salary
#     def __str__(self):
#         return super(SenDev, self).__str__()+ f'Technical skills {self.skills}\n' \
#                                               f'Previous jobs {self.previousjobs}\n'\
#                                               f'Current salary {self.salary}\n' \

#     def expsalary(self,salary):
#         if salary:
#             return f'Salary on new place should be more than {self.salary}'

# senior=SenDev('Cate','Javascript',8,'EPAM','Typescript,node.js','React,Redux,MaterialUI','Discovery,Commercial bank','3000$')
# print(senior)
# print(senior.expsalary(senior.salary))

# incapsulation
class BankAccount:
    def __init__(self, name,number, pin):
        self.name = name
        self.number = number
        self.__pin = pin


    def __str__(self):
        return f'name - {self.name}\n' \
               f'number of your bank account - {self.number}\n' \
               #f'pin - {self.pin}'
account = BankAccount('Alanov Alan Alanovich', '45625897556','a35s36')
print(account)

#Polymorphism
class JunDev:
    def __init__(self,name,lang,):
        self.name=name
        self.lang=lang
    def selfexp(self):
            return f'My name is {self.name} i am junior {self.lang} dev '

class MidDev:
    def __init__(self, name,lang,):
        self.name=name
        self.lang=lang
    def selfexp(self):
            return f'My name is {self.name} i am middle {self.lang} dev '

class SenDev:
    def __init__(self, name,lang,):
        self.name=name
        self.lang=lang
    def selfexp(self):
            return f'My name is {self.name} i am senior {self.lang} dev '

junior = JunDev('Said','Ruby')
middle = MidDev('Ermano','Typescript')
senior = SenDev('Alise','Node.js')

print(junior.selfexp())
print(middle.selfexp())
print(senior.selfexp())

#multiple inheritance
class Cat:
    def meow(self):
        print('Meow-meow-meowwww')

class Dog:
    def bark(self):
        print('Woof-woof-woof')

class CatDog(Cat,Dog):
    pass

catdog=CatDog()
catdog.bark()
catdog.meow()

#abstraction
class Film:
    def __init__(self,name,year,length,):
        self.name=name
        self.year=year
        self.length=length

    def wantToWatch(self,yesno):
        if yesno=='yes':
            return f'I really want to watch {self.name}'
        if yesno=='no':
            return f'I dont want to watch {self.name}'

    def __str__(self):
        return  f'Name {self.name}\n' \
                f'Year {self.year}\n' \
                f'Length {self.length}\n' \


sherlock=Film('Sherlock Holmes',2009,'2.50')
print(sherlock)
print(sherlock.wantToWatch('yes'))

class Series(Film):
    def __init__(self,name,year,length,):
        super().__init__(name,year,length,)


    def __str__(self):
        return super(Film, self).__str__()

hannibal= Series('Hannibal',2013,length='40-50min',)
print(hannibal)
print(hannibal.wantToWatch('yes'))

class Book(Film):
    def __init__(self,name,year,length,):
        super().__init__(name,year,length,)

    def __str__(self):
        return super(Film, self).__str__()

redDragon= Book('Red Dragon',1981,length=432,)
print(redDragon)
print(redDragon.wantToWatch('yes'))