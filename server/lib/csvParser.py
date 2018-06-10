#for parsing csv
import csv
#for navigating through directories
import os

#csv parser method
def csvParse(directoryName, filename):
    #get the file url

    #if running this file from the interpreter uncomment this line
    #fileLocation = os.getcwd()[:-3] + "model" + "\\" + directoryName + "\\" + filename + ".csv"

    #if running from server.py uncomment this line
    fileLocation = os.getcwd() + "\\model" + "\\" + directoryName + "\\" + filename + ".csv"

    #uncomment the print statement to see what is stored in fileLocation
    #print(filelocation)

    #open csvfile
    with open(fileLocation, "r") as csv_file:
        #read csv file
        csv_reader = csv.reader(csv_file)

        #set count to zero
        count = 0

        #empty key list
        keys = []

        #empty final json list
        finalList = []

        #iterate through each row in csv file
        for rows in csv_reader:
            #first row gives us the keys
            if count == 0:

                #append all items in 1st row to keys
                keys = rows

                #increment count
                count += 1

            else:
                #create empty dictionary
                dictionary = {}

                #now all other items will be stored in correspondance with keys
                for index,item in enumerate(rows):

                    #now assign each value of rows with corresponding keys
                    dictionary[keys[index]] = item

                #at this point after the loop a single dictionary has been created
                #uncomment the following line to see what dictionary prints
                #print(dictionary)

                #append the dictionary to final list
                finalList.append(dictionary)

                #by the end of for loop a list of dictionaries has been created

        #uncomment the following line to see what final list prints
        #print(finalList)

        #now add finalList to another dictionary and return the result
        finalDictionary = {
            "data":finalList
        }

        return finalDictionary

if __name__ == "__main__":
    #NOTE: The path to csv file will be different here than when run from the main python file
    csvParse("health","health")
