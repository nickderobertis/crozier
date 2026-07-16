

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TemplateParameter(UniversalBaseModel):
    """
    The TemplateParameter data type.
    """

    parameter_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ParameterKey")] = (
        pydantic.Field(default=None)
    )
    """
    The name associated with the parameter.
    """

    default_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="DefaultValue")] = (
        pydantic.Field(default=None)
    )
    """
    The default value associated with the parameter.
    """

    no_echo: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="NoEcho")] = pydantic.Field(
        default=None
    )
    """
    Flag indicating whether the parameter should be displayed as plain text in logs and UIs.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    User defined description associated with the parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
