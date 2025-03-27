class Guest:
    """Represents a guest in the hotel system, storing personal details and reservation history."""
    def __init__(self, guest_id, name, email, contact_info, loyalty_status=False):
        self.guest_id = guest_id  # Unique identifier for the guest
        self.name = name  # Guest's name
        self.email = email  # Guest's email address
        self.contact_info = contact_info  # Contact details
        self.loyalty_status = loyalty_status  # Boolean indicating if the guest is a loyalty program member
        self.reservations = []  # List to store guest's reservation history

    def update_info(self, email=None, contact_info=None, loyalty_status=None):
        """Allows updating guest details."""
        if email:
            self.email = email
        if contact_info:
            self.contact_info = contact_info
        if loyalty_status is not None:
            self.loyalty_status = loyalty_status

    def add_reservation(self, reservation):
        """Adds a reservation to the guest's history."""
        self.reservations.append(reservation)

class Room:
    """Represents a hotel room with an ID, type, and amenities."""
    def __init__(self, room_id, room_type, amenities):
        self.room_id = room_id  # Unique room number or ID
        self.room_type = room_type  # Type of room (e.g., Single, Double, Suite)
        self.amenities = amenities  # List of room amenities (e.g., Wi-Fi, TV, Mini-bar)
        self.available = True  # Availability status

    def book_room(self):
        """Marks the room as booked."""
        self.available = False

    def cancel_booking(self):
        """Marks the room as available again after cancellation."""
        self.available = True

class Hotel:
    """Represents a hotel with a name, rooms, and reservations."""
    def __init__(self, name):
        self.name = name  # Name of the hotel
        self.rooms = []  # List of all rooms in the hotel
        self.reservations = []  # List of all reservations
    
    def add_room(self, room):
        """Adds a new room to the hotel's inventory."""
        self.rooms.append(room)

    def search_available_rooms(self, room_type=None, amenities=None):
        """Finds and returns available rooms matching the given criteria."""
        return [room for room in self.rooms if room.available and 
                (room_type is None or room.room_type == room_type) and 
                (amenities is None or all(a in room.amenities for a in amenities))]

    def make_reservation(self, guest, room, check_in, check_out, payment):
        """Creates a new reservation if the room is available."""
        if room.available:
            room.book_room()
            invoice = Invoice(len(self.reservations) + 1, payment)
            reservation = Reservation(len(self.reservations) + 1, guest, room, check_in, check_out, invoice)
            self.reservations.append(reservation)
            guest.add_reservation(reservation)
            return reservation
        return None

    def cancel_reservation(self, reservation):
        """Cancels a reservation and marks the room as available again."""
        reservation.room.cancel_booking()
        self.reservations.remove(reservation)

class Payment:
    """Base class for handling payments."""
    def __init__(self, amount):
        self.amount = amount  # Payment amount
    
    def get_amount(self):
        """Returns the payment amount."""
        return self.amount

class CreditCardPayment(Payment):
    """Handles payments made via credit card."""
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number  # Credit card number

class CashPayment(Payment):
    """Handles cash payments with specified currency."""
    def __init__(self, amount, currency):
        super().__init__(amount)
        self.currency = currency  # Currency type (e.g., USD, EUR)

class Invoice:
    """Represents an invoice for a reservation, storing payment details."""
    def __init__(self, invoice_id, payment, nightly_rate=0, extra_charges=0, discount=0):
        self.invoice_id = invoice_id  # Unique identifier for the invoice
        self.payment = payment  # Payment details
        self.nightly_rate = nightly_rate  # Cost per night
        self.extra_charges = extra_charges  # Additional charges (e.g., minibar, room service)
        self.discount = discount  # Any applied discount
        self.total_amount = (nightly_rate + extra_charges - discount)  # Total amount to be paid
    
    def get_payment(self):
        """Returns the associated payment details."""
        return self.payment

class Reservation:
    """Represents a hotel room reservation."""
    def __init__(self, reservation_id, guest, room, check_in, check_out, invoice):
        self.reservation_id = reservation_id  # Unique reservation ID
        self.guest = guest  # Guest who made the reservation
        self.room = room  # Room assigned to the reservation
        self.check_in = check_in  # Check-in date
        self.check_out = check_out  # Check-out date
        self.invoice = invoice  # Associated invoice

class Feedback:
    """Allows guests to leave feedback about their stay."""
    def __init__(self, guest, comments):
        self.guest = guest  # Guest providing feedback
        self.comments = comments  # Feedback text/comments
