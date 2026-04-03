import tkinter as tk
from tkinter import messagebox

tickets = []

total_seats = 50
booked_seats = 0
booking_counter = 1


def add_ticket():
    global booked_seats
    global booking_counter

    if booked_seats >= total_seats:
        messagebox.showwarning("No Seats", "Sorry, no seats available.")
        return

    passenger_name = entry_name.get()
    passport_number = entry_passport.get()
    from_city = entry_from.get()
    to_city = entry_to.get()
    flight_number = entry_flight.get()
    seat_class = entry_class.get()
    seat_number = entry_seat.get()
    base_fare_text = entry_fare.get()

    if passenger_name == "" or passport_number == "" or from_city == "" or to_city == "" or flight_number == "" or seat_class == "" or seat_number == "" or base_fare_text == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        base_fare = float(base_fare_text)
    except:
        messagebox.showerror("Error", "Base fare must be a number.")
        return

    if seat_class.lower() == "business":
        extra_charge = 2000
    else:
        extra_charge = 0

    total_fare = base_fare + extra_charge
    booking_id = "B" + str(booking_counter)

    ticket = {
        "booking_id": booking_id,
        "passenger_name": passenger_name,
        "passport_number": passport_number,
        "from_city": from_city,
        "to_city": to_city,
        "flight_number": flight_number,
        "seat_class": seat_class,
        "seat_number": seat_number,
        "base_fare": base_fare,
        "total_fare": total_fare
    }

    tickets.append(ticket)
    booked_seats = booked_seats + 1
    booking_counter = booking_counter + 1

    messagebox.showinfo("Success", "Ticket booked successfully.\nBooking ID: " + booking_id + "\nTotal Fare: " + str(total_fare))
    clear_fields()


def show_all_tickets():
    output_text.delete(1.0, tk.END)

    if len(tickets) == 0:
        output_text.insert(tk.END, "No ticket booking data found.")
    else:
        count = 1
        for ticket in tickets:
            output_text.insert(tk.END, "Ticket " + str(count) + "\n")
            output_text.insert(tk.END, "Booking ID      : " + ticket["booking_id"] + "\n")
            output_text.insert(tk.END, "Passenger Name  : " + ticket["passenger_name"] + "\n")
            output_text.insert(tk.END, "Passport Number : " + ticket["passport_number"] + "\n")
            output_text.insert(tk.END, "From            : " + ticket["from_city"] + "\n")
            output_text.insert(tk.END, "To              : " + ticket["to_city"] + "\n")
            output_text.insert(tk.END, "Flight Number   : " + ticket["flight_number"] + "\n")
            output_text.insert(tk.END, "Seat Class      : " + ticket["seat_class"] + "\n")
            output_text.insert(tk.END, "Seat Number     : " + ticket["seat_number"] + "\n")
            output_text.insert(tk.END, "Base Fare       : " + str(ticket["base_fare"]) + "\n")
            output_text.insert(tk.END, "Total Fare      : " + str(ticket["total_fare"]) + "\n")
            output_text.insert(tk.END, "------------------------------\n")
            count = count + 1


def search_ticket():
    search_booking_id = entry_search_booking.get()
    output_text.delete(1.0, tk.END)

    found = False

    for ticket in tickets:
        if ticket["booking_id"] == search_booking_id:
            output_text.insert(tk.END, "Ticket Found\n")
            output_text.insert(tk.END, "Booking ID      : " + ticket["booking_id"] + "\n")
            output_text.insert(tk.END, "Passenger Name  : " + ticket["passenger_name"] + "\n")
            output_text.insert(tk.END, "Passport Number : " + ticket["passport_number"] + "\n")
            output_text.insert(tk.END, "From            : " + ticket["from_city"] + "\n")
            output_text.insert(tk.END, "To              : " + ticket["to_city"] + "\n")
            output_text.insert(tk.END, "Flight Number   : " + ticket["flight_number"] + "\n")
            output_text.insert(tk.END, "Seat Class      : " + ticket["seat_class"] + "\n")
            output_text.insert(tk.END, "Seat Number     : " + ticket["seat_number"] + "\n")
            output_text.insert(tk.END, "Base Fare       : " + str(ticket["base_fare"]) + "\n")
            output_text.insert(tk.END, "Total Fare      : " + str(ticket["total_fare"]) + "\n")
            found = True
            break

    if found == False:
        output_text.insert(tk.END, "Ticket not found.")


def update_ticket():
    search_booking_id = entry_search_booking.get()

    new_name = entry_name.get()
    new_passport = entry_passport.get()
    new_from = entry_from.get()
    new_to = entry_to.get()
    new_flight = entry_flight.get()
    new_class = entry_class.get()
    new_seat = entry_seat.get()
    new_fare_text = entry_fare.get()

    if new_fare_text == "":
        messagebox.showerror("Error", "Please enter base fare.")
        return

    try:
        new_base_fare = float(new_fare_text)
    except:
        messagebox.showerror("Error", "Base fare must be a number.")
        return

    found = False

    for ticket in tickets:
        if ticket["booking_id"] == search_booking_id:
            if new_class.lower() == "business":
                extra_charge = 2000
            else:
                extra_charge = 0

            new_total_fare = new_base_fare + extra_charge

            ticket["passenger_name"] = new_name
            ticket["passport_number"] = new_passport
            ticket["from_city"] = new_from
            ticket["to_city"] = new_to
            ticket["flight_number"] = new_flight
            ticket["seat_class"] = new_class
            ticket["seat_number"] = new_seat
            ticket["base_fare"] = new_base_fare
            ticket["total_fare"] = new_total_fare

            messagebox.showinfo("Success", "Ticket information updated successfully.")
            found = True
            break

    if found == False:
        messagebox.showerror("Error", "Ticket not found.")


