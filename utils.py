import csv

import logging
log = logging.getLogger(__name__)  # pylint: disable=invalid-name


def get_data():
    data = {}
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data['categories'] = {
            i: category for i, category in enumerate(next(reader)[1:])
        }
        data['countries'] = {}
        for i, row in enumerate(reader):
            try:
                country = row[0]
                for category, value in enumerate(row[1:]):
                    data['countries'][country] = validate_value(value)
            except (ValueError, TypeError):
                log.debug('Problem with line %d: ', i, exc_info=True)

    return data


def validate_value(value):
    try:
        return float(value.strip('%')) / 100
    except ValueError:
        return ''
