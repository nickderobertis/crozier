

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_sessions_checkpoint_response_data import ImportSessionsCheckpointResponseData


class ImportSessionsCheckpointResponse(UniversalBaseModel):
    data: ImportSessionsCheckpointResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
