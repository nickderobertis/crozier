

import typing

LiabilitiesAccountIdsWithUpdatedLiabilities = typing.Dict[str, typing.List[str]]
"""
An object with keys of `account_id`'s that are mapped to their respective liabilities fields that changed.

Example: `{ "XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58": ["past_amount_due"] }`
"""
