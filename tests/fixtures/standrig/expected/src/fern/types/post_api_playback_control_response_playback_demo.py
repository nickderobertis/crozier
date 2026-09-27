

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_api_playback_control_response_playback_demo_mode import PostApiPlaybackControlResponsePlaybackDemoMode


class PostApiPlaybackControlResponsePlaybackDemo(UniversalBaseModel):
    active: typing.Optional[bool] = None
    mode: typing.Optional[PostApiPlaybackControlResponsePlaybackDemoMode] = None
    parameter_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="parameterIds"), pydantic.Field(alias="parameterIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
