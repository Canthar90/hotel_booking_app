import pandas as pd
from abc import ABC, abstractmethod


df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    watermark = "The Real Estate Compant"  # its class variable
    def __init__(self, hotel_id) -> None:
        self.hotel_id = hotel_id   # this i an instance variab;e
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        pass
    
    def available(self):
        """Checks if hotel is available"""
        avalibility = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if avalibility == 'yes':
            return True
        else:
            return False
    
    @classmethod    
    def get_hotel_count(cls, data):  # this is Class method 
        return len(data)
    
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else: 
            return False
        

class Ticket(ABC): # Forcing every children method to chave same methods as abstract class
    
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object) -> None:
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank yoo for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    
    @property   # proprety you not need to call that :}
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
        
    @staticmethod
    def convert(amount):    # Static no need to add self or anything utylity methods
        return amount *1.2
        


class DigitalTicket(Ticket):
    def generate(self):
        return "Hello this is your digital ticket"
    
    def download(self):
        pass

        
hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.available())

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel1.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)

hotel11 = Hotel("188")
hotel12 = Hotel("188")
print(hotel11 == hotel12)