

import typing

FetchPaginationCursor = typing.Optional[str]
"""
An opaque string to be used as a cursor for the next page of results, in order from latest to earliest.

The string can be obtained directly from the `cursor` property of the previous fetch query
"""
