

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_distributions_by_web_acl_id_result_distribution_list_items_item_custom_error_responses_items_item import (
    ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponsesItemsItem,
)


class ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponses(UniversalBaseModel):
    """
    A complex type that contains zero or more <code>CustomErrorResponses</code> elements.
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.",
        ),
    ]
    """
    The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If <code>Quantity</code> is <code>0</code>, you can omit <code>Items</code>.
    """

    items: typing_extensions.Annotated[
        typing.Optional[
            typing.List[ListDistributionsByWebAclIdResultDistributionListItemsItemCustomErrorResponsesItemsItem]
        ],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="A complex type that contains a <code>CustomErrorResponse</code> element for each HTTP status code for which you want to specify a custom error page and/or a caching duration. ",
        ),
    ] = None
    """
    A complex type that contains a <code>CustomErrorResponse</code> element for each HTTP status code for which you want to specify a custom error page and/or a caching duration. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
