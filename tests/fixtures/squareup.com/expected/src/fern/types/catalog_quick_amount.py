

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CatalogQuickAmount(UniversalBaseModel):
    """
    Represents a Quick Amount in the Catalog.
    """

    amount: Money
    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The order in which this Quick Amount should be displayed.
    """

    score: typing.Optional[int] = pydantic.Field(default=None)
    """
    Describes the ranking of the Quick Amount provided by machine learning model, in the range [0, 100].
    MANUAL type amount will always have score = 100.
    """

    type: str = pydantic.Field()
    """
    Represents the type of the Quick Amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
