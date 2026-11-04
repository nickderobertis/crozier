

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .identifier import Identifier
from .location import Location
from .mscid import Mscid
from .slug import Slug
from .uri import Uri


class Organization(UniversalBaseModel):
    slug: typing.Optional[Slug] = None
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the organization as it is usually given.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A sentence or several describing the organization and its relevance to research data and metadata.
    """

    types: typing.Optional[typing.List[str]] = None
    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about the organization may be accessed.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify the organization.
    """

    related_entities: typing_extensions.Annotated[
        typing.Optional[typing.List["OrganizationRelatedEntitiesItem"]],
        FieldMetadata(alias="relatedEntities"),
        pydantic.Field(
            alias="relatedEntities",
            description="Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.",
        ),
    ] = None
    """
    Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .endorsement import Endorsement
from .endorsement_related_entities_item import EndorsementRelatedEntitiesItem
from .endorsement_related_entities_item_data import EndorsementRelatedEntitiesItemData
from .mapping import Mapping
from .mapping_related_entities_item import MappingRelatedEntitiesItem
from .mapping_related_entities_item_data import MappingRelatedEntitiesItemData
from .metadata_scheme import MetadataScheme
from .metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
from .metadata_scheme_related_entities_item_data import MetadataSchemeRelatedEntitiesItemData
from .organization_related_entities_item import OrganizationRelatedEntitiesItem
from .organization_related_entities_item_data import OrganizationRelatedEntitiesItemData
from .tool import Tool
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    Organization,
    Endorsement=Endorsement,
    EndorsementRelatedEntitiesItem=EndorsementRelatedEntitiesItem,
    EndorsementRelatedEntitiesItemData=EndorsementRelatedEntitiesItemData,
    Mapping=Mapping,
    MappingRelatedEntitiesItem=MappingRelatedEntitiesItem,
    MappingRelatedEntitiesItemData=MappingRelatedEntitiesItemData,
    MetadataScheme=MetadataScheme,
    MetadataSchemeRelatedEntitiesItem=MetadataSchemeRelatedEntitiesItem,
    MetadataSchemeRelatedEntitiesItemData=MetadataSchemeRelatedEntitiesItemData,
    OrganizationRelatedEntitiesItem=OrganizationRelatedEntitiesItem,
    OrganizationRelatedEntitiesItemData=OrganizationRelatedEntitiesItemData,
    Tool=Tool,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
