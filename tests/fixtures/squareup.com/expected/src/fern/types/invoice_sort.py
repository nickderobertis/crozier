

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvoiceSort(UniversalBaseModel):
    """
    Identifies the sort field and sort order.
    """

    field: str = pydantic.Field()
    """
    The field to use for sorting.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order to use for sorting the results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
