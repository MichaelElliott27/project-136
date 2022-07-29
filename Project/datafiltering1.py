import pandas as pd
import matplotlib.pyplot as plt
rows=[]
stars_data_rows=rows[1:]
stars=[]
final_stars={}
for index,stars_data in enumerate(stars_data_rows):
  feature_list=[]
  gravity = (float(stars_data[3])*5.972e+24) / (float(stars_data[7])*float(stars_data[7])*6371000*6371000) * 6.674e-11
  try:
    if gravity > 150 or gravity < 350:
      feature_list.append("gravity")
  except:
    pass
  try:
    if stars <= 100:
      feature_list.append("stars")
  except:
    pass
  final_stars[index]=feature_list
print(final_stars)