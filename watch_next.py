import spacy
import operator
nlp = spacy.load("en_core_web_md")

# open movies.txt and get description for each movie, store in list
def watch_next(movie_watched_desc):
    movie_list = []
    with open("movies.txt") as movies:
        for line in movies:
            fields = line.split(":")                                   
            movie_desc = fields[1]
            movie_desc = movie_desc.replace("\n","")            
            movie_list.append(movie_desc)                   
    
    # get score for each movie based on similarity of description of movie already watched vs list of movie descriptions in list above
    # store this in dict containing movie description and score
    model_sentence = nlp(movie_watched_desc)
    string_scores = {}    
    for movie in movie_list:        
        count = 0
        similarity = nlp(movie).similarity(model_sentence)
        score = str(similarity)
        score = score.split("-")    
        for x in score:                       
            count +=1              
        string_scores[movie] = (x)       
        
    # sort dict by score (highest first)
    sorted_result = dict(sorted(string_scores.items(), key=operator.itemgetter(1),reverse=True))
    
    # get first entry from dict (top score)
    next_watch = list(sorted_result.keys())[0]    

    # open movies file, compare movie descriptions to find one matching top score
    with open("movies.txt") as movies_again:
        for line in movies_again:
            fields = line.split(":")                                   
            movie_name = fields[0]
            movie_desc = fields[1]
            movie_desc = movie_desc.replace("\n","")      
            # when matching result found, output recommendation
            if movie_desc == next_watch:
                print(f"\nNext we recommend you watch: {movie_name}")
                print(f"Movie description: {movie_desc}")           

# inputs
movie_watched = "Planet Hulk"
movie_watched_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# call function
watch_next(movie_watched_desc)