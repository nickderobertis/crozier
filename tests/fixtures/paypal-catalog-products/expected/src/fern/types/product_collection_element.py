

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_time import DateTime
from .link_description_list import LinkDescriptionList


class ProductCollectionElement(UniversalBaseModel):
    """
    The details for a product in the collection response.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the product.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The product description.
    """

    create_time: typing.Optional[DateTime] = pydantic.Field(default=None)
    """
    The date and time when the product was created, in [Internet date and time format](https://tools.ietf.org/html/rfc3339#section-5.6).
    """

    links: typing.Optional[LinkDescriptionList] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
