

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_error404error import VisualizeSessionIdGetError404Error
from .visualize_session_id_get_error404meta import VisualizeSessionIdGetError404Meta


class VisualizeSessionIdGetError404(UniversalBaseModel):
    success: bool
    error: VisualizeSessionIdGetError404Error
    meta: typing.Optional[VisualizeSessionIdGetError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
