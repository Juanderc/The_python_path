import unittest
import requests as req
import json
import time


tickets_url = "http://127.0.0.1:5000/api/tickets"
flights_url = "http://127.0.0.1:5000/api/flights?startDate=2021-11-01&endDate=2021-11-03"

info = [{

    "event": {
        "ticketId": 2,
        "flightDate": "2021-11-02",
        "flightNumber": "AC1",
        "seatNumber": "8B",
        "ticketCost": 300000
    }
},
    {

    "event": {
        "ticketId": 3,
        "flightDate": "2021-11-03",
        "flightNumber": "AC1",
        "seatNumber": "2B",
        "ticketCost": 100000
    }
}, {

    "event": {
        "ticketId": 1,
        "flightDate": "2021-11-04",
        "flightNumber": "AC2",
        "seatNumber": "8B",
        "ticketCost": 400000
    },

},
    {

    "event": {
        "ticketId": 6,
        "flightDate": "2021-11-01",
        "flightNumber": "AC1",
        "seatNumber": "7B",
        "ticketCost": 200000
    }
}]


class Test(unittest.TestCase):

    def tickets_test(self):
        for x in info:
            resp = req.post(tickets_url, json=x)

            if resp.status_code == 200:
                print("Test 1 completed")
            else:
                print(resp.json())

    def flights_test(self):
        resp = req.get(flights_url)

        if resp.status_code == 200:
            print(resp.json())
        else:
            print(resp.json())


if __name__ == "__main__":

    test = Test()
    test.tickets_test()
    time.sleep(2)
    test.flights_test()
