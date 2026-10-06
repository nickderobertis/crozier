

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .discover_data_sources_command_type import DiscoverDataSourcesCommandType
from .request_id import RequestId


class DiscoverDataSourcesCommand(UniversalBaseModel):
    """
    Discover datasource connections from the live kernel environment and configuration.

        Attributes:
            request_id: Unique identifier for this request.
    """

    request_id: typing_extensions.Annotated[
        RequestId, FieldMetadata(alias="requestId"), pydantic.Field(alias="requestId")
    ]
    type: DiscoverDataSourcesCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
