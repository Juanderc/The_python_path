from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta

app_bp = Blueprint("airport", __name__, url_prefix="/api/")

tickets = []
ticketsIds = []
valid_tickets = {}
flights = {"dates": []}


class Methods():

    def Tickets(self,):
        data = request.json.get("event")

        flightN = data["flightNumber"]
        ticketI = data["ticketId"]
        seatN = data["seatNumber"]

        if len(tickets) == 0:  # this is the first evaluation that always execute in the first interaction
            tickets.append(data)
            # it save the ticked-id for future evaluation
            ticketsIds.append(ticketI)
            # it save the date in this format({"flight-number:[seat-number-list]"}) for a future evaluation
            valid_tickets[flightN] = [seatN]

            return jsonify({"status": "success"}), 200

        else:

            if flightN in valid_tickets.keys():  # if the flight-number is on the object it pass

                if ticketI in ticketsIds:  # It evaluate the disponibility of the ticked-id
                    return jsonify(status="failed", reason="ticketId already exists"), 400

                # it evaluate the list that correspond to the flight-number
                elif seatN in valid_tickets[f"{flightN}"]:
                    return jsonify(status="failed", reason="seatNumber already exists"), 400

                else:
                    tickets.append(data)
                    ticketsIds.append(data["ticketId"])

                    valid_tickets[flightN].append(seatN)

                    return jsonify({"status": "success"}), 200

            elif flightN not in valid_tickets.keys():

                tickets.append(data)
                ticketsIds.append(data["ticketId"])

                valid_tickets[flightN] = [seatN]

                return jsonify({"status": "success"}), 200

            elif len(tickets) == 300:
                return jsonify({"status": "full"})

    def Flights(self,):
        dates = []

        startDate = request.args.get('startDate')
        endDate = request.args.get('endDate')

        date_order = list(request.args)

        if startDate is None or endDate is None:
            who_none = ""
            if startDate is None:
                who_none = "startDate"
            elif endDate is None:
                who_none = "endDate"

            return jsonify(status="failed", reason=f"{who_none} is empty"), 400

        elif date_order[0] == "endDate":
            return jsonify(status="failed", reason="endDate cannot be before startDate"), 400

        else:
            try:
                start_date_formated = datetime.strptime(startDate, "%Y-%m-%d")
            except ValueError:
                return jsonify(status="failed", reason="startDate format is invalid")

            try:
                end_date_formated = datetime.strptime(endDate, "%Y-%m-%d")
            except ValueError:
                return jsonify(status="failed", reason="endDate format is invalid")

            start_day = start_date_formated.strftime("%d")
            end_day = end_date_formated.strftime("%d")

            # this go throw a list of date from start to end
            for d in range(int(start_day) - 1, int(end_day)):
                future_date = start_date_formated + timedelta(days=d)
                dates.append(future_date.strftime("%Y-%m-%d"))

            for t in tickets:

                for d in dates:

                    info = {"date": t["flightDate"], "flights": [
                        {"flighNumber": t["flightNumber"],
                         "revenue":t["ticketCost"], "occupiedSeats":valid_tickets[t["flightNumber"]]
                         }]}

                    if info not in flights["dates"] and t["flightDate"] in dates:
                        flights["dates"].append(info)

                    for f in flights["dates"]:

                        if f["date"] not in dates:
                            flights["dates"].pop(flights["dates"].index(f))

            flights["dates"].sort(key=lambda x: x["date"])
            return jsonify(flights)


@app_bp.route("tickets", methods=['POST'])
def Tickets():
    tickets = Methods()
    return tickets.Tickets()


@app_bp.route("flights", methods=['GET'])
def Flights():
    flights = Methods()
    return flights.Flights()
