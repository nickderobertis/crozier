

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .extraction_block_data_schema import ExtractionBlockDataSchema
from .extraction_block_parameters_item import ExtractionBlockParametersItem
from .output_parameter import OutputParameter
from .run_engine import RunEngine


class ExtractionBlock(UniversalBaseModel):
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
    task_type: typing.Optional[str] = None
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    engine: typing.Optional[RunEngine] = None
    complete_criterion: typing.Optional[str] = None
    complete_criterion_is_untrusted: typing.Optional[bool] = None
    terminate_criterion: typing.Optional[str] = None
    navigation_goal: typing.Optional[str] = None
    data_extraction_goal: str
    data_schema: typing.Optional[ExtractionBlockDataSchema] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    max_retries: typing.Optional[int] = None
    max_steps_per_run: typing.Optional[int] = None
    parameters: typing.Optional[typing.List[ExtractionBlockParametersItem]] = None
    complete_on_download: typing.Optional[bool] = None
    download_suffix: typing.Optional[str] = None
    totp_verification_url: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None
    complete_verification: typing.Optional[bool] = None
    include_action_history_in_verification: typing.Optional[bool] = None
    download_timeout: typing.Optional[float] = None
    include_extracted_text: typing.Optional[bool] = None
    export_enabled: typing.Optional[bool] = None
    export_data_schema: typing.Optional[typing.Dict[str, typing.Any]] = None
    export_file_name: typing.Optional[str] = None
    export_records: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ExtractionBlock)
