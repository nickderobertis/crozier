

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .common_connected_apps import CommonConnectedApps
from .common_recent_api_calls import CommonRecentApiCalls
from .common_recent_connections import CommonRecentConnections
from .common_summary_api_calls import CommonSummaryApiCalls


class CommonAnalytics(UniversalBaseModel):
    total_connections: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalConnections"), pydantic.Field(alias="totalConnections")
    ]
    connected_apps: typing_extensions.Annotated[
        typing.Optional[typing.List[CommonConnectedApps]],
        FieldMetadata(alias="connectedApps"),
        pydantic.Field(alias="connectedApps"),
    ] = None
    recent_connections: typing_extensions.Annotated[
        typing.Optional[typing.List[CommonRecentConnections]],
        FieldMetadata(alias="recentConnections"),
        pydantic.Field(alias="recentConnections"),
    ] = None
    recent_api_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[CommonRecentApiCalls]],
        FieldMetadata(alias="recentApiCalls"),
        pydantic.Field(alias="recentApiCalls"),
    ] = None
    total_api_calls: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalApiCalls"), pydantic.Field(alias="totalApiCalls")
    ] = None
    summary_api_calls: typing_extensions.Annotated[
        typing.Optional[typing.List[CommonSummaryApiCalls]],
        FieldMetadata(alias="summaryApiCalls"),
        pydantic.Field(alias="summaryApiCalls"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
