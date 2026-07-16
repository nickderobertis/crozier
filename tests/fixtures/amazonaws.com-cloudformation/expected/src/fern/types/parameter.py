

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Parameter(UniversalBaseModel):
    """
    The Parameter data type.
    """

    parameter_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParameterKey")] = (
        pydantic.Field(default=None)
    )
    """
    The key associated with the parameter. If you don't specify a key and value for a particular parameter, CloudFormation uses the default value that's specified in your template.
    """

    parameter_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParameterValue")] = (
        pydantic.Field(default=None)
    )
    """
    The input value associated with the parameter.
    """

    use_previous_value: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="UsePreviousValue")] = (
        pydantic.Field(default=None)
    )
    """
    During a stack update, use the existing parameter value that the stack is using for a given parameter key. If you specify <code>true</code>, do not specify a parameter value.
    """

    resolved_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ResolvedValue")] = (
        pydantic.Field(default=None)
    )
    """
    Read-only. The value that corresponds to a SSM parameter key. This field is returned only for <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html#aws-ssm-parameter-types"> <code>SSM</code> </a> parameter types in the template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
