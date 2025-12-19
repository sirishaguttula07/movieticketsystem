

from flask import Flask, render_template, request

app = Flask(__name__)

# Home page – booking form
@app.route('/')
def index():
    return render_template('index.html')


# Booking logic
@app.route('/book', methods=['POST']) 
def book_ticket():

    # ----------- INPUT FROM FRONTEND -----------
    age = int(request.form['age'])
    is_student = request.form['is_student'] == "True"
    movie_type = request.form['movie_type']
    day = int(request.form['day'])

    print("------- MOVIE TICKET BILLING SYSTEM -------")

    # ----------- STATUS CHECK -----------
    if age >= 18:
        status = "Adult"
    else:
        status = "Child"

    # ----------- BASE PRICE -----------
    if age < 18:
        base_price = 150
    else:
        base_price = 250

    # ----------- MOVIE TYPE CHARGES -----------
    if movie_type == "Normal":
        extra = 0
    elif movie_type == "3D":
        extra = 100
    elif movie_type == "IMAX":
        extra = 200
    else:
        extra = 0

    # ----------- STUDENT DISCOUNT (NESTED IF) -----------
    discount = 0
    if age > 18:
        if is_student:
            discount = 50
    else:
        if is_student:
            discount = 70

    # ----------- OFFER (TERNARY OPERATOR) -----------
    offer = "Eligible for Weekend Offer" if day >= 6 else "Weekday – No Offer"

    # ----------- DAY NAME (MATCH CASE) -----------
    match day:
        case 1:
            day_name = "Monday"
        case 2:
            day_name = "Tuesday"
        case 3:
            day_name = "Wednesday"
        case 4:
            day_name = "Thursday"
        case 5:
            day_name = "Friday"
        case 6:
            day_name = "Saturday"
        case 7:
            day_name = "Sunday"
        case _:
            day_name = "Invalid Day"

    # ----------- FINAL BILL -----------
    final_amount = (base_price + extra) - discount

    # ----------- SEND DATA TO RESULT PAGE -----------
    return render_template(
        'result.html',
        status=status,
        base_price=base_price,
        movie_type=movie_type,
        extra=extra,
        discount=discount,
        offer=offer,
        day_name=day_name,
        final_amount=final_amount
    )


if __name__ == '__main__':
    app.run(debug=True)
