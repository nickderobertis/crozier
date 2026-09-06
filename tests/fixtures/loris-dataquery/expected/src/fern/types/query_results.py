

import typing

QueryResults = typing.Any
"""
The result of running a query.

The result is a stream of data for each CandID that matched by the query. Candidates are separated by an ASCII unit separator (0x1f). Each cell within the candidate is separated by an ASCII record separator (0x1e). Each row should have the exact number of fields that were in the query fields attribute.

Within each cell, the data is returned as a JSON value, the exact format varies based on the cell's dictionary type. If the data is candidate scoped, a value is directly returned as a JSON primitive. If it is session scoped variable or has cardinality many:one, a JSON object is returned. Session scoped variables contain a JSON object with the key being the SessionID for each session where this row's candidate has data and the value of which is an object of the format `{ SessionID: number, VisitLabel: string, value: value }`
"""
