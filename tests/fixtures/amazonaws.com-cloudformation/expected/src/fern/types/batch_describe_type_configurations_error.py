

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_configuration_identifier import TypeConfigurationIdentifier


class BatchDescribeTypeConfigurationsError(UniversalBaseModel):
    """
    Detailed information concerning an error generated during the setting of configuration data for a CloudFormation extension.
    """

    error_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ErrorCode")] = pydantic.Field(
        default=None
    )
    """
    The error code.
    """

    error_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ErrorMessage")] = (
        pydantic.Field(default=None)
    )
    """
    The error message.
    """

    type_configuration_identifier: typing_extensions.Annotated[
        typing.Optional[TypeConfigurationIdentifier], FieldMetadata(alias="TypeConfigurationIdentifier")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
