

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacetCapability(UniversalBaseModel):
    """
    Describes a search facet field the implementation supports.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional human-readable display label for the facet field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
