

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomerGroup(UniversalBaseModel):
    """
    Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using
    the Customers API or within the Customer Directory in the Square Seller Dashboard or Point of Sale.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the customer group was created, in RFC 3339 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique Square-generated ID for the customer group.
    """

    name: str = pydantic.Field()
    """
    The name of the customer group.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the customer group was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
