

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_get_template_snapshot_response_agents_item_memory_variables_data_item import (
    TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariablesDataItem,
)


class TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables(UniversalBaseModel):
    version: str
    data: typing.List[TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariablesDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
