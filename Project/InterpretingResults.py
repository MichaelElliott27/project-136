planet_data_rows=[]
final_list={}
for index,planet_data in enumerate(planet_data_rows):
  feature_list=[]
  gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      feature_list.append("gravity")
  except:
    pass
  try:
    if planet_data[6].lower() == 'terrestrial' or planet_data[6].lower() == 'super earth':
      feature_list.append("planet_type")
  except:
    pass
  try:
    distance = 2 * 3.14 * (planet_data[8] * 1.496e+9)
    time = planet_data[9]*86400
    speed = distance/time
    if speed < 200:
      feature_list.append("speed_supporting")
  except:
    pass
  final_list[index]=feature_list
print(final_list)
gravity_planet_count=0
for key,value in final_list.items():
  if "gravity" in value:
    gravity_planet_count +=1
print(gravity_planet_count)
distance_planet_count=0
for key,value in final_list.items():
  if "planet_type" in value:
    distance_planet_count +=1
print(distance_planet_count)
planet_not_gravity_support=[]
for planet_data in planet_data_rows:
  if planet_data not in low_gravity_planets:
    planet_not_gravity_support.append(planet_data)
type_no_gravity_planet_count=0
for planet_data in planet_not_gravity_support:
  if planet_data[6].lower() == 'terrestrial' or planet_data[6].lower() == 'super earth':
    type_no_gravity_planet_count +=1

print(type_no_gravity_planet_count)
print(distance_planet_count-type_no_gravity_planet_count)
goldilock_planet_count=0
for key,value in final_list.items():
  if "goldilock" in value:
    goldilock_planet_count +=1
print(goldilock_planet_count)
speed_planet_count=0
for key,value in final_list.items():
  if "speed" in value:
    speed_planet_count +=1
print(speed_planet_count)
print(planet_data_rows[0])
final_dict = {}

for index, planet_data in enumerate(planet_data_rows):
  features_list = []
  gravity = (float(planet_data[3])*5.972e+24) / (float(planet_data[7])*float(planet_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity < 100:
      features_list.append("gravity")
  except: pass
  try:
    if planet_data[6].lower() == "terrestrial" or planet_data[6].lower() == "super earth":
      features_list.append("planet_type")
  except: pass
  try:
    if float(planet_data[8].split(" ")[0]) > 0.38 and float(planet_data[8].split(" ")[0]) < 2:
      features_list.append("goldilock")
  except: 
    try:
      if planet_data[8] > 0.38 and planet_data[8] < 2:
        features_list.append("goldilock")
    except: pass
  try:
    try:
      distance = 2 * 3.14 * (float(planet_data[8].split(" ")[0]) * 1.496e+9)
    except:
      try:
        distance = 2 * 3.14 * (float(planet_data[8]) * 1.496e+9)
      except: pass
    try:
      time, unit = planet_data[9].split(" ")[0], planet_data[9].split(" ")[1]
      if unit.lower() == "days":
        time = float(time)
      else:
        time = float(time) * 365
    except:
      time = planet_data[9]
    time = time * 86400
    speed = distance / time
    if speed < 200:
      features_list.append("speed")
  except: pass
  final_dict[planet_data[1]] = features_list

print(final_dict)
goldilock_planet_count = 0
for key, value in final_dict.items():
  if "goldilock" in value:
    goldilock_planet_count +=1
  
print(goldilock_planet_count)
goldilock_gravity_type_count = 0
for key, value in final_dict.items():
  if "goldilock" in value and "planet_type" in value and "gravity" in value:
    goldilock_gravity_type_count +=1

print(goldilock_gravity_type_count)
speed_planet_count = 0
for key,value in final_dict.items():
  if "speed" in value:
    speed_planet_count +=1

print(speed_planet_count)
speed_goldilock_gravity_type_count = 0
for key, value in final_dict.items():
  if "goldilock" in value and "planet_type" in value and "gravity" in value and "speed" in value:
    speed_goldilock_gravity_type_count +=1

print(speed_goldilock_gravity_type_count)