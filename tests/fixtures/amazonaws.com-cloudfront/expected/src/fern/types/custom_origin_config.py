

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .custom_origin_config_origin_protocol_policy import CustomOriginConfigOriginProtocolPolicy
from .custom_origin_config_origin_ssl_protocols import CustomOriginConfigOriginSslProtocols


class CustomOriginConfig(UniversalBaseModel):
    """
    A customer origin.
    """

    http_port: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="HTTPPort"),
        pydantic.Field(alias="HTTPPort", description="The HTTP port the custom origin listens on."),
    ]
    """
    The HTTP port the custom origin listens on.
    """

    https_port: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="HTTPSPort"),
        pydantic.Field(alias="HTTPSPort", description="The HTTPS port the custom origin listens on."),
    ]
    """
    The HTTPS port the custom origin listens on.
    """

    origin_protocol_policy: typing_extensions.Annotated[
        CustomOriginConfigOriginProtocolPolicy,
        FieldMetadata(alias="OriginProtocolPolicy"),
        pydantic.Field(alias="OriginProtocolPolicy", description="The origin protocol policy to apply to your origin."),
    ]
    """
    The origin protocol policy to apply to your origin.
    """

    origin_ssl_protocols: typing_extensions.Annotated[
        typing.Optional[CustomOriginConfigOriginSslProtocols],
        FieldMetadata(alias="OriginSslProtocols"),
        pydantic.Field(
            alias="OriginSslProtocols",
            description="The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.",
        ),
    ] = None
    """
    The SSL/TLS protocols that you want CloudFront to use when communicating with your origin over HTTPS.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
