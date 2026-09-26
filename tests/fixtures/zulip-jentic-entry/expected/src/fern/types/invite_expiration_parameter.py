

import typing

InviteExpirationParameter = typing.Optional[int]
"""
The number of minutes before the invitation will expire. If `null`, the
invitation will never expire. If unspecified, the server will use a default
value (based on the `INVITATION_LINK_VALIDITY_MINUTES` server setting, which
defaults to 14400, i.e. 10 days) for when the invitation will expire.

**Changes**: New in Zulip 6.0 (feature level 126). Previously, there was an
`invite_expires_in_days` parameter, which specified the duration in days instead
of minutes.
"""
