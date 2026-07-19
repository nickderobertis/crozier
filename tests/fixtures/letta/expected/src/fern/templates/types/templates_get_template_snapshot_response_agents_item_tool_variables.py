

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_get_template_snapshot_response_agents_item_tool_variables_data_item import (
    TemplatesGetTemplateSnapshotResponseAgentsItemToolVariablesDataItem,
)


class TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables(UniversalBaseModel):
    version: str
    data: typing.List[TemplatesGetTemplateSnapshotResponseAgentsItemToolVariablesDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
