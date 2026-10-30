

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganizationResource(UniversalBaseModel):
    id: str
    name: str
    is_platform: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isPlatform"), pydantic.Field(alias="isPlatform")
    ]
    has_logo: typing_extensions.Annotated[bool, FieldMetadata(alias="hasLogo"), pydantic.Field(alias="hasLogo")]
    user_count: typing_extensions.Annotated[int, FieldMetadata(alias="userCount"), pydantic.Field(alias="userCount")]
    active_user_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="activeUserCount"), pydantic.Field(alias="activeUserCount")
    ]
    invited_user_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="invitedUserCount"), pydantic.Field(alias="invitedUserCount")
    ]
    created_utc: typing_extensions.Annotated[str, FieldMetadata(alias="createdUtc"), pydantic.Field(alias="createdUtc")]
    updated_utc: typing_extensions.Annotated[str, FieldMetadata(alias="updatedUtc"), pydantic.Field(alias="updatedUtc")]
    logo_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="logoUrl"),
        pydantic.Field(
            alias="logoUrl",
            description="Always populated, and always answers: an organization with no uploaded logo is served\nthe placeholder, so a client has one address to point at rather than a branch and a\ncopy of the fallback image. `hasLogo` is for a client that needs to tell the two\napart, such as one offering to replace an image that is really there.",
        ),
    ]
    """
    Always populated, and always answers: an organization with no uploaded logo is served
    the placeholder, so a client has one address to point at rather than a branch and a
    copy of the fallback image. `hasLogo` is for a client that needs to tell the two
    apart, such as one offering to replace an image that is really there.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
