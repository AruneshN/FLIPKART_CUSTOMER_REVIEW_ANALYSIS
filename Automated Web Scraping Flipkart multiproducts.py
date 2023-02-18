from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
import tkinter 
from requests.exceptions import MissingSchema
from tkinter import ttk 
from tkinter import*
from tkinter import messagebox
import pandas as pd 
from tkinter import filedialog
import csv


root=tk.Tk()
root.geometry("1366x768")
root.config(bg="#A16E83")

url_entry = tk.Entry(root,width=80,fg="blue",font=("Courier",10, "underline"))
url_entry.pack()

var=StringVar()
var.set("AUTOMATED WEB SCRAPPING")
label=Label(root,textvariable=var,bd=4,bg='#A16E83',fg="black",
      font=("Algerian",45,"bold","italic")).place(x=240,y=20)


url_entry.place(x=280,y=180)


def flipkart():
    url = url_entry.get()
    
    link=url
   
    product_name=[]
    price=[]
    rate=[]
    
    #how many pages i want i.e.,(1,10)

    for i in range(1,6):
        para={'pageNumber':str(i)}
        page=requests.get(link,params=para)
        page.content
        soup=bs(page.content,'html.parser')
        soup.prettify()
        

        names=soup.find_all('div',attrs={'class':'_4rR01T'})
        prices=soup.find_all('div',attrs={'class':'_30jeq3 _1_WHN1'})
        ratings=soup.find_all('div',attrs={'class':'_3LWZlK'})
        
                
        for i in range(0,len(names)):
            product_name.append(names[i].get_text())
        #cust_name.pop(6)
        for i in range(0,len(prices)):
            price.append(prices[i].get_text())
            
                  
        for i in range(0,len(ratings)):
            rate.append(ratings[i].get_text())
            
    if len(rate)>len(price):
        length=len(rate)-len(price)
        
    for i in range(length):
        rate.pop(length)
        
    
      
    df=pd.DataFrame()
    df['Product_Name']=product_name
    df['Prices']=price
    df['Rating']=rate
    
    
    #df[Prices] = df[Prices].replace({'': '₹'}, regex=True)
           
    df.to_csv(r'D:\flipkartmultiproducts.csv',index = False)
    
def browsefiles():
    filename=filedialog.askopenfilename(initialdir="/D:",
                                        title="Select a File",
                            filetypes=(("csv files","*.csv*"),("all files"," *.* ")))
    
    
    
scrap_button = tk.Button(root, text='SCRAP ',bd=4, command=flipkart,bg="#0B0C10",fg="#A16E83",font=("times new roman",16,"bold")).place(x=970,y=166)


csv_button = tk.Button(root, text='IMPORT CSV FILE ',bd=4, command=browsefiles,bg="#0B0C10",fg="#A16E83",font=("times new roman",16,"bold")).place(x=550,y=280)



def read_csvfile():
    
    root1=Toplevel(root)    
    root1.title("Flipkart Product details form Multiple Page")
    width = 1366
    height = 768
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root1.resizable(1, 1)
    TableMargin = Frame(root1, width=866)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin,columns=("Product_Name", "Prices", "Rating"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Product_Name', text="Product_Name", anchor=W)
    tree.heading('Prices', text="Prices", anchor=W)
    tree.heading('Rating', text="Rating", anchor=W)
    tree.column('#0', stretch=YES, minwidth=1, width=0)
    tree.column('#1', stretch=YES, minwidth=1, width=550)
    tree.column('#2', stretch=YES, minwidth=1, width=400)
    tree.column('#3', stretch=YES, minwidth=1, width=370)
    tree.pack()
    with open(r'D:\flipkartmultiproducts.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Product_Name = row['Product_Name']
            Prices = row['Prices']
            Rating = row['Rating']
            tree.insert("", 0, values=(Product_Name, Prices, Rating))
            
    #============================INITIALIZATION==============================
    if __name__ == '__main__':
        root1.mainloop()


            
flipkart_button = tk.Button(root, text='FLIPKART',bd=4, command= read_csvfile,bg="#0B0C10",fg="#A16E83",font=("times new roman",16,"bold")).place(x=590,y=375)



root.mainloop()
