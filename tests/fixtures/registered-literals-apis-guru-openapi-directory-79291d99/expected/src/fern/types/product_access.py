

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProductAccess(UniversalBaseModel):
    """
    The product access being requested. Used to or disallow product access across all accounts. If unset, defaults to all products allowed.
    """

    accounts_details_transactions: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to "accounts_details_transactions". Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    accounts_routing_number: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to "accounts_routing_number". Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    accounts_statements: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to "accounts_statements". Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    accounts_tax_statements: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to "accounts_tax_statements". Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to account number details. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    customers_profiles: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to "customers_profiles". Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    identity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to the Identity product (name, email, phone, address). Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    statements: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    transactions: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow access to transaction details. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
