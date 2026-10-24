

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetOrganizationEndpointOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the organization.
    """

    name: str = pydantic.Field()
    """
    The human-readable name of the organization.
    """

    primary_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="primaryDomain"),
        pydantic.Field(
            alias="primaryDomain", description="The primary email domain associated with the organization, if any."
        ),
    ] = None
    """
    The primary email domain associated with the organization, if any.
    """

    auto_join_domain: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="autoJoinDomain"),
        pydantic.Field(
            alias="autoJoinDomain",
            description="The email domain claimed for auto-join, if any. New customers signing up with a confirmed\n email on this domain join the organization when auto-join is enabled.",
        ),
    ] = None
    """
    The email domain claimed for auto-join, if any. New customers signing up with a confirmed
     email on this domain join the organization when auto-join is enabled.
    """

    auto_join_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoJoinEnabled"),
        pydantic.Field(alias="autoJoinEnabled", description="Whether auto-join is enabled for the claimed domain."),
    ]
    """
    Whether auto-join is enabled for the claimed domain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
