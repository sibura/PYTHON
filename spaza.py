import csv

def ListOfproduct():
    f = open('Nelisa Sales History.csv')
    csv_f = csv.reader(f) 

# create an empty map first...
    filters = {}
    for row in csv_f:
        currentItem = row[2]
        numberSold =  row[3]
    # check if the item is already in the map
        if not filters.has_key(currentItem): 
           filters[currentItem] = 0
        filters[currentItem] += int(numberSold)

    print filters