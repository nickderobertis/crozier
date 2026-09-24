

IndexRange = str
"""
Range index  used to express the first (offset) and the last results index  to retrieve. With the respect to the regex pattern '\d+(-\d*)?', the start of  range is mandatory (use 0 for default).

*Example:*

*  '0-9'  : start=0, end=9    ==> offset=0 and number of items=10

* '5-'    : start =5, no end  ==> start at 5th to the end results.
"""
