

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .depository_account_subtypes import DepositoryAccountSubtypes


class DepositoryFilter(UniversalBaseModel):
    """
    A filter to apply to `depository`-type accounts
    """

    account_subtypes: DepositoryAccountSubtypes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
