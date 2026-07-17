

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .publish_type_input_type import PublishTypeInputType


class PublishTypeInput(UniversalBaseModel):
    type: typing_extensions.Annotated[
        typing.Optional[PublishTypeInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="<p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>",
        ),
    ] = None
    """
    <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Arn"),
        pydantic.Field(
            alias="Arn",
            description="<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>",
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>",
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    public_version_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicVersionNumber"),
        pydantic.Field(
            alias="PublicVersionNumber",
            description='<p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don\'t specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>',
        ),
    ] = None
    """
    <p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
