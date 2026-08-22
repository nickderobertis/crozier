

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_summary_origins_items_item_custom_origin_config_origin_protocol_policy import (
    DistributionSummaryOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
)
from .distribution_summary_origins_items_item_custom_origin_config_origin_ssl_protocols import (
    DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocols,
)


class DistributionSummaryOriginsItemsItemCustomOriginConfig(UniversalBaseModel):
    """
    A complex type that contains information about a custom origin. If the origin is an Amazon S3 bucket, use the <code>S3OriginConfig</code> element instead.
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
        DistributionSummaryOriginsItemsItemCustomOriginConfigOriginProtocolPolicy,
        FieldMetadata(alias="OriginProtocolPolicy"),
        pydantic.Field(alias="OriginProtocolPolicy", description="The origin protocol policy to apply to your origin."),
    ]
    """
    The origin protocol policy to apply to your origin.
    """

    origin_ssl_protocols: typing_extensions.Annotated[
        typing.Optional[DistributionSummaryOriginsItemsItemCustomOriginConfigOriginSslProtocols],
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
