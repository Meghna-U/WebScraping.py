import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import functionlibrary
parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse:",type=int)
args=parser.parse_args()
oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX=args.page_num_max
listof_scrapedinfo=[]
functionlibrary.connect(args.dbname)
for page_num in range(1,page_num_MAX):
    url=oyo_url+str(page_num)
    print("GET Request for: "+url)
    r=requests.get(oyo_url+str(page_num))
    cont=r.content
    soup=BeautifulSoup(cont,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice_finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating_ratingSummary"}).text
        except AttributeError:
            hoteldict["rating"]=None
        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        list_of_amenities=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper_amenity"}):
            list_of_amenities.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
        hotel_dict["amenities"]=', '.join(list_of_amenities[:-1])
        listof_scrapedinfo.append(hotel_dict)
        functionlibrary.insert_in_table(args.dbname,tuple(hotel_dict.values()))
dataFrame=pandas.DataFrame(listof_scrapedinfo)
dataFrame.to_csv("Oyo.csv")
functionlibrary.retrieve_hotelinfo(args.dbname)
            
