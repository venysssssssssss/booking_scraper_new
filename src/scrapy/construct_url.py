def construct_url(checkin_date, checkout_date, destination, adults, rooms, children, currency):
    """
    Constructs a URL for booking.com search results based on the provided check-in date, check-out date, and destination.

    Args:
        checkin_date (str): The check-in date in the format 'YYYY-MM-DD'.
        checkout_date (str): The check-out date in the format 'YYYY-MM-DD'.
        destination (str): The destination for the search.

    Returns:
        str: The constructed URL.

    Raises:
        Exception: If an error occurs during URL construction.
    """
    try:
        url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency={currency}&ss={destination}&ssne={destination}&ssne_untouched={destination}&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults={adults}&no_rooms={rooms}&group_children={children}&sb_travel_purpose=leisure'
        return url
    except Exception as e:
        print(f'An error occurred: {e}')
