

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .distribution_active_trusted_signers_items_item import DistributionActiveTrustedSignersItemsItem


class DistributionActiveTrustedSigners(UniversalBaseModel):
    """
    CloudFront automatically adds this element to the response only if you've set up the distribution to serve private content with signed URLs. The element lists the key pair IDs that CloudFront is aware of for each trusted signer. The <code>Signer</code> child element lists the AWS account number of the trusted signer (or an empty <code>Self</code> element if the signer is you). The <code>Signer</code> element also includes the IDs of any active key pairs associated with the trusted signer's AWS account. If no <code>KeyPairId</code> element appears for a <code>Signer</code>, that signer can't create working signed URLs.
    """

    enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Enabled"),
        pydantic.Field(
            alias="Enabled",
            description="<p>Enabled is <code>true</code> if any of the AWS accounts listed in the <code>TrustedSigners</code> complex type for this RTMP distribution have active CloudFront key pairs. If not, <code>Enabled</code> is <code>false</code>.</p> <p>For more information, see <a>ActiveTrustedSigners</a>.</p>",
        ),
    ]
    """
    <p>Enabled is <code>true</code> if any of the AWS accounts listed in the <code>TrustedSigners</code> complex type for this RTMP distribution have active CloudFront key pairs. If not, <code>Enabled</code> is <code>false</code>.</p> <p>For more information, see <a>ActiveTrustedSigners</a>.</p>
    """

    quantity: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Quantity"),
        pydantic.Field(
            alias="Quantity",
            description="<p>A complex type that contains one <code>Signer</code> complex type for each trusted signer specified in the <code>TrustedSigners</code> complex type.</p> <p>For more information, see <a>ActiveTrustedSigners</a>.</p>",
        ),
    ]
    """
    <p>A complex type that contains one <code>Signer</code> complex type for each trusted signer specified in the <code>TrustedSigners</code> complex type.</p> <p>For more information, see <a>ActiveTrustedSigners</a>.</p>
    """

    items: typing_extensions.Annotated[
        typing.Optional[typing.List[DistributionActiveTrustedSignersItemsItem]],
        FieldMetadata(alias="Items"),
        pydantic.Field(
            alias="Items",
            description="<p>A complex type that contains one <code>Signer</code> complex type for each trusted signer that is specified in the <code>TrustedSigners</code> complex type.</p> <p>For more information, see <a>ActiveTrustedSigners</a>. </p>",
        ),
    ] = None
    """
    <p>A complex type that contains one <code>Signer</code> complex type for each trusted signer that is specified in the <code>TrustedSigners</code> complex type.</p> <p>For more information, see <a>ActiveTrustedSigners</a>. </p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
