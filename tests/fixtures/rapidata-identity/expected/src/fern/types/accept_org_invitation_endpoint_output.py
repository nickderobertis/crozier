

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AcceptOrgInvitationEndpointOutput(UniversalBaseModel):
    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The organization the customer joined."),
    ]
    """
    The organization the customer joined.
    """

    membership_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="membershipId"),
        pydantic.Field(alias="membershipId", description="The id of the created membership."),
    ]
    """
    The id of the created membership.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
