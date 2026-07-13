

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .issuer import Issuer


class MonetaryAccountProfileFill(UniversalBaseModel):
    balance_preferred: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The goal balance.
    """

    balance_threshold_low: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The low threshold balance.
    """

    issuer: typing.Optional[Issuer] = pydantic.Field(default=None)
    """
    The bank the fill is supposed to happen from, with BIC and bank name.
    """

    method_fill: typing.Optional[str] = pydantic.Field(default=None)
    """
    The method used to fill the monetary account. Currently only iDEAL is supported, and it is the default one.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the profile.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
