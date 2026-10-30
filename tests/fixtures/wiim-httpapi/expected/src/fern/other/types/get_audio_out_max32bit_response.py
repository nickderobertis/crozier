

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetAudioOutMax32BitResponse(UniversalBaseModel):
    audio_out_max32bit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="audioOutMax32bit"),
        pydantic.Field(alias="audioOutMax32bit", description="Indicates if 32-bit audio output is supported (0 or 1)"),
    ] = None
    """
    Indicates if 32-bit audio output is supported (0 or 1)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
