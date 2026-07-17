

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserUserMembership(UniversalBaseModel):
    """
    Very basic info about a user as returned by the Account server.
    """

    bungie_global_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bungieGlobalDisplayName"),
        pydantic.Field(alias="bungieGlobalDisplayName", description="The bungie global display name, if set."),
    ] = None
    """
    The bungie global display name, if set.
    """

    bungie_global_display_name_code: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bungieGlobalDisplayNameCode"),
        pydantic.Field(alias="bungieGlobalDisplayNameCode", description="The bungie global display name code, if set."),
    ] = None
    """
    The bungie global display name code, if set.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.",
        ),
    ] = None
    """
    Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
    """

    membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipId"),
        pydantic.Field(alias="membershipId", description="Membership ID as they user is known in the Accounts service"),
    ] = None
    """
    Membership ID as they user is known in the Accounts service
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(alias="membershipType", description="Type of the membership. Not necessarily the native type."),
    ] = None
    """
    Type of the membership. Not necessarily the native type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
