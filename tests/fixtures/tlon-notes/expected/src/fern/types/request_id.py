

RequestId = str
"""
Canonical Hoon `@uv` (base-32 with `.` separators every 5
chars from the right, prefixed `0v`). A correlation id for the
request. OPTIONAL on POST: if you omit it (or send something
that isn't a valid `@uv`), the server mints one and returns it
in the response. You only need to supply your own if you intend
to poll `GET /request/{requestId}` or subscribe to the SSE
request stream — for the common case (read the held-open POST
response inline) you can leave it out entirely.
"""
