

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination import Pagination
from .pricebook import Pricebook


class GetPricebooksResponse(UniversalBaseModel):
    result: str
    data: typing.List[Pricebook]
    paging: typing.Optional[Pagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
