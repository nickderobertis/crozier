

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTriggerData(enum.StrEnum):
    """
    The left operand of the trigger function. The following Table details for each operand data its type, the supported operator and the possibly retruned value:

    |**Data**|**Type**|**Op**|**Value**|
    |---|---| ---:| ---:|
    | vehicle.alert | List of value | onChange (at least one)/includedIn/equalsTo | Value (ObjetAlert) |
    | vehicle.odometer | Number | equalsTo/greaterThan/lowerThan/ | Value |
    | vehicle.powertrain.status |Enum(powertrain.status) | equalsTo / onChange/includedIn | Value |
    | vehicle.engines.thermic.oil.temp | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.energy.electric.level | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.energy.electric.autonomy | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.energy.fuel.level | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.energy.fuel.autonomy | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.autonomy (global) | Integer | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.energy.charging.status | Enum(ChargingStatusEnum) | onChange/equalsTo/includedIn | Value |
    | vehicle.energy.charging.plugged | Boolean | onChange/equalsTo | Value |
    | vehicle.energy.charging.type | Enum(ChargingTypeEnum) | onChange/equalsTo | Value |
    | vehicle.doorsState.lockedState | N/A | onChange | Value |
    | vehicle.doorsState.opening | N/A | onChange | Value |
    | vehicle.kinetic.moving| Boolean | onChange/equalsTo | Value (true/false) |
    | vehicle.kinetic.speed | Number | equalsTo/greaterThan/ lowerThan/ | Value |
    | vehicle.trip (DEPRECATED)| Literal | onChange| Value(IDTRIP) |
    | vehicle.trip.start| Literal | onChange| Value(IDTRIP) |
    | vehicle.trip.stop| Literal | onChange| Value(IDTRIP) |
    | vehicle.trip.duration| Integer | equalsTo/greaterThan/lowerThan| Value |
    | vehicle.trip.distance| Number | equalsTo/greaterThan/lowerThan| Value |
    | vehicle.trip.state| List of value |includedIn| TripStateEnumArray |
    | vehicle.maintenance.daysBeforeMaintenance, | Number | equalsTo/ greaterThan/ lowerThan/ | Value |
    | vehicle.maintenance.mileageBeforeMaintenance| Number | equalsTo/ greaterThan/ lowerThan/ | Value |
    | vehicle.safety.beltWarning | Enum(beltWarning) | onChange/equalsTo | Value |
    | environment.air.temp | Number | equalsTo/greaterThan/lowerThan/ | Value |
    | privacy.state | Enum(Privacy) | equalsTo / onChange/includedIn | Value |
    | vehicle.drivingBehavior.mode | Enum(drivingBehavior.mode) | equalsTo / onChange/includedIn | Value |
    | vehicle.collision.side | Enum(collision.side) | equalsTo / includedIn | Value |
    | vehicle.collision.severity | Enum(collision.severity) | equalsTo / includedIn | Value |
    | vehicle.safety.autoECallTriggering | Enum(safety.autoECallTriggering) | equalsTo / onChange/includedIn | Value |
    | vehicle.preconditioning.airConditioning | N/A| onChange | Value |
    | vehicle.alarm.trigger.type | Enum(trigger.type)| onChange/equalsTo/includedIn  | Value |
    | vehicle.alarm.status.activation | Enum(status.activation)| onChange/equalsTo  | Value |
    | stolen.state |Boolean| onChange/equalsTo| Value |

    The right operand  (value) argument depends on the type of operation (OP) as following:

      * onChange: no value because we are monitoring the change between two states (before and after).
      * includedIn: value must be an array of size> = 1
      * equalsTo, greaterThan and lowerThan: the value must be an array of size = 1.
    """

    VEHICLE_ALERT = "vehicle.alert"
    VEHICLE_ODOMETER = "vehicle.odometer"
    VEHICLE_POWERTRAIN_STATUS = "vehicle.powertrain.status"
    VEHICLE_ENGINES_THERMIC_OIL_TEMP = "vehicle.engines.thermic.oil.temp"
    VEHICLE_ENERGY_ELECTRIC_LEVEL = "vehicle.energy.electric.level"
    VEHICLE_ENERGY_ELECTRIC_AUTONOMY = "vehicle.energy.electric.autonomy"
    VEHICLE_ENERGY_FUEL_LEVEL = "vehicle.energy.fuel.level"
    VEHICLE_ENERGY_FUEL_AUTONOMY = "vehicle.energy.fuel.autonomy"
    VEHICLE_AUTONOMY = "vehicle.autonomy"
    VEHICLE_ENERGY_CHARGING_STATUS = "vehicle.energy.charging.status"
    VEHICLE_ENERGY_CHARGING_PLUGGED = "vehicle.energy.charging.plugged"
    VEHICLE_ENERGY_CHARGING_TYPE = "vehicle.energy.charging.type"
    VEHICLE_DOORS_STATE_LOCKED_STATE = "vehicle.doorsState.lockedState"
    VEHICLE_DOORS_STATE_OPENING = "vehicle.doorsState.opening"
    VEHICLE_KINETIC_MOVING = "vehicle.kinetic.moving"
    VEHICLE_KINETIC_SPEED = "vehicle.kinetic.speed"
    VEHICLE_TRIP = "vehicle.trip"
    VEHICLE_TRIP_START = "vehicle.trip.start"
    VEHICLE_TRIP_STOP = "vehicle.trip.stop"
    VEHICLE_TRIP_DURATION = "vehicle.trip.duration"
    VEHICLE_TRIP_DISTANCE = "vehicle.trip.distance"
    VEHICLE_TRIP_STATE = "vehicle.trip.state"
    VEHICLE_MAINTENANCE_DAYS_BEFORE_MAINTENANCE = "vehicle.maintenance.daysBeforeMaintenance"
    VEHICLE_MAINTENANCE_MILEAGE_BEFORE_MAINTENANCE = "vehicle.maintenance.mileageBeforeMaintenance"
    VEHICLE_SAFETY_BELT_WARNING = "vehicle.safety.beltWarning"
    ENVIRONMENT_AIR_TEMP = "environment.air.temp"
    PRIVACY_STATE = "privacy.state"
    VEHICLE_DRIVING_BEHAVIOR_MODE = "vehicle.drivingBehavior.mode"
    VEHICLE_COLLISION_SIDE = "vehicle.collision.side"
    VEHICLE_COLLISION_SEVERITY = "vehicle.collision.severity"
    VEHICLE_SAFETY_AUTO_E_CALL_TRIGGERING = "vehicle.safety.autoECallTriggering"
    VEHICLE_PRECONDITIONING_AIR_CONDITIONING = "vehicle.preconditioning.airConditioning"
    VEHICLE_ALARM_TRIGGER_TYPE = "vehicle.alarm.trigger.type"
    VEHICLE_ALARM_STATUS_ACTIVATION = "vehicle.alarm.status.activation"
    STOLEN_STATE = "stolen.state"

    def visit(
        self,
        vehicle_alert: typing.Callable[[], T_Result],
        vehicle_odometer: typing.Callable[[], T_Result],
        vehicle_powertrain_status: typing.Callable[[], T_Result],
        vehicle_engines_thermic_oil_temp: typing.Callable[[], T_Result],
        vehicle_energy_electric_level: typing.Callable[[], T_Result],
        vehicle_energy_electric_autonomy: typing.Callable[[], T_Result],
        vehicle_energy_fuel_level: typing.Callable[[], T_Result],
        vehicle_energy_fuel_autonomy: typing.Callable[[], T_Result],
        vehicle_autonomy: typing.Callable[[], T_Result],
        vehicle_energy_charging_status: typing.Callable[[], T_Result],
        vehicle_energy_charging_plugged: typing.Callable[[], T_Result],
        vehicle_energy_charging_type: typing.Callable[[], T_Result],
        vehicle_doors_state_locked_state: typing.Callable[[], T_Result],
        vehicle_doors_state_opening: typing.Callable[[], T_Result],
        vehicle_kinetic_moving: typing.Callable[[], T_Result],
        vehicle_kinetic_speed: typing.Callable[[], T_Result],
        vehicle_trip: typing.Callable[[], T_Result],
        vehicle_trip_start: typing.Callable[[], T_Result],
        vehicle_trip_stop: typing.Callable[[], T_Result],
        vehicle_trip_duration: typing.Callable[[], T_Result],
        vehicle_trip_distance: typing.Callable[[], T_Result],
        vehicle_trip_state: typing.Callable[[], T_Result],
        vehicle_maintenance_days_before_maintenance: typing.Callable[[], T_Result],
        vehicle_maintenance_mileage_before_maintenance: typing.Callable[[], T_Result],
        vehicle_safety_belt_warning: typing.Callable[[], T_Result],
        environment_air_temp: typing.Callable[[], T_Result],
        privacy_state: typing.Callable[[], T_Result],
        vehicle_driving_behavior_mode: typing.Callable[[], T_Result],
        vehicle_collision_side: typing.Callable[[], T_Result],
        vehicle_collision_severity: typing.Callable[[], T_Result],
        vehicle_safety_auto_e_call_triggering: typing.Callable[[], T_Result],
        vehicle_preconditioning_air_conditioning: typing.Callable[[], T_Result],
        vehicle_alarm_trigger_type: typing.Callable[[], T_Result],
        vehicle_alarm_status_activation: typing.Callable[[], T_Result],
        stolen_state: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataTriggerData.VEHICLE_ALERT:
            return vehicle_alert()
        if self is DataTriggerData.VEHICLE_ODOMETER:
            return vehicle_odometer()
        if self is DataTriggerData.VEHICLE_POWERTRAIN_STATUS:
            return vehicle_powertrain_status()
        if self is DataTriggerData.VEHICLE_ENGINES_THERMIC_OIL_TEMP:
            return vehicle_engines_thermic_oil_temp()
        if self is DataTriggerData.VEHICLE_ENERGY_ELECTRIC_LEVEL:
            return vehicle_energy_electric_level()
        if self is DataTriggerData.VEHICLE_ENERGY_ELECTRIC_AUTONOMY:
            return vehicle_energy_electric_autonomy()
        if self is DataTriggerData.VEHICLE_ENERGY_FUEL_LEVEL:
            return vehicle_energy_fuel_level()
        if self is DataTriggerData.VEHICLE_ENERGY_FUEL_AUTONOMY:
            return vehicle_energy_fuel_autonomy()
        if self is DataTriggerData.VEHICLE_AUTONOMY:
            return vehicle_autonomy()
        if self is DataTriggerData.VEHICLE_ENERGY_CHARGING_STATUS:
            return vehicle_energy_charging_status()
        if self is DataTriggerData.VEHICLE_ENERGY_CHARGING_PLUGGED:
            return vehicle_energy_charging_plugged()
        if self is DataTriggerData.VEHICLE_ENERGY_CHARGING_TYPE:
            return vehicle_energy_charging_type()
        if self is DataTriggerData.VEHICLE_DOORS_STATE_LOCKED_STATE:
            return vehicle_doors_state_locked_state()
        if self is DataTriggerData.VEHICLE_DOORS_STATE_OPENING:
            return vehicle_doors_state_opening()
        if self is DataTriggerData.VEHICLE_KINETIC_MOVING:
            return vehicle_kinetic_moving()
        if self is DataTriggerData.VEHICLE_KINETIC_SPEED:
            return vehicle_kinetic_speed()
        if self is DataTriggerData.VEHICLE_TRIP:
            return vehicle_trip()
        if self is DataTriggerData.VEHICLE_TRIP_START:
            return vehicle_trip_start()
        if self is DataTriggerData.VEHICLE_TRIP_STOP:
            return vehicle_trip_stop()
        if self is DataTriggerData.VEHICLE_TRIP_DURATION:
            return vehicle_trip_duration()
        if self is DataTriggerData.VEHICLE_TRIP_DISTANCE:
            return vehicle_trip_distance()
        if self is DataTriggerData.VEHICLE_TRIP_STATE:
            return vehicle_trip_state()
        if self is DataTriggerData.VEHICLE_MAINTENANCE_DAYS_BEFORE_MAINTENANCE:
            return vehicle_maintenance_days_before_maintenance()
        if self is DataTriggerData.VEHICLE_MAINTENANCE_MILEAGE_BEFORE_MAINTENANCE:
            return vehicle_maintenance_mileage_before_maintenance()
        if self is DataTriggerData.VEHICLE_SAFETY_BELT_WARNING:
            return vehicle_safety_belt_warning()
        if self is DataTriggerData.ENVIRONMENT_AIR_TEMP:
            return environment_air_temp()
        if self is DataTriggerData.PRIVACY_STATE:
            return privacy_state()
        if self is DataTriggerData.VEHICLE_DRIVING_BEHAVIOR_MODE:
            return vehicle_driving_behavior_mode()
        if self is DataTriggerData.VEHICLE_COLLISION_SIDE:
            return vehicle_collision_side()
        if self is DataTriggerData.VEHICLE_COLLISION_SEVERITY:
            return vehicle_collision_severity()
        if self is DataTriggerData.VEHICLE_SAFETY_AUTO_E_CALL_TRIGGERING:
            return vehicle_safety_auto_e_call_triggering()
        if self is DataTriggerData.VEHICLE_PRECONDITIONING_AIR_CONDITIONING:
            return vehicle_preconditioning_air_conditioning()
        if self is DataTriggerData.VEHICLE_ALARM_TRIGGER_TYPE:
            return vehicle_alarm_trigger_type()
        if self is DataTriggerData.VEHICLE_ALARM_STATUS_ACTIVATION:
            return vehicle_alarm_status_activation()
        if self is DataTriggerData.STOLEN_STATE:
            return stolen_state()
