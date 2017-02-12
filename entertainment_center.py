import fresh_tomatoes
import media

blazing_saddles = media.Movie("Blazing Saddles", "To ruin a western town, a corrupt political boss appointsa black sheriff.",
                              "http://trailersfromhell.com/wp-content/uploads/2015/11/Blazing-Saddles.jpg",
                              "https://www.youtube.com/watch?v=VKayG1TrfuE")

#print (blazing_saddles.storyline)

inglourious_basterds = media.Movie("Inglourious Basterds","Story of an all Jewish group of soldiers who aim to kill Hitler",
                                   "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/watch?v=KnrRy6kSFF0")
#print (inglourious_basterds.storyline)

#inglourious_basterds.show_trailer()

waiting = media.Movie("Waiting...", "Follows the antics of young restaurant employee's",
                      "https://images-na.ssl-images-amazon.com/images/I/51TJVHXCPGL.jpg",
                      "https://www.youtube.com/watch?v=HJEsNjH3JT8")

goodfellas = media.Movie("Goodfellas", "Henry Hill and friends work their way up through the mob hierarchy",
                         "http://static.rogerebert.com/uploads/movie/movie_poster/goodfellas-1990/large_pDTuWp3jRcGbfWn0Ic6XZ0M0DwP.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

grandmas_boy = media.Movie("Grandma's Boy", "A 35 year old video game tester has to move back in with his grandmother.",
                           "https://resizing.flixster.com/IBDWrNV2oV9i50lRGeJ3WFPDRRE=/206x305/v1.bTsxMTIwOTMwMjtqOzE3MzE5OzEyMDA7MTIwMDsxNjAw",
                           "https://www.youtube.com/watch?v=vsEuOw3ihbs")

glory = media.Movie("Glory", "About the U.S. Civil War's first all-black volunteer company",
                    "http://static.rogerebert.com/uploads/movie/movie_poster/glory-1989/large_9xmWow6FTRN2MTn2enZhhCU5GLd.jpg",
                    "https://www.youtube.com/watch?v=8XuUGD7aa3E")

movies = [blazing_saddles, inglourious_basterds, waiting, goodfellas, grandmas_boy, glory]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
