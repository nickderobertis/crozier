

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .workflow_definition_blocks_item import WorkflowDefinitionBlocksItem
from .workflow_definition_parameters_item import WorkflowDefinitionParametersItem


class WorkflowDefinition(UniversalBaseModel):
    version: typing.Optional[int] = None
    parameters: typing.List[WorkflowDefinitionParametersItem]
    blocks: typing.List[WorkflowDefinitionBlocksItem]
    finally_block_label: typing.Optional[str] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    workflow_system_prompt: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowDefinition)
