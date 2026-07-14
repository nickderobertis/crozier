

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListTagsResponseTagsItem(UniversalBaseModel):
    count: typing.Optional[int] = None
    id: typing.Optional[str] = None
    pm_count: typing.Optional[int] = None
    target_tag: typing.Optional[str] = None
    text: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
