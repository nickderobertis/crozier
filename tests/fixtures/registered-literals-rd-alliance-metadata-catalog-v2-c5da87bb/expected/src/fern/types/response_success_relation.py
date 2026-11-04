

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .relation import Relation
from .response import Response


class ResponseSuccessRelation(Response):
    data: typing.Optional[Relation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
