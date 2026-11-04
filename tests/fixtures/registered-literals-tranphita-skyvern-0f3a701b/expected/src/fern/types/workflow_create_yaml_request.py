

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .proxy_location import ProxyLocation
from .workflow_definition_yaml import WorkflowDefinitionYaml
from .workflow_status import WorkflowStatus


class WorkflowCreateYamlRequest(UniversalBaseModel):
    title: str
    description: typing.Optional[str] = None
    proxy_location: typing.Optional[ProxyLocation] = None
    webhook_callback_url: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    persist_browser_session: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    workflow_definition: WorkflowDefinitionYaml
    is_saved_task: typing.Optional[bool] = None
    status: typing.Optional[WorkflowStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowCreateYamlRequest)
