

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserFeedbackResponse(UniversalBaseModel):
    id: str
    provider_id: str
    task_id: str
    context_id: str
    rating: int
    message: str
    comment: typing.Optional[str] = None
    comment_tags: typing.Optional[typing.List[str]] = None
    created_at: dt.datetime
    agent_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
