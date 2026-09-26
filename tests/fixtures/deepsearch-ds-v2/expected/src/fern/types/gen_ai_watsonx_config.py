

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenAiWatsonxConfig(UniversalBaseModel):
    """
    Config for watsonx
    """

    genai_api: typing_extensions.Annotated[str, FieldMetadata(alias="GENAI_API"), pydantic.Field(alias="GENAI_API")]
    genai_project_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_PROJECT_ID"), pydantic.Field(alias="GENAI_PROJECT_ID")
    ]
    genai_key: typing_extensions.Annotated[str, FieldMetadata(alias="GENAI_KEY"), pydantic.Field(alias="GENAI_KEY")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
