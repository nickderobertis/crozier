

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .import_session_event import ImportSessionEvent
from .import_session_thread import ImportSessionThread


class ImportSessionTurn(UniversalBaseModel):
    ancestor_ids: typing.List[str]
    checkpoint: typing.Optional[typing.Any] = None
    created_at: str
    custom: typing.Optional[typing.Dict[str, typing.Any]] = None
    events: typing.List[ImportSessionEvent]
    first_turn_id: str
    input: typing.List[typing.Any]
    previous_turn_id: typing.Optional[str] = None
    state: typing.Optional[typing.Any] = None
    threads: typing.List[ImportSessionThread]
    turn_id: str
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
