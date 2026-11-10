

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token import AccessToken


class DepositSwitchCreateRequestOptions(UniversalBaseModel):
    """
    Options to configure the `/deposit_switch/create` request. If provided, cannot be `null`.
    """

    transaction_item_access_tokens: typing.Optional[typing.List[AccessToken]] = pydantic.Field(default=None)
    """
    An array of access tokens corresponding to transaction items to use when attempting to match the user to their Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access to the transactions product.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL registered to receive webhooks when the status of a deposit switch request has changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
