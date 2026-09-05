

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marker_ui import MarkerUi
from .position_ui import PositionUi


class NodeUiPatch(UniversalBaseModel):
    position: typing.Optional[PositionUi] = pydantic.Field(default=None)
    """
    The node position in the workbench
    """

    marker: typing.Optional[MarkerUi] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
