

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueryAllOrganizationsEndpointOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the organization.
    """

    name: str = pydantic.Field()
    """
    The human-readable name of the organization.
    """

    member_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="memberCount"),
        pydantic.Field(alias="memberCount", description="The number of members the organization has."),
    ]
    """
    The number of members the organization has.
    """

    owner_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerEmail"),
        pydantic.Field(
            alias="ownerEmail", description="The email of the organization's owner, absent when it has no active owner."
        ),
    ] = None
    """
    The email of the organization's owner, absent when it has no active owner.
    """

    owner_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="ownerCount"),
        pydantic.Field(alias="ownerCount", description="The number of owners the organization has."),
    ]
    """
    The number of owners the organization has.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
