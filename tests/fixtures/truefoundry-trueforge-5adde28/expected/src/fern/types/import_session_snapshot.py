

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_by_subject import CreatedBySubject


class ImportSessionSnapshot(UniversalBaseModel):
    agent_id: typing.Optional[str] = None
    agent_name: typing.Optional[str] = None
    agent_spec: typing.Optional[typing.Dict[str, typing.Any]] = None
    created_at: str
    created_by_subject: CreatedBySubject
    custom: typing.Optional[typing.Dict[str, typing.Any]] = None
    last_activity_timestamp_ms: float
    last_turn_id: typing.Optional[str] = None
    session_id: str
    tenant_id: str
    title: typing.Optional[str] = None
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
