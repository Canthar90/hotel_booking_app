import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id) -> None:
        self.hotel_id = hotel_id
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


class ReservationTicket:
    def __init__(self, customer_name, hotel_object) -> None:
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content = f"""
        Thank yoo for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
        
        
class CreditCard:
    def __init__(self, number) -> None:
        self.number = number
        
    def validate(self, expiration, holder, cvc):
        """Validates credit card"""
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else: 
            return False
        

class SpaHotel(Hotel):
    def spaa_reservation():
        pass
    pass


class SpaTicket:
    def __init__(self, customer_name, hotel_object) -> None:
        self.customer_name = customer_name
        self.hotel = hotel_object
    
    def generate(self):
        content =f"""
        Thank you for your spa reservation!
        Here are your SPA booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content
    pass

        
print(df)
hotel_id = (input("Enter the id of the hotel: "))
hotel = SpaHotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            spa_option = input("Do you want to book SPA package? Print 'yes' or 'no': ")
            if spa_option == 'yes':
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("Bad credit card password")
    else:
        print("There was a problem with your credit card")
else:
    print("Hotel is not free. ")