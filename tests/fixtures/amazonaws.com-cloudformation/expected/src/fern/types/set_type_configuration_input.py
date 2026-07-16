

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .set_type_configuration_input_type import SetTypeConfigurationInputType


class SetTypeConfigurationInput(UniversalBaseModel):
    type_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeArn"),
        pydantic.Field(
            alias="TypeArn",
            description='<p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>',
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>
    """

    configuration: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Configuration"),
        pydantic.Field(
            alias="Configuration",
            description='<p>The configuration data for the extension, in this account and region.</p> <p>The configuration data must be formatted as JSON, and validate against the schema returned in the <code>ConfigurationSchema</code> response element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">API_DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining account-level configuration data for an extension</a> in the <i>CloudFormation CLI User Guide</i>.</p>',
        ),
    ]
    """
    <p>The configuration data for the extension, in this account and region.</p> <p>The configuration data must be formatted as JSON, and validate against the schema returned in the <code>ConfigurationSchema</code> response element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">API_DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining account-level configuration data for an extension</a> in the <i>CloudFormation CLI User Guide</i>.</p>
    """

    configuration_alias: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConfigurationAlias"),
        pydantic.Field(
            alias="ConfigurationAlias",
            description="<p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>",
        ),
    ] = None
    """
    <p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>",
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
    """

    type: typing_extensions.Annotated[
        typing.Optional[SetTypeConfigurationInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="<p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>",
        ),
    ] = None
    """
    <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
