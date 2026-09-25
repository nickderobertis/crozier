

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item18(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    order_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderStatus"), pydantic.Field(alias="orderStatus")
    ]
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="cvxCode"), pydantic.Field(alias="cvxCode")]
    description: str
    record_source_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="recordSourceCode"), pydantic.Field(alias="recordSourceCode")
    ]
    record_source_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="recordSourceName"), pydantic.Field(alias="recordSourceName")
    ]
    administer_cpt_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="administerCptCode"), pydantic.Field(alias="administerCptCode")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    cpt_code: typing_extensions.Annotated[str, FieldMetadata(alias="cptCode"), pydantic.Field(alias="cptCode")]
    sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="sequenceNumber"), pydantic.Field(alias="sequenceNumber")
    ]
    status: str
    comment: str
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="brandName"), pydantic.Field(alias="brandName")]
    site_code: typing_extensions.Annotated[str, FieldMetadata(alias="siteCode"), pydantic.Field(alias="siteCode")]
    site: str
    side_code: typing_extensions.Annotated[str, FieldMetadata(alias="sideCode"), pydantic.Field(alias="sideCode")]
    side: str
    route_code: typing_extensions.Annotated[str, FieldMetadata(alias="routeCode"), pydantic.Field(alias="routeCode")]
    route: str
    units_code: typing_extensions.Annotated[str, FieldMetadata(alias="unitsCode"), pydantic.Field(alias="unitsCode")]
    units: str
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="lotNumber"), pydantic.Field(alias="lotNumber")]
    expiration_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="expirationDate"), pydantic.Field(alias="expirationDate")
    ]
    dose: str
    mvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="mvxCode"), pydantic.Field(alias="mvxCode")]
    manufacturer_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="manufacturerNumber"), pydantic.Field(alias="manufacturerNumber")
    ]
    manufacturer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="manufacturerName"), pydantic.Field(alias="manufacturerName")
    ]
    not_administered_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="notAdministeredReason"), pydantic.Field(alias="notAdministeredReason")
    ]
    not_administered_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="notAdministeredCode"), pydantic.Field(alias="notAdministeredCode")
    ]
    purchase_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="purchaseType"), pydantic.Field(alias="purchaseType")
    ]
    strength: str
    administered_year: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredYear"), pydantic.Field(alias="administeredYear")
    ]
    administered_month: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredMonth"), pydantic.Field(alias="administeredMonth")
    ]
    administered_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredDay"), pydantic.Field(alias="administeredDay")
    ]
    administered_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredDate"), pydantic.Field(alias="administeredDate")
    ]
    administered_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredTimestamp"), pydantic.Field(alias="administeredTimestamp")
    ]
    administered_by_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredByUserId"), pydantic.Field(alias="administeredByUserId")
    ]
    administered_by_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="administeredByName"), pydantic.Field(alias="administeredByName")
    ]
    audit_id: typing_extensions.Annotated[str, FieldMetadata(alias="auditId"), pydantic.Field(alias="auditId")]
    charge_id: typing_extensions.Annotated[str, FieldMetadata(alias="chargeId"), pydantic.Field(alias="chargeId")]
    admin_charge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="adminChargeId"), pydantic.Field(alias="adminChargeId")
    ]
    is_exception: typing_extensions.Annotated[
        str, FieldMetadata(alias="isException"), pydantic.Field(alias="isException")
    ]
    is_counselled: typing_extensions.Annotated[
        str, FieldMetadata(alias="isCounselled"), pydantic.Field(alias="isCounselled")
    ]
    counselled_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="counselledCode"), pydantic.Field(alias="counselledCode")
    ]
    counselled_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="counselledUnit"), pydantic.Field(alias="counselledUnit")
    ]
    counsel_charge_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="counselChargeId"), pydantic.Field(alias="counselChargeId")
    ]
    consent_from: typing_extensions.Annotated[
        str, FieldMetadata(alias="consentFrom"), pydantic.Field(alias="consentFrom")
    ]
    consent_given_to: typing_extensions.Annotated[
        str, FieldMetadata(alias="consentGivenTo"), pydantic.Field(alias="consentGivenTo")
    ]
    ndc_id: typing_extensions.Annotated[str, FieldMetadata(alias="ndcId"), pydantic.Field(alias="ndcId")]
    is_error: typing_extensions.Annotated[str, FieldMetadata(alias="isError"), pydantic.Field(alias="isError")]
    snomed_immunity: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedImmunity"), pydantic.Field(alias="snomedImmunity")
    ]
    is_vfc: typing_extensions.Annotated[str, FieldMetadata(alias="isVfc"), pydantic.Field(alias="isVfc")]
    vfc_code: typing_extensions.Annotated[str, FieldMetadata(alias="vfcCode"), pydantic.Field(alias="vfcCode")]
    vfc_date: typing_extensions.Annotated[str, FieldMetadata(alias="vfcDate"), pydantic.Field(alias="vfcDate")]
    vfc_date_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="vfcDateTimezone"), pydantic.Field(alias="vfcDateTimezone")
    ]
    funding_source_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="fundingSourceCode"), pydantic.Field(alias="fundingSourceCode")
    ]
    sim_code: typing_extensions.Annotated[str, FieldMetadata(alias="simCode"), pydantic.Field(alias="simCode")]
    sign_off_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffUserId"), pydantic.Field(alias="signOffUserId")
    ]
    sign_off_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffName"), pydantic.Field(alias="signOffName")
    ]
    sign_off_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDate"), pydantic.Field(alias="signOffDate")
    ]
    sign_off_date_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDateTimezone"), pydantic.Field(alias="signOffDateTimezone")
    ]
    signoff_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="signoffComment"), pydantic.Field(alias="signoffComment")
    ]
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    hide_on_chart: typing_extensions.Annotated[
        str, FieldMetadata(alias="hideOnChart"), pydantic.Field(alias="hideOnChart")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modified_by_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifiedByUserId"), pydantic.Field(alias="modifiedByUserId")
    ]
    modified_by_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifiedByName"), pydantic.Field(alias="modifiedByName")
    ]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    override_invalid_dose: typing_extensions.Annotated[
        str, FieldMetadata(alias="overrideInvalidDose"), pydantic.Field(alias="overrideInvalidDose")
    ]
    billing_units: typing_extensions.Annotated[
        str, FieldMetadata(alias="billingUnits"), pydantic.Field(alias="billingUnits")
    ]
    vaccine_inventory_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineInventoryId"), pydantic.Field(alias="vaccineInventoryId")
    ]
    is_reported: typing_extensions.Annotated[str, FieldMetadata(alias="isReported"), pydantic.Field(alias="isReported")]
    was_not_given: typing_extensions.Annotated[
        str, FieldMetadata(alias="wasNotGiven"), pydantic.Field(alias="wasNotGiven")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
