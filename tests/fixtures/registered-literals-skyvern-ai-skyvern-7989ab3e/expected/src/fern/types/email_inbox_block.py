

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .email_inbox_block_email_client import EmailInboxBlockEmailClient
from .email_inbox_block_parameters_item import EmailInboxBlockParametersItem
from .output_parameter import OutputParameter


class EmailInboxBlock(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Author-facing identifier for a block; unique within a workflow.
    """

    next_block_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional pointer to the next block label when constructing a DAG. Defaults to sequential order when omitted.
    """

    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    disable_cache: typing.Optional[bool] = None
    ignore_workflow_system_prompt: typing.Optional[bool] = None
    next_loop_on_failure: typing.Optional[bool] = None
    email_client: EmailInboxBlockEmailClient
    credential_id: typing.Optional[str] = None
    folder: typing.Optional[str] = None
    prompt: typing.Optional[str] = None
    sender: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    newer_than_days: typing.Optional[int] = None
    max_results: typing.Optional[int] = None
    include_body: typing.Optional[bool] = None
    parameters: typing.Optional[typing.List[EmailInboxBlockParametersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EmailInboxBlock)
