

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok98(UniversalBaseModel):
    id: str
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    bmi: str
    blood_pressure: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressure"), pydantic.Field(alias="bloodPressure")
    ]
    blood_pressure_systolic: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureSystolic"), pydantic.Field(alias="bloodPressureSystolic")
    ]
    blood_pressure_diastolic: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureDiastolic"), pydantic.Field(alias="bloodPressureDiastolic")
    ]
    blood_pressure_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureMethod"), pydantic.Field(alias="bloodPressureMethod")
    ]
    blood_pressure_side: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureSide"), pydantic.Field(alias="bloodPressureSide")
    ]
    blood_pressure_body_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureBodySite"), pydantic.Field(alias="bloodPressureBodySite")
    ]
    blood_pressure_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureSite"), pydantic.Field(alias="bloodPressureSite")
    ]
    blood_pressure_body_position: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureBodyPosition"), pydantic.Field(alias="bloodPressureBodyPosition")
    ]
    is_blood_pressure_cuff_size_pediatric: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="isBloodPressureCuffSizePediatric"),
        pydantic.Field(alias="isBloodPressureCuffSizePediatric"),
    ]
    is_blood_pressure_cuff_size_adult: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBloodPressureCuffSizeAdult"), pydantic.Field(alias="isBloodPressureCuffSizeAdult")
    ]
    is_blood_pressure_cuff_size_large: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBloodPressureCuffSizeLarge"), pydantic.Field(alias="isBloodPressureCuffSizeLarge")
    ]
    is_blood_pressure_cuff_size_thigh: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBloodPressureCuffSizeThigh"), pydantic.Field(alias="isBloodPressureCuffSizeThigh")
    ]
    is_blood_pressure_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isBloodPressureCaptured"), pydantic.Field(alias="isBloodPressureCaptured")
    ]
    measured_by: typing_extensions.Annotated[str, FieldMetadata(alias="measuredBy"), pydantic.Field(alias="measuredBy")]
    vital_signs_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="vitalSignsDate"), pydantic.Field(alias="vitalSignsDate")
    ]
    vital_signs_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="vitalSignsTime"), pydantic.Field(alias="vitalSignsTime")
    ]
    fraction_of_inspired_oxygen: typing_extensions.Annotated[
        str, FieldMetadata(alias="fractionOfInspiredOxygen"), pydantic.Field(alias="fractionOfInspiredOxygen")
    ]
    pulse_pattern: typing_extensions.Annotated[
        str, FieldMetadata(alias="pulsePattern"), pydantic.Field(alias="pulsePattern")
    ]
    pulse_rate: typing_extensions.Annotated[str, FieldMetadata(alias="pulseRate"), pydantic.Field(alias="pulseRate")]
    pulse_oximeter_oxygen_saturation_rest: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationRest"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationRest"),
    ]
    pulse_oximeter_oxygen_saturation_rest_site: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationRestSite"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationRestSite"),
    ]
    is_growth_chart_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGrowthChartCaptured"), pydantic.Field(alias="isGrowthChartCaptured")
    ]
    is_health_assessment_questionnaire_captured: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="isHealthAssessmentQuestionnaireCaptured"),
        pydantic.Field(alias="isHealthAssessmentQuestionnaireCaptured"),
    ]
    is_exclusion_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isExclusionCaptured"), pydantic.Field(alias="isExclusionCaptured")
    ]
    bmi_percent: typing_extensions.Annotated[str, FieldMetadata(alias="bmiPercent"), pydantic.Field(alias="bmiPercent")]
    body_surface_area: typing_extensions.Annotated[
        str, FieldMetadata(alias="bodySurfaceArea"), pydantic.Field(alias="bodySurfaceArea")
    ]
    is_hip_circumference_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isHipCircumferenceCaptured"), pydantic.Field(alias="isHipCircumferenceCaptured")
    ]
    is_head_circumference_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isHeadCircumferenceCaptured"), pydantic.Field(alias="isHeadCircumferenceCaptured")
    ]
    is_height_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isHeightCaptured"), pydantic.Field(alias="isHeightCaptured")
    ]
    is_neck_circumference_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isNeckCircumferenceCaptured"), pydantic.Field(alias="isNeckCircumferenceCaptured")
    ]
    is_temperature_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isTemperatureCaptured"), pydantic.Field(alias="isTemperatureCaptured")
    ]
    is_waist_circumference_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isWaistCircumferenceCaptured"), pydantic.Field(alias="isWaistCircumferenceCaptured")
    ]
    is_weight_captured: typing_extensions.Annotated[
        str, FieldMetadata(alias="isWeightCaptured"), pydantic.Field(alias="isWeightCaptured")
    ]
    has_patient_refused: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasPatientRefused"), pydantic.Field(alias="hasPatientRefused")
    ]
    is_unobtainable: typing_extensions.Annotated[
        str, FieldMetadata(alias="isUnobtainable"), pydantic.Field(alias="isUnobtainable")
    ]
    comments: str
    head_circumference_centimeters: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferenceCentimeters"), pydantic.Field(alias="headCircumferenceCentimeters")
    ]
    head_circumference_inches: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferenceInches"), pydantic.Field(alias="headCircumferenceInches")
    ]
    head_circumference_percent: typing_extensions.Annotated[
        str, FieldMetadata(alias="headCircumferencePercent"), pydantic.Field(alias="headCircumferencePercent")
    ]
    height_centimeters: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightCentimeters"), pydantic.Field(alias="heightCentimeters")
    ]
    height_date: typing_extensions.Annotated[str, FieldMetadata(alias="heightDate"), pydantic.Field(alias="heightDate")]
    height_feet: typing_extensions.Annotated[str, FieldMetadata(alias="heightFeet"), pydantic.Field(alias="heightFeet")]
    height_inches: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightInches"), pydantic.Field(alias="heightInches")
    ]
    height_meters: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightMeters"), pydantic.Field(alias="heightMeters")
    ]
    height_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightMethod"), pydantic.Field(alias="heightMethod")
    ]
    height_percent: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightPercent"), pydantic.Field(alias="heightPercent")
    ]
    hip_circumference_centimeters: typing_extensions.Annotated[
        str, FieldMetadata(alias="hipCircumferenceCentimeters"), pydantic.Field(alias="hipCircumferenceCentimeters")
    ]
    hip_circumference_inches: typing_extensions.Annotated[
        str, FieldMetadata(alias="hipCircumferenceInches"), pydantic.Field(alias="hipCircumferenceInches")
    ]
    height_body_position: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightBodyPosition"), pydantic.Field(alias="heightBodyPosition")
    ]
    neck_circumference_centimeters: typing_extensions.Annotated[
        str, FieldMetadata(alias="neckCircumferenceCentimeters"), pydantic.Field(alias="neckCircumferenceCentimeters")
    ]
    neck_circumference_inches: typing_extensions.Annotated[
        str, FieldMetadata(alias="neckCircumferenceInches"), pydantic.Field(alias="neckCircumferenceInches")
    ]
    pulse_oximeter_oxygen_saturation_source: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationSource"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationSource"),
    ]
    pain_score_loinc: typing_extensions.Annotated[
        str, FieldMetadata(alias="painScoreLoinc"), pydantic.Field(alias="painScoreLoinc")
    ]
    pain_score_display: typing_extensions.Annotated[
        str, FieldMetadata(alias="painScoreDisplay"), pydantic.Field(alias="painScoreDisplay")
    ]
    peak_flow: typing_extensions.Annotated[str, FieldMetadata(alias="peakFlow"), pydantic.Field(alias="peakFlow")]
    peak_flow_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="peakFlowMethod"), pydantic.Field(alias="peakFlowMethod")
    ]
    peak_flow_timing: typing_extensions.Annotated[
        str, FieldMetadata(alias="peakFlowTiming"), pydantic.Field(alias="peakFlowTiming")
    ]
    respiration_rate: typing_extensions.Annotated[
        str, FieldMetadata(alias="respirationRate"), pydantic.Field(alias="respirationRate")
    ]
    pulse_oximeter_oxygen_saturation_measured: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationMeasured"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationMeasured"),
    ]
    temperature_degrees_celcius: typing_extensions.Annotated[
        str, FieldMetadata(alias="temperatureDegreesCelcius"), pydantic.Field(alias="temperatureDegreesCelcius")
    ]
    temperature_degrees_fahrenheit: typing_extensions.Annotated[
        str, FieldMetadata(alias="temperatureDegreesFahrenheit"), pydantic.Field(alias="temperatureDegreesFahrenheit")
    ]
    temperature_site: typing_extensions.Annotated[
        str, FieldMetadata(alias="temperatureSite"), pydantic.Field(alias="temperatureSite")
    ]
    fraction_of_inspired_oxygen_litres_per_minute: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fractionOfInspiredOxygenLitresPerMinute"),
        pydantic.Field(alias="fractionOfInspiredOxygenLitresPerMinute"),
    ]
    current_age: typing_extensions.Annotated[str, FieldMetadata(alias="currentAge"), pydantic.Field(alias="currentAge")]
    fraction_of_inspired_oxygen_room_air: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fractionOfInspiredOxygenRoomAir"),
        pydantic.Field(alias="fractionOfInspiredOxygenRoomAir"),
    ]
    pulse_oximeter_oxygen_saturation_rest_litres_per_minute: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationRestLitresPerMinute"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationRestLitresPerMinute"),
    ]
    pain_method: typing_extensions.Annotated[str, FieldMetadata(alias="painMethod"), pydantic.Field(alias="painMethod")]
    pulse_oximeter_oxygen_saturation_ambulatory: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pulseOximeterOxygenSaturationAmbulatory"),
        pydantic.Field(alias="pulseOximeterOxygenSaturationAmbulatory"),
    ]
    reason_refused: typing_extensions.Annotated[
        str, FieldMetadata(alias="reasonRefused"), pydantic.Field(alias="reasonRefused")
    ]
    unobtainable_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="unobtainableReason"), pydantic.Field(alias="unobtainableReason")
    ]
    patient_refused_vitals: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientRefusedVitals"), pydantic.Field(alias="patientRefusedVitals")
    ]
    unobtainable_vitals: typing_extensions.Annotated[
        str, FieldMetadata(alias="unobtainableVitals"), pydantic.Field(alias="unobtainableVitals")
    ]
    waist_circumference_centimeters: typing_extensions.Annotated[
        str, FieldMetadata(alias="waistCircumferenceCentimeters"), pydantic.Field(alias="waistCircumferenceCentimeters")
    ]
    waist_circumference_inches: typing_extensions.Annotated[
        str, FieldMetadata(alias="waistCircumferenceInches"), pydantic.Field(alias="waistCircumferenceInches")
    ]
    waist_hip_ratio: typing_extensions.Annotated[
        str, FieldMetadata(alias="waistHipRatio"), pydantic.Field(alias="waistHipRatio")
    ]
    weight_context: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightContext"), pydantic.Field(alias="weightContext")
    ]
    weight_kilograms: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightKilograms"), pydantic.Field(alias="weightKilograms")
    ]
    weight_pounds: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightPounds"), pydantic.Field(alias="weightPounds")
    ]
    weight_percent: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightPercent"), pydantic.Field(alias="weightPercent")
    ]
    blood_pressure_cuff_size: typing_extensions.Annotated[
        str, FieldMetadata(alias="bloodPressureCuffSize"), pydantic.Field(alias="bloodPressureCuffSize")
    ]
    are_orthostatic_vital_signs_captured: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="areOrthostaticVitalSignsCaptured"),
        pydantic.Field(alias="areOrthostaticVitalSignsCaptured"),
    ]
    menopausal_stage: typing_extensions.Annotated[
        str, FieldMetadata(alias="menopausalStage"), pydantic.Field(alias="menopausalStage")
    ]
    lmp: str
    gestational_weeks: typing_extensions.Annotated[
        str, FieldMetadata(alias="gestationalWeeks"), pydantic.Field(alias="gestationalWeeks")
    ]
    gestational_days: typing_extensions.Annotated[
        str, FieldMetadata(alias="gestationalDays"), pydantic.Field(alias="gestationalDays")
    ]
    height_centimeters_graph: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightCentimetersGraph"), pydantic.Field(alias="heightCentimetersGraph")
    ]
    height_inches_graph: typing_extensions.Annotated[
        str, FieldMetadata(alias="heightInchesGraph"), pydantic.Field(alias="heightInchesGraph")
    ]
    weight_kilograms_graph: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightKilogramsGraph"), pydantic.Field(alias="weightKilogramsGraph")
    ]
    weight_pounds_graph: typing_extensions.Annotated[
        str, FieldMetadata(alias="weightPoundsGraph"), pydantic.Field(alias="weightPoundsGraph")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
