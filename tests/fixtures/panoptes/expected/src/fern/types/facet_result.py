

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class FacetResult(UniversalBaseModel):
    value: typing.Optional[str] = None
    count: typing.Optional[float] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For tree facets. Name of this node (value is the full path including parent nodes)
    """

    children: typing.Optional[typing.List["FacetResult"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(FacetResult)
