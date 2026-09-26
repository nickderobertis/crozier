

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .consumption import Consumption
from .energy_sub_type import EnergySubType
from .energy_type import EnergyType


class EnergyConsumption(Consumption):
    avg_consumption: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="avgConsumption"),
        pydantic.Field(
            alias="avgConsumption",
            description="Vehicle Average consumption per 100kms for specific enery type. For eletric  in terms of Wh/100km or for fuel in terms of cl/100km respectively",
        ),
    ] = None
    """
    Vehicle Average consumption per 100kms for specific enery type. For eletric  in terms of Wh/100km or for fuel in terms of cl/100km respectively
    """

    type: typing.Optional[EnergyType] = None
    sub_type: typing_extensions.Annotated[
        typing.Optional[EnergySubType], FieldMetadata(alias="subType"), pydantic.Field(alias="subType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
