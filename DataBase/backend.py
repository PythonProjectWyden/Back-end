#                a função que inclue no banco de dados 
#                e verifica se os dados estão errados ou             #                                 repetidos
from database import RoomDB

couple_rooms = (102, 104, 202, 204, 302, 304, 402, 404)
single_rooms = (101, 103, 201, 203, 301, 303, 401, 403)

class BackEnd:
    def __init__(self):
        self.db = RoomDB()

    def verifica(self, date, number, cpf):
        if number not in couple_rooms and number not in single_rooms:
            print("Room number invalid!")
            return

        if self.db.select_by_date_and_number(date, number):
            print("Room already occupied at this date!")
            return

        self.db.insert_room(date, number, cpf)
        print("Room reserved!")