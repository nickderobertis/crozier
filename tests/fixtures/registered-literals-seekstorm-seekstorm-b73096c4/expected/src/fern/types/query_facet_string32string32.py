

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryFacetString32String32(UniversalBaseModel):
    """
    Facet field values of type string
    """

    field: str = pydantic.Field()
    """
    field name
    """

    prefix: str = pydantic.Field()
    """
    Prefix filter of facet values to return
    """

    length: int = pydantic.Field()
    """
    maximum number of facet values to return
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
