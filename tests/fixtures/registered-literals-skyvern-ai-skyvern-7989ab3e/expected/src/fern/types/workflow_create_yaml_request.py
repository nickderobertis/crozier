

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .workflow_create_yaml_request_proxy_location import WorkflowCreateYamlRequestProxyLocation
from .workflow_definition_yaml import WorkflowDefinitionYaml
from .workflow_status import WorkflowStatus


class WorkflowCreateYamlRequest(UniversalBaseModel):
    title: str
    recording_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Durable browser recording to attach to the workflow version created by this save.
    """

    description: typing.Optional[str] = None
    proxy_location: typing.Optional[WorkflowCreateYamlRequestProxyLocation] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it.
    """

    webhook_callback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it. URL validation errors identify the field and failure class without returning the URL or host.
    """

    totp_verification_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it. URL validation errors identify the field and failure class without returning the URL or host.
    """

    totp_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it.
    """

    persist_browser_session: typing.Optional[bool] = None
    reuse_browser_session: typing.Optional[bool] = None
    mask_secrets: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Mask secret values across this workflow's runs: hide them while they are typed (screenshots, recordings, live view) and redact them from stored artifacts, network logs, and LLM-bound text.
    """

    pin_saved_session_ip: typing.Optional[bool] = None
    browser_profile_id: typing.Optional[str] = None
    browser_profile_key: typing.Optional[str] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    workflow_definition: WorkflowDefinitionYaml
    is_saved_task: typing.Optional[bool] = None
    max_screenshot_scrolls: typing.Optional[int] = None
    max_elapsed_time_minutes: typing.Optional[int] = None
    extra_http_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it. An empty object ({}) clears the header map. Values, including ***, are literal.
    """

    cdp_connect_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    On PUT updates, omission keeps the stored value, null clears it, and a supplied value replaces it. An empty object ({}) clears the header map; each masked *** entry keeps the stored value for that key.
    """

    status: typing.Optional[WorkflowStatus] = None
    run_with: typing.Optional[str] = None
    browser_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Browser engine for runs of this workflow, one of the supported browser types (e.g. msedge, chrome, stealth-chromium). A workflow-run setting overrides this. Null means the system default.
    """

    ai_fallback: typing.Optional[bool] = None
    cache_key: typing.Optional[str] = None
    adaptive_caching: typing.Optional[bool] = None
    enable_self_healing: typing.Optional[bool] = None
    code_version: typing.Optional[int] = None
    generate_script_on_terminal: typing.Optional[bool] = None
    run_sequentially: typing.Optional[bool] = None
    sequential_key: typing.Optional[str] = None
    folder_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WorkflowCreateYamlRequest)
