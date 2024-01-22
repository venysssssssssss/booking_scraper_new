from unittest.mock import Mock

from selenium.webdriver.common.by import By


def test_extract_hotel_info():
    # Positive case 1: All elements present
    hotel_element_1 = create_hotel_element(
        title='Hotel A',
        price='$100',
        score='8.5',
        avg_review='Good',
        reviews_count='100 reviews',
    )
    expected_result_1 = {
        'hotel': 'Hotel A',
        'price': '$100',
        'score': '8.5',
        'avg review': 'Good',
        'reviews count': '100',
    }
    assert extract_hotel_info(hotel_element_1) == expected_result_1

    # Positive case 2: Some elements missing
    hotel_element_2 = create_hotel_element(
        title='Hotel B',
        price=None,
        score='9.0',
        avg_review=None,
        reviews_count='50 reviews',
    )
    expected_result_2 = {
        'hotel': 'Hotel B',
        'price': None,
        'score': '9.0',
        'avg review': None,
        'reviews count': '50',
    }
    assert extract_hotel_info(hotel_element_2) == expected_result_2

    # Positive case 3: All elements missing
    def extract_hotel_info(hotel_element):
        # Extract hotel information from the hotel element
        # Implementation goes here
        pass

    hotel_element_3 = create_hotel_element(
        title=None, price=None, score=None, avg_review=None, reviews_count=None
    )
    expected_result_3 = {
        'hotel': None,
        'price': None,
        'score': None,
        'avg review': None,
        'reviews count': None,
    }
    assert extract_hotel_info(hotel_element_3) == expected_result_3


def create_hotel_element(title, price, score, avg_review, reviews_count):
    # Create a mock hotel element with specified attributes
    hotel_element = Mock()
    hotel_element.find_element = Mock(side_effect=find_element_mock)
    hotel_element.get_attribute = Mock(side_effect=get_attribute_mock)
    hotel_element.title = title
    hotel_element.price = price
    hotel_element.score = score
    hotel_element.avg_review = avg_review
    hotel_element.reviews_count = reviews_count
    return hotel_element


def find_element_mock(by, xpath):
    # Mock implementation of find_element method
    if xpath == './/div[@data-testid="title"]':
        return Mock()
    elif xpath == './/span[@data-testid="price-and-discounted-price"]':
        return Mock()
    elif xpath == './/div[@data-testid="review-score"]/div[1]':
        return Mock()
    elif xpath == './/div[@data-testid="review-score"]/div[2]/div[1]':
        return Mock()
    elif xpath == './/div[@data-testid="review-score"]/div[2]/div[2]':
        return Mock()
    else:
        return None


def get_attribute_mock(attribute):
    # Mock implementation of get_attribute method
    if attribute == 'innerText':
        return Mock()
    else:
        return None
