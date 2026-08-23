

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message import Message
from .status_code import StatusCode


class Result(UniversalBaseModel):
    """
    General result object returned on failure (EN 18222 Table 12).
    """

    status_code: typing_extensions.Annotated[
        typing.Optional[StatusCode], FieldMetadata(alias="statusCode"), pydantic.Field(alias="statusCode")
    ] = None
    message: typing.Optional[typing.List[Message]] = pydantic.Field(default=None)
    """
    Additional messages for the requester.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
