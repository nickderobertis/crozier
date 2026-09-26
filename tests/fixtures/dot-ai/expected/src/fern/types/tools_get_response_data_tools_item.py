

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tools_get_response_data_tools_item_parameters_item import ToolsGetResponseDataToolsItemParametersItem


class ToolsGetResponseDataToolsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Tool name/identifier
    """

    description: str = pydantic.Field()
    """
    Tool description
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tool category for grouping
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags for filtering
    """

    parameters: typing.Optional[typing.List[ToolsGetResponseDataToolsItemParametersItem]] = pydantic.Field(default=None)
    """
    Tool parameters
    """

    input_schema: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="inputSchema"),
        pydantic.Field(alias="inputSchema", description="JSON Schema for tool input"),
    ] = None
    """
    JSON Schema for tool input
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
