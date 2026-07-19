

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trigger_category import TriggerCategory
from .trigger_type import TriggerType


class Trigger(UniversalBaseModel):
    trigger_type: typing_extensions.Annotated[
        TriggerType, FieldMetadata(alias="triggerType"), pydantic.Field(alias="triggerType")
    ]
    trigger_category: typing_extensions.Annotated[
        TriggerCategory, FieldMetadata(alias="triggerCategory"), pydantic.Field(alias="triggerCategory")
    ]
    time_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeLimit"), pydantic.Field(alias="timeLimit")
    ] = None
    volume_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="volumeLimit"), pydantic.Field(alias="volumeLimit")
    ] = None
    max_number_ofccc: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxNumberOfccc"), pydantic.Field(alias="maxNumberOfccc")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
