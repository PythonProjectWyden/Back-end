#               o banco de dados      
import sqlite3

class RoomDB:
    CREAT_ROOM_TABLE_QUERY = ('CREATE TABLE IF NOT EXISTS room(date text, occupied BOOLEAN,number int, CPF text)')  
    INSERT_ROOM_QUERY = 'INSERT INTO room(date,occupied,number,CPF) VALUES (?,?,?,?)'
    UPDATE_DATE_ROOM_QUERY = 'UPDATE room SET date = ? WHERE CPF = ?'
    UPDATE_OCCUPIED_ROOM_QUERY = 'UPDATE room SET occupied = ? WHERE number = ?'
    SELECT_ROOM_QUERY = 'SELECT * FROM room WHERE CPF = ?'
    SELECT_BY_DATE_AND_NUMBER_QUERY = 'SELECT * FROM room WHERE date = ? AND number = ?'
    DELETE_ROOM_QUERY = 'DELETE FROM room WHERE CPF = ?'
    
    def __init__(self):
        self.conect = sqlite3.connect("WydenHotel.db")
        self.c = self.conect.cursor()
        self.c.execute(self.CREAT_ROOM_TABLE_QUERY)
        self.conect.commit()
        
    def insert_room(self,date,number,CPF):
        self.c.execute(self.INSERT_ROOM_QUERY,(date,True,number,CPF))
        self.conect.commit()
        
    def update_date_room(self,date,CPF):
        self.c.execute(self.UPDATE_DATE_ROOM_QUERY,(date,CPF))
        self.conect.commit()
        
    def update_occupied_room(self, number):
        current_occupied = self.c.execute("SELECT occupied FROM room WHERE number = ?", (number,)).fetchone()[0]
        new_occupied = not current_occupied
        self.c.execute(self.UPDATE_OCCUPIED_ROOM_QUERY, (new_occupied, number))
        self.conect.commit()
        
    def select_room(self,CPF):
        self.c.execute(self.SELECT_ROOM_QUERY,(CPF,))
        return self.c.fetchall()
    
    def select_by_date_and_number(self, date, number):
        self.c.execute(self.SELECT_BY_DATE_AND_NUMBER_QUERY, (date, number))
        return self.c.fetchone()
    
    def delete_room(self,CPF):
        self.c.execute(self.DELETE_ROOM_QUERY,(CPF,))
        self.conect.commit()
        
    def __del__(self):
        self.conect.close()