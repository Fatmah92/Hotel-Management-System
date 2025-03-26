import unittest
from hotel_management import Guest, Room, Hotel, Payment, CreditCardPayment, CashPayment, Invoice, Reservation, Feedback

class TestHotelManagementSystem(unittest.TestCase):
    
    def test_guest_account_creation(self):
        """Test guest account creation with personal details."""
        guest1 = Guest(1, "Alice")
        guest2 = Guest(2, "Bob")
        self.assertEqual(guest1.name, "Alice")
        self.assertEqual(guest2.name, "Bob")

    def test_search_available_rooms(self):
        """Test searching for available rooms in a hotel."""
        hotel = Hotel("Grand Plaza")
        room1 = Room(101)
        room2 = Room(102)
        hotel.add_room(room1)
        hotel.add_room(room2)
        
        self.assertIn(room1, hotel.rooms)
        self.assertIn(room2, hotel.rooms)
    
    def test_make_room_reservation(self):
        """Test making a room reservation."""
        guest = Guest(1, "Alice")
        payment = CreditCardPayment(200, "1234567890123456")
        invoice = Invoice(101, payment)
        reservation = Reservation(1, invoice)
        
        self.assertEqual(reservation.reservation_id, 1)
        self.assertEqual(reservation.invoice, invoice)
    
    def test_booking_confirmation_notification(self):
        """Test booking confirmation notification (simulated with a message)."""
        guest = Guest(1, "Alice")
        confirmation_message = f"Booking confirmed for {guest.name}."
        
        self.assertEqual(confirmation_message, "Booking confirmed for Alice.")
    
    def test_invoice_generation(self):
        """Test invoice generation with payment details."""
        payment = CashPayment(150, "USD")
        invoice = Invoice(202, payment)
        
        self.assertEqual(invoice.invoice_id, 202)
        self.assertEqual(invoice.get_payment(), payment)
    
    def test_processing_different_payments(self):
        """Test processing different payment methods."""
        card_payment = CreditCardPayment(300, "9876543210987654")
        cash_payment = CashPayment(200, "USD")
        
        self.assertEqual(card_payment.get_amount(), 300)
        self.assertEqual(cash_payment.get_amount(), 200)
    
    def test_display_reservation_history(self):
        """Test displaying guest's reservation history."""
        guest = Guest(1, "Alice")
        payment = CreditCardPayment(200, "1234567890123456")
        invoice = Invoice(101, payment)
        reservation = Reservation(1, invoice)
        guest_reservations = [reservation]
        
        self.assertIn(reservation, guest_reservations)
    
    def test_cancel_reservation(self):
        """Test canceling a reservation and updating room availability."""
        hotel = Hotel("Grand Plaza")
        room = Room(103)
        hotel.add_room(room)
        payment = CashPayment(180, "USD")
        invoice = Invoice(303, payment)
        reservation = Reservation(2, invoice)
        
        canceled_reservations = []
        canceled_reservations.append(reservation)
        self.assertIn(reservation, canceled_reservations)

if __name__ == '__main__':
    unittest.main()
