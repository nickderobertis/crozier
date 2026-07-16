

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

    parameter_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ParameterKey"),
        pydantic.Field(alias="ParameterKey", description="The name that's associated with the parameter."),
    ] = None
    """
    The name that's associated with the parameter.
    """

    default_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DefaultValue"),
        pydantic.Field(alias="DefaultValue", description="The default value of the parameter."),
    ] = None
    """
    The default value of the parameter.
    """

    parameter_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ParameterType"),
        pydantic.Field(alias="ParameterType", description="The type of parameter."),
    ] = None
    """
    The type of parameter.
    """

    no_echo: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="NoEcho"),
        pydantic.Field(
            alias="NoEcho",
            description="Flag that indicates whether the parameter value is shown as plain text in logs and in the Amazon Web Services Management Console.",
        ),
    ] = None
    """
    Flag that indicates whether the parameter value is shown as plain text in logs and in the Amazon Web Services Management Console.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description that's associate with the parameter."),
    ] = None
    """
    The description that's associate with the parameter.
    """

    parameter_constraints: typing_extensions.Annotated[
        typing.Optional[ParameterDeclarationParameterConstraints],
        FieldMetadata(alias="ParameterConstraints"),
        pydantic.Field(
            alias="ParameterConstraints",
            description="The criteria that CloudFormation uses to validate parameter values.",
        ),
    ] = None
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
