

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delete_podcast_response_status import DeletePodcastResponseStatus


class DeletePodcastResponse(UniversalBaseModel):
    status: DeletePodcastResponseStatus = pydantic.Field()
    """
    The status of this podcast deletion request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
