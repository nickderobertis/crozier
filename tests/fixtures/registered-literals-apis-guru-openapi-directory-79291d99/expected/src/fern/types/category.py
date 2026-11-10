

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Category(UniversalBaseModel):
    """
    Information describing a transaction category
    """

    category_id: str = pydantic.Field()
    """
    An identifying number for the category. `category_id` is a Plaid-specific identifier and does not necessarily correspond to merchant category codes.
    """

    group: str = pydantic.Field()
    """
    `place` for physical transactions or `special` for other transactions such as bank charges.
    """

    hierarchy: typing.List[str] = pydantic.Field()
    """
    A hierarchical array of the categories to which this `category_id` belongs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
