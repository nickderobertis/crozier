

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class TransferOriginatorCreateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/originator/create`
    """

    company_name: str = pydantic.Field()
    """
    The company name of the end customer.
    """

    originator_client_id: str = pydantic.Field()
    """
    Client ID of the originator. This identifier will be used when creating transfers and should be stored associated with end user information.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
