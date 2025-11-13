import requests
from django.conf import settings


def get_cars(show_all=False, page=0, size=10):
    params = {"showAll": show_all, "page": page, "size": size}
    r = requests.get(f"{settings.CARS_SERVICE_URL}/cars", params=params)
    r.raise_for_status()
    return r.json()


def get_car(car_uid):
    r = requests.get(f"{settings.CARS_SERVICE_URL}/cars/{car_uid}")
    r.raise_for_status()
    return r.json()


def reserve_car(car_uid):
    r = requests.post(f"{settings.CARS_SERVICE_URL}/cars/{car_uid}/reserve")
    r.raise_for_status()


def release_car(car_uid):
    r = requests.post(f"{settings.CARS_SERVICE_URL}/cars/{car_uid}/release")
    r.raise_for_status()


def create_payment(price):
    r = requests.post(f"{settings.PAYMENT_SERVICE_URL}/payment", json={"price": price})
    r.raise_for_status()
    return r.json()


def cancel_payment(payment_uid):
    requests.delete(f"{settings.PAYMENT_SERVICE_URL}/payment/{payment_uid}")


def get_payment(payment_uid):
    r = requests.get(f"{settings.PAYMENT_SERVICE_URL}/payment/{payment_uid}")
    r.raise_for_status()
    return r.json()


def create_rental(username, car_uid, payment_uid, date_from, date_to):
    data = {"carUid": car_uid, "paymentUid": payment_uid, "dateFrom": date_from, "dateTo": date_to}
    headers = {"X-User-Name": username}
    r = requests.post(f"{settings.RENTAL_SERVICE_URL}/rental", json=data, headers=headers)
    r.raise_for_status()
    return r.json()


def get_rentals(username):
    headers = {"X-User-Name": username}
    r = requests.get(f"{settings.RENTAL_SERVICE_URL}/rental", headers=headers)
    r.raise_for_status()
    return r.json()


def get_rental(username, rental_uid):
    headers = {"X-User-Name": username}
    r = requests.get(f"{settings.RENTAL_SERVICE_URL}/rental/{rental_uid}", headers=headers)
    r.raise_for_status()
    return r.json()


def finish_rental(username, rental_uid):
    headers = {"X-User-Name": username}
    r = requests.post(f"{settings.RENTAL_SERVICE_URL}/rental/{rental_uid}/finish", headers=headers)
    r.raise_for_status()


def cancel_rental(username, rental_uid):
    headers = {"X-User-Name": username}
    r = requests.delete(f"{settings.RENTAL_SERVICE_URL}/rental/{rental_uid}", headers=headers)
    r.raise_for_status()
