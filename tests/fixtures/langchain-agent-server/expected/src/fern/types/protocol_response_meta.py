

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProtocolResponseMeta(UniversalBaseModel):
    """
    Optional metadata attached to command responses.
    """

    applied_through_seq: typing.Optional[int] = pydantic.Field(default=None)
    """
    Highest event `seq` observed on the session when this response was generated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
