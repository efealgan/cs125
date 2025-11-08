
movie_name=input("please enter movie name: ")
smiley=int(input("please enter smileys between 1-5: "))
smiley_emoji="\U0001F603"*smiley

if smiley<1 or smiley>5:
    print("movie review program finished")
else:
    print(movie_name, ":", smiley_emoji)
    print("movie review program finished")