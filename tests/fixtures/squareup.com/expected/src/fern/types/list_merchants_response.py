

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .merchant import Merchant


class ListMerchantsResponse(UniversalBaseModel):
    """
    The response object returned by the [ListMerchant](https://developer.squareup.com/reference/square_2021-08-18/merchants-api/list-merchants) endpoint.
    """

    cursor: typing.Optional[int] = pydantic.Field(default=None)
    """
    If the  response is truncated, the cursor to use in next  request to fetch next set of objects.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    merchant: typing.Optional[typing.List[Merchant]] = pydantic.Field(default=None)
    """
    The requested `Merchant` entities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
