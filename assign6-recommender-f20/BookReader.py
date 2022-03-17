'''
@author: Zane Harrison zlh4
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file = open('data/books.txt', 'r')  # Opening the file
    data = file.read().strip().split('\n')  # Creating a list of each line of the file
    # print(data[0])
    books = [data[0].split(',')[index] for index in range(1, len(data[0].split(',')), 2)] # Creating a
    # list of unique books
    # print(data[0].split(','))
    # print(data)
    ratings = {} # Creating a dictionary of raters to ratings
    for item in data: # Iterating over each line of books.txt
        ID = item[:item.index(',')] # Getting each student
        if ID not in ratings: # Adding to the dictionary
            ratings[ID] = [0]*55 # Giving each dictionary key (each student) a list of length equal to the
            # number of books to be rated
    # print(ratings)
    for item in data: # Iterating over each line of books.txt
        line = item.split(',') # Done to access individual pieces of data
        ID = line[0] # Getting each student
        valueIndex = 0 # Initializing index used to assign ratings to value in dictionary
        for ratingIndex in range(2, len(line), 2): # Iterating over indexes of ratings for a particular
            # student
            ratings[ID][valueIndex] = int(line[ratingIndex]) # Putting ratings in value
            valueIndex += 1
    #nprint(ratings)
    return(books, ratings)


if __name__ == '__main__':
    print(getdata())