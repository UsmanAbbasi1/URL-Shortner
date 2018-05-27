import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    """
    :param instance: instance of type 'KirrURL'
    :param size: size of code to be generated
    :return: unique code
    """
    new_code = code_generator()

    # We are using __class__ here because importing 'KirrURL' model will create circular import
    if instance.__class__.objects.filter(shortcode=new_code).exists():
        create_shortcode(instance, size=size)

    return new_code
