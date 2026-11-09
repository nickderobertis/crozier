

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conference_unmute_response_message import ConferenceUnmuteResponseMessage


class ConferenceUnmuteResponse(UniversalBaseModel):
    members: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Members"),
        pydantic.Field(alias="Members", description="List of affected members"),
    ] = None
    """
    List of affected members
    """

    message: typing_extensions.Annotated[
        ConferenceUnmuteResponseMessage,
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
