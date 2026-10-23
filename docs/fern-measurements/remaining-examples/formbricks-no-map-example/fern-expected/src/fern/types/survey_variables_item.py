

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SurveyVariablesItem_Number(UniversalBaseModel):
    type: typing.Literal["number"] = "number"
    id: str
    name: str
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SurveyVariablesItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    id: str
    name: str
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SurveyVariablesItem = typing_extensions.Annotated[
    typing.Union[SurveyVariablesItem_Number, SurveyVariablesItem_Text], pydantic.Field(discriminator="type")
]
