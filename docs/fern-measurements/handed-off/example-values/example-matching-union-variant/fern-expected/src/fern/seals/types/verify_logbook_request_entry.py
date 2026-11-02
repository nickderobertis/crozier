

import typing

from ...types.entry_v1 import EntryV1
from ...types.entry_v2 import EntryV2

VerifyLogbookRequestEntry = typing.Union[EntryV1, EntryV2]
