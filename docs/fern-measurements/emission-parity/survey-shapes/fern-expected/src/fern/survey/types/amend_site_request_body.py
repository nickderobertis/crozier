

import typing

from ...types.note import Note
from ...types.site_patch import SitePatch

AmendSiteRequestBody = typing.Union[SitePatch, typing.List[Note]]
