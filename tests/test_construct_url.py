from src.scrapy.construct_url import construct_url


def test_construct_url():
    # Test case 1: Check-in date, check-out date, and destination are valid
    checkin_date = '2022-01-01'
    checkout_date = '2022-01-02'
    destination = 'New York'
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    expected_url = 'https://www.booking.com/searchresults.en-us.html?checkin=2022-01-01&checkout=2022-01-02&selected_currency=USD&ss=New York&ssne=New York&ssne_untouched=New York&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    assert (
        construct_url(
            checkin_date,
            checkout_date,
            destination,
            adults,
            rooms,
            children,
            currency,
        )
        == expected_url
    )

    # Test case 2: Check-in date, check-out date, and destination contain special characters
    checkin_date = '2022-01-01'
    checkout_date = '2022-01-02'
    destination = 'Los Angeles, CA'
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    expected_url = 'https://www.booking.com/searchresults.en-us.html?checkin=2022-01-01&checkout=2022-01-02&selected_currency=USD&ss=Los Angeles, CA&ssne=Los Angeles, CA&ssne_untouched=Los Angeles, CA&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    assert (
        construct_url(
            checkin_date,
            checkout_date,
            destination,
            adults,
            rooms,
            children,
            currency,
        )
        == expected_url
    )

    # Test case 3: Check-in date, check-out date, and destination are empty strings
    checkin_date = ''
    checkout_date = ''
    destination = ''
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    expected_url = 'https://www.booking.com/searchresults.en-us.html?checkin=&checkout=&selected_currency=USD&ss=&ssne=&ssne_untouched=&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    assert (
        construct_url(
            checkin_date,
            checkout_date,
            destination,
            adults,
            rooms,
            children,
            currency,
        )
        == expected_url
    )

    # Test case 4: Check-in date, check-out date, and destination are None
    checkin_date = None
    checkout_date = None
    destination = None
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    expected_url = 'https://www.booking.com/searchresults.en-us.html?checkin=None&checkout=None&selected_currency=USD&ss=None&ssne=None&ssne_untouched=None&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    assert (
        construct_url(
            checkin_date,
            checkout_date,
            destination,
            adults,
            rooms,
            children,
            currency,
        )
        == expected_url
    )

    # Test case 5: Check-in date, check-out date, and destination are invalid
    checkin_date = '2022-01-01'
    checkout_date = '2022-01-02'
    destination = 12345
    adults = 1
    rooms = 1
    children = 0
    currency = 'USD'
    expected_url = 'https://www.booking.com/searchresults.en-us.html?checkin=2022-01-01&checkout=2022-01-02&selected_currency=USD&ss=12345&ssne=12345&ssne_untouched=12345&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
    assert (
        construct_url(
            checkin_date,
            checkout_date,
            destination,
            adults,
            rooms,
            children,
            currency,
        )
        == expected_url
    )

    print('All test cases passed!')


test_construct_url()
