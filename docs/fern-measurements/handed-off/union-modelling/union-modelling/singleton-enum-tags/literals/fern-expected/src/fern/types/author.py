

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Author_Crew(UniversalBaseModel):
    kind: typing.Literal["crew"] = "crew"
    name: str
    rank: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Author_Contractor(UniversalBaseModel):
    kind: typing.Literal["contractor"] = "contractor"
    company: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Author_Autopilot(UniversalBaseModel):
    kind: typing.Literal["autopilot"] = "autopilot"
    unit: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Author_Harbour(UniversalBaseModel):
    kind: typing.Literal["harbour"] = "harbour"
    office: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Author = typing_extensions.Annotated[
    typing.Union[Author_Crew, Author_Contractor, Author_Autopilot, Author_Harbour], pydantic.Field(discriminator="kind")
]
