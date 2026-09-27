

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_shape import LoadShape
from .load_stage import LoadStage


class LoadProfile(UniversalBaseModel):
    """
    describes the load over time, as EITHER an ordered list of 'stages' OR a single named 'shape' (which expands into stages). Set one, not both; if both are set the explicit stages win.
    """

    stages: typing.Optional[typing.List[LoadStage]] = pydantic.Field(default=None)
    """
    ordered stages run one after another (max 20). Each holds or ramps virtual users (VU, closed model) or an arrival rate (RATE, open model), or pauses (PAUSE).
    """

    shape: typing.Optional[LoadShape] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
