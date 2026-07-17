

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_publisher_output_identity_provider import DescribePublisherOutputIdentityProvider
from .describe_publisher_output_publisher_status import DescribePublisherOutputPublisherStatus


class DescribePublisherOutput(UniversalBaseModel):
    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(alias="PublisherId", description="The ID of the extension publisher."),
    ] = None
    """
    The ID of the extension publisher.
    """

    publisher_status: typing_extensions.Annotated[
        typing.Optional[DescribePublisherOutputPublisherStatus],
        FieldMetadata(alias="PublisherStatus"),
        pydantic.Field(
            alias="PublisherStatus",
            description="Whether the publisher is verified. Currently, all registered publishers are verified.",
        ),
    ] = None
    """
    Whether the publisher is verified. Currently, all registered publishers are verified.
    """

    identity_provider: typing_extensions.Annotated[
        typing.Optional[DescribePublisherOutputIdentityProvider],
        FieldMetadata(alias="IdentityProvider"),
        pydantic.Field(
            alias="IdentityProvider",
            description="The type of account used as the identity provider when registering this publisher with CloudFormation.",
        ),
    ] = None
    """
    The type of account used as the identity provider when registering this publisher with CloudFormation.
    """

    publisher_profile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherProfile"),
        pydantic.Field(
            alias="PublisherProfile", description="The URL to the publisher's profile with the identity provider."
        ),
    ] = None
    """
    The URL to the publisher's profile with the identity provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
