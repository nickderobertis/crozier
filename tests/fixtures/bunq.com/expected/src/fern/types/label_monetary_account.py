

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .avatar import Avatar
from .label_user import LabelUser
from .pointer import Pointer


class LabelMonetaryAccount(UniversalBaseModel):
    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The avatar of the monetary account.
    """

    bunq_me: typing.Optional[Pointer] = pydantic.Field(default=None)
    """
    Bunq.me pointer with type and value.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the user. Formatted as a ISO 3166-1 alpha-2 country code.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name to display with this monetary account.
    """

    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IBAN of the monetary account.
    """

    is_light: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the monetary account is light.
    """

    label_user: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user this monetary account belongs to.
    """

    merchant_category_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant category code.
    """

    swift_account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number used for a SWIFT payment. May or may not be an IBAN.
    """

    swift_bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    The BIC used for a SWIFT payment.
    """

    transferwise_account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number used for a Transferwise payment. May or may not be an IBAN.
    """

    transferwise_bank_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The bank code used for a Transferwise payment. May or may not be a BIC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
