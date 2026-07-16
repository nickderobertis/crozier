

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_user_info_card import UserUserInfoCard


class DestinyResponsesDestinyErrorProfile(UniversalBaseModel):
    """
    If a Destiny Profile can't be returned, but we're pretty certain it's a valid Destiny account, this will contain as much info as we can get about the profile for your use.
    Assume that the most you'll get is the Error Code, the Membership Type and the Membership ID.
    """

    error_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorCode"),
        pydantic.Field(
            alias="errorCode",
            description="The error that we encountered. You should be able to look up localized text to show to the user for these failures.",
        ),
    ] = None
    """
    The error that we encountered. You should be able to look up localized text to show to the user for these failures.
    """

    info_card: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard],
        FieldMetadata(alias="infoCard"),
        pydantic.Field(
            alias="infoCard",
            description="Basic info about the account that failed. Don't expect anything other than membership ID, Membership Type, and displayName to be populated.",
        ),
    ] = None
    """
    Basic info about the account that failed. Don't expect anything other than membership ID, Membership Type, and displayName to be populated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
