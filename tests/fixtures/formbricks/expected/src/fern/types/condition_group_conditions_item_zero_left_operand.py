

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConditionGroupConditionsItemZeroLeftOperand_Element(UniversalBaseModel):
    type: typing.Literal["element"] = "element"
    value: str
    meta: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConditionGroupConditionsItemZeroLeftOperand_Variable(UniversalBaseModel):
    type: typing.Literal["variable"] = "variable"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConditionGroupConditionsItemZeroLeftOperand_HiddenField(UniversalBaseModel):
    type: typing.Literal["hiddenField"] = "hiddenField"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConditionGroupConditionsItemZeroLeftOperand = typing_extensions.Annotated[
    typing.Union[
        ConditionGroupConditionsItemZeroLeftOperand_Element,
        ConditionGroupConditionsItemZeroLeftOperand_Variable,
        ConditionGroupConditionsItemZeroLeftOperand_HiddenField,
    ],
    pydantic.Field(discriminator="type"),
]
