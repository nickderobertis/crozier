

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSiteResponseGroupsItem(UniversalBaseModel):
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    id: int
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
