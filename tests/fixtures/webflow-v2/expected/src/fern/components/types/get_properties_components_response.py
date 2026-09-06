

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_properties_components_response_pagination import GetPropertiesComponentsResponsePagination
from .get_properties_components_response_properties_item import GetPropertiesComponentsResponsePropertiesItem


class GetPropertiesComponentsResponse(UniversalBaseModel):
    """
    The Component Properties schema represents a list of properties that store text content. Each property has a unique identifier and can be of different types like plain text or rich text. The schema also provides pagination details for scenarios where there more properties than the limit.
    """

    component_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="componentId"),
        pydantic.Field(alias="componentId", description="Component ID"),
    ] = None
    """
    Component ID
    """

    properties: typing.Optional[typing.List[GetPropertiesComponentsResponsePropertiesItem]] = None
    pagination: typing.Optional[GetPropertiesComponentsResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
