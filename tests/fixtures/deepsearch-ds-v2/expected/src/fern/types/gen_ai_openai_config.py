

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenAiOpenaiConfig(UniversalBaseModel):
    """
    Config for OpenAI API
    """

    genai_openai_api_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_OPENAI_API_KEY"), pydantic.Field(alias="GENAI_OPENAI_API_KEY")
    ]
    genai_openai_base_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_OPENAI_BASE_URL"), pydantic.Field(alias="GENAI_OPENAI_BASE_URL")
    ]
    genai_openai_verify_tls: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="GENAI_OPENAI_VERIFY_TLS"),
        pydantic.Field(alias="GENAI_OPENAI_VERIFY_TLS"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
