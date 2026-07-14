

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetTagResponseTopicListTagsItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    staff: typing.Optional[bool] = None
    topic_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
