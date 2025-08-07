from .models import CarMake, CarModel
import datetime

def initiate():
    if CarMake.objects.exists(): return
    makes = {}
    for name, desc in [
        ("NISSAN","Great cars. Japanese technology"),
        ("Mercedes","Great cars. German technology"),
        ("Audi","Great cars. German technology"),
        ("Kia","Great cars. Korean technology"),
        ("Toyota","Great cars. Japanese technology"),
    ]:
        makes[name] = CarMake.objects.create(name=name, description=desc)

    y = datetime.date.today().year
    data = [
      ("Pathfinder","SUV","NISSAN"),("Qashqai","SUV","NISSAN"),("XTRAIL","SUV","NISSAN"),
      ("A-Class","SUV","Mercedes"),("C-Class","SUV","Mercedes"),("E-Class","SUV","Mercedes"),
      ("A4","SUV","Audi"),("A5","SUV","Audi"),("A6","SUV","Audi"),
      ("Sorrento","SUV","Kia"),("Carnival","SUV","Kia"),("Cerato","SEDAN","Kia"),
      ("Corolla","SEDAN","Toyota"),("Camry","SEDAN","Toyota"),("Kluger","SUV","Toyota"),
    ]
    for name, t, mk in data:
        CarModel.objects.create(name=name, type=t, year=y, car_make=makes[mk])
