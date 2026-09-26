

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .trip_faults_item_cause import TripFaultsItemCause
from .trip_faults_item_fault import TripFaultsItemFault


class TripFaultsItem(UniversalBaseModel):
    fault: typing.Optional[TripFaultsItemFault] = None
    cause: typing.Optional[TripFaultsItemCause] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
