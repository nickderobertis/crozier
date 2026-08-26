

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .fuel_type import FuelType
from .reason_condition import ReasonCondition
from .reason_unit_symbol import ReasonUnitSymbol
from .restriction import Restriction
from .vehicle_type import VehicleType


class Base(UniversalBaseModel):
    unit_symbol: typing_extensions.Annotated[
        ReasonUnitSymbol, FieldMetadata(alias="unitSymbol"), pydantic.Field(alias="unitSymbol")
    ]
    condition: ReasonCondition
    because_of: typing_extensions.Annotated[
        typing.Optional[typing.List[Restriction]],
        FieldMetadata(alias="becauseOf"),
        pydantic.Field(alias="becauseOf", description="What triggerd this reason why the destination is inaccessible."),
    ] = None
    """
    What triggerd this reason why the destination is inaccessible.
    """

    request_exemption_urls: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="requestExemptionUrls"),
        pydantic.Field(
            alias="requestExemptionUrls",
            description="URLs where an exemption can be requested for the road operators responsible for this reason. Multiple reasons may share a url. No de-duplication done.",
        ),
    ] = None
    """
    URLs where an exemption can be requested for the road operators responsible for this reason. Multiple reasons may share a url. No de-duplication done.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleLengthReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleLengthReason"] = "vehicleLengthReason"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleHeightReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleHeightReason"] = "vehicleHeightReason"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleWidthReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleWidthReason"] = "vehicleWidthReason"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleAxleWeightReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleAxleWeightReason"] = "vehicleAxleWeightReason"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleWeightReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleWeightReason"] = "vehicleWeightReason"
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_FuelTypeReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["fuelTypeReason"] = "fuelTypeReason"
    values: typing.List[FuelType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_VehicleTypeReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["vehicleTypeReason"] = "vehicleTypeReason"
    values: typing.List[VehicleType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_AccessibleReason(Base):
    """
    Reason why the destination is inaccessible.
    """

    type: typing.Literal["accessibleReason"] = "accessibleReason"
    value: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Reason_Unknown(Base):
    value: "Reason"
    type: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True


Reason = typing_extensions.Annotated[
    typing.Union[
        Reason_VehicleLengthReason,
        Reason_VehicleHeightReason,
        Reason_VehicleWidthReason,
        Reason_VehicleAxleWeightReason,
        Reason_VehicleWeightReason,
        Reason_FuelTypeReason,
        Reason_VehicleTypeReason,
        Reason_AccessibleReason,
        Reason_Unknown,
    ],
    pydantic.Field(discriminator="type"),
]
update_forward_refs(Reason_Unknown, Reason=Reason)
