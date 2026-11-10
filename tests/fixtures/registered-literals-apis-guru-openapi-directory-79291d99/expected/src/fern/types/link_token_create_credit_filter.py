

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_account_subtypes import CreditAccountSubtypes


class LinkTokenCreateCreditFilter(UniversalBaseModel):
    """
    A filter to apply to `credit`-type accounts
    """

    account_subtypes: typing.Optional[CreditAccountSubtypes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
