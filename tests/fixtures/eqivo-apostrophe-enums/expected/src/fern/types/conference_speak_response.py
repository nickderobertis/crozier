

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conference_speak_response_message import ConferenceSpeakResponseMessage


class ConferenceSpeakResponse(UniversalBaseModel):
    message: typing_extensions.Annotated[
        ConferenceSpeakResponseMessage,
        FieldMetadata(alias="Message"),
        pydantic.Field(alias="Message", description="Response message"),
    ]
    """
    Response message
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
