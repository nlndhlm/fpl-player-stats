# read fantasy api
# convert to csv-file
# API found at: https://fantasy.premierleague.com/api/bootstrap-static/
  
import json
import csv
  
# Opening JSON file
f = open('bootstrap.json')

# Creating and opening csv-file for writing
w = open('datafile.csv', 'w')

writer = csv.writer(w)
  
# returns JSON object as  
# a dictionary 
data = json.load(f)
  

# Heading for csv-file
print('First name, Second name, Element type, Cost start, Now cost, Total points, Minutes, Goals scored, Assists, Clean sheets, Bonus')
writer.writerow(['First name', 'Second name', 'Element type', 'Cost start', 'Now cost', 'Total points', 'Minutes', 'Goals scored', 'Assists', 'Clean sheets', 'Bonus'])

# Iterating through the json 
# list 
for i in data['elements']: 
    dataline = i['first_name'], i['second_name'], i['element_type'], (i['now_cost'] + i['cost_change_start_fall']) / 10, i['now_cost'] / 10, i['total_points'], i['minutes'], i['goals_scored'], i['assists'], i['clean_sheets'], i['bonus']
    
    print(dataline)
    writer.writerow(dataline)


# Closing files
f.close()
w.close()
