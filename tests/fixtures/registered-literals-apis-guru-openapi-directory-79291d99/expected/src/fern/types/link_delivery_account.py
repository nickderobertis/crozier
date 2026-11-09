

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_verification_status import LinkDeliveryVerificationStatus


class LinkDeliveryAccount(UniversalBaseModel):
    """
    Information related to account attached to the connected Item
    """

    class_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    If micro-deposit verification is being used, indicates whether the account being verified is a `business` or `personal` account.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid `account_id`
    """

    mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts. It may also not match the mask that the bank displays to the user.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The official account name
    """

    subtype: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account subtype. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account type. See the [Account schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full list of possible values
    """

    verification_status: typing.Optional[LinkDeliveryVerificationStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
