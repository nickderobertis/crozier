

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .proxy_location import ProxyLocation
from .workflow_definition import WorkflowDefinition
from .workflow_status import WorkflowStatus


class Workflow(UniversalBaseModel):
    workflow_id: str
    organization_id: str
    title: str
    workflow_permanent_id: str
    version: int
    is_saved_task: bool
    description: typing.Optional[str] = None
    workflow_definition: WorkflowDefinition
    proxy_location: typing.Optional[ProxyLocation] = None
    webhook_callback_url: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    persist_browser_session: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: typing.Optional[WorkflowStatus] = None
    created_at: dt.datetime
    modified_at: dt.datetime
    deleted_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Workflow)
