

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authorization_relations_platform import AuthorizationRelationsPlatform
from .authorization_scope import AuthorizationScope


class GetPlatformRelationMembersEndpointOutput(UniversalBaseModel):
    customer: str = pydantic.Field()
    """
    The customer holding the relation.
    """

    email: str = pydantic.Field()
    """
    The email address of the customer.
    """

    organization_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationName"),
        pydantic.Field(alias="organizationName", description="The name of the customer's active organization."),
    ]
    """
    The name of the customer's active organization.
    """

    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The identifier of the customer's active organization."),
    ]
    """
    The identifier of the customer's active organization.
    """

    scope: AuthorizationScope = pydantic.Field()
    """
    The object the relation is on.
    """

    relation: AuthorizationRelationsPlatform
    granted_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="grantedAt"),
        pydantic.Field(alias="grantedAt", description="When the grant was written."),
    ]
    """
    When the grant was written.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
