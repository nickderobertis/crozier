

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .creator import Creator
from .endorsement_valid import EndorsementValid
from .identifier import Identifier
from .location import Location
from .mscid import Mscid
from .slug import Slug
from .uri import Uri


class Endorsement(UniversalBaseModel):
    slug: typing.Optional[Slug] = None
    mscid: typing.Optional[Mscid] = None
    uri: typing.Optional[Uri] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the endorsement document.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the endorsement document.
    - Use this to record any caveats to the endorsement.
    - This could indicate if only certain versions of the scheme(s) are endorsed.
    """

    creators: typing.Optional[typing.List[Creator]] = pydantic.Field(default=None)
    """
    Authors of the endorsement document
    """

    publication: typing.Optional[str] = pydantic.Field(default=None)
    """
    Other bibliographic information (excluding date).
    """

    issued: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which the endorsement was made. Use of this element does not imply that the originating organization reviews the endorsement for validity. If both `issued` and `valid` are given, issued is ignored.
    """

    valid: typing.Optional[EndorsementValid] = pydantic.Field(default=None)
    """
    The start date expresses when the endorsement was made. If there is no end date, this implies that the originating organization currently endorses the standard. (If that implication is inappropriate, the date should be given under `issued` instead.)
    If an end date is provided, it expresses the date on which the endorsement was withdrawn.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about the endorsement may be accessed.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify the endorsement.
    """

    related_entities: typing_extensions.Annotated[
        typing.Optional[typing.List["EndorsementRelatedEntitiesItem"]],
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
from .tool import Tool
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    Endorsement,
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
    Tool=Tool,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
