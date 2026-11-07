

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ForLoopBlockYaml(UniversalBaseModel):
    label: str
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    loop_blocks: typing.List["ForLoopBlockYamlLoopBlocksItem"]
    loop_over_parameter_key: typing.Optional[str] = None
    loop_variable_reference: typing.Optional[str] = None
    complete_if_empty: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .for_loop_block_yaml_loop_blocks_item import ForLoopBlockYamlLoopBlocksItem

update_forward_refs(ForLoopBlockYaml, ForLoopBlockYamlLoopBlocksItem=ForLoopBlockYamlLoopBlocksItem)
