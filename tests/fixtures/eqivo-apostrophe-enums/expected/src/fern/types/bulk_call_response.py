

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bulk_call_response_message import BulkCallResponseMessage


class BulkCallResponse(UniversalBaseModel):
    message: typing_extensions.Annotated[
        BulkCallResponseMessage,
        FieldMetadata(alias="Message"),
        pydantic.Field(alias="Message", description="Response message"),
    ]
    """
    Response message
    """

    request_uuid: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="RequestUUID"),
        pydantic.Field(alias="RequestUUID", description="Unique identifiers of each Call request (UUIDv4)"),
    ]
    """
    Unique identifiers of each Call request (UUIDv4)
    """

    rest_api_server: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RestApiServer"),
        pydantic.Field(alias="RestApiServer", description="API server which handled this request (an Eqivo extension)"),
    ]
    """
    API server which handled this request (an Eqivo extension)
    """

    success: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Success"),
        pydantic.Field(alias="Success", description="Whether the request was successful or not"),
    ]
    """
    Whether the request was successful or not
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
