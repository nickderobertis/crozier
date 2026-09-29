

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provenance import Provenance


class ResultCountry(UniversalBaseModel):
    code: typing.Optional[str] = None
    label: typing.Optional[str] = None
    provenance: typing.Optional[Provenance] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
