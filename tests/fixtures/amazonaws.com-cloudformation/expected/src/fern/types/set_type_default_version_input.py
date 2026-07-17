

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .set_type_default_version_input_type import SetTypeDefaultVersionInputType


class SetTypeDefaultVersionInput(UniversalBaseModel):
    arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Arn"),
        pydantic.Field(
            alias="Arn",
            description="<p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type: typing_extensions.Annotated[
        typing.Optional[SetTypeDefaultVersionInputType],
        FieldMetadata(alias="Type"),
        pydantic.Field(
            alias="Type",
            description="<p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(
            alias="TypeName",
            description="<p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>",
        ),
    ] = None
    """
    <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    """

    version_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VersionId"),
        pydantic.Field(
            alias="VersionId",
            description="The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.",
        ),
    ] = None
    """
    The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
