

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .player_update_metadata import PlayerUpdateMetadata


class GetApiV1PlayerUpdatesReleaseIdResponse(UniversalBaseModel):
    data: typing.Optional[PlayerUpdateMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
