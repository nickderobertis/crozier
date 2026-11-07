

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cities_row import CitiesRow
from .meta import Meta


class OpenAqCitiesResult(UniversalBaseModel):
    meta: typing.Optional[Meta] = None
    results: typing.List[CitiesRow]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
