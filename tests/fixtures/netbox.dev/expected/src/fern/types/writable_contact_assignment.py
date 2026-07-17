

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .writable_contact_assignment_priority import WritableContactAssignmentPriority


class WritableContactAssignment(UniversalBaseModel):
    contact: int
    content_type: str
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    object: typing.Optional[typing.Dict[str, typing.Any]] = None
    object_id: int
    priority: typing.Optional[WritableContactAssignmentPriority] = None
    role: int
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
