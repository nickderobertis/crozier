

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryItemsForTax(UniversalBaseModel):
    """
    The query filter to return the items containing the specified tax IDs.
    """

    tax_ids: typing.List[str] = pydantic.Field()
    """
    A set of `CatalogTax` IDs to be used to find associated `CatalogItem`s.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
