

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_engine import RunEngine


class ValidationBlockYaml(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Author-facing identifier; must be unique per workflow.
    """

    next_block_label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional pointer to the label of the next block. When omitted, it will default to sequential order. See [[s-4bnl]].
    """

    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    ignore_workflow_system_prompt: typing.Optional[bool] = None
    next_loop_on_failure: typing.Optional[bool] = None
    engine: typing.Optional[RunEngine] = None
    complete_criterion: typing.Optional[str] = None
    terminate_criterion: typing.Optional[str] = None
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    max_steps_per_run: typing.Optional[int] = None
    parameter_keys: typing.Optional[typing.List[str]] = None
    disable_cache: typing.Optional[bool] = None
    without_page_information: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
