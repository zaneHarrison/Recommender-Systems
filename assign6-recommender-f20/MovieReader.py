'''
@author: Zane Harrison zlh4
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file = open('data/movies.txt', 'r') # Opening the file
    data = file.read().strip().split('\n') # Creating a list of each line of the file
    # print(data)
    items = sorted(set([item.split(',')[1] for item in data])) # Creating a list of each unique movie
    # print(len(items))
    # print(items)
    ratings = {} # Creating a dictionary to hold raters to ratings
    for item in data: # Iterating over each unique movie
        ratingsList = [0]*162 # Creating the values for each rater, empty list with length equal to the
        # number of unique movies
        line = item.split(',')
        ID = line[0]
        movie = line[1]
        rating = line[2]
        movieIndex = items.index(movie)
        if ID not in ratings: # Adding to dictionary
            ratings[ID] = ratingsList
        ratings[ID][movieIndex] = int(rating) # Adding the rating to a student's value
    #print(ratings)
    return (items, ratings)


if __name__ == '__main__':
    print(getdata())