

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_get_template_snapshot_response_agents_item import TemplatesGetTemplateSnapshotResponseAgentsItem
from .templates_get_template_snapshot_response_blocks_item import TemplatesGetTemplateSnapshotResponseBlocksItem
from .templates_get_template_snapshot_response_configuration import TemplatesGetTemplateSnapshotResponseConfiguration
from .templates_get_template_snapshot_response_relationships_item import (
    TemplatesGetTemplateSnapshotResponseRelationshipsItem,
)
from .templates_get_template_snapshot_response_type import TemplatesGetTemplateSnapshotResponseType


class TemplatesGetTemplateSnapshotResponse(UniversalBaseModel):
    agents: typing.List[TemplatesGetTemplateSnapshotResponseAgentsItem]
    blocks: typing.List[TemplatesGetTemplateSnapshotResponseBlocksItem]
    relationships: typing.List[TemplatesGetTemplateSnapshotResponseRelationshipsItem]
    configuration: TemplatesGetTemplateSnapshotResponseConfiguration
    type: TemplatesGetTemplateSnapshotResponseType
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
