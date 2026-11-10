

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AccountProductAccess(UniversalBaseModel):
    """
    Allow the application to access specific products on this account
    """

    account_data: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow the application to access account data. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    statements: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow the application to access bank statements. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    tax_documents: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow the application to access tax documents. Only used by certain partners. If relevant to the partner and unset, defaults to `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
