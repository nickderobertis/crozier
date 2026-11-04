

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .output_parameter import OutputParameter
from .wait_block_parameters_item import WaitBlockParametersItem


class WaitBlock(UniversalBaseModel):
    label: str
    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    wait_sec: int
    parameters: typing.Optional[typing.List[WaitBlockParametersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WaitBlock)
