

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_response_data import VisualizeSessionIdGetResponseData
from .visualize_session_id_get_response_meta import VisualizeSessionIdGetResponseMeta


class VisualizeSessionIdGetResponse(UniversalBaseModel):
    success: bool
    data: VisualizeSessionIdGetResponseData
    meta: typing.Optional[VisualizeSessionIdGetResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
