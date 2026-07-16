

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .merchant import Merchant


class RetrieveMerchantResponse(UniversalBaseModel):
    """
    The response object returned by the [RetrieveMerchant](https://developer.squareup.com/reference/square_2021-08-18/merchants-api/retrieve-merchant) endpoint.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    merchant: typing.Optional[Merchant] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
