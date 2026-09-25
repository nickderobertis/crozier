

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vehicle_detail_response_data import VehicleDetailResponseData
from .vehicle_detail_response_type import VehicleDetailResponseType


class VehicleDetailResponse(UniversalBaseModel):
    """
    Typed AAP response for the `inventory.vehicle` skill. The `data` field is a Vehicle (v1.0 unified the former Vehicle + VehicleDetail into one type). Because it is always an inventory listing, `condition` is constrained to `new` | `used` | `cpo` and `status` (one of `available` | `intransit` | `pending`) is required. Carried inside an A2A `Message.parts[].data` DataPart returned from the `SendMessage` operation.
    """

    type: VehicleDetailResponseType
    data: VehicleDetailResponseData
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional contextual note. MAY be omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
