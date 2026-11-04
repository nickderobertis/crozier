

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .response import Response
from .response_page_inv_relation_data import ResponsePageInvRelationData


class ResponsePageInvRelation(Response):
    data: typing.Optional[ResponsePageInvRelationData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
