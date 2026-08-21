

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_uuid import ContextUuid
from .deletion_denied_reason import DeletionDeniedReason


class DeletionDeniedResponse(UniversalBaseModel):
    context_uuid: ContextUuid
    retention_reason: typing.List[DeletionDeniedReason]
    retention_human_readable_reason: str = pydantic.Field()
    """
    A human readable reason for why the request was denied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
