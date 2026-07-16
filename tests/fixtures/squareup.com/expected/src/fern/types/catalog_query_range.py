

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryRange(UniversalBaseModel):
    """
    The query filter to return the search result whose named attribute values fall between the specified range.
    """

    attribute_max_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The desired maximum value for the search attribute (inclusive).
    """

    attribute_min_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The desired minimum value for the search attribute (inclusive).
    """

    attribute_name: str = pydantic.Field()
    """
    The name of the attribute to be searched.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
