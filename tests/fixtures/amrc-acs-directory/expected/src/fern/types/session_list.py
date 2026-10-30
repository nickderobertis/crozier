

import typing

from .session import Session

SessionList = typing.List[Session]
"""
Represents a list of sessions for a particular device; note that a device may not necessarily have the same group/node/device ID every time it comes online. The list MUST be sorted by birth time, newest first. Entries that overlap in time indicate a problem on the network, but MUST be reported as seen on the wire. Clients MUST correctly handle overlapping entries.
"""
