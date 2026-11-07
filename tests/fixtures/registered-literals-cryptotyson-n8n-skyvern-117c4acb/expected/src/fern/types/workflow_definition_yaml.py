

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .workflow_definition_yaml_blocks_item import WorkflowDefinitionYamlBlocksItem
from .workflow_definition_yaml_parameters_item import WorkflowDefinitionYamlParametersItem


class WorkflowDefinitionYaml(UniversalBaseModel):
    parameters: typing.List[WorkflowDefinitionYamlParametersItem]
    blocks: typing.List[WorkflowDefinitionYamlBlocksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowDefinitionYaml)
