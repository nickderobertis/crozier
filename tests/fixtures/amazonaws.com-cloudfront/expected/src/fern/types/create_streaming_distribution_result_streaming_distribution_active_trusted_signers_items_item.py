

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_streaming_distribution_result_streaming_distribution_active_trusted_signers_items_item_key_pair_ids import (
    CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds,
)


class CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItem(UniversalBaseModel):
    """
    A complex type that lists the AWS accounts that were included in the <code>TrustedSigners</code> complex type, as well as their active CloudFront key pair IDs, if any.
    """

    aws_account_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AwsAccountNumber"),
        pydantic.Field(
            alias="AwsAccountNumber",
            description="<p>An AWS account that is included in the <code>TrustedSigners</code> complex type for this RTMP distribution. Valid values include:</p> <ul> <li> <p> <code>self</code>, which is the AWS account used to create the distribution.</p> </li> <li> <p>An AWS account number.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>An AWS account that is included in the <code>TrustedSigners</code> complex type for this RTMP distribution. Valid values include:</p> <ul> <li> <p> <code>self</code>, which is the AWS account used to create the distribution.</p> </li> <li> <p>An AWS account number.</p> </li> </ul>
    """

    key_pair_ids: typing_extensions.Annotated[
        typing.Optional[CreateStreamingDistributionResultStreamingDistributionActiveTrustedSignersItemsItemKeyPairIds],
        FieldMetadata(alias="KeyPairIds"),
        pydantic.Field(
            alias="KeyPairIds",
            description="A complex type that lists the active CloudFront key pairs, if any, that are associated with <code>AwsAccountNumber</code>.",
        ),
    ] = None
    """
    A complex type that lists the active CloudFront key pairs, if any, that are associated with <code>AwsAccountNumber</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
