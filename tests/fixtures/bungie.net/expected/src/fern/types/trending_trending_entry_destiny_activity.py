

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_activities_destiny_public_activity_status import DestinyActivitiesDestinyPublicActivityStatus


class TrendingTrendingEntryDestinyActivity(UniversalBaseModel):
    activity_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activityHash"), pydantic.Field(alias="activityHash")
    ] = None
    status: typing.Optional[DestinyActivitiesDestinyPublicActivityStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
