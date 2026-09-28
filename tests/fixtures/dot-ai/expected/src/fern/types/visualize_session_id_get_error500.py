

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_error500error import VisualizeSessionIdGetError500Error
from .visualize_session_id_get_error500meta import VisualizeSessionIdGetError500Meta


class VisualizeSessionIdGetError500(UniversalBaseModel):
    success: bool
    error: VisualizeSessionIdGetError500Error
    meta: typing.Optional[VisualizeSessionIdGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
