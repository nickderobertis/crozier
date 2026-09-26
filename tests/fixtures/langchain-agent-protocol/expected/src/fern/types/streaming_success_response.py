

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .streaming_success_response_meta import StreamingSuccessResponseMeta


class StreamingSuccessResponse(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    ID of the command this response belongs to.
    """

    result: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Command result. Shape depends on the command method.
    """

    meta: typing.Optional[StreamingSuccessResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
