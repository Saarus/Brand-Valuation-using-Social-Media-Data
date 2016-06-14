import csv
import statistics
from sklearn import preprocessing

#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file_obj, delimiter=',')
    num_likes = []
    num_comments = []
    num_shares = []
    for line in reader:
        p = int(line["num_likes"])
        q = int(line["first_page_comment"])
        r = int(line["comments_beyond_pageone"])
        num_likes.append(p)
        num_comments.append(q)
        num_shares.append(r)
    mean_num_likes = statistics.mean(num_likes)
    stdev_num_likes = statistics.stdev(num_likes)
    mean_num_comments = statistics.mean(num_comments)
    stdev_num_comments = statistics.stdev(num_comments)
    mean_num_shares = statistics.mean(num_shares)
    stdev_num_shares = statistics.stdev(num_shares)
    covariance_likes = stdev_num_likes / mean_num_likes
    covariance_comments = stdev_num_comments / mean_num_comments
    covariance_shares = stdev_num_shares / mean_num_shares
    w = csv.writer(open("svm_dataset.csv","a"),delimiter=',',quoting=csv.QUOTE_ALL)
    
    w.writerow([mean_num_likes,stdev_num_likes,covariance_likes,mean_num_comments,stdev_num_comments,covariance_comments,mean_num_shares,stdev_num_shares,covariance_shares])
    #z_scores = [(x_i - mean)/stdev for x_i in num_likes]
    #minmax = [(x_i - min(num_likes)) / (max(num_likes) - min(num_likes)) for x_i in num_likes]
    #print mean_num_likes,stdev_num_likes,mean_num_comments,stdev_num_comments,mean_num_shares,stdev_num_shares


#----------------------------------------------------------------------
if __name__ == "__main__":
    file = ['FB/LGMobile_facebook_statuses.csv', 'FB/acerindia_facebook_statuses.csv', 'FB/AirtelIndia_facebook_statuses.csv',#'FB/AmazonIN_facebook_statuses.csv',
            'FB/Amazon_facebook_statuses.csv', 'FB/Apple-Inc_facebook_statuses.csv',
            'FB/BlackBerry_facebook_statuses.csv', 'FB/Dropbox_facebook_statuses.csv', 'FB/Google_facebook_statuses.csv',
            'FB/HuaweiArabia_facebook_statuses.csv', 'FB/IBM_facebook_statuses.csv', 'FB/MicrosoftIndia_facebook_statuses.csv',
            'FB/MicrosoftLumiaIn_facebook_statuses.csv', 'FB/PhilipsIndia_facebook_statuses.csv', 'FB/PhilipsMen_facebook_statuses.csv',
            'FB/SanDisk_facebook_statuses.csv', 'FB/Siemens_facebook_statuses.csv', 'FB/Snapdeal_facebook_statuses.csv',
            'FB/SoundCloud_facebook_statuses.csv', 'FB/Xiaomiworld_facebook_statuses.csv','FB/aircel_facebook_statuses.csv',
            'FB/beatsbydre_facebook_statuses.csv', 'FB/dellindia_facebook_statuses.csv', 'FB/flipkart_facebook_statuses.csv',
            'FB/huaweidevice_facebook_statuses.csv', 'FB/micromaxindia_facebook_statuses.csv', 'FB/myntra_facebook_statuses.csv',
            'FB/yahoo_facebook_statuses.csv']
    for i in file:
        with open(i) as f_obj:
           csv_dict_reader(f_obj)
        
       
