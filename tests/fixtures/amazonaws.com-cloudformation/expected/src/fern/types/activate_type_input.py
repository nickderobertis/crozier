

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .activate_type_input_type import ActivateTypeInputType
from .activate_type_input_version_bump import ActivateTypeInputVersionBump
from .logging_config import LoggingConfig


class ActivateTypeInput(UniversalBaseModel):
    type: typing_extensions.Annotated[
        typing.Optional[ActivateTypeInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="<p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>",
        ),
    ] = None
    """
    <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    """

    public_type_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicTypeArn"),
        pydantic.Field(
            alias="PublicTypeArn",
            description="<p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>",
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(
            alias="PublisherId",
            description="<p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>",
        ),
    ] = None
    """
    <p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>",
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    """

    type_name_alias: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeNameAlias"),
        pydantic.Field(
            alias="TypeNameAlias",
            description="<p>An alias to assign to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and region. You can activate the same public resource multiple times in the same account and region, using different type name aliases.</p>",
        ),
    ] = None
    """
    <p>An alias to assign to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and region. You can activate the same public resource multiple times in the same account and region, using different type name aliases.</p>
    """

    auto_update: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AutoUpdate"),
        pydantic.Field(
            alias="AutoUpdate",
            description="<p>Whether to automatically update the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>",
        ),
    ] = None
    """
    <p>Whether to automatically update the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>
    """

    logging_config: typing_extensions.Annotated[
        typing.Optional[LoggingConfig], FieldMetadata(alias="LoggingConfig"), pydantic.Field(alias="LoggingConfig")
    ] = None
    execution_role_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExecutionRoleArn"),
        pydantic.Field(
            alias="ExecutionRoleArn", description="The name of the IAM execution role to use to activate the extension."
        ),
    ] = None
    """
    The name of the IAM execution role to use to activate the extension.
    """

    version_bump: typing_extensions.Annotated[
        typing.Optional[ActivateTypeInputVersionBump],
        FieldMetadata(alias="VersionBump"),
        pydantic.Field(
            alias="VersionBump",
            description="<p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>",
        ),
    ] = None
    """
    <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>
    """

    major_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MajorVersion"),
        pydantic.Field(
            alias="MajorVersion",
            description="<p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>",
        ),
    ] = None
    """
    <p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
