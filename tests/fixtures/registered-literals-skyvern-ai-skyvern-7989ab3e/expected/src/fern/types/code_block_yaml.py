

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .code_block_step_yaml import CodeBlockStepYaml
from .code_block_yaml_data_schema import CodeBlockYamlDataSchema


class CodeBlockYaml(UniversalBaseModel):
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
    code: str
    error_code_mapping: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    parameter_keys: typing.Optional[typing.List[str]] = None
    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain-language goal of this code block, shown as the block's Goal in the editor
    """

    steps: typing.Optional[typing.List[CodeBlockStepYaml]] = pydantic.Field(default=None)
    """
    Plain-language step outline mapped to code line ranges; always rebuilt from the code on save, so any value sent is ignored
    """

    data_schema: typing.Optional[CodeBlockYamlDataSchema] = pydantic.Field(default=None)
    """
    JSON schema of the object this block's return produces; keys match the return keys; null when the block returns nothing
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
