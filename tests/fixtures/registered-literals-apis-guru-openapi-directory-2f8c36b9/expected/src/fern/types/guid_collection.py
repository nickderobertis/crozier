

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .guid_collection_physical_state import GuidCollectionPhysicalState
from .guid_collection_type import GuidCollectionType


class GuidCollection(UniversalBaseModel):
    created_timestamp: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="createdTimestamp"),
        pydantic.Field(
            alias="createdTimestamp", description="The UTC unix timestamp of when this collection has been created"
        ),
    ] = None
    """
    The UTC unix timestamp of when this collection has been created
    """

    holder_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="holderOrganizationId"),
        pydantic.Field(
            alias="holderOrganizationId", description="Organization namespace of the holder of the collection"
        ),
    ] = None
    """
    Organization namespace of the holder of the collection
    """

    id4n: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID
    """

    label: typing.Optional[str] = None
    owner_organization_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerOrganizationId"),
        pydantic.Field(alias="ownerOrganizationId", description="Organization namespace of the collection owner"),
    ] = None
    """
    Organization namespace of the collection owner
    """

    physical_state: typing_extensions.Annotated[
        typing.Optional[GuidCollectionPhysicalState],
        FieldMetadata(alias="physicalState"),
        pydantic.Field(alias="physicalState", description="Physical attachment state of the collection"),
    ] = None
    """
    Physical attachment state of the collection
    """

    type: typing.Optional[GuidCollectionType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
