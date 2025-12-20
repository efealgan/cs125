"""
import numpy as np

table=([[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]])

row_sums=np.sum([1])
column_sums=np.sum([0])
print(row_sums)
print(column_sums)
"""

"""
import numpy as np

numbers=np.array([4,12,7,19,3,15])
is_over=numbers>10
print(f"original array: {numbers}\n")
print(f"elements greater than 10 are: {is_over}")
"""
"""
import numpy as np
bool_arr = np.array( [ True, False, False, True, True])
data = np.array( [15.8,2.6,11.5,8.3,21.6] )
is_over = data > 10
print( is_over )
result = sum( is_over )
print( "how many over:", result )

"""
"""
import numpy as np
rainfall=np.random.randint(0,21,7)
print(f"Rainfall each day: {rainfall}")
days=np.array(["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
#Display True/False values if the rainfall is over 10 millimetres
is_over=rainfall>10
print(is_over)
#Display the values where rainfall is over 10 millimetres
result_is_over=rainfall[is_over]
print(f"Rainfall values over 10: {result_is_over}")
#Display the indexes in the array where rainfall is over 10 millimetres
indexes_rainfall=np.where(is_over)
print(f"Indexes of elements: {indexes_rainfall[0]}")
#Display the number of days that the rainfall was over 10 millimetres
number_of_days=sum(is_over)
print("NUmber of days: ", number_of_days)
#Display the days of the week that the rainfall was over 10 millimetres.
days_of_the_week=days[indexes_rainfall]
print("Days of the week: ", days_of_the_week)
"""
"""


import numpy as np
hours=np.random.randint(10000,100001,10)
print("HOurs spent on social media: ", hours)
#how many years each value represents
years=np.round(hours/(24*365),1)
print("Years spent on social media: ",years)
#average number of years for all people
avg=np.mean(years)
print("avg is: ", round(avg))
"""

import numpy as np
scores=np.array([17,95,30,24,67,69,30,54,35,76,86])
study_hours=np.array([1.1, 8.9,2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8])
cities=np.array(['Ordu', 'Antalya', 'Izmir','Ankara', 'Adana', 'Ankara', 'Mersin', 'Antalya', 'Diyarbakir', 'Mersin','Ankara'])

# total study hours for all students.
total_study_hours=np.sum(study_hours)
print("Total study hours: ", np.round((total_study_hours),1))

#average exam score of all students.
avg_exam_scores=np.mean(scores)
print("Avergae score: ", np.round(avg_exam_scores))

#display the cities, excluding duplicates (unique cities).
unique_cities=np.unique(cities)
print("Unique cities: ", unique_cities)

#number of students from Ankara.
ankara=len(cities[cities=="Ankara"])
print("from ankara: ", ankara)

#points per study hour (scores // study_hours)
points_study_hour=scores//study_hours
print("points per hour: ", points_study_hour)

#scores that were below the average.
scores_below_avg=scores<avg_exam_scores
scores_below_avg_not_bool=scores[scores_below_avg]
print("scores below avergae: ", scores_below_avg_not_bool)

#study_hours of students who scored below the average score.
students_below_avg=study_hours[scores_below_avg]
print("study below avg: ", students_below_avg)

#average study hours of all students
avg_study_hour=np.mean(study_hours)
print("avg study hours: ", np.round((avg_study_hour),1))

#average study hours of students with scores below the average.
avg_study_hour_below_avg=np.mean(students_below_avg)
print("Average study hours of students with scores below average: ",avg_study_hour_below_avg)

# city of the student with the maximum score.
max_score=np.argmax(scores)
max_city=cities[max_score]
print("student with highest score: ", max_city)










































