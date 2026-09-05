

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry import Entry
from .list_meta import ListMeta


class EntryListResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[Entry]] = None
    meta: typing.Optional[ListMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
