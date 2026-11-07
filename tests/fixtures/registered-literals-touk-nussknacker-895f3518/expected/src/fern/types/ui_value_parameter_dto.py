

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .expression import Expression
from .ui_value_parameter_dto_typ import UiValueParameterDtoTyp


class UiValueParameterDto(UniversalBaseModel):
    name: str
    typ: UiValueParameterDtoTyp
    expression: Expression

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(UiValueParameterDto)
