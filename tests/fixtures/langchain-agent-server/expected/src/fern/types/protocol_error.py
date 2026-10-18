

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .protocol_error_error import ProtocolErrorError
from .protocol_error_type import ProtocolErrorType
from .protocol_response_meta import ProtocolResponseMeta


class ProtocolError(UniversalBaseModel):
    """
    Error response for a command.
    """

    type: ProtocolErrorType
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The `id` of the offending command, or null if the envelope was unparseable.
    """

    error: ProtocolErrorError
    message: str
    stacktrace: typing.Optional[str] = None
    meta: typing.Optional[ProtocolResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
