

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacetFilterStringSet16StringSet16(UniversalBaseModel):
    """
    StringSet16 filter
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: typing.List[str] = pydantic.Field()
    """
    filter: array of facet string values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
