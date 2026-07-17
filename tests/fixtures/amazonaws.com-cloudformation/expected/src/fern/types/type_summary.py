

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_summary_publisher_identity import TypeSummaryPublisherIdentity
from .type_summary_type import TypeSummaryType


class TypeSummary(UniversalBaseModel):
    """
    Contains summary information about the specified CloudFormation extension.
    """

    type: typing_extensions.Annotated[
        typing.Optional[TypeSummaryType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The kind of extension."),
    ] = None
    """
    The kind of extension.
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description='<p>The name of the extension.</p> <p>If you specified a <code>TypeNameAlias</code> when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate this extension</a> in your account and region, CloudFormation considers that alias as the type name.</p>',
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>If you specified a <code>TypeNameAlias</code> when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate this extension</a> in your account and region, CloudFormation considers that alias as the type name.</p>
    """

    default_version_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefaultVersionId"),
        pydantic.Field(
            alias="DefaultVersionId",
            description='<p>The ID of the default version of the extension. The default version is used when the extension version isn\'t specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <code> <a>SetTypeDefaultVersion</a> </code>.</p>',
        ),
    ] = None
    """
    <p>The ID of the default version of the extension. The default version is used when the extension version isn't specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <code> <a>SetTypeDefaultVersion</a> </code>.</p>
    """

    type_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeArn"),
        pydantic.Field(alias="TypeArn", description="The Amazon Resource Name (ARN) of the extension."),
    ] = None
    """
    The Amazon Resource Name (ARN) of the extension.
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastUpdated"),
        pydantic.Field(
            alias="LastUpdated",
            description='<p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul> <p>For all other extension types, CloudFormation returns <code>null</code>.</p>',
        ),
    ] = None
    """
    <p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul> <p>For all other extension types, CloudFormation returns <code>null</code>.</p>
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the extension."),
    ] = None
    """
    The description of the extension.
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(
            alias="PublisherId",
            description="The ID of the extension publisher, if the extension is published by a third party. Extensions published by Amazon don't return a publisher ID.",
        ),
    ] = None
    """
    The ID of the extension publisher, if the extension is published by a third party. Extensions published by Amazon don't return a publisher ID.
    """

    original_type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OriginalTypeName"),
        pydantic.Field(
            alias="OriginalTypeName",
            description='<p>For public extensions that have been activated for this account and region, the type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and region, CloudFormation treats that alias as the extension\'s type name within the account and region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Specifying aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For public extensions that have been activated for this account and region, the type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and region, CloudFormation treats that alias as the extension's type name within the account and region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Specifying aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    public_version_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicVersionNumber"),
        pydantic.Field(
            alias="PublicVersionNumber",
            description='<p>For public extensions that have been activated for this account and region, the version of the public extension to be used for CloudFormation operations in this account and Region.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For public extensions that have been activated for this account and region, the version of the public extension to be used for CloudFormation operations in this account and Region.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    latest_public_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LatestPublicVersion"),
        pydantic.Field(
            alias="LatestPublicVersion",
            description='<p>For public extensions that have been activated for this account and region, the latest version of the public extension <i>that is available</i>. For any extensions other than activated third-arty extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For public extensions that have been activated for this account and region, the latest version of the public extension <i>that is available</i>. For any extensions other than activated third-arty extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    publisher_identity: typing_extensions.Annotated[
        typing.Optional[TypeSummaryPublisherIdentity],
        FieldMetadata(alias="PublisherIdentity"),
        pydantic.Field(
            alias="PublisherIdentity",
            description='<p>The service used to verify the publisher identity.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Registering your account to publish CloudFormation extensions</a> in the <i> CFN-CLI User Guide for Extension Development</i>.</p>',
        ),
    ] = None
    """
    <p>The service used to verify the publisher identity.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Registering your account to publish CloudFormation extensions</a> in the <i> CFN-CLI User Guide for Extension Development</i>.</p>
    """

    publisher_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherName"),
        pydantic.Field(
            alias="PublisherName",
            description="The publisher name, as defined in the public profile for that publisher in the service used to verify the publisher identity.",
        ),
    ] = None
    """
    The publisher name, as defined in the public profile for that publisher in the service used to verify the publisher identity.
    """

    is_activated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsActivated"),
        pydantic.Field(
            alias="IsActivated",
            description="<p>Whether the extension is activated for this account and region.</p> <p>This applies only to third-party public extensions. Extensions published by Amazon are activated by default.</p>",
        ),
    ] = None
    """
    <p>Whether the extension is activated for this account and region.</p> <p>This applies only to third-party public extensions. Extensions published by Amazon are activated by default.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
