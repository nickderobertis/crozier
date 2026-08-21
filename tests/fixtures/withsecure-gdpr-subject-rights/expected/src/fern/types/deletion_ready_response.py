

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_uuid import ContextUuid
from .deletion_ready_response_deletion_feedback import DeletionReadyResponseDeletionFeedback


class DeletionReadyResponse(UniversalBaseModel):
    context_uuid: ContextUuid
    deletion_feedback: DeletionReadyResponseDeletionFeedback = pydantic.Field()
    """
    State of the performed deletion request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
