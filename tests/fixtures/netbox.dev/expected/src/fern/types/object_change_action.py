

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .object_change_action_label import ObjectChangeActionLabel
from .object_change_action_value import ObjectChangeActionValue


class ObjectChangeAction(UniversalBaseModel):
    label: ObjectChangeActionLabel
    value: ObjectChangeActionValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
