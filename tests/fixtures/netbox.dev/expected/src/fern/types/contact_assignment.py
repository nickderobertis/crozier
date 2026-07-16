

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact_assignment_priority import ContactAssignmentPriority
from .nested_contact import NestedContact
from .nested_contact_role import NestedContactRole


class ContactAssignment(UniversalBaseModel):
    contact: NestedContact
    content_type: str
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    object_id: int
    priority: typing.Optional[ContactAssignmentPriority] = None
    role: typing.Optional[NestedContactRole] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
