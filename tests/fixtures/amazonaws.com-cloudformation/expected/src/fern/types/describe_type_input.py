

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .describe_type_input_type import DescribeTypeInputType


class DescribeTypeInput(UniversalBaseModel):
    type: typing_extensions.Annotated[typing.Optional[DescribeTypeInputType], FieldMetadata(alias="Type")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Arn")] = pydantic.Field(default=None)
    """
    <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    version_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="VersionId")] = pydantic.Field(
        default=None
    )
    """
    <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>
    """

    publisher_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PublisherId")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>
    """

    public_version_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PublicVersionNumber")
    ] = pydantic.Field(default=None)
    """
    The version number of a public third-party extension.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
