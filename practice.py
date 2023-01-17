import pandas as pd
from fpdf import FPDF


df = pd.read_csv("articles.csv")


class Order:
    def __init__(self, product_id) -> None:
        self.product = product_id
        self.product_name = df.loc[df["id"] == self.product, "name"].squeeze()
        self.product_price = df.loc[df["id"] == self.product, "price"].squeeze()
        self.product_stock = df.loc[df["id"] == self.product, "in stock"].squeeze()
    
    def in_stock(self):
        """Checks if product is in stock"""
        if self.product_stock > 0:
            return True
        else:
            return False
        
    def receipt_creation(self):
        """Creates reciept for the client"""
        
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Product nr.{self.product}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{self.product_name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.product_price}", ln=1)

        pdf.output("receipt.pdf")
    
    def decrease_available_number(self):
        """Decrease number of available count"""
        self.product_stock -= 1
        df.loc[df["id"] == self.product, "in stock"] = self.product_stock
        df.to_csv("articles.csv")
        
        
        
print(df)
product = int(input("Please choose item by Id: "))
order = Order(product_id=product)
if order.in_stock():
    order.receipt_creation()
    order.decrease_available_number()
else:
    print("This item is not available")
       
        