

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GenAiawsBedrockConfig(UniversalBaseModel):
    """
    Config for AWS Bedrock
    """

    genai_aws_access_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_AWS_ACCESS_KEY"), pydantic.Field(alias="GENAI_AWS_ACCESS_KEY")
    ]
    genai_aws_secret_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_AWS_SECRET_KEY"), pydantic.Field(alias="GENAI_AWS_SECRET_KEY")
    ]
    genai_aws_region_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="GENAI_AWS_REGION_NAME"), pydantic.Field(alias="GENAI_AWS_REGION_NAME")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
