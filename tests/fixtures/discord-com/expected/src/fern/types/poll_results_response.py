

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .poll_results_entry_response import PollResultsEntryResponse


class PollResultsResponse(UniversalBaseModel):
    answer_counts: typing.Optional[typing.List[PollResultsEntryResponse]] = None
    is_finalized: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
