

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogQueryPrefix(UniversalBaseModel):
    """
    The query filter to return the search result whose named attribute values are prefixed by the specified attribute value.
    """

    attribute_name: str = pydantic.Field()
    """
    The name of the attribute to be searched.
    """

    attribute_prefix: str = pydantic.Field()
    """
    The desired prefix of the search attribute value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
