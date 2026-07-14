

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSiteResponseTopicFlagTypesItem(UniversalBaseModel):
    description: str
    id: typing.Optional[int] = None
    is_custom_flag: bool
    is_flag: bool
    name: str
    name_key: typing.Optional[str] = None
    short_description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
