

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deactivate_type_input_type import DeactivateTypeInputType


class DeactivateTypeInput(UniversalBaseModel):
    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    <p>The type name of the extension, in this account and region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    type: typing_extensions.Annotated[typing.Optional[DeactivateTypeInputType], FieldMetadata(alias="Type")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Arn")] = pydantic.Field(default=None)
    """
    <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
