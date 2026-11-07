

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .workflow_create_yaml_request import WorkflowCreateYamlRequest


class WorkflowRequest(UniversalBaseModel):
    json_definition: typing.Optional[WorkflowCreateYamlRequest] = pydantic.Field(default=None)
    """
    Workflow definition in JSON format
    """

    yaml_definition: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workflow definition in YAML format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowRequest)
