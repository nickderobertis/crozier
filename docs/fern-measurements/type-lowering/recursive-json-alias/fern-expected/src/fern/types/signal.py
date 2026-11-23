

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class Signal(UniversalBaseModel):
    id: str
    payload: "JsonValue"
    history: typing.List["JsonValue"]
    labels: typing.Optional[typing.Dict[str, "JsonValue"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .json_value import JsonValue

update_forward_refs(Signal, JsonValue=JsonValue)
