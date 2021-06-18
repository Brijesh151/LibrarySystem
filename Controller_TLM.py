import mysql.connector
from datetime import date
import View_TLM
from random import choice

def add_user():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
    cursor = conn.cursor()
    name = input('Enter Your Name  : ')
    phone = input('Enter Your Phone  : ')
    email = input('Enter Your Email  : ')
    sql = 'insert into user(name,phone,email) values ("' +name+ '","'+phone+ '","'+email+'");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nNew User added successfully')
    wait = input('\n\n\n Press any key to continue....')

# def add_librarian():
def add_book():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
    cursor = conn.cursor()
    title = input('Enter Book Title :')
    author = input('Enter Book Author : ')
    publisher = input('Enter Book Publisher : ')
    sql = 'insert into book(title,author,publisher,book_status) values ( "' +title+ '","' + author+'","'+publisher+'","available");'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('\n\nNew Book added successfully')
    wait = input('\n\n\n Press any key to continue....')
      
def update_user():  
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print('Modify User Details Screen ')
  print('-'*120)
  print('\n1. Name')
  print('\n2. Phone')
  print('\n3. Email id')
  choice = int(input('Enter your choice :'))
  field =''
  if choice == 1:
    field ='name'
  if choice == 2:
    field = 'phone'
  if choice == 3:
    field = 'email'
  user_id =input('Enter User ID :')
  value = input('Enter new value :')
  if field=='phone':
    sql = 'update user set '+ field +' = '+value+' where userid = '+user_id+';'
  else:
    sql = 'update user set '+ field +' = "'+value+'" where userid = '+user_id+';'
    #print(sql)
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('User details Updated.....')
  wait = input('\n\n\n Press any key to continue....')

def update_bookdetails():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print('Modify BOOK Details Screen')
  print('-'*120)
  print('\n1. Book Title')
  print('\n2. Book Author')
  print('\n3. Book Publisher')
  choice = int(input('Enter your choice :'))
  field = ''
  if choice == 1:
    field = 'title' 
  if choice == 2:
    field = 'author'
  if choice == 3:
    field = 'publisher'
  book_id = input('Enter Book ID :')
  value = input('Enter new value :')
  if field =='title' or field =='author' or field == 'publisher':
    sql = 'update book set ' + field + ' = "'+value+'" where bookid = '+book_id+';'
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('\n\n\nBook details Updated.....')
  wait = input('\n\n\n Press any key to continue....')
      
def delete_user():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  user_id =input('Enter User ID to be deleted:')  
  sql = 'DELETE FROM user WHERE userid ='+user_id+ ';'
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('User Deleted.....')
  wait = input('\n\n\n Press any key to continue....')
     
def delete_book():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  book_id =input('Enter Book ID to be deleted:')  
  sql = 'DELETE FROM book WHERE bookid ='+book_id+ ';'
  cursor.execute(sql)
  conn.commit()
  conn.close()
  print('Book Deleted.....')
  wait = input('\n\n\n Press any key to continue....')
     
def books_details():

  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  book_id=input('Enter Book ID for Book details:')
  sql = 'select * from book where bookid ='+book_id + ';'  
  cursor.execute(sql)  
  result = cursor.fetchone()  
  print('Book Details.....',result)
  conn.close()
  wait = input('\n\n\n Press any key to continue....')
        
def books_available():    # List of available books in library
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print('\n BOOK TITLES - Available')
  print('-'*120)
  sql = 'select * from book where book_status = "available";'
  cursor.execute(sql)
  rows = cursor.fetchall()
  for rows in rows:
    print(rows) 
  conn.close()      
  wait = input('\n\n\nPress any key to continue.....')
      
def rent_book():    # Book issue/checkout
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print('\n BOOK ISSUE SCREEN ')
  print('-'*120)
  book_id = input('Enter Book ID : ')
  user_id  = input('Enter User ID : ')
  try:

    sql = 'select book_status from book where bookid ='+book_id + ';'
    cursor.execute(sql)
    result = cursor.fetchone() 
    for row in result:
        bk_status=row

  except:
    print("Error: Unable to fetch data") 
    conn.close()
     
  today = date.today()

  if bk_status == 'available':
    print("This book is Available")
    sql = 'insert into book_rental(book_id, user_id, doi) values('+book_id+','+user_id+',"'+str(today)+'");'
    cursor.execute(sql)
    conn.commit()
    
    sql_book = 'update book set book_status= "issued" where bookid ='+book_id + ';'
    cursor.execute(sql_book)
    conn.commit()

    print('\n\n\n Book issued successfully')

  else:
     print("Not Available- Book already Issued")     
  wait = input('\n\n\n Press any key to continue....')

def return_book():
  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print('\n BOOK RETURN SCREEN ')
  print('-'*120)
  book_id = input('Enter Book  ID : ')
  user_id = input('Enter User ID : ')
    # print("Enter Date of Return")
  today1 =date.today()
  sql = 'update book_rental set dor ="'+str(today1)+'" where book_id ='+book_id +';'
  cursor.execute(sql)
  conn.commit()
  sql2='update book set book_status ="available" where bookid ='+book_id +';'
  cursor.execute(sql2)
  conn.commit()    
#     d = datetime.date(2020, 5, 26) # yyyy-mm-dd
# print(d)
  conn.close() 
  print('\n\n\n Book returned successfully')     
  wait = input('\n\n\nPress any key to continue.....')
  
def fine_calc():

  conn = mysql.connector.connect(host='localhost', database='library', user='root', password='1907')
  cursor = conn.cursor()
  print("Fine Calculation")
  book_id = input('Enter Book  ID : ')
  user_id = input('Enter User ID : ')

  sql='select doi from book_rental where book_id='+book_id +' and user_id='+user_id +';'
  cursor.execute(sql)
  result1 = cursor.fetchone() 
  for r in result1:
    di=r

  sql1='select dor from book_rental where book_id='+book_id +' and user_id='+user_id +';'
  cursor.execute(sql1)
  result2 = cursor.fetchone() 
  for i in result2:
    dr=i

  t_days = (dr - di).days
  if t_days>14 and t_days<=20:
    print("REMINDER--Hey User! Book is Issued for more than 2 Weeks. Please Return...")

  elif t_days>=21:
    print("Book Returned in",t_days,"Days") 
    fine_amt=t_days*5   
    print("Fine Amount=Rs.",fine_amt)
    sql3='update book_rental set fine = "'+str(fine_amt)+'"  where book_id ='+book_id +' and user_id='+user_id +';'
    cursor.execute(sql3)
    conn.commit()
  conn.close() 
  wait = input('\n\n\nPress any key to continue.....')

# def lib_functions(): 

def main_methods():
  """Enter 1- Log in as Librarian/Admin \nEnter 2- Log in as User/Member \nEnter 0- Close Application"""
  choice = None
  while choice != 0:

    choice = View_TLM.main_menu()
    if choice==1:
      View_TLM.librarian_menu()
      choice = None
      while choice != 0:
        choice = View_TLM.librarian_menu()
        if choice == 1:
          add_user()
        if choice == 2:
          add_book()
        if choice==3:
          update_user()
        if choice == 4:
          update_bookdetails()
        if choice == 5:
          delete_user()
        if choice == 6:
          delete_book()        
        if choice == 7:
          books_details()
        if choice == 8:
          books_available()
        if choice==9:
          fine_calc()
        if choice==0:
          break
    if choice==2:
      View_TLM.user_menu() 
           
if __name__ == "__main__":
  main_methods()
    
        