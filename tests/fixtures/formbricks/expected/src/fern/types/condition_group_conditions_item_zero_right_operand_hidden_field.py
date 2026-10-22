

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConditionGroupConditionsItemZeroRightOperandHiddenField_Element(UniversalBaseModel):
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


class ConditionGroupConditionsItemZeroRightOperandHiddenField_Variable(UniversalBaseModel):
    type: typing.Literal["variable"] = "variable"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ConditionGroupConditionsItemZeroRightOperandHiddenField_HiddenField(UniversalBaseModel):
    type: typing.Literal["hiddenField"] = "hiddenField"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ConditionGroupConditionsItemZeroRightOperandHiddenField = typing_extensions.Annotated[
    typing.Union[
        ConditionGroupConditionsItemZeroRightOperandHiddenField_Element,
        ConditionGroupConditionsItemZeroRightOperandHiddenField_Variable,
        ConditionGroupConditionsItemZeroRightOperandHiddenField_HiddenField,
    ],
    pydantic.Field(discriminator="type"),
]
