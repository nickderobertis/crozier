

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyAdvancedAwaAuthorizationResult(UniversalBaseModel):
    action_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actionToken"),
        pydantic.Field(
            alias="actionToken", description="Credential used to prove the user authorized an advanced write action."
        ),
    ] = None
    """
    Credential used to prove the user authorized an advanced write action.
    """

    developer_note: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="developerNote"),
        pydantic.Field(
            alias="developerNote", description="Message to the app developer to help understand the response."
        ),
    ] = None
    """
    Message to the app developer to help understand the response.
    """

    maximum_number_of_uses: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maximumNumberOfUses"),
        pydantic.Field(
            alias="maximumNumberOfUses",
            description="This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit.",
        ),
    ] = None
    """
    This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit.
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(alias="membershipType", description="MembershipType from the permission request."),
    ] = None
    """
    MembershipType from the permission request.
    """

    response_reason: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="responseReason"), pydantic.Field(alias="responseReason")
    ] = None
    type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Advanced Write Action Type from the permission request.
    """

    user_selection: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="userSelection"),
        pydantic.Field(
            alias="userSelection",
            description='Indication of how the user responded to the request. If the value is "Approved" the actionToken will contain the token that can be presented when performing the advanced write action.',
        ),
    ] = None
    """
    Indication of how the user responded to the request. If the value is "Approved" the actionToken will contain the token that can be presented when performing the advanced write action.
    """

    valid_until: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="validUntil"),
        pydantic.Field(alias="validUntil", description="Time, UTC, when token expires."),
    ] = None
    """
    Time, UTC, when token expires.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
