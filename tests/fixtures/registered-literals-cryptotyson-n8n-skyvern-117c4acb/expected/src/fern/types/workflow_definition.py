

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .workflow_definition_blocks_item import WorkflowDefinitionBlocksItem
from .workflow_definition_parameters_item import WorkflowDefinitionParametersItem


class WorkflowDefinition(UniversalBaseModel):
    parameters: typing.List[WorkflowDefinitionParametersItem]
    blocks: typing.List[WorkflowDefinitionBlocksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowDefinition)
