

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .inv_relation import InvRelation
from .response import Response


class ResponseSuccessInvRelation(Response):
    data: typing.Optional[InvRelation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
