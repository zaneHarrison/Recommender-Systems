'''
@author: Zane Harrison zlh4
'''

import SmallDukeEatsReader
import RecommenderEngine


def driver():
    
    (items,ratings) = SmallDukeEatsReader.getdata()
    print("items = ",items)
    print("ratings = ", ratings)

    
    avg = RecommenderEngine.averages(items,ratings)
    print("average",avg)
     
    for key in ratings:
        slist = RecommenderEngine.similarities(key,ratings)
        print(key,slist)
        r3 = RecommenderEngine.recommendations(key,items,ratings,3)
        print("top",r3)

    average = [('DivinityCafe', 4.0), ('TheCommons', 3.0), ('Tandoor', 2.4285714285714284),
               ('IlForno', 1.8), ('FarmStead', 1.4), ('LoopPizzaGrill', 1.0), ('TheSkillet', 0.0),
               ('PandaExpress', -0.2), ('McDonalds', -0.3333333333333333)]
    if average == avg:
        print("Averages works.")
    check2 = [('Wei', 1), ('Sly one', -1), ('Melanie', -2), ('Sarah Lee', -6), ('J J', -14),
              ('Harry', -24), ('Nana Grace', -29)]
    if check2 == RecommenderEngine.similarities("Sung-Hoon",ratings):
        print("Similarities works.")
    check3 = [('Tandoor', 149.5), ('TheCommons', 128.0), ('DivinityCafe', 123.33333333333333),
              ('FarmStead', 69.5), ('TheSkillet', 66.0), ('LoopPizzaGrill', 62.0), ('IlForno', 33.0),
              ('McDonalds', -69.5), ('PandaExpress', -165.0)]
    if check3 == RecommenderEngine.recommendations("Sarah Lee",items,ratings,3):
        print("Recommendations works.")
        
if __name__ == '__main__':
    driver()