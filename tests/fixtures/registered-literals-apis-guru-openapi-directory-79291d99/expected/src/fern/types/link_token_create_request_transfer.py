

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenCreateRequestTransfer(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with the Transfer product.
    """

    intent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `id` returned by the `/transfer/intent/create` endpoint.
    """

    payment_profile_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `payment_profile_token` returned by the `/payment_profile/create` endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
