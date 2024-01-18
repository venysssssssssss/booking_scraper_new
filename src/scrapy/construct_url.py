def construct_url(checkin_date, checkout_date, destination):
    try:
        url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss={destination}&ssne={destination}&ssne_untouched={destination}&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
        return url
    except Exception as e:
        print(f"An error occurred: {e}")
