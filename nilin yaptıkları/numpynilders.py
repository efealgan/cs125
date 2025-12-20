"""
import numpy as np
import math

number=np.random.randint(10000,100000,10)
print("hours spent on social media: ", number)
years=np.round(number/(24*365),1)
print("years spent on social media: ", years)
avg=math.ceil(np.mean(years))
print("average spent for all people: ", avg)
"""

import numpy as nh

scores=nh.array([17,95,30,24,67,69,30,54,35,76,86])
study_hours=nh.array([1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8])
cities=nh.array(['Ordu', 'Antalya', 'Izmir','Ankara', 'Adana', 'Ankara', 'Mersin', 'Antalya', 'Diyarbakir', 'Mersin', 'Ankara'])

total_study=nh.sum(study_hours)
print("total study hours: ", total_study)

avg_exam=nh.mean(scores)
print("avg exam score: ", avg_exam)

unique_cities=nh.unique(cities)
print("unique cities: ", unique_cities)

ankara=len(cities[cities=="Ankara"])
print("number of ankasa: ", ankara)

study_points=scores//study_hours
print("points per hour: ", study_points)

below_avg=scores < avg_exam
value_below=scores[below_avg]
print("scores below avg: ", value_below)

study_below_avg=study_hours[below_avg]
print("study below avg: ", study_below_avg)

avg_study=nh.mean(study_hours)
print("avg study hours: ", avg_study)

avg_below=nh.sum(study_below_avg)
print("scores below avg: ", avg_below)

highest=nh.argmax(scores)
print("highest score from the city: ", cities[highest])




























