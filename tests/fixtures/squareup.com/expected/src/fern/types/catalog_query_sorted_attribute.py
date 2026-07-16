

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQuerySortedAttribute(UniversalBaseModel):
    """
    The query expression to specify the key to sort search results.
    """

    attribute_name: str = pydantic.Field()
    """
    The attribute whose value is used as the sort key.
    """

    initial_attribute_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first attribute value to be returned by the query. Ascending sorts will return only
    objects with this value or greater, while descending sorts will return only objects with this value
    or less. If unset, start at the beginning (for ascending sorts) or end (for descending sorts).
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The desired sort order, `"ASC"` (ascending) or `"DESC"` (descending).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
