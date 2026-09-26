

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdImmunizationsOrdersOrderIdVaccinesRequest(UniversalBaseModel):
    administer_year: typing_extensions.Annotated[
        str, FieldMetadata(alias="AdministerYear"), pydantic.Field(alias="AdministerYear")
    ]
    administer_month: typing_extensions.Annotated[
        str, FieldMetadata(alias="AdministerMonth"), pydantic.Field(alias="AdministerMonth")
    ]
    administer_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="AdministerDay"), pydantic.Field(alias="AdministerDay")
    ]
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="CvxCode"), pydantic.Field(alias="CvxCode")]
    vaccine_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="VaccineDescription"), pydantic.Field(alias="VaccineDescription")
    ]
    record_source: typing_extensions.Annotated[
        str, FieldMetadata(alias="RecordSource"), pydantic.Field(alias="RecordSource")
    ]
    cpt4code: typing_extensions.Annotated[str, FieldMetadata(alias="Cpt4Code"), pydantic.Field(alias="Cpt4Code")]
    sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="SequenceNumber"), pydantic.Field(alias="SequenceNumber")
    ]
    status: typing_extensions.Annotated[str, FieldMetadata(alias="Status"), pydantic.Field(alias="Status")]
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="BrandName"), pydantic.Field(alias="BrandName")]
    site_code: typing_extensions.Annotated[str, FieldMetadata(alias="SiteCode"), pydantic.Field(alias="SiteCode")]
    site: typing_extensions.Annotated[str, FieldMetadata(alias="Site"), pydantic.Field(alias="Site")]
    route_code: typing_extensions.Annotated[str, FieldMetadata(alias="RouteCode"), pydantic.Field(alias="RouteCode")]
    route: typing_extensions.Annotated[str, FieldMetadata(alias="Route"), pydantic.Field(alias="Route")]
    units_code: typing_extensions.Annotated[str, FieldMetadata(alias="UnitsCode"), pydantic.Field(alias="UnitsCode")]
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="LotNumber"), pydantic.Field(alias="LotNumber")]
    expiration_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="ExpirationDate"), pydantic.Field(alias="ExpirationDate")
    ]
    units: typing_extensions.Annotated[str, FieldMetadata(alias="Units"), pydantic.Field(alias="Units")]
    dose: typing_extensions.Annotated[str, FieldMetadata(alias="Dose"), pydantic.Field(alias="Dose")]
    manufacturer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="ManufacturerName"), pydantic.Field(alias="ManufacturerName")
    ]
    not_administered_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="NotAdministeredReason"), pydantic.Field(alias="NotAdministeredReason")
    ]
    not_administered_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="NotAdministeredCode"), pydantic.Field(alias="NotAdministeredCode")
    ]
    comment: typing_extensions.Annotated[str, FieldMetadata(alias="Comment"), pydantic.Field(alias="Comment")]
    manufacturer_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="ManufacturerNumber"), pydantic.Field(alias="ManufacturerNumber")
    ]
    strength: typing_extensions.Annotated[str, FieldMetadata(alias="Strength"), pydantic.Field(alias="Strength")]
    administer_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="AdministerBy"), pydantic.Field(alias="AdministerBy")
    ]
    audit_id: typing_extensions.Annotated[str, FieldMetadata(alias="AuditId"), pydantic.Field(alias="AuditId")]
    is_exception: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsException"), pydantic.Field(alias="IsException")
    ]
    is_counselled: typing_extensions.Annotated[
        str, FieldMetadata(alias="IsCounselled"), pydantic.Field(alias="IsCounselled")
    ]
    consent_from: typing_extensions.Annotated[
        str, FieldMetadata(alias="ConsentFrom"), pydantic.Field(alias="ConsentFrom")
    ]
    ndc_id: typing_extensions.Annotated[str, FieldMetadata(alias="NdcId"), pydantic.Field(alias="NdcId")]
    is_error: typing_extensions.Annotated[str, FieldMetadata(alias="IsError"), pydantic.Field(alias="IsError")]
    snomed_immunity_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="SnomedImmunityCode"), pydantic.Field(alias="SnomedImmunityCode")
    ]
    administer_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="AdministerTime"), pydantic.Field(alias="AdministerTime")
    ]
    vfc_code: typing_extensions.Annotated[str, FieldMetadata(alias="VfcCode"), pydantic.Field(alias="VfcCode")]
    funding_source_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="FundingSourceCode"), pydantic.Field(alias="FundingSourceCode")
    ]
    is_vfc: typing_extensions.Annotated[str, FieldMetadata(alias="IsVfc"), pydantic.Field(alias="IsVfc")]
    override_invalid_dose: typing_extensions.Annotated[
        str, FieldMetadata(alias="OverrideInvalidDose"), pydantic.Field(alias="OverrideInvalidDose")
    ]
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
