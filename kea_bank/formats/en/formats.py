DATE_FORMAT = 'd-m-Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'Y-m-d H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'F j'
SHORT_DATE_FORMAT = 'm/d/Y'
SHORT_DATETIME_FORMAT = 'm/d/Y P'
FIRST_DAY_OF_WEEK = 1

DATE_INPUT_FORMATS = (
    '%Y-%m-%d',     # '21-03-2014'
)
TIME_INPUT_FORMATS = (
    '%H:%M:%S',     # '17:59:59'
    '%H:%M',        # '17:59'
)
DATETIME_INPUT_FORMATS = (
    '%d-%m-%Y %H:%M',     # '21-03-2014 17:59'
)

DECIMAL_SEPARATOR = u','
THOUSAND_SEPARATOR = u'.'
NUMBER_GROUPING = 3
