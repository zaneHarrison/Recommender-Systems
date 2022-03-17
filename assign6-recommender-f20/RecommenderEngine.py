'''
@author: Zane Harrison zlh4
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    retList = [] #Return list
    for item in items: #Iterating over the items being rated
        ratingList = [] #List of ratings for each item
        index = items.index(item) #Index of the ratings for a particular item
        for rating in ratings.values(): #Finding the rating
            rating = rating[index]
            if rating != 0: #If there's no rating, don't add to ratingList
                ratingList.append(rating)
        if len(ratingList) == 0: #If there are no ratings for an item
            average = 0
        else: #If there are any ratings for an item
            average = sum(ratingList)/len(ratingList) #Calculating average rating
        retList.append((item, float(average)))
    return sorted(retList, key=lambda x: (-x[1], x[0])) #Sorting tuples


def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    retList = [] #Return list
    nameRatings = ratings[name] #Ratings list for name
    for key in ratings: #Iterating over dictionary keys
        if key == name: #Skipping comparison for name's rating list
            continue
        else:
            compareRatings = ratings[key] #Rating list for person being compared to
            dotProduct = sum([compareRatings[index] * nameRatings[index] for index in range(len(
                nameRatings))]) #Calculating dot product for name and someone else
            tuple = (key, dotProduct) #Creating tuple
            retList.append(tuple)
    return sorted(retList, key=lambda x: (-x[1], x[0])) #Sorting tuples


def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    similaritiesList = similarities(name, ratings)[:numUsers] #Uses numUsers to create list with raters'
    # names and their similarity scores
    # print(similaritiesList)
    newRatings = {} #New dictionary to store weighted ratings
    for tuple in similaritiesList: #Iterating over names and similarity scores
        person = tuple[0] #Rater's name
        similarityScore = tuple[1] #Similarity score
        newRatings[person] = [rating * similarityScore for rating in ratings[person]] #Adding to dictionary
        # which stores raters and their weighted ratings
    weightedAverages = averages(items, newRatings) #List of tuples containing item names and their weighted
    # ratings
    return weightedAverages


if __name__ == '__main__':
    '''
    print(recommendations('J J', ["DivinityCafe", "FarmStead", "IlForno",
    "LoopPizzaGrill", "McDonalds", "PandaExpress",
     "Tandoor", "TheCommons", "TheSkillet"], {"Sarah Lee":[3, 3, 3, 3, 0, -3, 5, 0, -3], "Melanie":[5, 0,
                                                                                                     3, 0, 1, 3, 3, 3, 1], "J J":[0, 1, 0, -1, 1, 1, 3, 0,
                                                                                1], "Sly one":[5, 0, 1, 3, 0, 0,
                                                                                        3, 3, 3],
                                              "Sung-Hoon":[0, -1, -1, 5, 1, 3,
                                                                                     -3, 1, -3], "Nana Grace":[5, 0, 3, -5, -1,
                                                                                           0, 1, 3, 0], "Harry":[5, 3, 0, -1, -3,
                                                                                         -5, 0, 5, 1], "Wei":[1, 1, 0, 3, -1, 0, 5, 3,
                                                                                 0]}, 3))
    '''
    '''
    print(recommendations('student1367', ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful '
                                                                                          'Mind',
                                          'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan'], {'student1367': [ 0, 3,-5, 0, 0, 1, 5, 1, 3, 0],
'student1046': [ 0, 0, 0, 3, 0, 0, 0, 0, 3, 5],
'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],
'student1103': [-3, 3,-3, 5, 0, 0, 5, 3, 5, 5]}, 2))
    '''
    print(averages(['DivinityCafe', 'FarmStead', 'IlForno', 'LoopPizzaGrill', 'McDonalds', 'PandaExpress',
                    'Tandoor', 'TheCommons', 'TheSkillet'], {'Sarah Lee': [3, 3, 3, 3, 0, -3, 5, 0, -3], 'Melanie': [5, 0, 3, 0, 1, 3, 3, 3, 1], 'J J': [0, 1, 0, -1, 1, 1, 3, 0, 1], 'Sly one': [5, 0, 1, 3, 0, 0, 3, 3, 3], 'Sung-Hoon': [0, -1, -1, 5, 1, 3, -3, 1, -3], 'Nana Grace': [5, 0, 3, -5, -1, 0, 1, 3, 0], 'Harry': [5, 3, 0, -1, -3, -5, 0, 5, 1], 'Wei': [1, 1, 0, 3, -1, 0, 5, 3, 0]}))