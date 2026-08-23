

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .input_description import InputDescription
from .output_description import OutputDescription
from .process_summary import ProcessSummary


class ProcessDescription(ProcessSummary):
    inputs: typing.Optional[typing.Dict[str, InputDescription]] = None
    outputs: typing.Optional[typing.Dict[str, OutputDescription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ProcessDescription)
