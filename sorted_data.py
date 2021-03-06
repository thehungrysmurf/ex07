'''
Your job is to write a program named 'sorted_data.py' reads the file, then spits out the ratings in alphabetical order by restaurant
'''
from sys import argv

script, test_file = argv

def open_and_read(filename):
    f = open(filename)
    file_text = f.read()
    f.close
    return file_text

def main():
    dict_of_restaurants = {}
    dict_of_ratings = {}
    list_of_restaurants = open_and_read(test_file).split("\n")
    
    for i in list_of_restaurants:
        i = i.split(":")
        #list by rating, highest to lowest (build a dictionary)
        dict_of_restaurants[i[0]] = int(i[1])
        dict_of_ratings.setdefault(i[1], []).append(i[0])

    sorted_restaurants = sorted(dict_of_restaurants.iteritems())
    for i in range(len(sorted_restaurants)):
        print "%s has %d stars!" % (sorted_restaurants[i][0], sorted_restaurants[i][1])

    sorted_ratings = sorted(dict_of_ratings.iteritems(), reverse = True)
    for i in range(len(sorted_ratings)):
        print sorted_ratings[i][0],"stars: ", sorted_ratings[i][1]

main()