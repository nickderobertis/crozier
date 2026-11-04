

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataExportBlockYaml(UniversalBaseModel):
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
    data: str
    data_schema: typing.Dict[str, typing.Any]
    file_name: typing.Optional[str] = None
    parameter_keys: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
