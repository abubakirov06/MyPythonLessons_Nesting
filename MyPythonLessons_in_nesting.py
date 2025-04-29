# Dictionary in the List
car0 = {'brend':'Mersedes',
        'masofa':50000, 'rangi':'qora', 'narx':30000, 'yil' : 2018 ,'korobka':'mexanika'
        }
car1 = {'brend':'Ferrari',
        'masofa':70000, 'rangi':'qizil', 'narx' : 130000, 'yil':2020, 'korobka':'avtomat'
        }
car2 = {'brend':'Lambarghini',
        'masofa':200000, 'rangi':'sariq', 'narx':150000, 'yil':2021,
        'korobka':'avtomat'
        }
car3 = {'brend':'Toyota',
        'masofa':65000, 'rangi':'oq', 'narx':40000, 'yil':2023, 
        'korobka':'mexanika'
        }
car4 = {'brend':'BYD',
        'masofa':55000, 'rangi':'ko\'k', 'narx':30000, 'yil':2023, 'korobka':'avtomat'
        }
car = car0
print(f"{car['brend'].title()}, "
      f"{car['rangi'].lower()} rang, "
      f"{car['korobka']} korobka, {car['yil']}-yil chiqqan, {car['narx']}$ga sotiladi, "
      f"{car['masofa']}km yo\'l yurgan")

cars = [car0, car1, car2, car3, car4]
for car in cars:
    print(f"{car['brend'].title()}, "
          f"{car['rangi'].lower()} rang, "
          f"{car['korobka']} korobka, {car['yil']}-yil chiqqan, {car['narx']}$ga sotiladi, "
          f"{car['masofa']}km yo\'l yurgan")
    
print(f"{cars[2]['rangi'].title()} rangli {cars[2]['brend']} ")

malibus = []
for n in range(10):
    new_car = {
        'model':'Malibu', 'rangi':None, 'narx':None, 'yili' : 2023,
        'masofa': None, 'korobka':'avtomat'
        }
    
    malibus.append(new_car)
    
    
for malibu in malibus[:3]:
    malibu['rang']='qora'
for malibu in malibus[3:7]:
    malibu['rang'] = 'oq'
for malibu in malibus[7:10]:
    malibu['rang'] = 'qizil'
    malibu['korobka'] = 'mexanika'
for malibu in malibus:
    if malibu['korobka'] == 'avtomat':
        malibu['narx'] = 22000
    else:
        malibu['narx'] = 20000
       
#list in the dictionary
developers = {
    'ali':['python', 'c++'], 'oybek':['c++', 'HTML'], 
    'diyorbek':['python', 'c++', 'c', 'javascript'], 
    'davron': [ 'go', 'react', 'python'], 'abdulmajid':['C#', 'C++']
    }
for developer, languages in developers.items():
    print(f"\n{developer.title()} quyidagi tillar bilan ishlay oladi: ", end = '')
    for language in languages:
        print(f'{language.upper()}', end = ' ') #naturally, there is endl at the end of print function,
        #end = '' deletes that function so the next item comes directly after the previous one

collegues = {
    'ali':{'birthyear':2002,
           'languages':['python', 'c#'],
           'education':'bakalavr',
           'familiya':'sobirov'
           },
    'vali':{'birthyear':2001,
           'languages':['go', 'python', 'c#', 'html', 'react', 'c++'],
           'education':'magistr',
           'familiya':'sobirov'
           },
    'sobir':{'birthyear':2001,
           'languages':['go', 'python', 'html', 'c++'],
           'education':'bakalavr',
           'familiya':'sobirov'
           },
    'ortiq':{'birthyear':2004,
           'languages':[ 'python', 'c#',  'c++'],
           'education':'o\'rta',
           'familiya':'sobirov'
           }
    }
for name, info in collegues.items():
    print(f"{name.title()} {info['familiya'].title()}",
   f"{info['birthyear']}-yilda tug'ilgan, ",
   f"{info['education']}ni bitirgan",
   'Quyidagi dasturlash tillarini biladi:'
   )
    for language in info['languages']:
        print(f'{language.upper()}', end = ' ')
    

