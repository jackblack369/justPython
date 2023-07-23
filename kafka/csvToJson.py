import csv 
import json 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Takes the file paths as arguments 
def make_json(csvFilePath, jsonFilePath): 
      
    # create a dictionary 
    data = []
      
    # Open a csv reader called DictReader 
    with open(csvFilePath,'r') as csvf: 
        csvReader = csv.DictReader(csvf) 
          
        # Convert each row into a dictionary  
        # and add it to data 
        for rows in csvReader: 
            data.append(rows)
  
    # function to dump data 
    with open(jsonFilePath, 'w') as jsonf: 
        jsonf.write(json.dumps(data,ensure_ascii=False)) 
        
csvFilePath = '/data/tmp/csv/tbl_202101201410.csv'
jsonFilePath = '/data/tmp/tbl.json'
  
# Call the make_json function 
make_json(csvFilePath, jsonFilePath)