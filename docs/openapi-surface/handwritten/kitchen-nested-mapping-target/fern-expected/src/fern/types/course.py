

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .grill_course import GrillCourse


class Course_Grill(UniversalBaseModel):
    value: GrillCourse
    station: typing.Literal["grill"] = "grill"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


class Course_Pastry(UniversalBaseModel):
    station: typing.Literal["pastry"] = "pastry"
    item: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Course = typing_extensions.Annotated[typing.Union[Course_Grill, Course_Pastry], pydantic.Field(discriminator="station")]
