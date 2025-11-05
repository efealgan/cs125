brandOrigin = {'Toyota':    'Japan',
               'Volkswagen':'Germany',
               'Honda':     'Japan',
               'BMW':       'Germany',
               'Volvo':     'Sweden'}

brandQuery = input("Input a brand name: ")
print(brandQuery, "is in", brandOrigin[brandQuery])

countryQuery = input("Input a country: ")
print("Brands from", countryQuery ,"are:")
for key in brandOrigin: #key sırasıyla Toyota, VW, Honda.. oluyor
    if brandOrigin[key] == countryQuery:
        print(key)