def cancel_ticket():
    global booked_seats

    search_booking_id = entry_search_booking.get()
    found = False

    for ticket in tickets:
        if ticket["booking_id"] == search_booking_id:
            tickets.remove(ticket)
            booked_seats = booked_seats - 1
            messagebox.showinfo("Success", "Ticket cancelled successfully.")
            found = True
            break

    if found == False:
        messagebox.showerror("Error", "Ticket not found.")


def show_available_seats():
    available_seats = total_seats - booked_seats
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Total Seats     : " + str(total_seats) + "\n")
    output_text.insert(tk.END, "Booked Seats    : " + str(booked_seats) + "\n")
    output_text.insert(tk.END, "Available Seats : " + str(available_seats) + "\n")


def show_total_sales():
    total_sales = 0

    for ticket in tickets:
        total_sales = total_sales + ticket["total_fare"]

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Total Ticket Sales : " + str(total_sales))


def search_by_passport():
    passport = entry_search_passport.get()
    output_text.delete(1.0, tk.END)

    found = False

    for ticket in tickets:
        if ticket["passport_number"] == passport:
            output_text.insert(tk.END, "Ticket Found\n")
            output_text.insert(tk.END, "Booking ID      : " + ticket["booking_id"] + "\n")
            output_text.insert(tk.END, "Passenger Name  : " + ticket["passenger_name"] + "\n")
            output_text.insert(tk.END, "Passport Number : " + ticket["passport_number"] + "\n")
            output_text.insert(tk.END, "From            : " + ticket["from_city"] + "\n")
            output_text.insert(tk.END, "To              : " + ticket["to_city"] + "\n")
            output_text.insert(tk.END, "Flight Number   : " + ticket["flight_number"] + "\n")
            output_text.insert(tk.END, "Seat Class      : " + ticket["seat_class"] + "\n")
            output_text.insert(tk.END, "Seat Number     : " + ticket["seat_number"] + "\n")
            output_text.insert(tk.END, "Base Fare       : " + str(ticket["base_fare"]) + "\n")
            output_text.insert(tk.END, "Total Fare      : " + str(ticket["total_fare"]) + "\n")
            output_text.insert(tk.END, "------------------------------\n")
            found = True

    if found == False:
        output_text.insert(tk.END, "No ticket found for this passport number.")


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_passport.delete(0, tk.END)
    entry_from.delete(0, tk.END)
    entry_to.delete(0, tk.END)
    entry_flight.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_seat.delete(0, tk.END)
    entry_fare.delete(0, tk.END)


root = tk.Tk()
root.title("Air Ticket Management System")
root.geometry("900x700")


label_title = tk.Label(root, text="Air Ticket Management System", font=("Arial", 18, "bold"))
label_title.pack(pady=10)


frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Passenger Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Passport Number").grid(row=1, column=0, padx=5, pady=5)
entry_passport = tk.Entry(frame_inputs, width=25)
entry_passport.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="From City").grid(row=2, column=0, padx=5, pady=5)
entry_from = tk.Entry(frame_inputs, width=25)
entry_from.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="To City").grid(row=3, column=0, padx=5, pady=5)
entry_to = tk.Entry(frame_inputs, width=25)
entry_to.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Flight Number").grid(row=4, column=0, padx=5, pady=5)
entry_flight = tk.Entry(frame_inputs, width=25)
entry_flight.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Seat Class").grid(row=5, column=0, padx=5, pady=5)
entry_class = tk.Entry(frame_inputs, width=25)
entry_class.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Seat Number").grid(row=6, column=0, padx=5, pady=5)
entry_seat = tk.Entry(frame_inputs, width=25)
entry_seat.grid(row=6, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Base Fare").grid(row=7, column=0, padx=5, pady=5)
entry_fare = tk.Entry(frame_inputs, width=25)
entry_fare.grid(row=7, column=1, padx=5, pady=5)


frame_search = tk.Frame(root)
frame_search.pack(pady=10)

tk.Label(frame_search, text="Search / Update / Cancel by Booking ID").grid(row=0, column=0, padx=5, pady=5)
entry_search_booking = tk.Entry(frame_search, width=20)
entry_search_booking.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_search, text="Search by Passport Number").grid(row=1, column=0, padx=5, pady=5)
entry_search_passport = tk.Entry(frame_search, width=20)
entry_search_passport.grid(row=1, column=1, padx=5, pady=5)


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Ticket", width=18, command=add_ticket).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Show All Tickets", width=18, command=show_all_tickets).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Search Ticket", width=18, command=search_ticket).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame_buttons, text="Update Ticket", width=18, command=update_ticket).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Cancel Ticket", width=18, command=cancel_ticket).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Available Seats", width=18, command=show_available_seats).grid(row=1, column=2, padx=5, pady=5)

tk.Button(frame_buttons, text="Total Sales", width=18, command=show_total_sales).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Search Passport", width=18, command=search_by_passport).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame_buttons, text="Clear Fields", width=18, command=clear_fields).grid(row=2, column=2, padx=5, pady=5)


output_text = tk.Text(root, width=100, height=20)
output_text.pack(pady=15)


root.mainloop()

