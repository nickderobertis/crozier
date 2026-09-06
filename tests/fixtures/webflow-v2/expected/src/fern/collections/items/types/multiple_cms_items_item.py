

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MultipleCmsItemsItem(UniversalBaseModel):
    """
    A single CMS item to create
    """

    name: str = pydantic.Field()
    """
    The name of the item.
    """

    slug: str = pydantic.Field()
    """
    URL slug for the item in your site.
    Note: Updating the item slug will break all links referencing the old slug.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
