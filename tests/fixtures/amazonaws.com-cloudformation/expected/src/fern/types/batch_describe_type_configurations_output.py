

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .batch_describe_type_configurations_error import BatchDescribeTypeConfigurationsError
from .type_configuration_details import TypeConfigurationDetails
from .type_configuration_identifier import TypeConfigurationIdentifier


class BatchDescribeTypeConfigurationsOutput(UniversalBaseModel):
    errors: typing_extensions.Annotated[
        typing.Optional[typing.List[BatchDescribeTypeConfigurationsError]], FieldMetadata(alias="Errors")
    ] = pydantic.Field(default=None)
    """
    A list of information concerning any errors generated during the setting of the specified configurations.
    """

    unprocessed_type_configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[TypeConfigurationIdentifier]], FieldMetadata(alias="UnprocessedTypeConfigurations")
    ] = pydantic.Field(default=None)
    """
    A list of any of the specified extension configurations that CloudFormation could not process for any reason.
    """

    type_configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[TypeConfigurationDetails]], FieldMetadata(alias="TypeConfigurations")
    ] = pydantic.Field(default=None)
    """
    A list of any of the specified extension configurations from the CloudFormation registry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
