

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateTopicTimerResponse(UniversalBaseModel):
    based_on_last_post: typing.Optional[bool] = None
    category_id: typing.Optional[str] = None
    closed: typing.Optional[bool] = None
    duration: typing.Optional[str] = None
    execute_at: typing.Optional[str] = None
    success: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
