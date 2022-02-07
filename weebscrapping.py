import requests
from bs4 import BeautifulSoup
import pandas
url="https://www.oyorooms.com/hotels-in-bangalore/"
page_num=3
scraped_info=[]
for page in range(1,page_num):
    req=requests.get(url+str(page))
    content=req.content
    print(content)
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})
    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription_hotelName"}).text
        hotel_dict["addres"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            pass
        parent_amenities=hotel.find("div",{"class":"amenityWrapper"})
        ammenitieslist=[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenitieslist.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())
        hotel_dict["amenities"]= ', '.join(amenitieslist[:-1])
        scraped_info.append(hotel_dict)
        print(hotel_name,hotel_address,hotel_price,hotel_rating,amenitieslist)
dataFrame=pandas.DataFrame(scraped_info)
dataFrame.to_csv("Oyo.csv")
