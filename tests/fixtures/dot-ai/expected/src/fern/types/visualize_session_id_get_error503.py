

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_error503error import VisualizeSessionIdGetError503Error
from .visualize_session_id_get_error503meta import VisualizeSessionIdGetError503Meta


class VisualizeSessionIdGetError503(UniversalBaseModel):
    success: bool
    error: VisualizeSessionIdGetError503Error
    meta: typing.Optional[VisualizeSessionIdGetError503Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
