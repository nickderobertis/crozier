

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_error404error_code import VisualizeSessionIdGetError404ErrorCode


class VisualizeSessionIdGetError404Error(UniversalBaseModel):
    code: VisualizeSessionIdGetError404ErrorCode
    message: str
    details: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
