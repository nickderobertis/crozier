

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endorsement_related_entities_item_role import EndorsementRelatedEntitiesItemRole


class EndorsementRelatedEntitiesItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full MSC ID of the entity.
    """

    role: typing.Optional[EndorsementRelatedEntitiesItemRole] = pydantic.Field(default=None)
    """
    The manner of the relationship between the entity and the endorsement.
    """

    data: typing.Optional["EndorsementRelatedEntitiesItemData"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .endorsement import Endorsement
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
    EndorsementRelatedEntitiesItem,
    Endorsement=Endorsement,
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
