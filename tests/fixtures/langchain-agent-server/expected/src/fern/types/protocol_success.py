

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .protocol_response_meta import ProtocolResponseMeta


class ProtocolSuccess(UniversalBaseModel):
    """
    Successful command response.
    """

    id: int
    result: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Method-specific result payload.
    """

    meta: typing.Optional[ProtocolResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
