

import typing

TransferAuthorizationIdempotencyKey = typing.Optional[str]
"""
A random key provided by the client, per unique authorization. Maximum of 50 characters.

The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create an authorization fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single authorization is created.

Failure to provide this key may result in duplicate charges.

Required for guaranteed ACH customers.
"""
