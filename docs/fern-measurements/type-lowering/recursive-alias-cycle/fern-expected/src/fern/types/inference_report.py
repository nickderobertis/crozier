

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class InferenceReport(UniversalBaseModel):
    engine: str
    inference_diagnostics: typing.Optional["JsonObjectOutput"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_array_output import JsonArrayOutput
from .json_object_output import JsonObjectOutput
from .json_value_output import JsonValueOutput

update_forward_refs(
    InferenceReport, JsonArrayOutput=JsonArrayOutput, JsonObjectOutput=JsonObjectOutput, JsonValueOutput=JsonValueOutput
)
