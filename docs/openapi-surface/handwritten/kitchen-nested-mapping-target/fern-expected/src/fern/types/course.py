

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Course_Grill(UniversalBaseModel):
    station: typing.Literal["grill"] = "grill"
    doneness: typing.Optional[str] = None
    count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


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
