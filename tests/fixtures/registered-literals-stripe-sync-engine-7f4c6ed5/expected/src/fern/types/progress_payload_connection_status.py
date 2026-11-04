

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_payload_connection_status_status import ProgressPayloadConnectionStatusStatus


class ProgressPayloadConnectionStatus(UniversalBaseModel):
    """
    Set when source or destination emits connection_status: failed.
    """

    status: ProgressPayloadConnectionStatusStatus = pydantic.Field()
    """
    Whether the connection check passed.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable explanation of the check result.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
