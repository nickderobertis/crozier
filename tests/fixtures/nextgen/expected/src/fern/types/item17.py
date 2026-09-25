

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item17(UniversalBaseModel):
    blood_pressure_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureHealthConcern"), pydantic.Field(alias="bloodPressureHealthConcern")
    ]
    blood_pressure_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureCategory"), pydantic.Field(alias="bloodPressureCategory")
    ]
    blood_pressure_systolic_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureSystolicValue"), pydantic.Field(alias="bloodPressureSystolicValue")
    ]
    blood_pressure_diastolic_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureDiastolicValue"), pydantic.Field(alias="bloodPressureDiastolicValue")
    ]
    blood_pressure_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureUnit"), pydantic.Field(alias="bloodPressureUnit")
    ]
    body_temperature_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="bodyTemperatureHealthConcern"), pydantic.Field(alias="bodyTemperatureHealthConcern")
    ]
    body_temperature_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="bodyTemperatureCategory"), pydantic.Field(alias="bodyTemperatureCategory")
    ]
    body_temperature_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="bodyTemperatureValue"), pydantic.Field(alias="bodyTemperatureValue")
    ]
    body_temperature_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="bodyTemperatureUnit"), pydantic.Field(alias="bodyTemperatureUnit")
    ]
    head_circumference_health_concern: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="headCircumferenceHealthConcern"),
        pydantic.Field(alias="headCircumferenceHealthConcern"),
    ]
    head_circumference_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferenceCategory"), pydantic.Field(alias="headCircumferenceCategory")
    ]
    head_circumference_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferenceValue"), pydantic.Field(alias="headCircumferenceValue")
    ]
    head_circumference_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferenceUnit"), pydantic.Field(alias="headCircumferenceUnit")
    ]
    heart_rate_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="heartRateHealthConcern"), pydantic.Field(alias="heartRateHealthConcern")
    ]
    heart_rate_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="heartRateCategory"), pydantic.Field(alias="heartRateCategory")
    ]
    heart_rate_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="heartRateValue"), pydantic.Field(alias="heartRateValue")
    ]
    heart_rate_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="heartRateUnit"), pydantic.Field(alias="heartRateUnit")
    ]
    height_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightHealthConcern"), pydantic.Field(alias="heightHealthConcern")
    ]
    height_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightCategory"), pydantic.Field(alias="heightCategory")
    ]
    height_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightValue"), pydantic.Field(alias="heightValue")
    ]
    height_unit: typing_extensions.Annotated[str, FieldMetadata(alias="heightUnit"), pydantic.Field(alias="heightUnit")]
    weight_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightHealthConcern"), pydantic.Field(alias="weightHealthConcern")
    ]
    weight_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightCategory"), pydantic.Field(alias="weightCategory")
    ]
    weight_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightValue"), pydantic.Field(alias="weightValue")
    ]
    weight_unit: typing_extensions.Annotated[str, FieldMetadata(alias="weightUnit"), pydantic.Field(alias="weightUnit")]
    bmi_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="bmiHealthConcern"), pydantic.Field(alias="bmiHealthConcern")
    ]
    bmi_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="bmiCategory"), pydantic.Field(alias="bmiCategory")
    ]
    bmi_value: typing_extensions.Annotated[str, FieldMetadata(alias="bmiValue"), pydantic.Field(alias="bmiValue")]
    o2bld_c_oximetry_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="o2BldCOximetryHealthConcern"), pydantic.Field(alias="o2BldCOximetryHealthConcern")
    ]
    o2bld_c_oximetry_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="o2BldCOximetryCategory"), pydantic.Field(alias="o2BldCOximetryCategory")
    ]
    o2bld_c_oximetry_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="o2BldCOximetryValue"), pydantic.Field(alias="o2BldCOximetryValue")
    ]
    o2bld_c_oximetry_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="o2BldCOximetryUnit"), pydantic.Field(alias="o2BldCOximetryUnit")
    ]
    respiratory_rate_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="respiratoryRateHealthConcern"), pydantic.Field(alias="respiratoryRateHealthConcern")
    ]
    respiratory_rate_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="respiratoryRateCategory"), pydantic.Field(alias="respiratoryRateCategory")
    ]
    respiratory_rate_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="respiratoryRateValue"), pydantic.Field(alias="respiratoryRateValue")
    ]
    respiratory_rate_unit: typing_extensions.Annotated[
        str, FieldMetadata(alias="respiratoryRateUnit"), pydantic.Field(alias="respiratoryRateUnit")
    ]
    id: str
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
