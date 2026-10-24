

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetCapabilityGranteesEndpointOutput(UniversalBaseModel):
    organization_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationId"),
        pydantic.Field(alias="organizationId", description="The organization that holds the capability."),
    ]
    """
    The organization that holds the capability.
    """

    organization_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="organizationName"),
        pydantic.Field(alias="organizationName", description="The human-readable name of the organization."),
    ]
    """
    The human-readable name of the organization.
    """

    timestamp: dt.datetime = pydantic.Field()
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
