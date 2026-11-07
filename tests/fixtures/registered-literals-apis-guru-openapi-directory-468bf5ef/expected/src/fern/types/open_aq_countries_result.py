

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .countries_row import CountriesRow
from .meta import Meta


class OpenAqCountriesResult(UniversalBaseModel):
    meta: typing.Optional[Meta] = None
    results: typing.List[CountriesRow]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
