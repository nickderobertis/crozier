

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .poll_answer_response import PollAnswerResponse
from .poll_layout_types import PollLayoutTypes
from .poll_media_response import PollMediaResponse
from .poll_results_response import PollResultsResponse


class PollResponse(UniversalBaseModel):
    question: PollMediaResponse
    answers: typing.List[PollAnswerResponse]
    expiry: dt.datetime
    allow_multiselect: bool
    layout_type: PollLayoutTypes
    results: PollResultsResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
