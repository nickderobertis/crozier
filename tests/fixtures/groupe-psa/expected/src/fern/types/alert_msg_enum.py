

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertMsgEnum(enum.StrEnum):
    """
    MPH alert list
    """

    ABS_BRAKING_SYSTEM_FAULT = "AbsBrakingSystemFault"
    ACTIVE_SPOILER_FAULT = "ActiveSpoilerFault"
    AD_BLUE_FAULT = "AdBlueFault"
    AD_BLUE_FAULT_STARTING_IMPOSSIBLE = "AdBlueFaultStartingImpossible"
    AD_BLUE_FAULT_STARTING_IMPOSSIBLE_SOON = "AdBlueFaultStartingImpossibleSoon"
    ADD_WASHER_FLUID = "AddWasherFluid"
    AIRBAG_OR_SEAT_BELT_PRETENSIONER_OR_ACTIVE_HOOD_FAILURE = "AirbagOrSeatBeltPretensionerOrActiveHoodFailure"
    ASSISTANCE_BUTTON_FAULT = "AssistanceButtonFault"
    AUTOMATIC_BRAKING_DEACTIVATED = "AutomaticBrakingDeactivated"
    AUTOMATIC_HEADLIGHT_ADJUSTMENT_FAULT = "AutomaticHeadlightAdjustmentFault"
    BATTERY_CHARGE_OR_ELECTRICAL_CIRCUIT_SYSTEM_FAILURE = "BatteryChargeOrElectricalCircuitSystemFailure"
    BRAKING_SYSTEM_FAILURE = "BrakingSystemFailure"
    CHARGING_FAILURE = "ChargingFailure"
    CHECK_THE_CENTER_BRAKE_LAMP = "CheckTheCenterBrakeLamp"
    COLLISION_DETECTION_SYSTEM_FAULT = "CollisionDetectionSystemFault"
    COLLISION_MITIGATION_SYSTEM_FAULT = "CollisionMitigationSystemFault"
    COOLANT_LEVELLOW = "CoolantLevellow"
    DRIVING_ASSISTANCE_SENSOR_BLIND = "DrivingAssistanceSensorBlind"
    ELECTRIC_TRACTION_SYSTEM_FAILURE_LIMIT_SPEED = "ElectricTractionSystemFailureLimitSpeed"
    ELECTRIC_TRACTION_SYSTEM_FAILURE_STOP_VEHICLE = "ElectricTractionSystemFailureStopVehicle"
    ELECTRIC_TRACTION_SYSTEM_FAULT = "ElectricTractionSystemFault"
    ELECTRONIC_IMMOBILISER_FAULT = "ElectronicImmobiliserFault"
    EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILUE_STARTING_IMPOSSIBLE = (
        "EmissionSystemOrAdBlueQualityFailueStartingImpossible"
    )
    EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILUE_STARTING_IMPOSSIBLE_SOON = (
        "EmissionSystemOrAdBlueQualityFailueStartingImpossibleSoon"
    )
    EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILURE = "EmissionSystemOrAdBlueQualityFailure"
    ENGINE_FAILURE = "EngineFailure"
    ENGINE_FAULT = "EngineFault"
    ENGINE_MISFIRING_FUEL = "EngineMisfiringFuel"
    ENGINE_OIL_PRESSURE_FAILURE = "EngineOilPressureFailure"
    ENGINE_TEMPERATURE_FAILURE = "EngineTemperatureFailure"
    ESP_ASR_SYSTEM_FAULT = "EspAsrSystemFault"
    FRONT_LEFT_FLASHING_INDICATOR_FAULT = "FrontLeftFlashingIndicatorFault"
    FRONT_LEFT_FOG_LAMPS_FAULT = "FrontLeftFogLampsFault"
    FRONT_LEFT_PARKING_LAMPS_FAULT = "FrontLeftParkingLampsFault"
    FRONT_RIGHT_FLASHING_INDICATOR_FAULT = "FrontRightFlashingIndicatorFault"
    FRONT_RIGHT_FOG_LAMPS_FAULT = "FrontRightFogLampsFault"
    FRONT_RIGHT_PARKING_LAMPS_FAULT = "FrontRightParkingLampsFault"
    FUEL_LEVEL_LOW = "FuelLevelLow"
    GEARBOX_FAULT = "GearboxFault"
    HEADLIGHTS_FAULT = "HeadlightsFault"
    INSTALLED_SPARE_WHEEL_FAULT = "InstalledSpareWheelFault"
    INTER_VEHICLE_TIME_MEASUREMENT_FAULT = "InterVehicleTimeMeasurementFault"
    LANE_CHANGE_ASSISTANCE_FAULT = "LaneChangeAssistanceFault"
    LANE_DEPARTURE_WARNING_SYSTEM_FAULT = "LaneDepartureWarningSystemFault"
    LEFT_BRAKE_LAMP_FAULT = "LeftBrakeLampFault"
    LEFT_FRONT_DOOR_OPEN = "LeftFrontDoorOpen"
    LEFT_FRONT_DOOR_OPEN_LOW_SPEED = "LeftFrontDoorOpenLowSpeed"
    LEFT_FRONT_TIRE_PRESSUR_SENSOR_FAULT = "LeftFrontTirePressurSensorFault"
    LEFT_FRONT_TIRE_PUNCTURE = "LeftFrontTirePuncture"
    LEFT_FRONT_TIRE_UNDER_INFLATED = "LeftFrontTireUnderInflated"
    LEFT_REAR_DOOR_OPEN = "LeftRearDoorOpen"
    LEFT_REAR_DOOR_OPEN_LOW_SPEED = "LeftRearDoorOpenLowSpeed"
    LEFT_REAR_TIRE_PRESSUR_SENSOR_FAULT = "LeftRearTirePressurSensorFault"
    LEFT_REAR_TIRE_PUNCTURE = "LeftRearTirePuncture"
    LEFT_REAR_TIRE_UNDER_INFLATED = "LeftRearTireUnderInflated"
    LEFT_REVERSE_LAMP_FAULT = "LeftReverseLampFault"
    OIL_LEVEL_LOW = "OilLevelLow"
    PARK_ASSIST_SYSTEM_FAULT = "ParkAssistSystemFault"
    PARKING_BRAKE_OR_HILL_START_SYSTEM_FAILURE = "ParkingBrakeOrHillStartSystemFailure"
    PARTICLE_FILTER_ADDITIVE_LEVEL_TOO_LOW = "ParticleFilterAdditiveLevelTooLow"
    PARTICLE_FILTER_FULL = "ParticleFilterFull"
    PARTICLE_FILTER_REGENERATING = "ParticleFilterRegenerating"
    POWER_STEERING_FAILURE = "PowerSteeringFailure"
    POWER_STEERING_FAULT = "PowerSteeringFault"
    PREHEATING_PREVENTILATION_DEACTIVATED_BATTERY_LOW = "PreheatingPreventilationDeactivatedBatteryLow"
    PREHEATING_PREVENTILATION_DEACTIVATED_CLOCK_UNSET = "PreheatingPreventilationDeactivatedClockUnset"
    PREHEATING_PREVENTILATION_DEACTIVATED_FUEL_LEVEL_LOW = "PreheatingPreventilationDeactivatedFuelLevelLow"
    REAR_LEFT_FLASHING_INDICATOR_FAULT = "RearLeftFlashingIndicatorFault"
    REAR_LEFT_FOG_LAMPS_FAULT = "RearLeftFogLampsFault"
    REAR_LEFT_PARKING_LAMPS_FAULT = "RearLeftParkingLampsFault"
    REAR_RIGHT_FLASHING_INDICATOR_FAULT = "RearRightFlashingIndicatorFault"
    REAR_RIGHT_FOG_LAMPS_FAULT = "RearRightFogLampsFault"
    REAR_RIGHT_PARKING_LAMPS_FAULT = "RearRightParkingLampsFault"
    REAR_WINDOW_OPEN = "RearWindowOpen"
    REAR_WINDOW_OPEN_LOW_SPEED = "RearWindowOpenLowSpeed"
    REPLACE_BRAKE_PADS = "ReplaceBrakePads"
    REPLACE_THE_REMOTE_CONTROL_BATTERY = "ReplaceTheRemoteControlBattery"
    RETRACTABLE_ROOF_MECHANISM_FAULT = "RetractableRoofMechanismFault"
    RIGHT_BRAKE_LAMP_FAULT = "RightBrakeLampFault"
    RIGHT_FRONT_DOOR_OPEN_LOW_SPEED = "RightFrontDoorOpenLowSpeed"
    RIGHT_FRONT_DOOR_OPEN = "RightFrontDoorOpen"
    RIGHT_FRONT_TIRE_PRESSUR_SENSOR_FAULT = "RightFrontTirePressurSensorFault"
    RIGHT_FRONT_TIRE_PUNCTURE = "RightFrontTirePuncture"
    RIGHT_FRONT_TIRE_UNDER_INFLATED = "RightFrontTireUnderInflated"
    RIGHT_REAR_DOOR_OPEN = "RightRearDoorOpen"
    RIGHT_REAR_DOOR_OPEN_LOW_SPEED = "RightRearDoorOpenLowSpeed"
    RIGHT_REAR_TIRE_PRESSUR_SENSOR_FAULT = "RightRearTirePressurSensorFault"
    RIGHT_REAR_TIRE_PUNCTURE = "RightRearTirePuncture"
    RIGHT_REAR_TIRE_UNDER_INFLATED = "RightRearTireUnderInflated"
    RIGHT_REVERSE_LAMP_FAULT = "RightReverseLampFault"
    RISK_OF_ICE = "RiskOfIce"
    ROOF_OPERATION_NOT_POSSIBLE_SPEED_UNKNOWN = "RoofOperationNotPossibleSpeedUnknown"
    ROOF_OPERATION_NOT_POSSIBLE_TOO_HIGH_TEMP = "RoofOperationNotPossibleTooHighTemp"
    SHIFT_TO_PARK = "ShiftToPark"
    STEERING_LOCK_FAULT = "SteeringLockFault"
    SUSPENSION_FAULT = "SuspensionFault"
    SUSPENSION_FAULT_LIMIT_SPEED = "SuspensionFaultLimitSpeed"
    SUSPENSION_FAULT_REPAIRE_VEHICLE = "SuspensionFaultRepaireVehicle"
    TIRE_UNDER_INFLATION_DETECTION_SYSTEM_FAULT = "TireUnderInflationDetectionSystemFault"
    TOO_MANY_ROOF_OPERATION = "TooManyRoofOperation"
    TRAILER_CONNECTION_FAULT = "TrailerConnectionFault"
    TRUNK_OR_HOOD_OPEN = "TrunkOrHoodOpen"
    TRUNK_OR_HOOD_OPEN_LOW_SPEED = "TrunkOrHoodOpenLowSpeed"
    WATER_IN_THE_DIESEL_FUEL_FILTER = "WaterInTheDieselFuelFilter"

    def visit(
        self,
        abs_braking_system_fault: typing.Callable[[], T_Result],
        active_spoiler_fault: typing.Callable[[], T_Result],
        ad_blue_fault: typing.Callable[[], T_Result],
        ad_blue_fault_starting_impossible: typing.Callable[[], T_Result],
        ad_blue_fault_starting_impossible_soon: typing.Callable[[], T_Result],
        add_washer_fluid: typing.Callable[[], T_Result],
        airbag_or_seat_belt_pretensioner_or_active_hood_failure: typing.Callable[[], T_Result],
        assistance_button_fault: typing.Callable[[], T_Result],
        automatic_braking_deactivated: typing.Callable[[], T_Result],
        automatic_headlight_adjustment_fault: typing.Callable[[], T_Result],
        battery_charge_or_electrical_circuit_system_failure: typing.Callable[[], T_Result],
        braking_system_failure: typing.Callable[[], T_Result],
        charging_failure: typing.Callable[[], T_Result],
        check_the_center_brake_lamp: typing.Callable[[], T_Result],
        collision_detection_system_fault: typing.Callable[[], T_Result],
        collision_mitigation_system_fault: typing.Callable[[], T_Result],
        coolant_levellow: typing.Callable[[], T_Result],
        driving_assistance_sensor_blind: typing.Callable[[], T_Result],
        electric_traction_system_failure_limit_speed: typing.Callable[[], T_Result],
        electric_traction_system_failure_stop_vehicle: typing.Callable[[], T_Result],
        electric_traction_system_fault: typing.Callable[[], T_Result],
        electronic_immobiliser_fault: typing.Callable[[], T_Result],
        emission_system_or_ad_blue_quality_failue_starting_impossible: typing.Callable[[], T_Result],
        emission_system_or_ad_blue_quality_failue_starting_impossible_soon: typing.Callable[[], T_Result],
        emission_system_or_ad_blue_quality_failure: typing.Callable[[], T_Result],
        engine_failure: typing.Callable[[], T_Result],
        engine_fault: typing.Callable[[], T_Result],
        engine_misfiring_fuel: typing.Callable[[], T_Result],
        engine_oil_pressure_failure: typing.Callable[[], T_Result],
        engine_temperature_failure: typing.Callable[[], T_Result],
        esp_asr_system_fault: typing.Callable[[], T_Result],
        front_left_flashing_indicator_fault: typing.Callable[[], T_Result],
        front_left_fog_lamps_fault: typing.Callable[[], T_Result],
        front_left_parking_lamps_fault: typing.Callable[[], T_Result],
        front_right_flashing_indicator_fault: typing.Callable[[], T_Result],
        front_right_fog_lamps_fault: typing.Callable[[], T_Result],
        front_right_parking_lamps_fault: typing.Callable[[], T_Result],
        fuel_level_low: typing.Callable[[], T_Result],
        gearbox_fault: typing.Callable[[], T_Result],
        headlights_fault: typing.Callable[[], T_Result],
        installed_spare_wheel_fault: typing.Callable[[], T_Result],
        inter_vehicle_time_measurement_fault: typing.Callable[[], T_Result],
        lane_change_assistance_fault: typing.Callable[[], T_Result],
        lane_departure_warning_system_fault: typing.Callable[[], T_Result],
        left_brake_lamp_fault: typing.Callable[[], T_Result],
        left_front_door_open: typing.Callable[[], T_Result],
        left_front_door_open_low_speed: typing.Callable[[], T_Result],
        left_front_tire_pressur_sensor_fault: typing.Callable[[], T_Result],
        left_front_tire_puncture: typing.Callable[[], T_Result],
        left_front_tire_under_inflated: typing.Callable[[], T_Result],
        left_rear_door_open: typing.Callable[[], T_Result],
        left_rear_door_open_low_speed: typing.Callable[[], T_Result],
        left_rear_tire_pressur_sensor_fault: typing.Callable[[], T_Result],
        left_rear_tire_puncture: typing.Callable[[], T_Result],
        left_rear_tire_under_inflated: typing.Callable[[], T_Result],
        left_reverse_lamp_fault: typing.Callable[[], T_Result],
        oil_level_low: typing.Callable[[], T_Result],
        park_assist_system_fault: typing.Callable[[], T_Result],
        parking_brake_or_hill_start_system_failure: typing.Callable[[], T_Result],
        particle_filter_additive_level_too_low: typing.Callable[[], T_Result],
        particle_filter_full: typing.Callable[[], T_Result],
        particle_filter_regenerating: typing.Callable[[], T_Result],
        power_steering_failure: typing.Callable[[], T_Result],
        power_steering_fault: typing.Callable[[], T_Result],
        preheating_preventilation_deactivated_battery_low: typing.Callable[[], T_Result],
        preheating_preventilation_deactivated_clock_unset: typing.Callable[[], T_Result],
        preheating_preventilation_deactivated_fuel_level_low: typing.Callable[[], T_Result],
        rear_left_flashing_indicator_fault: typing.Callable[[], T_Result],
        rear_left_fog_lamps_fault: typing.Callable[[], T_Result],
        rear_left_parking_lamps_fault: typing.Callable[[], T_Result],
        rear_right_flashing_indicator_fault: typing.Callable[[], T_Result],
        rear_right_fog_lamps_fault: typing.Callable[[], T_Result],
        rear_right_parking_lamps_fault: typing.Callable[[], T_Result],
        rear_window_open: typing.Callable[[], T_Result],
        rear_window_open_low_speed: typing.Callable[[], T_Result],
        replace_brake_pads: typing.Callable[[], T_Result],
        replace_the_remote_control_battery: typing.Callable[[], T_Result],
        retractable_roof_mechanism_fault: typing.Callable[[], T_Result],
        right_brake_lamp_fault: typing.Callable[[], T_Result],
        right_front_door_open_low_speed: typing.Callable[[], T_Result],
        right_front_door_open: typing.Callable[[], T_Result],
        right_front_tire_pressur_sensor_fault: typing.Callable[[], T_Result],
        right_front_tire_puncture: typing.Callable[[], T_Result],
        right_front_tire_under_inflated: typing.Callable[[], T_Result],
        right_rear_door_open: typing.Callable[[], T_Result],
        right_rear_door_open_low_speed: typing.Callable[[], T_Result],
        right_rear_tire_pressur_sensor_fault: typing.Callable[[], T_Result],
        right_rear_tire_puncture: typing.Callable[[], T_Result],
        right_rear_tire_under_inflated: typing.Callable[[], T_Result],
        right_reverse_lamp_fault: typing.Callable[[], T_Result],
        risk_of_ice: typing.Callable[[], T_Result],
        roof_operation_not_possible_speed_unknown: typing.Callable[[], T_Result],
        roof_operation_not_possible_too_high_temp: typing.Callable[[], T_Result],
        shift_to_park: typing.Callable[[], T_Result],
        steering_lock_fault: typing.Callable[[], T_Result],
        suspension_fault: typing.Callable[[], T_Result],
        suspension_fault_limit_speed: typing.Callable[[], T_Result],
        suspension_fault_repaire_vehicle: typing.Callable[[], T_Result],
        tire_under_inflation_detection_system_fault: typing.Callable[[], T_Result],
        too_many_roof_operation: typing.Callable[[], T_Result],
        trailer_connection_fault: typing.Callable[[], T_Result],
        trunk_or_hood_open: typing.Callable[[], T_Result],
        trunk_or_hood_open_low_speed: typing.Callable[[], T_Result],
        water_in_the_diesel_fuel_filter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertMsgEnum.ABS_BRAKING_SYSTEM_FAULT:
            return abs_braking_system_fault()
        if self is AlertMsgEnum.ACTIVE_SPOILER_FAULT:
            return active_spoiler_fault()
        if self is AlertMsgEnum.AD_BLUE_FAULT:
            return ad_blue_fault()
        if self is AlertMsgEnum.AD_BLUE_FAULT_STARTING_IMPOSSIBLE:
            return ad_blue_fault_starting_impossible()
        if self is AlertMsgEnum.AD_BLUE_FAULT_STARTING_IMPOSSIBLE_SOON:
            return ad_blue_fault_starting_impossible_soon()
        if self is AlertMsgEnum.ADD_WASHER_FLUID:
            return add_washer_fluid()
        if self is AlertMsgEnum.AIRBAG_OR_SEAT_BELT_PRETENSIONER_OR_ACTIVE_HOOD_FAILURE:
            return airbag_or_seat_belt_pretensioner_or_active_hood_failure()
        if self is AlertMsgEnum.ASSISTANCE_BUTTON_FAULT:
            return assistance_button_fault()
        if self is AlertMsgEnum.AUTOMATIC_BRAKING_DEACTIVATED:
            return automatic_braking_deactivated()
        if self is AlertMsgEnum.AUTOMATIC_HEADLIGHT_ADJUSTMENT_FAULT:
            return automatic_headlight_adjustment_fault()
        if self is AlertMsgEnum.BATTERY_CHARGE_OR_ELECTRICAL_CIRCUIT_SYSTEM_FAILURE:
            return battery_charge_or_electrical_circuit_system_failure()
        if self is AlertMsgEnum.BRAKING_SYSTEM_FAILURE:
            return braking_system_failure()
        if self is AlertMsgEnum.CHARGING_FAILURE:
            return charging_failure()
        if self is AlertMsgEnum.CHECK_THE_CENTER_BRAKE_LAMP:
            return check_the_center_brake_lamp()
        if self is AlertMsgEnum.COLLISION_DETECTION_SYSTEM_FAULT:
            return collision_detection_system_fault()
        if self is AlertMsgEnum.COLLISION_MITIGATION_SYSTEM_FAULT:
            return collision_mitigation_system_fault()
        if self is AlertMsgEnum.COOLANT_LEVELLOW:
            return coolant_levellow()
        if self is AlertMsgEnum.DRIVING_ASSISTANCE_SENSOR_BLIND:
            return driving_assistance_sensor_blind()
        if self is AlertMsgEnum.ELECTRIC_TRACTION_SYSTEM_FAILURE_LIMIT_SPEED:
            return electric_traction_system_failure_limit_speed()
        if self is AlertMsgEnum.ELECTRIC_TRACTION_SYSTEM_FAILURE_STOP_VEHICLE:
            return electric_traction_system_failure_stop_vehicle()
        if self is AlertMsgEnum.ELECTRIC_TRACTION_SYSTEM_FAULT:
            return electric_traction_system_fault()
        if self is AlertMsgEnum.ELECTRONIC_IMMOBILISER_FAULT:
            return electronic_immobiliser_fault()
        if self is AlertMsgEnum.EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILUE_STARTING_IMPOSSIBLE:
            return emission_system_or_ad_blue_quality_failue_starting_impossible()
        if self is AlertMsgEnum.EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILUE_STARTING_IMPOSSIBLE_SOON:
            return emission_system_or_ad_blue_quality_failue_starting_impossible_soon()
        if self is AlertMsgEnum.EMISSION_SYSTEM_OR_AD_BLUE_QUALITY_FAILURE:
            return emission_system_or_ad_blue_quality_failure()
        if self is AlertMsgEnum.ENGINE_FAILURE:
            return engine_failure()
        if self is AlertMsgEnum.ENGINE_FAULT:
            return engine_fault()
        if self is AlertMsgEnum.ENGINE_MISFIRING_FUEL:
            return engine_misfiring_fuel()
        if self is AlertMsgEnum.ENGINE_OIL_PRESSURE_FAILURE:
            return engine_oil_pressure_failure()
        if self is AlertMsgEnum.ENGINE_TEMPERATURE_FAILURE:
            return engine_temperature_failure()
        if self is AlertMsgEnum.ESP_ASR_SYSTEM_FAULT:
            return esp_asr_system_fault()
        if self is AlertMsgEnum.FRONT_LEFT_FLASHING_INDICATOR_FAULT:
            return front_left_flashing_indicator_fault()
        if self is AlertMsgEnum.FRONT_LEFT_FOG_LAMPS_FAULT:
            return front_left_fog_lamps_fault()
        if self is AlertMsgEnum.FRONT_LEFT_PARKING_LAMPS_FAULT:
            return front_left_parking_lamps_fault()
        if self is AlertMsgEnum.FRONT_RIGHT_FLASHING_INDICATOR_FAULT:
            return front_right_flashing_indicator_fault()
        if self is AlertMsgEnum.FRONT_RIGHT_FOG_LAMPS_FAULT:
            return front_right_fog_lamps_fault()
        if self is AlertMsgEnum.FRONT_RIGHT_PARKING_LAMPS_FAULT:
            return front_right_parking_lamps_fault()
        if self is AlertMsgEnum.FUEL_LEVEL_LOW:
            return fuel_level_low()
        if self is AlertMsgEnum.GEARBOX_FAULT:
            return gearbox_fault()
        if self is AlertMsgEnum.HEADLIGHTS_FAULT:
            return headlights_fault()
        if self is AlertMsgEnum.INSTALLED_SPARE_WHEEL_FAULT:
            return installed_spare_wheel_fault()
        if self is AlertMsgEnum.INTER_VEHICLE_TIME_MEASUREMENT_FAULT:
            return inter_vehicle_time_measurement_fault()
        if self is AlertMsgEnum.LANE_CHANGE_ASSISTANCE_FAULT:
            return lane_change_assistance_fault()
        if self is AlertMsgEnum.LANE_DEPARTURE_WARNING_SYSTEM_FAULT:
            return lane_departure_warning_system_fault()
        if self is AlertMsgEnum.LEFT_BRAKE_LAMP_FAULT:
            return left_brake_lamp_fault()
        if self is AlertMsgEnum.LEFT_FRONT_DOOR_OPEN:
            return left_front_door_open()
        if self is AlertMsgEnum.LEFT_FRONT_DOOR_OPEN_LOW_SPEED:
            return left_front_door_open_low_speed()
        if self is AlertMsgEnum.LEFT_FRONT_TIRE_PRESSUR_SENSOR_FAULT:
            return left_front_tire_pressur_sensor_fault()
        if self is AlertMsgEnum.LEFT_FRONT_TIRE_PUNCTURE:
            return left_front_tire_puncture()
        if self is AlertMsgEnum.LEFT_FRONT_TIRE_UNDER_INFLATED:
            return left_front_tire_under_inflated()
        if self is AlertMsgEnum.LEFT_REAR_DOOR_OPEN:
            return left_rear_door_open()
        if self is AlertMsgEnum.LEFT_REAR_DOOR_OPEN_LOW_SPEED:
            return left_rear_door_open_low_speed()
        if self is AlertMsgEnum.LEFT_REAR_TIRE_PRESSUR_SENSOR_FAULT:
            return left_rear_tire_pressur_sensor_fault()
        if self is AlertMsgEnum.LEFT_REAR_TIRE_PUNCTURE:
            return left_rear_tire_puncture()
        if self is AlertMsgEnum.LEFT_REAR_TIRE_UNDER_INFLATED:
            return left_rear_tire_under_inflated()
        if self is AlertMsgEnum.LEFT_REVERSE_LAMP_FAULT:
            return left_reverse_lamp_fault()
        if self is AlertMsgEnum.OIL_LEVEL_LOW:
            return oil_level_low()
        if self is AlertMsgEnum.PARK_ASSIST_SYSTEM_FAULT:
            return park_assist_system_fault()
        if self is AlertMsgEnum.PARKING_BRAKE_OR_HILL_START_SYSTEM_FAILURE:
            return parking_brake_or_hill_start_system_failure()
        if self is AlertMsgEnum.PARTICLE_FILTER_ADDITIVE_LEVEL_TOO_LOW:
            return particle_filter_additive_level_too_low()
        if self is AlertMsgEnum.PARTICLE_FILTER_FULL:
            return particle_filter_full()
        if self is AlertMsgEnum.PARTICLE_FILTER_REGENERATING:
            return particle_filter_regenerating()
        if self is AlertMsgEnum.POWER_STEERING_FAILURE:
            return power_steering_failure()
        if self is AlertMsgEnum.POWER_STEERING_FAULT:
            return power_steering_fault()
        if self is AlertMsgEnum.PREHEATING_PREVENTILATION_DEACTIVATED_BATTERY_LOW:
            return preheating_preventilation_deactivated_battery_low()
        if self is AlertMsgEnum.PREHEATING_PREVENTILATION_DEACTIVATED_CLOCK_UNSET:
            return preheating_preventilation_deactivated_clock_unset()
        if self is AlertMsgEnum.PREHEATING_PREVENTILATION_DEACTIVATED_FUEL_LEVEL_LOW:
            return preheating_preventilation_deactivated_fuel_level_low()
        if self is AlertMsgEnum.REAR_LEFT_FLASHING_INDICATOR_FAULT:
            return rear_left_flashing_indicator_fault()
        if self is AlertMsgEnum.REAR_LEFT_FOG_LAMPS_FAULT:
            return rear_left_fog_lamps_fault()
        if self is AlertMsgEnum.REAR_LEFT_PARKING_LAMPS_FAULT:
            return rear_left_parking_lamps_fault()
        if self is AlertMsgEnum.REAR_RIGHT_FLASHING_INDICATOR_FAULT:
            return rear_right_flashing_indicator_fault()
        if self is AlertMsgEnum.REAR_RIGHT_FOG_LAMPS_FAULT:
            return rear_right_fog_lamps_fault()
        if self is AlertMsgEnum.REAR_RIGHT_PARKING_LAMPS_FAULT:
            return rear_right_parking_lamps_fault()
        if self is AlertMsgEnum.REAR_WINDOW_OPEN:
            return rear_window_open()
        if self is AlertMsgEnum.REAR_WINDOW_OPEN_LOW_SPEED:
            return rear_window_open_low_speed()
        if self is AlertMsgEnum.REPLACE_BRAKE_PADS:
            return replace_brake_pads()
        if self is AlertMsgEnum.REPLACE_THE_REMOTE_CONTROL_BATTERY:
            return replace_the_remote_control_battery()
        if self is AlertMsgEnum.RETRACTABLE_ROOF_MECHANISM_FAULT:
            return retractable_roof_mechanism_fault()
        if self is AlertMsgEnum.RIGHT_BRAKE_LAMP_FAULT:
            return right_brake_lamp_fault()
        if self is AlertMsgEnum.RIGHT_FRONT_DOOR_OPEN_LOW_SPEED:
            return right_front_door_open_low_speed()
        if self is AlertMsgEnum.RIGHT_FRONT_DOOR_OPEN:
            return right_front_door_open()
        if self is AlertMsgEnum.RIGHT_FRONT_TIRE_PRESSUR_SENSOR_FAULT:
            return right_front_tire_pressur_sensor_fault()
        if self is AlertMsgEnum.RIGHT_FRONT_TIRE_PUNCTURE:
            return right_front_tire_puncture()
        if self is AlertMsgEnum.RIGHT_FRONT_TIRE_UNDER_INFLATED:
            return right_front_tire_under_inflated()
        if self is AlertMsgEnum.RIGHT_REAR_DOOR_OPEN:
            return right_rear_door_open()
        if self is AlertMsgEnum.RIGHT_REAR_DOOR_OPEN_LOW_SPEED:
            return right_rear_door_open_low_speed()
        if self is AlertMsgEnum.RIGHT_REAR_TIRE_PRESSUR_SENSOR_FAULT:
            return right_rear_tire_pressur_sensor_fault()
        if self is AlertMsgEnum.RIGHT_REAR_TIRE_PUNCTURE:
            return right_rear_tire_puncture()
        if self is AlertMsgEnum.RIGHT_REAR_TIRE_UNDER_INFLATED:
            return right_rear_tire_under_inflated()
        if self is AlertMsgEnum.RIGHT_REVERSE_LAMP_FAULT:
            return right_reverse_lamp_fault()
        if self is AlertMsgEnum.RISK_OF_ICE:
            return risk_of_ice()
        if self is AlertMsgEnum.ROOF_OPERATION_NOT_POSSIBLE_SPEED_UNKNOWN:
            return roof_operation_not_possible_speed_unknown()
        if self is AlertMsgEnum.ROOF_OPERATION_NOT_POSSIBLE_TOO_HIGH_TEMP:
            return roof_operation_not_possible_too_high_temp()
        if self is AlertMsgEnum.SHIFT_TO_PARK:
            return shift_to_park()
        if self is AlertMsgEnum.STEERING_LOCK_FAULT:
            return steering_lock_fault()
        if self is AlertMsgEnum.SUSPENSION_FAULT:
            return suspension_fault()
        if self is AlertMsgEnum.SUSPENSION_FAULT_LIMIT_SPEED:
            return suspension_fault_limit_speed()
        if self is AlertMsgEnum.SUSPENSION_FAULT_REPAIRE_VEHICLE:
            return suspension_fault_repaire_vehicle()
        if self is AlertMsgEnum.TIRE_UNDER_INFLATION_DETECTION_SYSTEM_FAULT:
            return tire_under_inflation_detection_system_fault()
        if self is AlertMsgEnum.TOO_MANY_ROOF_OPERATION:
            return too_many_roof_operation()
        if self is AlertMsgEnum.TRAILER_CONNECTION_FAULT:
            return trailer_connection_fault()
        if self is AlertMsgEnum.TRUNK_OR_HOOD_OPEN:
            return trunk_or_hood_open()
        if self is AlertMsgEnum.TRUNK_OR_HOOD_OPEN_LOW_SPEED:
            return trunk_or_hood_open_low_speed()
        if self is AlertMsgEnum.WATER_IN_THE_DIESEL_FUEL_FILTER:
            return water_in_the_diesel_fuel_filter()
