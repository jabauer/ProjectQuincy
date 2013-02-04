#This file is for little helper functions that need to be accessed by several applications

from django.utils import datetime_safe
#This is a patch that allows for formatting dates before 1900, seriously


#This function takes a date and three boolean values associated with that date and outputs a
#formatted date that only displays to the end user the components of the date that are "known"
#It is typically used in a view to format a date from a given model in that application.
#It could also be used to create a 'phantom' table in the database that holds a phantom date
#using the property() function.
#If you want to change how the dates are formated see the python date format options list at
# http://docs.python.org/library/datetime.html#strftime-strptime-behavior
def partial_date(db_date, year_known, month_known, day_known):
    #example date (1735, 10, 30)
    if db_date is not None:
        if year_known == True and month_known == True and day_known == False:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%B %Y")
            # "October 1735"
        elif year_known == True and month_known == False and day_known == True:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%e ____ %Y")
            # "30 ____ 1735"
        elif year_known == False and month_known == True and day_known == True:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%e %B")
            # "30 October"
        elif year_known == True and month_known == False and day_known == False:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%Y")
            # "1735"
        elif year_known == False and month_known == True and day_known == False:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%B")
            # "October"
        elif year_known == False and month_known == False and day_known == True:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%e (month and year unknown)")
            # "30 (month and date unknown)"
        else:
            return datetime_safe.date(db_date.year, db_date.month, db_date.day).strftime("%e %B %Y")
            # "30 October 1735"