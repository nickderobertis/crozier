

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PlaceFulfillmentOrderRequestItemsItemBundleItemsItem(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Service identifier.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service name.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    Service price. The last two digits are the cents.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Service type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
