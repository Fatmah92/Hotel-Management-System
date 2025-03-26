# Assigment2
# Hotel Management System Implementation
# Parent class: Payment (Base class for inheritance)
class Payment:
   def __init__(self, amount):
       self._amount = amount  # Protected attribute to store the payment amount


   def get_amount(self):
       return self._amount  # Getter method to retrieve the payment amount


   def set_amount(self, amount):
       self._amount = amount  # Setter method to update the payment amount
     def __str__(self):
       return f"Payment Amount: {self._amount}"  # String representation of the payment object


# Child classes (Inheritance from Payment)
class CreditCardPayment(Payment):
   def __init__(self, amount, card_number):
       super().__init__(amount)  # Calling the parent constructor
       self.__card_number = card_number  # Private attribute for card number
  
   def __str__(self):
       return f"Credit Card Payment - Amount: {self._amount}, Card: ****{self.__card_number[-4:]}"  # Masked card number for security


class CashPayment(Payment):
   def __init__(self, amount, currency):
       super().__init__(amount)  # Calling the parent constructor
       self.currency = currency  # Storing the currency type
  
   def __str__(self):
       return f"Cash Payment - Amount: {self._amount} {self.currency}"  # String representation of cash payment


# Invoice class (Composition with Payment)
class Invoice:
   def __init__(self, invoice_id, payment):
       self.invoice_id = invoice_id  # Unique identifier for the invoice
       self.__payment = payment  # Private attribute linking an invoice to a payment


   def get_payment(self):
       return self.__payment  # Getter method to access payment details
  
   def __str__(self):
       return f"Invoice {self.invoice_id} - {self.__payment}"  # String representation of an invoice


# Reservation class (Binary association with Invoice)
class Reservation:
   def __init__(self, reservation_id, invoice):
       self.reservation_id = reservation_id  # Unique identifier for the reservation
       self.invoice = invoice  # Association with an Invoice instance
  
   def __str__(self):
       return f"Reservation {self.reservation_id} - Invoice: {self.invoice}"  # String representation of a reservation


# Room class (Composition with Hotel)
class Room:
   def __init__(self, room_number):
       self.room_number = room_number  # Unique room number
  
   def __str__(self):
       return f"Room {self.room_number}"  # String representation of a room


# Hotel class (Aggregation with Guest, Composition with Room)
class Hotel:
   def __init__(self, name):
       self.name = name  # Name of the hotel
       self.rooms = []  # Composition: Hotel owns rooms


   def add_room(self, room):
       self.rooms.append(room)  # Method to add a room to the hotel
  
   def __str__(self):
       return f"Hotel {self.name} - Rooms: {[str(room) for room in self.rooms]}"  # String representation of the hotel


# Guest class (Aggregation with Hotel, Binary with Payment, Feedback)
class Guest:
   def __init__(self, guest_id, name):
       self.guest_id = guest_id  # Unique identifier for the guest
       self.name = name  # Guest's name
       self.payments = []  # Binary association with Payment
       self.feedbacks = [] # Binary association with Feedback
  
   def add_payment(self, payment):
       self.payments.append(payment)  # Method to add a payment to the guest's record
  
   def add_feedback(self, feedback):
       self.feedbacks.append(feedback)  # Method to add feedback left by the guest
  
   def __str__(self):
       return f"Guest {self.guest_id} - {self.name}"  # String representation of the guest


# Feedback class (Binary association with Guest)
class Feedback:
   def __init__(self, feedback_id, message):
       self.feedback_id = feedback_id  # Unique identifier for the feedback
       self.message = message  # Feedback message left by the guest
  
   def __str__(self):
       return f"Feedback {self.feedback_id}: {self.message}"  # String representation of feedback


# Example usage
if __name__ == "__main__":
   # Create Hotel
   hotel = Hotel("Grand Plaza")
     # Create Rooms
   room1 = Room(101)
   room2 = Room(102)
   hotel.add_room(room1)  # Adding room 101 to the hotel
   hotel.add_room(room2)  # Adding room 102 to the hotel
     # Create Guest
   guest = Guest(1, "Alice")  # Creating a guest named Alice
     # Create Payment & Invoice
   payment1 = CreditCardPayment(200, "1234567890123456")  # Creating a credit card payment
   invoice1 = Invoice(101, payment1)  # Linking the payment to an invoice
   # Create Reservation
   reservation1 = Reservation(1, invoice1)  # Creating a reservation linked to an invoice
    
 # Guest makes a payment
   guest.add_payment(payment1)  # Associating the payment with the guest
   # Guest leaves feedback
   feedback1 = Feedback(1, "Great stay!")  # Creating feedback from the guest
   guest.add_feedback(feedback1)  # Associating the feedback with the guest
   
# Print information
   print(hotel)  # Display hotel details
   print(guest)  # Display guest details
   print(reservation1)  # Display reservation details
   print(feedback1)  # Display feedback details

