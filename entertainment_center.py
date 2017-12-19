import media
import fresh_tomatoes

# instance media.Movie
maze_runner3 = media.Movie("MAZE RUNNER 3",
                           "https://upload.wikimedia.org/wikipedia/commons/d/d4/Maze_runner_thomas.jpg",
                           "https://www.youtube.com/watch?v=v5EOEIkCIOA")

replicas = media.Movie("REPLICAS",
                       "https://upload.wikimedia.org/wikipedia/commons/8/82/Rosettastone.jpg",
                       "https://www.youtube.com/watch?v=YYoypeZmjHE")

# group Movie instance to a list
movie_list = [maze_runner3, replicas]
# run open_movies_page w/ move list as param
fresh_tomatoes.open_movies_page(movie_list)
