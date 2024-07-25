capitals={'BD':'Dhaka','India':'Delhi','Argentina':'Bunos iris'}
#print(capitals)
print(capitals['India'])
#print(capitals.get('Germany'))
#print(capitals.get('India'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({'germany':'berlin'})
capitals.update({'BD':'Chittagong'})
capitals.pop('India')
capitals.clear()
for key, value in capitals.items():
    print(key,value)