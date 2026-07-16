

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact_assignment_priority_label import ContactAssignmentPriorityLabel
from .contact_assignment_priority_value import ContactAssignmentPriorityValue


class ContactAssignmentPriority(UniversalBaseModel):
    label: ContactAssignmentPriorityLabel
    value: ContactAssignmentPriorityValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
