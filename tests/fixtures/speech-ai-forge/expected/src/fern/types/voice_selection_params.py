

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VoiceSelectionParams(UniversalBaseModel):
    language_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="languageCode"), pydantic.Field(alias="languageCode")
    ] = None
    name: typing.Optional[str] = None
    style: typing.Optional[str] = None
    temperature: typing.Optional[float] = None
    top_p: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="topP"), pydantic.Field(alias="topP")
    ] = None
    top_k: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="topK"), pydantic.Field(alias="topK")
    ] = None
    seed: typing.Optional[int] = None
    eos: typing.Optional[str] = None
    model: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
