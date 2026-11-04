

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_value import FilterValue


class Filter(UniversalBaseModel):
    name: typing.Optional[str] = None
    type: typing.Optional[str] = None
    values: typing.Optional[typing.List[FilterValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
