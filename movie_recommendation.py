# modules/libraries to import

# import spacy
import spacy

#################################################################################################

# functions_

# ● Read in the movies.txt file. Each separate line is a description of a different movie.
# create a function that takes the movies.txt file as an argument and reads it
def read_movies(text_file):
    # create an empty list to store the movie dictionaries
    movie_list = []
    # open the text file in read mode and assign it to the variable m
    # use a with statement to ensure that the file is properly closed after reading, even if an exception occurs
    with open(text_file, 'r') as m:
        # use a for loop to iterate over each line in the file
        for line in m:
            # split() each line into two parts based on the colon (':') delimiter
            # strip() any leading or trailing whitespace from the line
            movie_entry = line.strip().split(':')
            # first part of the split line, movie_entry[0], represents the movie name
            # assign it to the variable movie_letter & strip off any whitespace
            movie_letter = movie_entry[0].strip()
            # second part of the split line, represents the movie description
            # assign it to the variable movie_description & strip off any whitespace
            movie_description = movie_entry[1].strip()
            # create a dictionary with the keys 'name' and 'description' and their respective values
            movie_dict = {'name': movie_letter, 'description': movie_description}
            # append() movie_dict to movie_list
            movie_list.append(movie_dict)

    # return the movie_list containing the movie dictionaries
    return movie_list

# create a function that takes Planet Hulk as an argument and compares its semantic similarity with a list of other movies
# create a model for the movie to compare
# natural language processing (NLP) model is used to analyse and understand text
# pass 'Planet Hulk' as an argument to the nlp model
# print out a statement that indicates the start of the comparison process
def compare_movies(movie_to_compare):
    model_movie = nlp(movie_to_compare['Planet Hulk'])
    print('''The similarity score is a floating decimal between 0 and 1, where 1 indicates a high similarity.
          The semantic similarity between 'Planet Hulk' and the list of movies:\n
          ''')
    # use a for loop to iterate over each movie in the read_text_file list
    # calculate the semantic similarity between the current movie's description and the movie to compare
    # create a model for the current movie's description
    # use the similarity method to compare this model with the model of the movie to compare (Planet Hulk)
    # print out the name of the current movie and its similarity score
    for movie in read_text_file:
        similarity = nlp(movie['description']).similarity(model_movie)
        print((movie['name']), " - ", similarity)
    print("-" * 100)

# create a function that takes two parameters: movie_to_compare and movie_list
def most_similar_movie(movie_to_compare, movie_list):
    # create an NLP object that uses a natural language processing (NLP) model to process the movie_to_compare string
    model_movie = nlp(movie_to_compare)

    # define a nested function that takes a movie as a parameter
    # -use as a key function for the max function in the next step
    # calculate the similarity between the description of each movie in the movie_list and the model_movie using the similarity method of the NLP object
    # return the similarity score (store for max() calculation)
    def similarity_key(movie):
        return nlp(movie['description']).similarity(model_movie)
    
    # use the max function to find the movie in the movie_list with the highest similarity score
    # the similarity_key function is the key parameter because the similarity scores are the basis for comparison 
    most_similar = max(movie_list, key=similarity_key)
    # print out a recommendation statement
    # return the title of the most similar movie to Planet Hulk.
    print("If you have watched Planet Hulk, try this next!\n")
    return most_similar['name']

#################################################################################################

# build a system that will tell you what to watch next based on the word vector similarity of the description of movies
# print out introduction
print("\nThe following program will use the spacy similarity function to determine the movie you should watch next")
print("=" * 100, "\n")

# specify the spacy model to use
nlp = spacy.load('en_core_web_md')


# set the path to the text file that will be used in the read_movies function as an argument
text_file = 'movies.txt'

# call the read_movies function
# print out the list of movies read from the text file
read_text_file = read_movies(text_file)
print("\tDictionary list of movies\n")
print("-" * 100)
for movie in read_text_file:
    print(movie)
print("-" * 100)
print()

# set the dictionary for the movie to compare with a key-value pair
#Planet Hulk with the description “Will he save
#their world or destroy it? When the Hulk becomes too dangerous for the
#Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
#planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
#planet Sakaar where he is sold into slavery and trained as a gladiator.”
movie_to_compare = {'Planet Hulk':'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'}

# call the function to find the similarity score between 'Planet Hulk' & the movie list    
compare = compare_movies(movie_to_compare)                         

# Call the most_similar_movie() function
# print out the most similar to recommend
movie_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar = most_similar_movie(movie_to_compare, read_text_file)
print("\t:", most_similar)
print("-" * 100)
print()
















