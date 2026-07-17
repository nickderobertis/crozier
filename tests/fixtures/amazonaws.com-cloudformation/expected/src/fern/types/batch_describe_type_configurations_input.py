

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_configuration_identifier import TypeConfigurationIdentifier


class BatchDescribeTypeConfigurationsInput(UniversalBaseModel):
    type_configuration_identifiers: typing_extensions.Annotated[
        typing.List[TypeConfigurationIdentifier],
        FieldMetadata(alias="TypeConfigurationIdentifiers"),
        pydantic.Field(
            alias="TypeConfigurationIdentifiers",
            description="The list of identifiers for the desired extension configurations.",
        ),
    ]
    """
    The list of identifiers for the desired extension configurations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
