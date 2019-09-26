def get_formatted_name(first, last, middle=''):
    """Create formatted full name."""
    if middle:
        full_name = '{} {} {}'.format(first, middle, last)
    else:
        full_name = '{} {}'.format(first, last)
    return full_name.title()
