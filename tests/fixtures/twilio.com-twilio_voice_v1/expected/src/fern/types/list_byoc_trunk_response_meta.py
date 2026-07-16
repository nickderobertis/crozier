

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListByocTrunkResponseMeta(UniversalBaseModel):
    first_page_url: typing.Optional[str] = None
    key: typing.Optional[str] = None
    next_page_url: typing.Optional[str] = None
    page: typing.Optional[int] = None
    page_size: typing.Optional[int] = None
    previous_page_url: typing.Optional[str] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
