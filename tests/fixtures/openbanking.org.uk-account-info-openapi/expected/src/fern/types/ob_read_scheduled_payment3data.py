

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_scheduled_payment3 import ObScheduledPayment3


class ObReadScheduledPayment3Data(UniversalBaseModel):
    scheduled_payment: typing_extensions.Annotated[
        typing.Optional[typing.List[ObScheduledPayment3]],
        FieldMetadata(alias="ScheduledPayment"),
        pydantic.Field(alias="ScheduledPayment"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
