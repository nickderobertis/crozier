

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomerSegment(UniversalBaseModel):
    """
    Represents a group of customer profiles that match one or more predefined filter criteria.

    Segments (also known as Smart Groups) are defined and created within the Customer Directory in the
    Square Seller Dashboard or Point of Sale.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the segment was created, in RFC 3339 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique Square-generated ID for the segment.
    """

    name: str = pydantic.Field()
    """
    The name of the segment.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the segment was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
