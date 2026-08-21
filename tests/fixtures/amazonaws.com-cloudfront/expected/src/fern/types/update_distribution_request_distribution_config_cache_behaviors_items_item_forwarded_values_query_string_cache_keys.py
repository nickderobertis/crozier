

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateDistributionRequestDistributionConfigCacheBehaviorsItemsItemForwardedValuesQueryStringCacheKeys(
    UniversalBaseModel
):
    """
    A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of <code>whitelisted</code> query string parameters for this cache behavior.",
        ),
    ]
    """
    The number of <code>whitelisted</code> query string parameters for this cache behavior.
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="(Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If <code>Quantity</code> is 0, you can omit <code>Items</code>. ",
        ),
    ] = None
    """
    (Optional) A list that contains the query string parameters that you want CloudFront to use as a basis for caching for this cache behavior. If <code>Quantity</code> is 0, you can omit <code>Items</code>. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
