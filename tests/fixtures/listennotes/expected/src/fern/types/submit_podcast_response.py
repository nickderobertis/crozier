

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .podcast_minimum import PodcastMinimum
from .submit_podcast_response_status import SubmitPodcastResponseStatus


class SubmitPodcastResponse(UniversalBaseModel):
    podcast: PodcastMinimum
    status: SubmitPodcastResponseStatus = pydantic.Field()
    """
    The status of this submission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
