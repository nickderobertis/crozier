

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .guid_physical_state import GuidPhysicalState


class Guid(UniversalBaseModel):
    created_timestamp: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdTimestamp"),
        pydantic.Field(
            alias="createdTimestamp", description="The UTC unix timestamp of when this GUID has been created"
        ),
    ] = None
    """
    The UTC unix timestamp of when this GUID has been created
    """

    holder_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="holderOrganizationId"),
        pydantic.Field(alias="holderOrganizationId", description="Organization namespace of the GUID holder"),
    ] = None
    """
    Organization namespace of the GUID holder
    """

    id4n: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID
    """

    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="Organization namespace of the GUID owner"),
    ] = None
    """
    Organization namespace of the GUID owner
    """

    physical_state: typing_extensions.Annotated[
        typing.Optional[GuidPhysicalState],
        FieldMetadata(alias="physicalState"),
        pydantic.Field(alias="physicalState", description="Physical attachment state of the GUID"),
    ] = None
    """
    Physical attachment state of the GUID
    """

    properties: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The properties of the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
