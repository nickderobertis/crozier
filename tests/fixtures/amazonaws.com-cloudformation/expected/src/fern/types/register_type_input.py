

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .register_type_input_logging_config import RegisterTypeInputLoggingConfig
from .register_type_input_type import RegisterTypeInputType


class RegisterTypeInput(UniversalBaseModel):
    type: typing_extensions.Annotated[
        typing.Optional[RegisterTypeInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The kind of extension."),
    ] = None
    """
    The kind of extension.
    """

    type_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <i>company_or_organization</i>::<i>service</i>::<i>type</i>.</p> </li> <li> <p>For modules, <i>company_or_organization</i>::<i>service</i>::<i>type</i>::MODULE.</p> </li> <li> <p>For hooks, <i>MyCompany</i>::<i>Testing</i>::<i>MyTestHook</i>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>",
        ),
    ]
    """
    <p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <i>company_or_organization</i>::<i>service</i>::<i>type</i>.</p> </li> <li> <p>For modules, <i>company_or_organization</i>::<i>service</i>::<i>type</i>::MODULE.</p> </li> <li> <p>For hooks, <i>MyCompany</i>::<i>Testing</i>::<i>MyTestHook</i>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>
    """

    schema_handler_package: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="SchemaHandlerPackage"),
        pydantic.Field(
            alias="SchemaHandlerPackage",
            description='<p>A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation CLI User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That\'s, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>',
        ),
    ]
    """
    <p>A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation CLI User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>
    """

    logging_config: typing_extensions.Annotated[
        typing.Optional[RegisterTypeInputLoggingConfig],
        FieldMetadata(alias="LoggingConfig"),
        pydantic.Field(
            alias="LoggingConfig", description="Specifies logging configuration information for an extension."
        ),
    ] = None
    """
    Specifies logging configuration information for an extension.
    """

    execution_role_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExecutionRoleArn"),
        pydantic.Field(
            alias="ExecutionRoleArn",
            description='<p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>',
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>
    """

    client_request_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientRequestToken"),
        pydantic.Field(
            alias="ClientRequestToken",
            description="A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.",
        ),
    ] = None
    """
    A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
