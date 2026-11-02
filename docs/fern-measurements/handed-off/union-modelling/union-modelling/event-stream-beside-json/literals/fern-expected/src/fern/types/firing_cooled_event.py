

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .firing_cooled_event_type import FiringCooledEventType


class FiringCooledEvent(UniversalBaseModel):
    type: FiringCooledEventType = pydantic.Field()
    """
    Always `firing.cooled`.
    """

    cooled_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="cooledAt"), pydantic.Field(alias="cooledAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
