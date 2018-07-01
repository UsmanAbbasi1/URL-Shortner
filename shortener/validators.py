from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    validation1 = True
    validation2 = True

    try:
        url_validator(value)
    except:
        validation1 = False

    try:
        # Add 'http://' to url to make urls without 'http' valid
        url_validator('http://' + value)
    except:
        validation2 = False

    # If even after adding 'http', validation fails, we want to raise ValidationError
    if not validation1 and not validation2:
        raise ValidationError("Invalid value for this field!")

    return value


def validate_dot_com(value):
    if not '.com' in value:
        raise ValidationError('This is not valid because of no .com')
