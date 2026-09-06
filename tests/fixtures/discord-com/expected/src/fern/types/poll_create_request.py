

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .poll_answer_create_request import PollAnswerCreateRequest
from .poll_layout_types import PollLayoutTypes
from .poll_media import PollMedia


class PollCreateRequest(UniversalBaseModel):
    question: PollMedia
    answers: typing.List[PollAnswerCreateRequest]
    allow_multiselect: typing.Optional[bool] = None
    layout_type: typing.Optional[PollLayoutTypes] = None
    duration: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
