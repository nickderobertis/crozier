

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BedrockConfig(UniversalBaseModel):
    """
    Configuration options for Bedrock.

        **Keys.**

        - `profile_name`: the AWS profile to use
        - `region_name`: the AWS region to use
        - `aws_access_key_id`: the AWS access key ID
        - `aws_secret_access_key`: the AWS secret access key
    """

    aws_access_key_id: typing.Optional[str] = None
    aws_secret_access_key: typing.Optional[str] = None
    profile_name: typing.Optional[str] = None
    region_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
