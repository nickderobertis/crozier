

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenAicpdConfig(UniversalBaseModel):
    """
    Config for CPD watsonx
    """

    genai_api: typing_extensions.Annotated[str, FieldMetadata(alias="GENAI_API"), pydantic.Field(alias="GENAI_API")]
    genai_project_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_PROJECT_ID"), pydantic.Field(alias="GENAI_PROJECT_ID")
    ]
    genai_cpd_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_CPD_URL"), pydantic.Field(alias="GENAI_CPD_URL")
    ]
    genai_cpd_verify_tls: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="GENAI_CPD_VERIFY_TLS"), pydantic.Field(alias="GENAI_CPD_VERIFY_TLS")
    ] = None
    genai_cpd_username: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_CPD_USERNAME"), pydantic.Field(alias="GENAI_CPD_USERNAME")
    ]
    genai_cpd_password: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="GENAI_CPD_PASSWORD"), pydantic.Field(alias="GENAI_CPD_PASSWORD")
    ] = None
    genai_cpd_api_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="GENAI_CPD_API_KEY"), pydantic.Field(alias="GENAI_CPD_API_KEY")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
