

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_session_snapshot import ImportSessionSnapshot
from .import_session_turn import ImportSessionTurn


class ImportSessionRequest(UniversalBaseModel):
    session: ImportSessionSnapshot
    turns: typing.List[ImportSessionTurn]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
