from flask import Flask, render_template, request
from random import sample
from classes.movie import Movie

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return populatePageWithNewMovie()

@app.route('/newMovie', methods=["POST"])
def populatePageWithNewMovie():
    #print(getRandomMovie())
    new_movie = get_random_movie()
    return render_template("index.html", movie=new_movie.name)


# list instead of set because random.sample
movies = [
Movie.iron_man(),
Movie.hulk(),
Movie.iron_man_2(),
Movie.thor(),
Movie.captain_america(),
Movie.avengers(),
Movie.iron_man_3(),
Movie.thor_2(),
Movie.captain_america_2(),
Movie.guardians_of_the_galaxy(),
Movie.avengers_2(),
Movie.ant_man(),
Movie.captain_america_3(),
Movie.doctor_strange(),
Movie.guardians_of_the_galaxy_2(),
Movie.spider_man(),
Movie.thor_3(),
Movie.black_panther(),
Movie.avengers_3(),
Movie.ant_man_2(),
Movie.captain_marvel(),
Movie.avengers_4(),
Movie.spider_man_2()]

def get_random_movie():
    return sample(movies, 1)[0]
