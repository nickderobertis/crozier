

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .creator import Creator
from .identifier import Identifier
from .location import Location
from .mapping_versions_item import MappingVersionsItem
from .mscid import Mscid
from .slug import Slug
from .uri import Uri


class Mapping(UniversalBaseModel):
    slug: typing.Optional[Slug] = None
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name or descriptor for the mapping.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the mapping.
    - This could indicate if only certain versions of the input and output schemes are supported; if the mapping has been tailored to the outputs or inputs of specific repositories or services; if certain parts of the input or output schemes have been ignored; or if specific conventions in the input scheme are preferred (or necessary).
    - This could recommend steps to be taken before or after applying the mapping in order to improve results.
    """

    creators: typing.Optional[typing.List[Creator]] = pydantic.Field(default=None)
    """
    Persons or organizations responsible for creating, maintaining, or approving the mapping (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about the tool may be accessed.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify the mapping or version.
    """

    related_entities: typing_extensions.Annotated[
        typing.Optional[typing.List["MappingRelatedEntitiesItem"]],
        FieldMetadata(alias="relatedEntities"),
        pydantic.Field(
            alias="relatedEntities",
            description="Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.",
        ),
    ] = None
    """
    Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.
    """

    versions: typing.Optional[typing.List[MappingVersionsItem]] = None

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
from .mapping_related_entities_item import MappingRelatedEntitiesItem
from .mapping_related_entities_item_data import MappingRelatedEntitiesItemData
from .metadata_scheme import MetadataScheme
from .metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
from .metadata_scheme_related_entities_item_data import MetadataSchemeRelatedEntitiesItemData
from .organization import Organization
from .organization_related_entities_item import OrganizationRelatedEntitiesItem
from .organization_related_entities_item_data import OrganizationRelatedEntitiesItemData
from .tool import Tool
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    Mapping,
    Endorsement=Endorsement,
    EndorsementRelatedEntitiesItem=EndorsementRelatedEntitiesItem,
    EndorsementRelatedEntitiesItemData=EndorsementRelatedEntitiesItemData,
    MappingRelatedEntitiesItem=MappingRelatedEntitiesItem,
    MappingRelatedEntitiesItemData=MappingRelatedEntitiesItemData,
    MetadataScheme=MetadataScheme,
    MetadataSchemeRelatedEntitiesItem=MetadataSchemeRelatedEntitiesItem,
    MetadataSchemeRelatedEntitiesItemData=MetadataSchemeRelatedEntitiesItemData,
    Organization=Organization,
    OrganizationRelatedEntitiesItem=OrganizationRelatedEntitiesItem,
    OrganizationRelatedEntitiesItemData=OrganizationRelatedEntitiesItemData,
    Tool=Tool,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
