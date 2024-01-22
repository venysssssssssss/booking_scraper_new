from src.scrapy.extract_hotel_info import extract_hotel_info


def test_extract_hotel_info_with_price(self):
    # Create a mock hotel element with price data
    class MockHotelElement:
        def find_element(self, *args):
            return MockElement()

    class MockElement:
        def get_attribute(self, attr):
            if attr == 'innerText':
                if args[0] == 'price':
                    return '$100'
                return 'Hotel Name'
            return None

    hotel = MockHotelElement()
    expected_result = {
        'hotel': 'Hotel Name',
        'price': '$100',
        'score': None,
        'avg review': None,
        'reviews count': None,
    }

    result = extract_hotel_info(hotel)
    self.assertEqual(result, expected_result)


def test_extract_hotel_info_with_score_and_reviews(self):
    # Create a mock hotel element with score and reviews data
    class MockHotelElement:
        def find_element(self, *args):
            return MockElement()

    class MockElement:
        def get_attribute(self, attr):
            if attr == 'innerText':
                if args[0] == 'score':
                    return '8.5'
                elif args[0] == 'reviews':
                    return '1000 reviews'
                return 'Hotel Name'
            return None

    hotel = MockHotelElement()
    expected_result = {
        'hotel': 'Hotel Name',
        'price': None,
        'score': '8.5',
        'avg review': None,
        'reviews count': '1000 reviews',
    }

    result = extract_hotel_info(hotel)
    self.assertEqual(result, expected_result)


def test_extract_hotel_info_with_avg_review(self):
    # Create a mock hotel element with average review data
    class MockHotelElement:
        def find_element(self, *args):
            return MockElement()

    class MockElement:
        def get_attribute(self, attr):
            if attr == 'innerText':
                if args[0] == 'avg_review':
                    return '4.2'
                return 'Hotel Name'
            return None

    hotel = MockHotelElement()
    expected_result = {
        'hotel': 'Hotel Name',
        'price': None,
        'score': None,
        'avg review': '4.2',
        'reviews count': None,
    }

    result = extract_hotel_info(hotel)
    self.assertEqual(result, expected_result)
