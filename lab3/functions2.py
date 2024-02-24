
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

#ex.1 
def imdb_score(morethan55):
    return [movie["imdb"] >= 5.5 for movie in movies]

print(imdb_score(movies))

#ex.2
def sublist(morethan55):
    return [m for m in movies if m["imdb"] >= 5.5]
        
names = sublist(movies)
for m in names:
    print(m["name"])       

#ex.3
def cat(category):
    for i in movies:
        if i["category"] == category:
            print(i["name"])

category = input()
(cat(category))

#ex.4
def avr(mvs, names):
    sum = 0
    count = 0
    for name in names:
        for m in mvs:
            if m["name"] == name:
                sum += m["imdb"]
                count += 1
    avrg_score = sum / count
    print(avrg_score)

names = list(input().split(","))
avr(movies, names)

#ex.5
def avr(category):
    sum = 0
    count = 0
    for m in movies:
        if m["category"] == category:
            sum += m["imdb"]
            count += 1
    avrg_score = sum / count
    print(avrg_score)

cats = input()
avr(cats)