

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .component_link import ComponentLink
from .component_type import ComponentType


class ComponentListElement(UniversalBaseModel):
    id: str
    name: str
    icon: str
    component_type: typing_extensions.Annotated[
        ComponentType, FieldMetadata(alias="componentType"), pydantic.Field(alias="componentType")
    ]
    component_group_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="componentGroupName"), pydantic.Field(alias="componentGroupName")
    ]
    categories: typing.Optional[typing.List[str]] = None
    links: typing.Optional[typing.List[ComponentLink]] = None
    usage_count: typing_extensions.Annotated[int, FieldMetadata(alias="usageCount"), pydantic.Field(alias="usageCount")]
    allowed_processing_modes: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="allowedProcessingModes"), pydantic.Field(alias="allowedProcessingModes")
    ]
    label: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
