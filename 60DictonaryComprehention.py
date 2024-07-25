# 60. Dictionary Comprehention [05:11:00]-----------------------------------------------------------------
# dictionary comprehention = create dictionaries using an expression 
#can replace for loops and certain lambda functions
# Formula: 
# dictionary={key: expression for (key,value) in iterable }
# dictionary={key: expression for (key,value) in iterable if conditionals}
# dictionary={key: expression if/else conditionals for (key,value) in iterable}
# dictionary={key: function(value) for (key,value) in iterable}
# ------------------
cities_in_f={"New York":32,"Boston":75,"Los Angles":100,"Chicago":50}
cities_in_c={key: round((value-32)*(5/9)) for(key,value) in cities_in_f.items()}
print(cities_in_c)
# -------------------
weather ={"New York":"snowing","Boston":"sunny","Los Angeles":"sunny","Chicago":"cloudy"}
sunny_weather={key: value for(key,value) in weather.items() if value=="sunny" }
print(sunny_weather)
# -----------------------
cities_in_f={"New York":32,"Boston":75,"Los Angles":100,"Chicago":50}
desc_cities = {key: ("Warm" if value>=40 else "Cold")  for(key,value) in cities_in_f.items()}
print(desc_cities)
# -----------------------
def check_temp(value):
    if value >= 70: 
        return "Hot"
    elif 69>=value>=40:
        return "Warm"
    else:
        return "Cold"
cities_in_f={"New York":32,"Boston":75,"Los Angles":100,"Chicago":50}
desc_cities = {key: check_temp(value) for(key,value) in cities_in_f.items()}
print(desc_cities)