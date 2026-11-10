

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .category import Category
from .request_id import RequestId


class CategoriesGetResponse(UniversalBaseModel):
    """
    CategoriesGetResponse defines the response schema for `/categories/get`
    """

    categories: typing.List[Category] = pydantic.Field()
    """
    An array of all of the transaction categories used by Plaid.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
