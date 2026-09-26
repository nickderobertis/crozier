

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesVaccineIdWastedVaccinesRequest(
    UniversalBaseModel
):
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="LotNumber"), pydantic.Field(alias="LotNumber")]
    manufacturer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="ManufacturerName"), pydantic.Field(alias="ManufacturerName")
    ]
    manufacturer_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="ManufacturerNumber"), pydantic.Field(alias="ManufacturerNumber")
    ]
    strength: typing_extensions.Annotated[str, FieldMetadata(alias="Strength"), pydantic.Field(alias="Strength")]
    units: typing_extensions.Annotated[str, FieldMetadata(alias="Units"), pydantic.Field(alias="Units")]
    units_code: typing_extensions.Annotated[str, FieldMetadata(alias="UnitsCode"), pydantic.Field(alias="UnitsCode")]
    dose: typing_extensions.Annotated[str, FieldMetadata(alias="Dose"), pydantic.Field(alias="Dose")]
    route: typing_extensions.Annotated[str, FieldMetadata(alias="Route"), pydantic.Field(alias="Route")]
    route_code: typing_extensions.Annotated[str, FieldMetadata(alias="RouteCode"), pydantic.Field(alias="RouteCode")]
    site: typing_extensions.Annotated[str, FieldMetadata(alias="Site"), pydantic.Field(alias="Site")]
    site_code: typing_extensions.Annotated[str, FieldMetadata(alias="SiteCode"), pydantic.Field(alias="SiteCode")]
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="BrandName"), pydantic.Field(alias="BrandName")]
    wasted_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="WastedReason"), pydantic.Field(alias="WastedReason")
    ]
    wasted_date: typing_extensions.Annotated[str, FieldMetadata(alias="WastedDate"), pydantic.Field(alias="WastedDate")]
    vaccine_inventory_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="VaccineInventoryId"), pydantic.Field(alias="VaccineInventoryId")
    ]
    billing_units: typing_extensions.Annotated[
        str, FieldMetadata(alias="BillingUnits"), pydantic.Field(alias="BillingUnits")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
