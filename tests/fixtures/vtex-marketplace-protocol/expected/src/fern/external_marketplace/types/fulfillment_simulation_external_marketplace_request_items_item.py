

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FulfillmentSimulationExternalMarketplaceRequestItemsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SKU ID.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The quantity of items of this specific SKU in the cart to be simulated.
    """

    seller: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller responsible for this SKU. This ID can be found in your VTEX Admin.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
