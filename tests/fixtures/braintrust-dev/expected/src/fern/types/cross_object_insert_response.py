

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insert_events_response import InsertEventsResponse


class CrossObjectInsertResponse(UniversalBaseModel):
    experiment: typing.Optional[typing.Dict[str, typing.Optional[InsertEventsResponse]]] = pydantic.Field(default=None)
    """
    A mapping from experiment id to row ids for inserted `events`
    """

    dataset: typing.Optional[typing.Dict[str, typing.Optional[InsertEventsResponse]]] = pydantic.Field(default=None)
    """
    A mapping from dataset id to row ids for inserted `events`
    """

    project_logs: typing.Optional[typing.Dict[str, typing.Optional[InsertEventsResponse]]] = pydantic.Field(
        default=None
    )
    """
    A mapping from project id to row ids for inserted `events`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
