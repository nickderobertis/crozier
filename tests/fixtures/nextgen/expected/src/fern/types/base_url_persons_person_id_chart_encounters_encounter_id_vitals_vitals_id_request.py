

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdVitalsVitalsIdRequest(UniversalBaseModel):
    height_in_feet: typing_extensions.Annotated[
        float, FieldMetadata(alias="heightInFeet"), pydantic.Field(alias="heightInFeet")
    ]
    height_in_inches: typing_extensions.Annotated[
        float, FieldMetadata(alias="heightInInches"), pydantic.Field(alias="heightInInches")
    ]
    height_in_total_inches: typing_extensions.Annotated[
        float, FieldMetadata(alias="heightInTotalInches"), pydantic.Field(alias="heightInTotalInches")
    ]
    height_in_centimeters: typing_extensions.Annotated[
        float, FieldMetadata(alias="heightInCentimeters"), pydantic.Field(alias="heightInCentimeters")
    ]
    height_body_position: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightBodyPosition"), pydantic.Field(alias="heightBodyPosition")
    ]
    height_date: typing_extensions.Annotated[str, FieldMetadata(alias="heightDate"), pydantic.Field(alias="heightDate")]
    height_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightMethod"), pydantic.Field(alias="heightMethod")
    ]
    weight_in_pounds: typing_extensions.Annotated[
        float, FieldMetadata(alias="weightInPounds"), pydantic.Field(alias="weightInPounds")
    ]
    weight_in_kilograms: typing_extensions.Annotated[
        float, FieldMetadata(alias="weightInKilograms"), pydantic.Field(alias="weightInKilograms")
    ]
    weight_context: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightContext"), pydantic.Field(alias="weightContext")
    ]
    temperature_degrees_fahrenheit: typing_extensions.Annotated[
        float, FieldMetadata(alias="temperatureDegreesFahrenheit"), pydantic.Field(alias="temperatureDegreesFahrenheit")
    ]
    temperature_degrees_celcius: typing_extensions.Annotated[
        float, FieldMetadata(alias="temperatureDegreesCelcius"), pydantic.Field(alias="temperatureDegreesCelcius")
    ]
    temperature_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="temperatureSite"), pydantic.Field(alias="temperatureSite")
    ]
    blood_pressure_systolic: typing_extensions.Annotated[
        int, FieldMetadata(alias="bloodPressureSystolic"), pydantic.Field(alias="bloodPressureSystolic")
    ]
    blood_pressure_diastolic: typing_extensions.Annotated[
        int, FieldMetadata(alias="bloodPressureDiastolic"), pydantic.Field(alias="bloodPressureDiastolic")
    ]
    blood_pressure_body_position: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureBodyPosition"), pydantic.Field(alias="bloodPressureBodyPosition")
    ]
    blood_pressure_target_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureTargetSite"), pydantic.Field(alias="bloodPressureTargetSite")
    ]
    blood_pressure_target_side: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureTargetSide"), pydantic.Field(alias="bloodPressureTargetSide")
    ]
    blood_pressure_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureMethod"), pydantic.Field(alias="bloodPressureMethod")
    ]
    blood_pressure_cuff_size: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureCuffSize"), pydantic.Field(alias="bloodPressureCuffSize")
    ]
    pulse_rate: typing_extensions.Annotated[int, FieldMetadata(alias="pulseRate"), pydantic.Field(alias="pulseRate")]
    pulse_pattern: typing_extensions.Annotated[
        str, FieldMetadata(alias="pulsePattern"), pydantic.Field(alias="pulsePattern")
    ]
    respiration_rate: typing_extensions.Annotated[
        int, FieldMetadata(alias="respirationRate"), pydantic.Field(alias="respirationRate")
    ]
    fraction_of_inspired_oxygen_delivery_method: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fractionOfInspiredOxygenDeliveryMethod"),
        pydantic.Field(alias="fractionOfInspiredOxygenDeliveryMethod"),
    ]
    fraction_of_inspired_oxygen_room_air: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="fractionOfInspiredOxygenRoomAir"),
        pydantic.Field(alias="fractionOfInspiredOxygenRoomAir"),
    ]
    fraction_of_inspired_oxygen: typing_extensions.Annotated[
        int, FieldMetadata(alias="fractionOfInspiredOxygen"), pydantic.Field(alias="fractionOfInspiredOxygen")
    ]
    fraction_of_inspired_oxygen_score: typing_extensions.Annotated[
        str, FieldMetadata(alias="fractionOfInspiredOxygenScore"), pydantic.Field(alias="fractionOfInspiredOxygenScore")
    ]
    pulse_ox_rest: typing_extensions.Annotated[
        int, FieldMetadata(alias="pulseOxRest"), pydantic.Field(alias="pulseOxRest")
    ]
    pulse_ox_amb: typing_extensions.Annotated[
        int, FieldMetadata(alias="pulseOxAmb"), pydantic.Field(alias="pulseOxAmb")
    ]
    oxygen_type: typing_extensions.Annotated[str, FieldMetadata(alias="oxygenType"), pydantic.Field(alias="oxygenType")]
    oxygen_liter_per_minute: typing_extensions.Annotated[
        float, FieldMetadata(alias="oxygenLiterPerMinute"), pydantic.Field(alias="oxygenLiterPerMinute")
    ]
    sp_o2timing: typing_extensions.Annotated[str, FieldMetadata(alias="spO2Timing"), pydantic.Field(alias="spO2Timing")]
    finger_probe: typing_extensions.Annotated[
        str, FieldMetadata(alias="fingerProbe"), pydantic.Field(alias="fingerProbe")
    ]
    peak_flow: typing_extensions.Annotated[int, FieldMetadata(alias="peakFlow"), pydantic.Field(alias="peakFlow")]
    peak_flow_timing: typing_extensions.Annotated[
        str, FieldMetadata(alias="peakFlowTiming"), pydantic.Field(alias="peakFlowTiming")
    ]
    peak_flow_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="peakFlowMethod"), pydantic.Field(alias="peakFlowMethod")
    ]
    pain_level: typing_extensions.Annotated[str, FieldMetadata(alias="painLevel"), pydantic.Field(alias="painLevel")]
    pain_method: typing_extensions.Annotated[str, FieldMetadata(alias="painMethod"), pydantic.Field(alias="painMethod")]
    is_unobtainable: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isUnobtainable"), pydantic.Field(alias="isUnobtainable")
    ]
    unobtainable_vital: typing_extensions.Annotated[
        str, FieldMetadata(alias="unobtainableVital"), pydantic.Field(alias="unobtainableVital")
    ]
    has_patient_refused: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasPatientRefused"), pydantic.Field(alias="hasPatientRefused")
    ]
    patient_refused_vital: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientRefusedVital"), pydantic.Field(alias="patientRefusedVital")
    ]
    calculate_bsa: typing_extensions.Annotated[
        bool, FieldMetadata(alias="calculateBsa"), pydantic.Field(alias="calculateBsa")
    ]
    vital_signs_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="vitalSignsDate"), pydantic.Field(alias="vitalSignsDate")
    ]
    comments: str
    performed_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="performedBy"), pydantic.Field(alias="performedBy")
    ]
    provenance_info: typing_extensions.Annotated[
        str, FieldMetadata(alias="provenanceInfo"), pydantic.Field(alias="provenanceInfo")
    ]
    is_external_data: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isExternalData"), pydantic.Field(alias="isExternalData")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
