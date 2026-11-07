

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionsHistoryLink(UniversalBaseModel):
    """
    Hypermedia link used for transaction history pagination.
    """

    rel: str = pydantic.Field()
    """
    Relation.
    """

    href: str = pydantic.Field()
    """
    Location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
