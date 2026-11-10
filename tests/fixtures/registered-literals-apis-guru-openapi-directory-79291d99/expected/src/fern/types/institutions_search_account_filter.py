

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_subtype import AccountSubtype


class InstitutionsSearchAccountFilter(UniversalBaseModel):
    """
    An account filter to apply to institutions search requests
    """

    credit: typing.Optional[typing.List[typing.Optional[AccountSubtype]]] = None
    depository: typing.Optional[typing.List[typing.Optional[AccountSubtype]]] = None
    investment: typing.Optional[typing.List[typing.Optional[AccountSubtype]]] = None
    loan: typing.Optional[typing.List[typing.Optional[AccountSubtype]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
