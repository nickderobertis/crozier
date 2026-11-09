

TransferRecurringIdempotencyKey = str
"""
A random key provided by the client, per unique recurring transfer. Maximum of 50 characters.

The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. For example, if a request to create a recurring fails due to a network connection error, you can retry the request with the same idempotency key to guarantee that only a single recurring transfer is created.
"""
