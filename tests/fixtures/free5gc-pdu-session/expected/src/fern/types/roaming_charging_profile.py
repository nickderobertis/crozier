

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .partial_record_method import PartialRecordMethod
from .trigger import Trigger


class RoamingChargingProfile(UniversalBaseModel):
    triggers: typing.Optional[typing.List[Trigger]] = None
    partial_record_method: typing_extensions.Annotated[
        typing.Optional[PartialRecordMethod],
        FieldMetadata(alias="partialRecordMethod"),
        pydantic.Field(alias="partialRecordMethod"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
