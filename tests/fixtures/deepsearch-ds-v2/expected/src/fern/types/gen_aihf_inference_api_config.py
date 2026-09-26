

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenAihfInferenceApiConfig(UniversalBaseModel):
    """
    Config for HF Inference API
    """

    genai_hf_api_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_HF_API_KEY"), pydantic.Field(alias="GENAI_HF_API_KEY")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
