

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marker_at import MarkerAt
from .marker_kind import MarkerKind


class Marker(UniversalBaseModel):
    extent: typing.Optional[typing.List[typing.Any]] = None
    kind: MarkerKind
    at: MarkerAt

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
