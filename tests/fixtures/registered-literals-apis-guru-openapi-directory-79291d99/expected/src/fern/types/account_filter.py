

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_filter_subtypes import AccountFilterSubtypes


class AccountFilter(UniversalBaseModel):
    """
    Enumerates the account subtypes that the application wishes for the user to be able to select from. For more details refer to Plaid documentation on account filters.
    """

    credit: typing.Optional[AccountFilterSubtypes] = None
    depository: typing.Optional[AccountFilterSubtypes] = None
    investment: typing.Optional[AccountFilterSubtypes] = None
    loan: typing.Optional[AccountFilterSubtypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
