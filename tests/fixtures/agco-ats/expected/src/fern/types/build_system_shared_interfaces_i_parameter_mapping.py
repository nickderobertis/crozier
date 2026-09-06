

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .build_system_shared_interfaces_i_parameter_mapping_source_type import (
    BuildSystemSharedInterfacesIParameterMappingSourceType,
)


class BuildSystemSharedInterfacesIParameterMapping(UniversalBaseModel):
    """
    IParameterMapping
    """

    name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="name")
    ] = None
    """
    name
    """

    source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Source"), pydantic.Field(alias="Source", description="Source")
    ] = None
    """
    Source
    """

    source_type: typing_extensions.Annotated[
        typing.Optional[BuildSystemSharedInterfacesIParameterMappingSourceType],
        FieldMetadata(alias="SourceType"),
        pydantic.Field(alias="SourceType", description="SourceType"),
    ] = None
    """
    SourceType
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
