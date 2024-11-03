
import customtkinter as c
import jdatetime 

app = c.CTk()
app.geometry("600x500")
app.title("time changer")
app.configure(fg_color="#16423c")




def optionmenu_callback2(hoice) :
    print("a") 

    




def optionmenu_callback3(hoice) :
    
    global optionmenu1_1
    global optionmenu1_2
    global optionmenu2_1
    global optionmenu2_2
    global entry1
    global entry2

    if optionmenu33.get()=="میلادی به شمسی" :
         optionmenu_var1_1 = c.StringVar(value="option 10")
         optionmenu1_1 = c.CTkOptionMenu(app , values=["1", "2" , "3" ,"4","5","6","7","8","9","10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" 
      
                                        ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30"],
                             command=optionmenu_callback2,
                             variable=optionmenu_var1_1 ,fg_color="#6a9c89", button_color="#6a9c89" ,button_hover_color="#629584") 
         optionmenu1_1.place( x=80,y=90) 
   
         optionmenu_var1_2 = c.StringVar(value="فروردین")
         optionmenu1_2 = c.CTkOptionMenu(app , values=["فروردین", "اردیبهشت" , "خرداد" ,"تیر","مرداد",
                                           "شهریور","مهر","ابان","اذر","تیر" ,"بهمن" ,"اسفند"],
                             command=optionmenu_callback2,
                             variable=optionmenu_var1_2 , fg_color="#6a9c89", button_color="#6a9c89" ,button_hover_color="#629584")
         optionmenu1_2.place( x=250,y=90)  

         entry1 = c.CTkEntry(app ,  fg_color="#e9edec")
         entry1.place( x=420,y=90) 

         button1 = c.CTkButton(app , text="send", command=SHtoM, fg_color="#697565", hover="#697565")
         button1.place( x=250,y=150)
       
    else :
        optionmenu_var2_1 = c.StringVar(value="1")
        optionmenu2_1 = c.CTkOptionMenu(app , values=["1", "2" , "3" ,"4","5","6","7","8","9","10" ,"11" ,"12" ,"13" ,"14" ,"15" ,"16" ,"17" ,"18" ,"19" 
                                           ,"20" ,"21" ,"22" ,"23" ,"24" ,"25" ,"26" ,"27" ,"28" ,"29" ,"30"],
                             command=optionmenu_callback2,
                             variable=optionmenu_var2_1 ,fg_color="#6a9c89", button_color="#6a9c89" ,button_hover_color="#629584") 
        optionmenu2_1.place( x=80,y=90) 
        optionmenu_var2_2 = c.StringVar(value="January")
        optionmenu2_2 = c.CTkOptionMenu(app , values=[

                 "January" ,"February" ,  "March" , "April" ,   "May",  "June", "July" , 
                 "August","September" ,"October" ,"November", "December"   ],
                             command=optionmenu_callback2,
                             variable=optionmenu_var2_2 , fg_color="#6a9c89", button_color="#6a9c89" ,button_hover_color="#629584")
        optionmenu2_2.place( x=250,y=90)  

        entry2 = c.CTkEntry(app ,  fg_color="#e9edec")
        entry2.place( x=420,y=90) 

        button2 = c.CTkButton(app , text="send", command=MtoSH, fg_color="#697565", hover="#697565")
        button2.place( x=250,y=150)  
     





def SHtoM():

   # print(jdatetime.date.fromgregorian( day = 4 ,month = 5 , year = 2020 ))
    month_sun = {

     "فروردین" : 1,
     "اردیبهشت" :2 ,
     "خرداد" :3 ,
     "تیر" :4,
     "مرداد" :5,
     "شهریور" :6,
     "مهر" :7,
     "ابان": 8 ,
     "اذر"  :9 ,
     "تیر" :10 ,
     "بهمن" : 11 ,
     "اسفند" :12  

    } 

    str_date_changed=str((jdatetime.date( day = int(optionmenu1_1.get()) ,month = month_sun[optionmenu1_2.get()], year = int(entry1.get())).togregorian()))
    list_of_changed_date=str_date_changed.split("-")
    #print( int(optionmenu1_1.get()), month_sun[optionmenu1_2.get()], int(entry1.get()))
    if optionmenu33.get()== "میلادی به شمسی" :
        label_answer2=c.CTkLabel(app,text=f'''  day ={list_of_changed_date[2]}    month = {list_of_changed_date[1]}    year = {list_of_changed_date[0]}  ''', fg_color="lightgreen")
        label_answer2.place(x=220,y=200)






def MtoSH():


    month_sun = {

     "January" : 1,
     "February" :2 ,
     "March" :3 ,
     "April" :4,
     "May" :5,
     "June" :6,
     "July" :7,
     "August": 8 ,
     "September"  :9 ,
     "October" :10 ,
     "November" : 11 ,
     "December" :12  
    } 

    str_date_changed=str((jdatetime.date.fromgregorian( day = int(optionmenu2_1.get()) , month = month_sun[optionmenu2_2.get()] , year = int(entry2.get()) )))
    list_of_changed_date=str_date_changed.split("-")


    if optionmenu33.get()== "شمسی به میلادی" :
        label_answer2=c.CTkLabel(app,text=f'''  day ={list_of_changed_date[2]}    month = {list_of_changed_date[1]}    year = {list_of_changed_date[0]}  ''', fg_color="lightgreen")
        label_answer2.place(x=220,y=200)





optionmenu_var33 = c.StringVar(value="تبدیل انتخاب")
optionmenu33 = c.CTkOptionMenu(app , values=["میلادی به شمسی", "شمسی به میلادی" ],
                             command=optionmenu_callback3,
                             variable=optionmenu_var33 ,fg_color="#6a9c89", button_color="#6a9c89" ,button_hover_color="#629584") 

optionmenu33.place( x=420,y=40) 


app.mainloop()




