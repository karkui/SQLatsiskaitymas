import sqlite3


connection = sqlite3.connect("duombaze.db")
c = connection.cursor()

lentele = """
CREATE TABLE IF NOT EXISTS Finances(
id INTEGER PRIMARY KEY AUTOINCREMENT,
type STRING,
amount FLOAT,
category STRING
)"""
c.execute(lentele)
connection.commit()

def enter_income():
    income = "Pliusas"

    while True:
        try:
            suma = float(input("Įveskite įplaukas: "))
            break
        except ValueError:
            print("Netinkamas įvesties formatas. Prašome įvesti skaičių.")

    kategorija = input("Įveskite paskirti: ")

    qwerty = """
    INSERT INTO Finances ("type", "amount", "category") VALUES (?,?,?)
    """

    c.execute(qwerty,(income,suma,kategorija))
    connection.commit()

def enter_expenses():
    income = "Minusas"

    while True:
        try:
            suma = float(input("Įveskite išlaidas: "))
            break
        except ValueError:
            print("Netinkamas įvesties formatas. Prašome įvesti skaičių.")


    kategorija = input("Įveskite paskirti: ")

    qwerty = """
    INSERT INTO Finances ("type", "amount", "category") VALUES (?,?,?)
    """

    c.execute(qwerty,(income,suma,kategorija))
    connection.commit()

def get_balance():

    qwerty = """
    SELECT * FROM Finances WHERE type = "Pliusas"
    """

    c.execute(qwerty)
    test = c.fetchall()
    count = len(test)

    ## -------------------------------TEIGIAMAS----------------------------------------------
    tsuma = 0
    print("Jūsų balansas teigiamas: ")
    for i in range(count):
        print(test[i][2])
        tsuma = tsuma + test[i][2]

    print(f"Bendra teigiama suma: {tsuma:.2f}")

## -------------------------------NEIGIAMAS----------------------------------------------

    qwerty2 = """
        SELECT * FROM Finances WHERE type = "Minusas"
        """

    c.execute(qwerty2)
    test2 = c.fetchall()
    count2 = len(test2)

    nsuma = 0
    print("Jūsų balansas neigiamas: ")
    for i in range(count2):
        print(test2[i][2])
        nsuma = nsuma + test2[i][2]

    print(f"Bendra neigiama suma: {nsuma:.2f}")

## --------------------------------BENDRAS----------------------------------------------
    atsakymas = tsuma - nsuma
    print(f"Jūsų balansas: {atsakymas:.2f}")

    connection.commit()


def get_all_incomes():
    qwerty = """
        SELECT * FROM Finances WHERE type = "Pliusas"
        """

    c.execute(qwerty)
    test = c.fetchall()
    count = len(test)
    print("Viso teigiamų įplaukų: ",count)
    print("------------------------")

    for i in range(count):
        print("Paskirtis: ", test[i][3])
        print("Suma: ", test[i][2])
        print("------------------------")

def get_all_expenses():
    qwerty = """
        SELECT * FROM Finances WHERE type = "Minusas"
        """

    c.execute(qwerty)
    test = c.fetchall()
    count = len(test)
    print("Viso neigiamų įplaukų: ",count)
    print("------------------------")

    for i in range(count):
        print("Paskirtis: ", test[i][3])
        print("Suma: ", test[i][2])
        print("------------------------")



def delete_record():
    while True:
        try:
            atsakymas = int(input("Įrašykite trinamą ID: "))
            break
        except ValueError:
            print("Netinkamas įvesties formatas. Prašome įvesti sveikąjį skaičių.")

    qwerty = """
        DELETE FROM Finances WHERE id = ?
        """
    c.execute(qwerty, (atsakymas,))

    connection.commit()

def update_record():
    while True:
        try:
            atsakymas = int(input("Įrašykite redaguojamą ID: "))
            break
        except ValueError:
            print("Netinkamas įvesties formatas. Prašome įvesti sveikąjį skaičių.")

    tipas = input("Įrašykite nauja tipo reikšmę(Pliusas/Minusas): ")
    suma = input("Įrašykite nauja sumos reikšmę: ")
    kategorija = input("Įrašykite paskirties tipo reikšmę: ")


    atnaujinimas ="""
        UPDATE Finances SET type = ?, amount = ?, category = ?
        WHERE id = ?
        """
    
    c.execute(atnaujinimas, (tipas, suma, kategorija, atsakymas))
    connection.commit()
    print("Atnaujinimas atliktas")

def main_menu():
    while True:
        print("\nAsmeninė finansų tvarkyklė")
        print("1. Įveskite įplaukas")
        print("2. Įveskite išlaidas")
        print("3. Balansas")
        print("4. Teigiamos įplaukos")
        print("5. Neigiamos išlaidos")
        print("6. Ištrinti Įplaukas/Išlaidas")
        print("7. Atnaujinti Įplaukas/Išlaidas")
        print("8. Išeiti")

        choice = input("Pasirinkite opciją: ")

        if choice == '1':
            enter_income()
        elif choice == '2':
            enter_expenses()
        elif choice == '3':
            get_balance()
        elif choice == '4':
            get_all_incomes()
        elif choice == '5':
            get_all_expenses()
        elif choice == '6':
            delete_record()
        elif choice == '7':
            update_record()
        elif choice == '8':
            print("Programos pabaiga.")
            break
        else:
            print("Bloga opcija. Prašome pabandyti dar.")

main_menu()

connection.close()