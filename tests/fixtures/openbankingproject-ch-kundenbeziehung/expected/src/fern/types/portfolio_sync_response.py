

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .portfolio_sync_response_status import PortfolioSyncResponseStatus


class PortfolioSyncResponse(UniversalBaseModel):
    sync_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="syncId"), pydantic.Field(alias="syncId")
    ] = None
    status: typing.Optional[PortfolioSyncResponseStatus] = None
    synced_assets: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="syncedAssets"),
        pydantic.Field(alias="syncedAssets"),
    ] = None
    data_quality: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dataQuality"), pydantic.Field(alias="dataQuality")
    ] = None
    estimated_completion: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="estimatedCompletion"),
        pydantic.Field(alias="estimatedCompletion"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
