

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelParamsMaxOutputTokens(UniversalBaseModel):
    use_cache: typing.Optional[bool] = None
    reasoning_enabled: typing.Optional[bool] = None
    reasoning_budget: typing.Optional[float] = None
    temperature: typing.Optional[float] = None
    max_output_tokens: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="maxOutputTokens"), pydantic.Field(alias="maxOutputTokens")
    ] = None
    top_p: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="topP"), pydantic.Field(alias="topP")
    ] = None
    top_k: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="topK"), pydantic.Field(alias="topK")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
