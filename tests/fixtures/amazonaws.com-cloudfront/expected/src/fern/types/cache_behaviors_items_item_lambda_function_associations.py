

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cache_behaviors_items_item_lambda_function_associations_items_item import (
    CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem,
)


class CacheBehaviorsItemsItemLambdaFunctionAssociations(UniversalBaseModel):
    """
    A complex type that contains zero or more Lambda function associations for a cache behavior.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity", description="The number of Lambda function associations for this cache behavior."
        ),
    ]
    """
    The number of Lambda function associations for this cache behavior.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[CacheBehaviorsItemsItemLambdaFunctionAssociationsItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description=" <b>Optional</b>: A complex type that contains <code>LambdaFunctionAssociation</code> items for this cache behavior. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.",
        ),
    ] = None
    """
     <b>Optional</b>: A complex type that contains <code>LambdaFunctionAssociation</code> items for this cache behavior. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
