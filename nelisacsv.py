import csv

def readCSV(filename):
	reader = csv.reader(open(filename,'rbu'), delimiter =',',quotechar =',',quoting=csv.QUOTE_MINIMAL)
	SaleList = []
	for row in reader:
		SaleList.append(row)
	return SaleList

saleList = readCSV('sales.csv')
#print saleList

def ListSales(SaleList):
	Listsale = []
	for row in saleList:
		for num in range(len(row)):
			Listsale.append({row[2]:row[3]})
	return Listsale
		
ProdList = ListSales(saleList)
