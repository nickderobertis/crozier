

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_distributions_result_distribution_list_items_item_cache_behaviors_items_item import (
    ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItem,
)


class ListDistributionsResultDistributionListItemsItemCacheBehaviors(UniversalBaseModel):
    """
    A complex type that contains zero or more <code>CacheBehavior</code> elements.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(alias="Quantity", description="The number of cache behaviors for this distribution. "),
    ]
    """
    The number of cache behaviors for this distribution. 
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[ListDistributionsResultDistributionListItemsItemCacheBehaviorsItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="Optional: A complex type that contains cache behaviors for this distribution. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.",
        ),
    ] = None
    """
    Optional: A complex type that contains cache behaviors for this distribution. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
