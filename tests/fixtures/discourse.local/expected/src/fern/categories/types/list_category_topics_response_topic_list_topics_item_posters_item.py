

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCategoryTopicsResponseTopicListTopicsItemPostersItem(UniversalBaseModel):
    description: str
    extras: str
    primary_group_id: typing.Optional[str] = None
    user_id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
