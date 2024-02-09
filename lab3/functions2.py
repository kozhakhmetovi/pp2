"""
# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
"""

# ex1
"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""

def score_5_5(movie_name):
    for m in movies:
        if m['name'] == movie_name:
            if m['imdb'] > 5.5:
                return True
    return False

film = input("Enter the name of the movie:")
print(score_5_5(film))
# ex2
"""
Write a function that returns a sublist of movies with an IMDB score above 5.5.
"""

def score_5_5():
    result = []
    for m in movies:
        if m['imdb'] > 5.5:
                result.append(m['name'])
    return result

print(score_5_5())
# ex3
"""
Write a function that takes a category name and returns just those movies under that category.
"""

def score_5_5(genre):
    result = []
    for m in movies:
        if m['category'] == genre:
                result.append(m['name'])
    return result

nameofcategory = input("Enter the name of the category:")
print(score_5_5(nameofcategory))
# ex4
"""
Write a function that takes a list of movies and computes the average IMDB score.
"""

def func(movies):
    sum = 0
    for i in movies:
        sum+=i['imdb']
    return round(sum/len(movies),2)


print(func(movies))
# ex5
"""
Write a function that takes a category and computes the average IMDB score.
"""


def category_computes_average(category):
    sum_category_movie = 0
    result = []
    for m in movies:
        if m['category'] == category:
            result.append(m['name'])
            sum_category_movie += m['imdb']
    return sum_category_movie / len(result)


category = input("Enter the name of the category:")
print(category_computes_average(category))