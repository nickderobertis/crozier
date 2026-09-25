

import typing

FolderId = typing.Optional[int]
"""
The ID of the folder to which the channel belongs.

Is `null` if channel does not belong to any folder.

**Changes**: New in Zulip 11.0 (feature level 389).
"""
