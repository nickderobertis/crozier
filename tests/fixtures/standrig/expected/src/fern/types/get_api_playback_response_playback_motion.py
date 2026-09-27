

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetApiPlaybackResponsePlaybackMotion(UniversalBaseModel):
    loaded: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    duration: typing.Optional[float] = None
    time: typing.Optional[float] = None
    running: typing.Optional[bool] = None
    active: typing.Optional[bool] = None
    ended: typing.Optional[bool] = None
    speed: typing.Optional[float] = None
    loop: typing.Optional[bool] = None
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
