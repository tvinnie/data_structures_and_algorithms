The functions we've shown you so far aren't everything the calendar module offers. In addition to them, we can use the following classes:

# calendar.Calendar:
 provides methods to prepare calendar data for formatting;
# calendar.TextCalendar 
 is used to create regular text calendars;
# calendar.HTMLCalendar 
 is used to create HTML calendars;
# calendar.LocalTextCalendar
 is a subclass of the calendar.TextCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.
# calendar.LocalHTMLCalendar
 is a subclass of the calendar.HTMLCalendar class. The constructor of this class takes the locale parameter, which is used to return the appropriate months and weekday names.