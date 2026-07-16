

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .parameter_declaration_parameter_constraints import ParameterDeclarationParameterConstraints


class ParameterDeclaration(UniversalBaseModel):
    """
    The ParameterDeclaration data type.
    """

    parameter_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParameterKey")] = (
        pydantic.Field(default=None)
    )
    """
    The name that's associated with the parameter.
    """

    default_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="DefaultValue")] = (
        pydantic.Field(default=None)
    )
    """
    The default value of the parameter.
    """

    parameter_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParameterType")] = (
        pydantic.Field(default=None)
    )
    """
    The type of parameter.
    """

    no_echo: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="NoEcho")] = pydantic.Field(
        default=None
    )
    """
    Flag that indicates whether the parameter value is shown as plain text in logs and in the Amazon Web Services Management Console.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    The description that's associate with the parameter.
    """

    parameter_constraints: typing_extensions.Annotated[
        typing.Optional[ParameterDeclarationParameterConstraints], FieldMetadata(alias="ParameterConstraints")
    ] = pydantic.Field(default=None)
    """
    The criteria that CloudFormation uses to validate parameter values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
