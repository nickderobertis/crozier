

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_item_type import ErrorItemType
from .log_message_type import LogMessageType


class ErrorGet(UniversalBaseModel):
    message: str = pydantic.Field()
    """
    Message displayed to the user
    """

    support_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supportId"),
        pydantic.Field(alias="supportId", description="ID to track the incident during support"),
    ] = None
    """
    ID to track the incident during support
    """

    status: int = pydantic.Field()
    """
    Redundant HTTP status code of the error.Must be the same as in the HTTP response
    """

    errors: typing.Optional[typing.List[ErrorItemType]] = None
    logs: typing.Optional[typing.List[LogMessageType]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
