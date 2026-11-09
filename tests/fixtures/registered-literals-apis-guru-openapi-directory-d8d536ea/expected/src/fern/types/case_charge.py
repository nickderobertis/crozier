

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .charge import Charge
from .charge_additional_data import ChargeAdditionalData
from .charge_degree import ChargeDegree
from .charge_severity import ChargeSeverity


class CaseCharge(UniversalBaseModel):
    charge: typing.Optional[Charge] = None
    charge_additional_data_array: typing_extensions.Annotated[
        typing.List[ChargeAdditionalData],
        FieldMetadata(alias="chargeAdditionalDataArray"),
        pydantic.Field(alias="chargeAdditionalDataArray"),
    ]
    charge_degree: typing_extensions.Annotated[
        typing.Optional[ChargeDegree], FieldMetadata(alias="chargeDegree"), pydantic.Field(alias="chargeDegree")
    ] = None
    charge_severity: typing_extensions.Annotated[
        typing.Optional[ChargeSeverity], FieldMetadata(alias="chargeSeverity"), pydantic.Field(alias="chargeSeverity")
    ] = None
    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
