from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.String(50), nullable=True)
    car_number = db.Column(db.String(10), nullable=True)

    def __repr__(self):
        return f"Client {self.name} {self.surname}, Car: {self.car_number}"

    def to_dict(self):
        """Метод для конвертации модели в словарь."""
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "credit_card": self.credit_card,
            "car_number": self.car_number
        }


class Parking(db.Model):
    __tablename__ = 'parking'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    opened = db.Column(db.Boolean, default=True)
    count_places = db.Column(db.Integer, nullable=False)
    count_available_places = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Parking {self.address}, Available: {self.count_available_places}/{self.count_places}"

    def to_dict(self):
        """Преобразуем объект Parking в словарь для отправки в JSON."""
        return {
            'id': self.id,
            'address': self.address,
            'opened': self.opened,
            'count_places': self.count_places,
            'count_available_places': self.count_available_places
        }

class ClientParking(db.Model):
    __tablename__ = 'client_parking'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'), nullable=False)
    time_in = db.Column(db.DateTime, nullable=False)
    time_out = db.Column(db.DateTime, nullable=True)

    client = db.relationship('Client', backref='parkings')
    parking = db.relationship('Parking', backref='clients')

    def __repr__(self):
        return f"ClientParking Client:{self.client_id} Parking:{self.parking_id} In:{self.time_in} Out:{self.time_out}"