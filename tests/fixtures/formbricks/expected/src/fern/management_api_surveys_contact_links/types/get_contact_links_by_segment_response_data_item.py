

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetContactLinksBySegmentResponseDataItem(UniversalBaseModel):
    contact_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contactId"),
        pydantic.Field(alias="contactId", description="The ID of the contact"),
    ] = None
    """
    The ID of the contact
    """

    survey_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="surveyUrl"),
        pydantic.Field(alias="surveyUrl", description="Personalized survey link"),
    ] = None
    """
    Personalized survey link
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="The date and time the link expires, null if no expiration"),
    ] = None
    """
    The date and time the link expires, null if no expiration
    """

    attributes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The attributes of the contact
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
