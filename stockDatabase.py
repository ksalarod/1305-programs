#CIST 1305
#Assignment: Design a database with a menu that allows the user to choose a stock option.
#By Karla Salamanca Rodriguez
def menuchoice():
    def print_menu():       #Menu design here
        print(30 * "-", "Stock Options Menu", 30 * "-")
        print("1. Choose this to buy NVIDIA Stock")
        print("2. Choose this to buy Meta Stock")
        print("3. Choose this to buy Apple Stock")
        print("4. Exit from the script ")
        print(73 * "-")

    loop = True
    int_choice = -1

    while loop:          # While loop which will keep going until loop = False
        print_menu()    # Displays menu
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            choice = ''
            while len(choice) == 0:
                choice = input("How many shares of NVDA would you like to buy? ")
            int_choice = 1
            import sqlite3
            conn = sqlite3.connect ('example.db')
            data = conn.cursor()
            data.execute ('''CREATE TABLE IF NOT EXISTS stocks
              (data text, trans text, symbol text, qty real, price real)''')
            data.execute ("INSERT INTO stocks VALUES ('Today','BUY', 'NVDA', 100, 762)")
            data.execute ('SELECT * FROM stocks')
            conn.commit ()
            for row in data.fetchall():
                print (row)
            conn.close()
            def menuchoice():
                def print_menu():
                    loop = False
        elif choice == '2':
            choice =''
            while len(choice) == 0:
                choice = input("How many shares of Meta would you like to buy? ")
            int_choice = 2
            import sqlite3
            conn = sqlite3.connect ('example.db')
            data = conn.cursor()
            data.execute ('''
              (data text, trans text, symbol text, qty real, price real)''')
            data.execute ("INSERT INTO stocks VALUES ('Today', 'BUY', 'META', 100, 481)")
            data.execute ('SELECT * FROM stocks')
            def menuchoice():
                def print_menu():
                    loop = False
            loop = False
        elif choice == '3':
            choice = ''
            while len(choice) == 0:
                choice = input("How many shares of AAPL would you like to buy? ")
            int_choice = 3
            import sqlite3
            conn = sqlite3.connect ('example.db')
            data = conn.cursor()
            data.execute ('''
              (data text, trans text, symbol text, qty real, price real)''')
            data.execute ("INSERT INTO stocks VALUES ('Today','BUY', 'NVDA', 100, 165)")
            data.execute ('SELECT * FROM stocks')
            def menuchoice():
                def print_menu():
                    loop = False
            loop = False
        
        elif choice == '4':
            int_choice = -1
            print("Exiting..")
            loop = False  # This cause while loop to end and prevents and infinite loop.
        else:
            # Any inputs other than values 1-4 we print an error message
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


print(menuchoice())
