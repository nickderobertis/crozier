

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .confidence import Confidence
from .geometry import Geometry
from .selection_mark_type import SelectionMarkType
from .selection_state import SelectionState
from .source_provenance import SourceProvenance


class SelectionMarkElement(UniversalBaseModel):
    id: str
    locations: typing.List[Geometry]
    confidence: typing.Optional[Confidence] = None
    source: typing.Optional[SourceProvenance] = None
    state: SelectionState
    mark_type: SelectionMarkType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
