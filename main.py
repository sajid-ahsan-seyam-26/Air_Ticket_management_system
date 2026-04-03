import tkinter as tk
from tkinter import messagebox
tickets=[]
total_seats=50
booked_seats=0
book_counter=1
def add_ticket():
    global booked_seats
    global book_counter

    if booked_seats >=total_seats:
        messagebox.showwarning("No seats, sorry wait for the next free slot")
        return
    passenger_name=entry_name.get()
    passport_number=entry_passport.get()
    from_city=entry_from.get()
    to_city=entry_to.get()
    flight_number=entry_flight.get()
    seat_class=entry_class.get()
    seat_number = entry_seat.get()
    base_fare_text = entry_fare.get()

    if passenger_name=="" or passport_number
