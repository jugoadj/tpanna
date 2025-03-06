from flask import Flask
import json
import datetime
import tempfile

app = Flask(__name__)

class WaterConsumption:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.file_path = f'./water{user_id}.json' if user_id else './water.json'
        self.water_data = self.read_water()

    def read_water(self):
        """Charge les données de consommation d'eau à partir du fichier"""
        try:
            with open(self.file_path, 'r') as f:
                data = f.read()
                return json.loads(data)
        except FileNotFoundError:
            return {"water": 0, "adding": []}

    def save_water(self):
        """Sauvegarde les données de consommation d'eau dans le fichier"""
        with open(self.file_path, 'w') as f:
            f.write(json.dumps(self.water_data))

    def add_water(self, quantity=10):
        """Ajoute de l'eau à la consommation"""
        self.water_data["water"] += quantity
        self.water_data["adding"].append({'added_at': str(datetime.datetime.now()), 'quantity': quantity})
        self.save_water()

    def get_water(self):
        """Retourne la consommation d'eau actuelle"""
        return self.water_data

    def check_alert(self):
        """Vérifie si l'alerte doit être déclenchée (consommation inférieure à un seuil)"""
        if self.water_data["water"] < 10:
            return True
        return False

class Alert:
    def __init__(self, water_consumption: WaterConsumption):
        self.water_consumption = water_consumption

    def trigger_alert(self):
        """Vérifie si l'alerte doit être déclenchée et enregistre la notification"""
        if self.water_consumption.check_alert():
            Logger.log(f"Alerte, manque d'eau pour le profile {self.water_consumption.user_id if self.water_consumption.user_id else 'global'}")

class Logger:
    @staticmethod
    def log(message):
        """Enregistre les messages de log dans un fichier de notifications"""
        with open("notification.log", "a") as logfile:
            logfile.write(f'{datetime.datetime.now()}: {message}\n')

# Routes de l'application
@app.route('/add_water', methods=['GET'])
def add_water():
    water = WaterConsumption()
    water.add_water(10)
    return water.get_water()

@app.route('/water', methods=['GET'])
def get_water():
    water = WaterConsumption()
    filename = tempfile.mktemp()
    logfile = open(filename, 'a')
    logfile.write(f'getting water at {datetime.datetime.now()}\n')
    logfile.close()
    return water.get_water()

@app.route('/add_water/<user_id>', methods=['GET'])
def add_water_user(user_id):
    water = WaterConsumption(user_id=user_id)
    water.add_water(10)
    return water.get_water()

@app.route('/add_alert/<user_id>', methods=['GET'])
def check_alert(user_id):
    water = WaterConsumption(user_id=user_id)
    alert = Alert(water)
    alert.trigger_alert()
    return 'Alert triggered if needed'

if __name__ == '__main__':
    app.run(debug=True)
