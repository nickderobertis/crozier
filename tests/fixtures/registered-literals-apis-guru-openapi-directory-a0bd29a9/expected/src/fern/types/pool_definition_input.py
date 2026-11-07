

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .azure_location import AzureLocation
from .resource_subtype import ResourceSubtype
from .resource_type import ResourceType


class PoolDefinitionInput(UniversalBaseModel):
    dimensions: typing.Dict[str, typing.Optional[str]]
    is_enabled: typing_extensions.Annotated[bool, FieldMetadata(alias="isEnabled"), pydantic.Field(alias="isEnabled")]
    location: AzureLocation
    logical_skus: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="logicalSkus"), pydantic.Field(alias="logicalSkus")
    ] = None
    subtype: ResourceSubtype
    target_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="targetCount"), pydantic.Field(alias="targetCount")
    ]
    type: ResourceType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
