

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .meta import Meta
from .parameters_row import ParametersRow


class OpenAqParametersResult(UniversalBaseModel):
    meta: typing.Optional[Meta] = None
    results: typing.List[ParametersRow]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
