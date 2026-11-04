

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .identifier import Identifier
from .location import Location
from .metadata_scheme_versions_item import MetadataSchemeVersionsItem
from .mscid import Mscid
from .namespace import Namespace
from .slug import Slug
from .uri import Uri


class MetadataScheme(UniversalBaseModel):
    slug: typing.Optional[Slug] = None
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full, human understandable name of the metadata scheme.
    - If the scheme is known by an abbreviation, put this at the start of the title, then give the expanded form in parentheses, e.g. “SDMX (Statistical Data and Metadata Exchange)”.
    - If the title is in English, use title case, i.e. give each significant word a capital letter. Do not use an irregular case to indicate how an abbreviation was defined, e.g. do not write “Statistical Data and Metadata eXchange”.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A few sentences describing the nature of the standard and for what it is meant to be used. If any of the information in the remainder of the record needs be clarified, perhaps because the reality is more nuanced than the coarse semantics provide for, then an explanation can be given here.
    """

    keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Keywords indicating the disciplinary scope of the scheme. Provide as few terms as possible to describe the subject areas in which the scheme is most used and useful. In some cases, it may be better to use a broader term even if not all of the available narrower terms apply.
    """

    data_types: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="dataTypes"),
        pydantic.Field(
            alias="dataTypes",
            description="Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.",
        ),
    ] = None
    """
    Data types most commonly described by metadata records that conform to this scheme. The data type must be specified by its internal MSC ID.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about the scheme may be accessed.
    """

    namespaces: typing.Optional[typing.List[Namespace]] = pydantic.Field(default=None)
    """
    Namespaces that may be used to identify predicates of the scheme in Linked Data contexts.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify all versions of this scheme collectively.
    """

    related_entities: typing_extensions.Annotated[
        typing.Optional[typing.List["MetadataSchemeRelatedEntitiesItem"]],
        FieldMetadata(alias="relatedEntities"),
        pydantic.Field(
            alias="relatedEntities",
            description="Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.",
        ),
    ] = None
    """
    Other entities in the MSC database. Note that relationships may be added but may not be deleted through this endpoint.
    """

    versions: typing.Optional[typing.List[MetadataSchemeVersionsItem]] = None

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
from .metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
from .metadata_scheme_related_entities_item_data import MetadataSchemeRelatedEntitiesItemData
from .organization import Organization
from .organization_related_entities_item import OrganizationRelatedEntitiesItem
from .organization_related_entities_item_data import OrganizationRelatedEntitiesItemData
from .tool import Tool
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    MetadataScheme,
    Endorsement=Endorsement,
    EndorsementRelatedEntitiesItem=EndorsementRelatedEntitiesItem,
    EndorsementRelatedEntitiesItemData=EndorsementRelatedEntitiesItemData,
    Mapping=Mapping,
    MappingRelatedEntitiesItem=MappingRelatedEntitiesItem,
    MappingRelatedEntitiesItemData=MappingRelatedEntitiesItemData,
    MetadataSchemeRelatedEntitiesItem=MetadataSchemeRelatedEntitiesItem,
    MetadataSchemeRelatedEntitiesItemData=MetadataSchemeRelatedEntitiesItemData,
    Organization=Organization,
    OrganizationRelatedEntitiesItem=OrganizationRelatedEntitiesItem,
    OrganizationRelatedEntitiesItemData=OrganizationRelatedEntitiesItemData,
    Tool=Tool,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
