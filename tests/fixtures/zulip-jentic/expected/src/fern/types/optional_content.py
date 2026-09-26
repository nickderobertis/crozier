

OptionalContent = str
"""
The updated content of the target message.

Clients should use the `max_message_length` returned by the
[`POST /register`](/api/register-queue) endpoint to determine
the maximum message size.

Note that a message's content and channel cannot be changed at the
same time, so sending both `content` and `stream_id` parameters will
throw an error.
"""
