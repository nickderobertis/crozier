

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImportSessionThread(UniversalBaseModel):
    agent_info: typing.Optional[typing.Any] = None
    capability_state: typing.Optional[typing.Dict[str, typing.Any]] = None
    completion: typing.Optional[typing.Any] = None
    context: typing.List[typing.Any]
    current_context_usage: typing.Optional[typing.Any] = None
    parent: typing.Optional[typing.Any] = None
    thread_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
