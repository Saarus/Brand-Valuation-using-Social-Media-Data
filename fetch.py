import csv
#----------------------------------------------------------------------
file_out = open('guilt.txt', 'w')
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        if line["sentiment"] == "guilt":
           file_out.write(line["sentence"])
        #print(line["sentence"])
#----------------------------------------------------------------------
if __name__ == "__main__":
    with open("ise_processed.csv") as f_obj:
        csv_dict_reader(f_obj)
