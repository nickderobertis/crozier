

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .creator import Creator
from .identifier import Identifier
from .location import Location
from .mscid import Mscid
from .slug import Slug
from .tool_versions_item import ToolVersionsItem
from .uri import Uri


class Tool(UniversalBaseModel):
    slug: typing.Optional[Slug] = None
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full, human understandable name of the tool.
    - If the tool is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “CMOR (Climate Model Output Rewriter)”.
    - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “eXtensible Editor”.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the intended use of the tool, and its capabilities.
    """

    types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Terms describing how a user interacts with the tool.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify the tool or version.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about the tool may be accessed.
    """

    creators: typing.Optional[typing.List[Creator]] = pydantic.Field(default=None)
    """
    Persons or organizations responsible for creating, maintaining, or approving the tool (the emphasis here is on establishing provenance/responsibility rather than a strict understanding of creation). If a maintaining organization has an entry in the MSC, it should be given under `relatedEntities` with type ‘maintainer’ rather than here.
    """

    related_entities: typing_extensions.Annotated[
        typing.Optional[typing.List["ToolRelatedEntitiesItem"]],
        FieldMetadata(alias="relatedEntities"),
        pydantic.Field(
            alias="relatedEntities",
            description="Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.",
        ),
    ] = None
    """
    Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.
    """

    versions: typing.Optional[typing.List[ToolVersionsItem]] = None

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
from .organization import Organization
from .organization_related_entities_item import OrganizationRelatedEntitiesItem
from .organization_related_entities_item_data import OrganizationRelatedEntitiesItemData
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    Tool,
    Endorsement=Endorsement,
    EndorsementRelatedEntitiesItem=EndorsementRelatedEntitiesItem,
    EndorsementRelatedEntitiesItemData=EndorsementRelatedEntitiesItemData,
    Mapping=Mapping,
    MappingRelatedEntitiesItem=MappingRelatedEntitiesItem,
    MappingRelatedEntitiesItemData=MappingRelatedEntitiesItemData,
    MetadataScheme=MetadataScheme,
    MetadataSchemeRelatedEntitiesItem=MetadataSchemeRelatedEntitiesItem,
    MetadataSchemeRelatedEntitiesItemData=MetadataSchemeRelatedEntitiesItemData,
    Organization=Organization,
    OrganizationRelatedEntitiesItem=OrganizationRelatedEntitiesItem,
    OrganizationRelatedEntitiesItemData=OrganizationRelatedEntitiesItemData,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
