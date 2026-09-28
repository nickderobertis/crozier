

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2log_detail_cost_items_item import V2LogDetailCostItemsItem


class V2LogDetailCost(UniversalBaseModel):
    total: float = pydantic.Field()
    """
    Total execution cost in USD.
    """

    items: typing.Optional[typing.List[V2LogDetailCostItemsItem]] = pydantic.Field(default=None)
    """
    Billed lines reconciling to `total`, or null when no itemized ledger exists for the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
