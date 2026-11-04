

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .response import Response


class ResponseItemOrganization(Response):
    data: typing.Optional["Organization"] = None

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
from .tool import Tool
from .tool_related_entities_item import ToolRelatedEntitiesItem
from .tool_related_entities_item_data import ToolRelatedEntitiesItemData

update_forward_refs(
    ResponseItemOrganization,
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
    Tool=Tool,
    ToolRelatedEntitiesItem=ToolRelatedEntitiesItem,
    ToolRelatedEntitiesItemData=ToolRelatedEntitiesItemData,
)
