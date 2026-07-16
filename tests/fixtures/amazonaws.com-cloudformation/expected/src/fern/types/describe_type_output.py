

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_type_output_deprecated_status import DescribeTypeOutputDeprecatedStatus
from .describe_type_output_logging_config import DescribeTypeOutputLoggingConfig
from .describe_type_output_provisioning_type import DescribeTypeOutputProvisioningType
from .describe_type_output_type import DescribeTypeOutputType
from .describe_type_output_type_tests_status import DescribeTypeOutputTypeTestsStatus
from .describe_type_output_visibility import DescribeTypeOutputVisibility
from .required_activated_type import RequiredActivatedType


class DescribeTypeOutput(UniversalBaseModel):
    arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Arn"),
        pydantic.Field(alias="Arn", description="The Amazon Resource Name (ARN) of the extension."),
    ] = None
    """
    The Amazon Resource Name (ARN) of the extension.
    """

    type: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputType],
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
            description='<p>The name of the extension.</p> <p>If the extension is a public third-party type you have activated with a type name alias, CloudFormation returns the type name alias. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p>',
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>If the extension is a public third-party type you have activated with a type name alias, CloudFormation returns the type name alias. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p>
    """

    default_version_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefaultVersionId"),
        pydantic.Field(
            alias="DefaultVersionId",
            description='<p>The ID of the default version of the extension. The default version is used when the extension version isn\'t specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <code> <a>SetTypeDefaultVersion</a> </code>.</p>',
        ),
    ] = None
    """
    <p>The ID of the default version of the extension. The default version is used when the extension version isn't specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <code> <a>SetTypeDefaultVersion</a> </code>.</p>
    """

    is_default_version: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsDefaultVersion"),
        pydantic.Field(
            alias="IsDefaultVersion",
            description="<p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon Web Services. For public third-party extensions, whether they are activated in your account, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon Web Services. For public third-party extensions, whether they are activated in your account, CloudFormation returns <code>null</code>.</p>
    """

    type_tests_status: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputTypeTestsStatus],
        FieldMetadata(alias="TypeTestsStatus"),
        pydantic.Field(
            alias="TypeTestsStatus",
            description="<p>The contract test status of the registered extension version. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p> <ul> <li> <p> <code>PASSED</code>: The extension has passed all its contract tests.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href=\"https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html\">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface User Guide</i>.</p> </li> <li> <p> <code>FAILED</code>: The extension has failed one or more contract tests.</p> </li> <li> <p> <code>IN_PROGRESS</code>: Contract tests are currently being performed on the extension.</p> </li> <li> <p> <code>NOT_TESTED</code>: Contract tests haven't been performed on the extension.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>The contract test status of the registered extension version. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p> <ul> <li> <p> <code>PASSED</code>: The extension has passed all its contract tests.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface User Guide</i>.</p> </li> <li> <p> <code>FAILED</code>: The extension has failed one or more contract tests.</p> </li> <li> <p> <code>IN_PROGRESS</code>: Contract tests are currently being performed on the extension.</p> </li> <li> <p> <code>NOT_TESTED</code>: Contract tests haven't been performed on the extension.</p> </li> </ul>
    """

    type_tests_status_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeTestsStatusDescription"),
        pydantic.Field(
            alias="TypeTestsStatusDescription",
            description="<p>The description of the test status. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p>",
        ),
    ] = None
    """
    <p>The description of the test status. To return the extension test status of a specific extension version, you must specify <code>VersionId</code>.</p> <p>This applies only to registered private extension versions. CloudFormation doesn't return this information for public extensions, whether they are activated in your account.</p>
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the extension."),
    ] = None
    """
    The description of the extension.
    """

    schema_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Schema"),
        pydantic.Field(
            alias="Schema",
            description='<p>The schema that defines the extension.</p> <p>For more information about extension schemas, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">Resource Provider Schema</a> in the <i>CloudFormation CLI User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>The schema that defines the extension.</p> <p>For more information about extension schemas, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html">Resource Provider Schema</a> in the <i>CloudFormation CLI User Guide</i>.</p>
    """

    provisioning_type: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputProvisioningType],
        FieldMetadata(alias="ProvisioningType"),
        pydantic.Field(
            alias="ProvisioningType",
            description="<p>For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.</p> <ul> <li> <p>create</p> </li> <li> <p>read</p> </li> <li> <p>delete</p> </li> </ul> </li> </ul>",
        ),
    ] = None
    """
    <p>For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.</p> <ul> <li> <p>create</p> </li> <li> <p>read</p> </li> <li> <p>delete</p> </li> </ul> </li> </ul>
    """

    deprecated_status: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputDeprecatedStatus],
        FieldMetadata(alias="DeprecatedStatus"),
        pydantic.Field(
            alias="DeprecatedStatus",
            description="<p>The deprecation status of the extension version.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is activated or registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deactivated or deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>For public third-party extensions, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>The deprecation status of the extension version.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is activated or registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deactivated or deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>For public third-party extensions, CloudFormation returns <code>null</code>.</p>
    """

    logging_config: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputLoggingConfig],
        FieldMetadata(alias="LoggingConfig"),
        pydantic.Field(
            alias="LoggingConfig",
            description='Contains logging configuration information for private extensions. This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.',
        ),
    ] = None
    """
    Contains logging configuration information for private extensions. This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon Web Services and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.
    """

    required_activated_types: typing_extensions.Annotated[
        typing.Optional[typing.List[RequiredActivatedType]],
        FieldMetadata(alias="RequiredActivatedTypes"),
        pydantic.Field(
            alias="RequiredActivatedTypes",
            description="For extensions that are modules, the public third-party extensions that must be activated in your account in order for the module itself to be activated.",
        ),
    ] = None
    """
    For extensions that are modules, the public third-party extensions that must be activated in your account in order for the module itself to be activated.
    """

    execution_role_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExecutionRoleArn"),
        pydantic.Field(
            alias="ExecutionRoleArn",
            description='<p>The Amazon Resource Name (ARN) of the IAM execution role used to register the extension. This applies only to private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>If the registered extension calls any Amazon Web Services APIs, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your extension with the appropriate credentials.</p>',
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the IAM execution role used to register the extension. This applies only to private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>If the registered extension calls any Amazon Web Services APIs, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. CloudFormation then assumes that execution role to provide your extension with the appropriate credentials.</p>
    """

    visibility: typing_extensions.Annotated[
        typing.Optional[DescribeTypeOutputVisibility],
        FieldMetadata(alias="Visibility"),
        pydantic.Field(
            alias="Visibility",
            description="<p>The scope at which the extension is visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: The extension is only visible and usable within the account in which it is registered. CloudFormation marks any extensions you register as <code>PRIVATE</code>.</p> </li> <li> <p> <code>PUBLIC</code>: The extension is publicly visible and usable within any Amazon Web Services account.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>The scope at which the extension is visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: The extension is only visible and usable within the account in which it is registered. CloudFormation marks any extensions you register as <code>PRIVATE</code>.</p> </li> <li> <p> <code>PUBLIC</code>: The extension is publicly visible and usable within any Amazon Web Services account.</p> </li> </ul>
    """

    source_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SourceUrl"),
        pydantic.Field(alias="SourceUrl", description="The URL of the source code for the extension."),
    ] = None
    """
    The URL of the source code for the extension.
    """

    documentation_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DocumentationUrl"),
        pydantic.Field(
            alias="DocumentationUrl",
            description="The URL of a page providing detailed documentation for this extension.",
        ),
    ] = None
    """
    The URL of a page providing detailed documentation for this extension.
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastUpdated"),
        pydantic.Field(
            alias="LastUpdated",
            description='<p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul>',
        ),
    ] = None
    """
    <p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul>
    """

    time_created: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="TimeCreated"),
        pydantic.Field(
            alias="TimeCreated",
            description="When the specified private extension version was registered or activated in your account.",
        ),
    ] = None
    """
    When the specified private extension version was registered or activated in your account.
    """

    configuration_schema: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConfigurationSchema"),
        pydantic.Field(
            alias="ConfigurationSchema",
            description='<p>A JSON string that represent the current configuration data for the extension in this account and region.</p> <p>To set the configuration data for an extension, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>A JSON string that represent the current configuration data for the extension in this account and region.</p> <p>To set the configuration data for an extension, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(
            alias="PublisherId",
            description="<p>The publisher ID of the extension publisher.</p> <p>This applies only to public third-party extensions. For private registered extensions, and extensions provided by Amazon Web Services, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>The publisher ID of the extension publisher.</p> <p>This applies only to public third-party extensions. For private registered extensions, and extensions provided by Amazon Web Services, CloudFormation returns <code>null</code>.</p>
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

    original_type_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OriginalTypeArn"),
        pydantic.Field(
            alias="OriginalTypeArn",
            description="For public extensions that have been activated for this account and region, the Amazon Resource Name (ARN) of the public extension.",
        ),
    ] = None
    """
    For public extensions that have been activated for this account and region, the Amazon Resource Name (ARN) of the public extension.
    """

    public_version_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicVersionNumber"),
        pydantic.Field(
            alias="PublicVersionNumber",
            description="<p>The version number of a public third-party extension.</p> <p>This applies only if you specify a public extension you have activated in your account, or specify a public extension without specifying a version. For all other extensions, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>The version number of a public third-party extension.</p> <p>This applies only if you specify a public extension you have activated in your account, or specify a public extension without specifying a version. For all other extensions, CloudFormation returns <code>null</code>.</p>
    """

    latest_public_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LatestPublicVersion"),
        pydantic.Field(
            alias="LatestPublicVersion",
            description="<p>The latest version of a public extension <i>that is available</i> for use.</p> <p>This only applies if you specify a public extension, and you don't specify a version. For all other requests, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>The latest version of a public extension <i>that is available</i> for use.</p> <p>This only applies if you specify a public extension, and you don't specify a version. For all other requests, CloudFormation returns <code>null</code>.</p>
    """

    is_activated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsActivated"),
        pydantic.Field(
            alias="IsActivated",
            description="<p>Whether the extension is activated in the account and region.</p> <p>This only applies to public third-party extensions. For all other extensions, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>Whether the extension is activated in the account and region.</p> <p>This only applies to public third-party extensions. For all other extensions, CloudFormation returns <code>null</code>.</p>
    """

    auto_update: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AutoUpdate"),
        pydantic.Field(
            alias="AutoUpdate",
            description='Whether CloudFormation automatically updates the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated. For more information, see <a href="AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable">Activating public extensions for use in your account</a> in the <i>CloudFormation User Guide</i>.',
        ),
    ] = None
    """
    Whether CloudFormation automatically updates the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated. For more information, see <a href="AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable">Activating public extensions for use in your account</a> in the <i>CloudFormation User Guide</i>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
