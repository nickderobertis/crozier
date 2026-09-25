



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .adas import Adas
    from .adas_artiv import AdasArtiv
    from .adas_bsm import AdasBsm
    from .adas_llka import AdasLlka
    from .adas_park_assist import AdasParkAssist
    from .adas_park_assist_front_item import AdasParkAssistFrontItem
    from .adas_park_assist_rear_item import AdasParkAssistRearItem
    from .adas_rgi import AdasRgi
    from .adas_rlka import AdasRlka
    from .air import Air
    from .air_base import AirBase
    from .alarm import Alarm
    from .alarm_details import AlarmDetails
    from .alarm_status import AlarmStatus
    from .alarm_trigger import AlarmTrigger
    from .alarm_type_enum import AlarmTypeEnum
    from .alarm_type_enum_item import AlarmTypeEnumItem
    from .alarms import Alarms
    from .alarms_embedded import AlarmsEmbedded
    from .alert import Alert
    from .alert_end_position import AlertEndPosition
    from .alert_end_position_properties import AlertEndPositionProperties
    from .alert_end_position_properties_fix_status import AlertEndPositionPropertiesFixStatus
    from .alert_end_position_properties_type import AlertEndPositionPropertiesType
    from .alert_end_position_type import AlertEndPositionType
    from .alert_links import AlertLinks
    from .alert_msg_enum import AlertMsgEnum
    from .alert_severity import AlertSeverity
    from .alert_start_position import AlertStartPosition
    from .alert_start_position_properties import AlertStartPositionProperties
    from .alert_start_position_properties_fix_status import AlertStartPositionPropertiesFixStatus
    from .alert_start_position_properties_type import AlertStartPositionPropertiesType
    from .alert_start_position_type import AlertStartPositionType
    from .alerts import Alerts
    from .alerts_embedded import AlertsEmbedded
    from .attribute import Attribute
    from .attribute_set import AttributeSet
    from .attribute_type import AttributeType
    from .attribute_value import AttributeValue
    from .attribute_value_one import AttributeValueOne
    from .base_alarm import BaseAlarm
    from .base_alarm_status import BaseAlarmStatus
    from .base_alarm_status_activation import BaseAlarmStatusActivation
    from .base_alarm_trigger import BaseAlarmTrigger
    from .base_alarm_trigger_position import BaseAlarmTriggerPosition
    from .base_alarm_trigger_position_properties import BaseAlarmTriggerPositionProperties
    from .base_alarm_trigger_position_properties_fix_status import BaseAlarmTriggerPositionPropertiesFixStatus
    from .base_alarm_trigger_position_properties_type import BaseAlarmTriggerPositionPropertiesType
    from .base_alarm_trigger_position_type import BaseAlarmTriggerPositionType
    from .base_alarm_trigger_type import BaseAlarmTriggerType
    from .base_safety import BaseSafety
    from .base_safety_auto_e_call_triggering import BaseSafetyAutoECallTriggering
    from .basic_kinetic import BasicKinetic
    from .basic_program import BasicProgram
    from .basic_program_occurence import BasicProgramOccurence
    from .basic_program_occurence_day_item import BasicProgramOccurenceDayItem
    from .battery import Battery
    from .battery_base import BatteryBase
    from .belt_status import BeltStatus
    from .belt_status_belt import BeltStatusBelt
    from .belt_status_id import BeltStatusId
    from .callback_ref import CallbackRef
    from .callback_ref_links import CallbackRefLinks
    from .callback_status import CallbackStatus
    from .callback_subscribe import CallbackSubscribe
    from .callback_subscribe_batch_notify import CallbackSubscribeBatchNotify
    from .callback_subscribe_callback import CallbackSubscribeCallback
    from .callback_subscribe_retry_policy import CallbackSubscribeRetryPolicy
    from .callback_subscribe_retry_policy_policy import CallbackSubscribeRetryPolicyPolicy
    from .charge_schedule_program import ChargeScheduleProgram
    from .charging_status_enum import ChargingStatusEnum
    from .collection_result import CollectionResult
    from .collision import Collision
    from .collision_details import CollisionDetails
    from .collision_details_severity import CollisionDetailsSeverity
    from .collision_details_side import CollisionDetailsSide
    from .collision_links import CollisionLinks
    from .collision_obj import CollisionObj
    from .collisions import Collisions
    from .collisions_embedded import CollisionsEmbedded
    from .composit_fuel_energy_consumption import CompositFuelEnergyConsumption
    from .consumption import Consumption
    from .created_at_field import CreatedAtField
    from .data_profile import DataProfile
    from .data_trigger import DataTrigger
    from .data_trigger_data import DataTriggerData
    from .data_trigger_op import DataTriggerOp
    from .doors_state import DoorsState
    from .doors_state_base import DoorsStateBase
    from .doors_state_base_locked_states_item import DoorsStateBaseLockedStatesItem
    from .doors_state_base_opening_item import DoorsStateBaseOpeningItem
    from .doors_state_base_opening_item_identifier import DoorsStateBaseOpeningItemIdentifier
    from .doors_state_base_opening_item_state import DoorsStateBaseOpeningItemState
    from .driving_behavior import DrivingBehavior
    from .driving_behavior_base import DrivingBehaviorBase
    from .driving_behavior_base_mode import DrivingBehaviorBaseMode
    from .e_coaching import ECoaching
    from .e_coaching_links import ECoachingLinks
    from .e_coaching_scores_item import ECoachingScoresItem
    from .e_coaching_scores_item_category import ECoachingScoresItemCategory
    from .energy import Energy
    from .energy_base import EnergyBase
    from .energy_base_extension import EnergyBaseExtension
    from .energy_base_extension_electric import EnergyBaseExtensionElectric
    from .energy_base_extension_fuel import EnergyBaseExtensionFuel
    from .energy_base_sub_type import EnergyBaseSubType
    from .energy_base_type import EnergyBaseType
    from .energy_battery import EnergyBattery
    from .energy_battery_base import EnergyBatteryBase
    from .energy_battery_health import EnergyBatteryHealth
    from .energy_battery_load import EnergyBatteryLoad
    from .energy_charging import EnergyCharging
    from .energy_charging_charging_power_level import EnergyChargingChargingPowerLevel
    from .energy_charging_schedule import EnergyChargingSchedule
    from .energy_charging_type import EnergyChargingType
    from .energy_consumption import EnergyConsumption
    from .energy_extension import EnergyExtension
    from .energy_extension_electric import EnergyExtensionElectric
    from .energy_extension_fuel import EnergyExtensionFuel
    from .energy_sub_type import EnergySubType
    from .energy_type import EnergyType
    from .engine import Engine
    from .engine_air import EngineAir
    from .engine_base import EngineBase
    from .engine_base_extension import EngineBaseExtension
    from .engine_base_extension_thermic import EngineBaseExtensionThermic
    from .engine_base_extension_thermic_coolant import EngineBaseExtensionThermicCoolant
    from .engine_base_extension_thermic_oil import EngineBaseExtensionThermicOil
    from .engine_base_gmp_status import EngineBaseGmpStatus
    from .engine_base_type import EngineBaseType
    from .engine_liquid import EngineLiquid
    from .environment import Environment
    from .environment_base import EnvironmentBase
    from .extension import Extension
    from .fleet import Fleet
    from .fleet_links import FleetLinks
    from .fleets import Fleets
    from .fleets_embedded import FleetsEmbedded
    from .geometry import Geometry
    from .health_electric_energy import HealthElectricEnergy
    from .ignition import Ignition
    from .ignition_base import IgnitionBase
    from .ignition_base_type import IgnitionBaseType
    from .index_range import IndexRange
    from .kinetic import Kinetic
    from .lighting_base import LightingBase
    from .lighting_base_light_item import LightingBaseLightItem
    from .lighting_base_turn_item import LightingBaseTurnItem
    from .lighting_system import LightingSystem
    from .lighting_system_base import LightingSystemBase
    from .lights import Lights
    from .lights_item import LightsItem
    from .lights_item_direction import LightsItemDirection
    from .lights_item_position import LightsItemPosition
    from .link import Link
    from .lite_energy import LiteEnergy
    from .load_electric_energy import LoadElectricEnergy
    from .luminosity import Luminosity
    from .luminosity_base import LuminosityBase
    from .maintenance import Maintenance
    from .maintenance_base import MaintenanceBase
    from .maintenance_links import MaintenanceLinks
    from .maintenance_list import MaintenanceList
    from .maintenance_list_embedded import MaintenanceListEmbedded
    from .maintenance_obj import MaintenanceObj
    from .monitor import Monitor
    from .monitor_callback_subscribe import MonitorCallbackSubscribe
    from .monitor_id import MonitorId
    from .monitor_links import MonitorLinks
    from .monitor_parameter import MonitorParameter
    from .monitor_parameter_extended_event_param_item import MonitorParameterExtendedEventParamItem
    from .monitor_parameter_trigger_param import MonitorParameterTriggerParam
    from .monitor_ref import MonitorRef
    from .monitor_ref_links import MonitorRefLinks
    from .monitor_status import MonitorStatus
    from .monitor_trigger import MonitorTrigger
    from .monitors import Monitors
    from .monitors_embedded import MonitorsEmbedded
    from .onboard_capabilities import OnboardCapabilities
    from .onboard_capabilities_data_item import OnboardCapabilitiesDataItem
    from .onboard_capabilities_remote import OnboardCapabilitiesRemote
    from .onboard_capabilities_remote_charging import OnboardCapabilitiesRemoteCharging
    from .onboard_capabilities_remote_charging_parameters import OnboardCapabilitiesRemoteChargingParameters
    from .onboard_capabilities_remote_charging_parameters_immediate import (
        OnboardCapabilitiesRemoteChargingParametersImmediate,
    )
    from .onboard_capabilities_remote_charging_parameters_preferences import (
        OnboardCapabilitiesRemoteChargingParametersPreferences,
    )
    from .onboard_capabilities_remote_charging_parameters_schedule import (
        OnboardCapabilitiesRemoteChargingParametersSchedule,
    )
    from .onboard_capabilities_remote_charging_parameters_schedule_programs import (
        OnboardCapabilitiesRemoteChargingParametersSchedulePrograms,
    )
    from .onboard_capabilities_remote_charging_scope_name import OnboardCapabilitiesRemoteChargingScopeName
    from .onboard_capabilities_remote_door import OnboardCapabilitiesRemoteDoor
    from .onboard_capabilities_remote_door_scope_name import OnboardCapabilitiesRemoteDoorScopeName
    from .onboard_capabilities_remote_horn import OnboardCapabilitiesRemoteHorn
    from .onboard_capabilities_remote_horn_scope_name import OnboardCapabilitiesRemoteHornScopeName
    from .onboard_capabilities_remote_lights import OnboardCapabilitiesRemoteLights
    from .onboard_capabilities_remote_lights_scope_name import OnboardCapabilitiesRemoteLightsScopeName
    from .onboard_capabilities_remote_navigation import OnboardCapabilitiesRemoteNavigation
    from .onboard_capabilities_remote_navigation_scope_name import OnboardCapabilitiesRemoteNavigationScopeName
    from .onboard_capabilities_remote_preconditioning import OnboardCapabilitiesRemotePreconditioning
    from .onboard_capabilities_remote_preconditioning_parameters import (
        OnboardCapabilitiesRemotePreconditioningParameters,
    )
    from .onboard_capabilities_remote_preconditioning_parameters_programs import (
        OnboardCapabilitiesRemotePreconditioningParametersPrograms,
    )
    from .onboard_capabilities_remote_preconditioning_scope_name import (
        OnboardCapabilitiesRemotePreconditioningScopeName,
    )
    from .onboard_capabilities_remote_stolen import OnboardCapabilitiesRemoteStolen
    from .onboard_capabilities_remote_wakeup import OnboardCapabilitiesRemoteWakeup
    from .onboard_capabilities_remote_wakeup_scope_name import OnboardCapabilitiesRemoteWakeupScopeName
    from .point import Point
    from .point_type import PointType
    from .position import Position
    from .position_base import PositionBase
    from .position_base_properties import PositionBaseProperties
    from .position_base_properties_fix_status import PositionBasePropertiesFixStatus
    from .position_base_properties_type import PositionBasePropertiesType
    from .position_base_type import PositionBaseType
    from .position_properties import PositionProperties
    from .position_properties_fix_status import PositionPropertiesFixStatus
    from .position_properties_type import PositionPropertiesType
    from .position_type import PositionType
    from .powertrain import Powertrain
    from .powertrain_base import PowertrainBase
    from .powertrain_base_status import PowertrainBaseStatus
    from .preconditioning import Preconditioning
    from .preconditioning_air_conditioning import PreconditioningAirConditioning
    from .preconditioning_air_conditioning_failure_cause import PreconditioningAirConditioningFailureCause
    from .preconditioning_air_conditioning_starting_cause import PreconditioningAirConditioningStartingCause
    from .preconditioning_air_conditioning_status import PreconditioningAirConditioningStatus
    from .preconditioning_base import PreconditioningBase
    from .preconditioning_base_air_conditioning import PreconditioningBaseAirConditioning
    from .preconditioning_base_air_conditioning_failure_cause import PreconditioningBaseAirConditioningFailureCause
    from .preconditioning_base_air_conditioning_starting_cause import PreconditioningBaseAirConditioningStartingCause
    from .preconditioning_base_air_conditioning_status import PreconditioningBaseAirConditioningStatus
    from .preconditioning_program import PreconditioningProgram
    from .privacy import Privacy
    from .privacy_base import PrivacyBase
    from .privacy_base_state import PrivacyBaseState
    from .program import Program
    from .program_occurence import ProgramOccurence
    from .program_occurence_day_item import ProgramOccurenceDayItem
    from .program_recurrence import ProgramRecurrence
    from .range import Range
    from .remote import Remote
    from .remote_action import RemoteAction
    from .remote_action_id import RemoteActionId
    from .remote_action_links import RemoteActionLinks
    from .remote_action_status import RemoteActionStatus
    from .remote_actions import RemoteActions
    from .remote_actions_embedded import RemoteActionsEmbedded
    from .remote_attribute import RemoteAttribute
    from .remote_attribute_set import RemoteAttributeSet
    from .remote_attribute_value import RemoteAttributeValue
    from .remote_attribute_value_one import RemoteAttributeValueOne
    from .remote_callback import RemoteCallback
    from .remote_callback_id import RemoteCallbackId
    from .remote_callback_links import RemoteCallbackLinks
    from .remote_callback_subscribe import RemoteCallbackSubscribe
    from .remote_callback_subscribe_callback import RemoteCallbackSubscribeCallback
    from .remote_callback_subscribe_callback_webhook import RemoteCallbackSubscribeCallbackWebhook
    from .remote_callback_subscribe_retry_policy import RemoteCallbackSubscribeRetryPolicy
    from .remote_callback_subscribe_retry_policy_policy import RemoteCallbackSubscribeRetryPolicyPolicy
    from .remote_callbacks import RemoteCallbacks
    from .remote_callbacks_embedded import RemoteCallbacksEmbedded
    from .remote_charging import RemoteCharging
    from .remote_charging_preferences import RemoteChargingPreferences
    from .remote_charging_preferences_level import RemoteChargingPreferencesLevel
    from .remote_charging_preferences_type import RemoteChargingPreferencesType
    from .remote_charging_schedule import RemoteChargingSchedule
    from .remote_charging_schedule_programs_item import RemoteChargingScheduleProgramsItem
    from .remote_doors_state import RemoteDoorsState
    from .remote_doors_state_state import RemoteDoorsStateState
    from .remote_event_feedback_detail import RemoteEventFeedbackDetail
    from .remote_failed_event_status import RemoteFailedEventStatus
    from .remote_horn import RemoteHorn
    from .remote_horn_state import RemoteHornState
    from .remote_lights import RemoteLights
    from .remote_navigation import RemoteNavigation
    from .remote_post_response import RemotePostResponse
    from .remote_post_response_links import RemotePostResponseLinks
    from .remote_preconditioning import RemotePreconditioning
    from .remote_preconditioning_air_conditioning import RemotePreconditioningAirConditioning
    from .remote_preconditioning_air_conditioning_programs_item import RemotePreconditioningAirConditioningProgramsItem
    from .remote_preconditioning_air_conditioning_programs_item_actions_type import (
        RemotePreconditioningAirConditioningProgramsItemActionsType,
    )
    from .remote_ref import RemoteRef
    from .remote_set_immobilization import RemoteSetImmobilization
    from .remote_stolen import RemoteStolen
    from .remote_stolen_immobilization import RemoteStolenImmobilization
    from .remote_stolen_tracking_period import RemoteStolenTrackingPeriod
    from .remote_type import RemoteType
    from .remote_types import RemoteTypes
    from .remote_wake_up import RemoteWakeUp
    from .safety import Safety
    from .service_type import ServiceType
    from .service_type_type import ServiceTypeType
    from .status import Status
    from .status_embedded import StatusEmbedded
    from .status_links import StatusLinks
    from .status_list import StatusList
    from .status_list_embedded import StatusListEmbedded
    from .stolen import Stolen
    from .stolen_base import StolenBase
    from .stolen_base_end_position import StolenBaseEndPosition
    from .stolen_base_end_position_properties import StolenBaseEndPositionProperties
    from .stolen_base_end_position_properties_fix_status import StolenBaseEndPositionPropertiesFixStatus
    from .stolen_base_end_position_properties_type import StolenBaseEndPositionPropertiesType
    from .stolen_base_end_position_type import StolenBaseEndPositionType
    from .stolen_base_links import StolenBaseLinks
    from .stolen_base_start_position import StolenBaseStartPosition
    from .stolen_base_start_position_properties import StolenBaseStartPositionProperties
    from .stolen_base_start_position_properties_fix_status import StolenBaseStartPositionPropertiesFixStatus
    from .stolen_base_start_position_properties_type import StolenBaseStartPositionPropertiesType
    from .stolen_base_start_position_type import StolenBaseStartPositionType
    from .stolen_collection import StolenCollection
    from .stolen_collection_embedded import StolenCollectionEmbedded
    from .stolen_obj import StolenObj
    from .tab_links import TabLinks
    from .telemetries import Telemetries
    from .telemetries_embedded import TelemetriesEmbedded
    from .telemetry import Telemetry
    from .telemetry_embedded import TelemetryEmbedded
    from .telemetry_enum import TelemetryEnum
    from .telemetry_enum_item import TelemetryEnumItem
    from .telemetry_extension import TelemetryExtension
    from .telemetry_extension_type import TelemetryExtensionType
    from .telemetry_extension_type_item import TelemetryExtensionTypeItem
    from .telemetry_links import TelemetryLinks
    from .telemetry_vehicle import TelemetryVehicle
    from .telemetry_vehicle_odometer import TelemetryVehicleOdometer
    from .time_trigger import TimeTrigger
    from .time_trigger_entry import TimeTriggerEntry
    from .time_trigger_entry_occurence import TimeTriggerEntryOccurence
    from .time_trigger_entry_occurence_day_item import TimeTriggerEntryOccurenceDayItem
    from .transmission import Transmission
    from .transmission_gearbox import TransmissionGearbox
    from .transmission_gearbox_mode import TransmissionGearboxMode
    from .transmission_gearbox_ratio import TransmissionGearboxRatio
    from .trip import Trip
    from .trip_faults_item import TripFaultsItem
    from .trip_faults_item_cause import TripFaultsItemCause
    from .trip_faults_item_fault import TripFaultsItemFault
    from .trip_kinetic import TripKinetic
    from .trip_links import TripLinks
    from .trip_segment import TripSegment
    from .trip_segment_propulsion import TripSegmentPropulsion
    from .trip_state_enum import TripStateEnum
    from .trip_state_enum_array import TripStateEnumArray
    from .trips import Trips
    from .trips_embedded import TripsEmbedded
    from .updated_at_field import UpdatedAtField
    from .url import Url
    from .vehicle import Vehicle
    from .vehicle_branding import VehicleBranding
    from .vehicle_branding_single import VehicleBrandingSingle
    from .vehicle_capabilities import VehicleCapabilities
    from .vehicle_capabilities_embedded import VehicleCapabilitiesEmbedded
    from .vehicle_capabilities_motorization import VehicleCapabilitiesMotorization
    from .vehicle_embedded import VehicleEmbedded
    from .vehicle_extension import VehicleExtension
    from .vehicle_extension_type import VehicleExtensionType
    from .vehicle_extension_type_item import VehicleExtensionTypeItem
    from .vehicle_extensions import VehicleExtensions
    from .vehicle_item import VehicleItem
    from .vehicle_item_embedded import VehicleItemEmbedded
    from .vehicle_item_links import VehicleItemLinks
    from .vehicle_item_motorization import VehicleItemMotorization
    from .vehicle_links import VehicleLinks
    from .vehicle_motorization import VehicleMotorization
    from .vehicle_odometer import VehicleOdometer
    from .vehicle_pictures import VehiclePictures
    from .vehicle_status_alarm import VehicleStatusAlarm
    from .vehicles import Vehicles
    from .vehicles_embedded import VehiclesEmbedded
    from .vehicles_extension_type import VehiclesExtensionType
    from .vehicles_extension_type_item import VehiclesExtensionTypeItem
    from .vin import Vin
    from .way_points import WayPoints
    from .way_points_embedded import WayPointsEmbedded
    from .webhook import Webhook
    from .wiping_blades_state import WipingBladesState
    from .wiping_blades_state_base import WipingBladesStateBase
    from .wiping_blades_state_base_speed import WipingBladesStateBaseSpeed
    from .x_error import XError
    from .zone_trigger import ZoneTrigger
    from .zone_trigger_place import ZoneTriggerPlace
    from .zone_trigger_place_center import ZoneTriggerPlaceCenter
    from .zone_trigger_transition import ZoneTriggerTransition
_dynamic_imports: typing.Dict[str, str] = {
    "Adas": ".adas",
    "AdasArtiv": ".adas_artiv",
    "AdasBsm": ".adas_bsm",
    "AdasLlka": ".adas_llka",
    "AdasParkAssist": ".adas_park_assist",
    "AdasParkAssistFrontItem": ".adas_park_assist_front_item",
    "AdasParkAssistRearItem": ".adas_park_assist_rear_item",
    "AdasRgi": ".adas_rgi",
    "AdasRlka": ".adas_rlka",
    "Air": ".air",
    "AirBase": ".air_base",
    "Alarm": ".alarm",
    "AlarmDetails": ".alarm_details",
    "AlarmStatus": ".alarm_status",
    "AlarmTrigger": ".alarm_trigger",
    "AlarmTypeEnum": ".alarm_type_enum",
    "AlarmTypeEnumItem": ".alarm_type_enum_item",
    "Alarms": ".alarms",
    "AlarmsEmbedded": ".alarms_embedded",
    "Alert": ".alert",
    "AlertEndPosition": ".alert_end_position",
    "AlertEndPositionProperties": ".alert_end_position_properties",
    "AlertEndPositionPropertiesFixStatus": ".alert_end_position_properties_fix_status",
    "AlertEndPositionPropertiesType": ".alert_end_position_properties_type",
    "AlertEndPositionType": ".alert_end_position_type",
    "AlertLinks": ".alert_links",
    "AlertMsgEnum": ".alert_msg_enum",
    "AlertSeverity": ".alert_severity",
    "AlertStartPosition": ".alert_start_position",
    "AlertStartPositionProperties": ".alert_start_position_properties",
    "AlertStartPositionPropertiesFixStatus": ".alert_start_position_properties_fix_status",
    "AlertStartPositionPropertiesType": ".alert_start_position_properties_type",
    "AlertStartPositionType": ".alert_start_position_type",
    "Alerts": ".alerts",
    "AlertsEmbedded": ".alerts_embedded",
    "Attribute": ".attribute",
    "AttributeSet": ".attribute_set",
    "AttributeType": ".attribute_type",
    "AttributeValue": ".attribute_value",
    "AttributeValueOne": ".attribute_value_one",
    "BaseAlarm": ".base_alarm",
    "BaseAlarmStatus": ".base_alarm_status",
    "BaseAlarmStatusActivation": ".base_alarm_status_activation",
    "BaseAlarmTrigger": ".base_alarm_trigger",
    "BaseAlarmTriggerPosition": ".base_alarm_trigger_position",
    "BaseAlarmTriggerPositionProperties": ".base_alarm_trigger_position_properties",
    "BaseAlarmTriggerPositionPropertiesFixStatus": ".base_alarm_trigger_position_properties_fix_status",
    "BaseAlarmTriggerPositionPropertiesType": ".base_alarm_trigger_position_properties_type",
    "BaseAlarmTriggerPositionType": ".base_alarm_trigger_position_type",
    "BaseAlarmTriggerType": ".base_alarm_trigger_type",
    "BaseSafety": ".base_safety",
    "BaseSafetyAutoECallTriggering": ".base_safety_auto_e_call_triggering",
    "BasicKinetic": ".basic_kinetic",
    "BasicProgram": ".basic_program",
    "BasicProgramOccurence": ".basic_program_occurence",
    "BasicProgramOccurenceDayItem": ".basic_program_occurence_day_item",
    "Battery": ".battery",
    "BatteryBase": ".battery_base",
    "BeltStatus": ".belt_status",
    "BeltStatusBelt": ".belt_status_belt",
    "BeltStatusId": ".belt_status_id",
    "CallbackRef": ".callback_ref",
    "CallbackRefLinks": ".callback_ref_links",
    "CallbackStatus": ".callback_status",
    "CallbackSubscribe": ".callback_subscribe",
    "CallbackSubscribeBatchNotify": ".callback_subscribe_batch_notify",
    "CallbackSubscribeCallback": ".callback_subscribe_callback",
    "CallbackSubscribeRetryPolicy": ".callback_subscribe_retry_policy",
    "CallbackSubscribeRetryPolicyPolicy": ".callback_subscribe_retry_policy_policy",
    "ChargeScheduleProgram": ".charge_schedule_program",
    "ChargingStatusEnum": ".charging_status_enum",
    "CollectionResult": ".collection_result",
    "Collision": ".collision",
    "CollisionDetails": ".collision_details",
    "CollisionDetailsSeverity": ".collision_details_severity",
    "CollisionDetailsSide": ".collision_details_side",
    "CollisionLinks": ".collision_links",
    "CollisionObj": ".collision_obj",
    "Collisions": ".collisions",
    "CollisionsEmbedded": ".collisions_embedded",
    "CompositFuelEnergyConsumption": ".composit_fuel_energy_consumption",
    "Consumption": ".consumption",
    "CreatedAtField": ".created_at_field",
    "DataProfile": ".data_profile",
    "DataTrigger": ".data_trigger",
    "DataTriggerData": ".data_trigger_data",
    "DataTriggerOp": ".data_trigger_op",
    "DoorsState": ".doors_state",
    "DoorsStateBase": ".doors_state_base",
    "DoorsStateBaseLockedStatesItem": ".doors_state_base_locked_states_item",
    "DoorsStateBaseOpeningItem": ".doors_state_base_opening_item",
    "DoorsStateBaseOpeningItemIdentifier": ".doors_state_base_opening_item_identifier",
    "DoorsStateBaseOpeningItemState": ".doors_state_base_opening_item_state",
    "DrivingBehavior": ".driving_behavior",
    "DrivingBehaviorBase": ".driving_behavior_base",
    "DrivingBehaviorBaseMode": ".driving_behavior_base_mode",
    "ECoaching": ".e_coaching",
    "ECoachingLinks": ".e_coaching_links",
    "ECoachingScoresItem": ".e_coaching_scores_item",
    "ECoachingScoresItemCategory": ".e_coaching_scores_item_category",
    "Energy": ".energy",
    "EnergyBase": ".energy_base",
    "EnergyBaseExtension": ".energy_base_extension",
    "EnergyBaseExtensionElectric": ".energy_base_extension_electric",
    "EnergyBaseExtensionFuel": ".energy_base_extension_fuel",
    "EnergyBaseSubType": ".energy_base_sub_type",
    "EnergyBaseType": ".energy_base_type",
    "EnergyBattery": ".energy_battery",
    "EnergyBatteryBase": ".energy_battery_base",
    "EnergyBatteryHealth": ".energy_battery_health",
    "EnergyBatteryLoad": ".energy_battery_load",
    "EnergyCharging": ".energy_charging",
    "EnergyChargingChargingPowerLevel": ".energy_charging_charging_power_level",
    "EnergyChargingSchedule": ".energy_charging_schedule",
    "EnergyChargingType": ".energy_charging_type",
    "EnergyConsumption": ".energy_consumption",
    "EnergyExtension": ".energy_extension",
    "EnergyExtensionElectric": ".energy_extension_electric",
    "EnergyExtensionFuel": ".energy_extension_fuel",
    "EnergySubType": ".energy_sub_type",
    "EnergyType": ".energy_type",
    "Engine": ".engine",
    "EngineAir": ".engine_air",
    "EngineBase": ".engine_base",
    "EngineBaseExtension": ".engine_base_extension",
    "EngineBaseExtensionThermic": ".engine_base_extension_thermic",
    "EngineBaseExtensionThermicCoolant": ".engine_base_extension_thermic_coolant",
    "EngineBaseExtensionThermicOil": ".engine_base_extension_thermic_oil",
    "EngineBaseGmpStatus": ".engine_base_gmp_status",
    "EngineBaseType": ".engine_base_type",
    "EngineLiquid": ".engine_liquid",
    "Environment": ".environment",
    "EnvironmentBase": ".environment_base",
    "Extension": ".extension",
    "Fleet": ".fleet",
    "FleetLinks": ".fleet_links",
    "Fleets": ".fleets",
    "FleetsEmbedded": ".fleets_embedded",
    "Geometry": ".geometry",
    "HealthElectricEnergy": ".health_electric_energy",
    "Ignition": ".ignition",
    "IgnitionBase": ".ignition_base",
    "IgnitionBaseType": ".ignition_base_type",
    "IndexRange": ".index_range",
    "Kinetic": ".kinetic",
    "LightingBase": ".lighting_base",
    "LightingBaseLightItem": ".lighting_base_light_item",
    "LightingBaseTurnItem": ".lighting_base_turn_item",
    "LightingSystem": ".lighting_system",
    "LightingSystemBase": ".lighting_system_base",
    "Lights": ".lights",
    "LightsItem": ".lights_item",
    "LightsItemDirection": ".lights_item_direction",
    "LightsItemPosition": ".lights_item_position",
    "Link": ".link",
    "LiteEnergy": ".lite_energy",
    "LoadElectricEnergy": ".load_electric_energy",
    "Luminosity": ".luminosity",
    "LuminosityBase": ".luminosity_base",
    "Maintenance": ".maintenance",
    "MaintenanceBase": ".maintenance_base",
    "MaintenanceLinks": ".maintenance_links",
    "MaintenanceList": ".maintenance_list",
    "MaintenanceListEmbedded": ".maintenance_list_embedded",
    "MaintenanceObj": ".maintenance_obj",
    "Monitor": ".monitor",
    "MonitorCallbackSubscribe": ".monitor_callback_subscribe",
    "MonitorId": ".monitor_id",
    "MonitorLinks": ".monitor_links",
    "MonitorParameter": ".monitor_parameter",
    "MonitorParameterExtendedEventParamItem": ".monitor_parameter_extended_event_param_item",
    "MonitorParameterTriggerParam": ".monitor_parameter_trigger_param",
    "MonitorRef": ".monitor_ref",
    "MonitorRefLinks": ".monitor_ref_links",
    "MonitorStatus": ".monitor_status",
    "MonitorTrigger": ".monitor_trigger",
    "Monitors": ".monitors",
    "MonitorsEmbedded": ".monitors_embedded",
    "OnboardCapabilities": ".onboard_capabilities",
    "OnboardCapabilitiesDataItem": ".onboard_capabilities_data_item",
    "OnboardCapabilitiesRemote": ".onboard_capabilities_remote",
    "OnboardCapabilitiesRemoteCharging": ".onboard_capabilities_remote_charging",
    "OnboardCapabilitiesRemoteChargingParameters": ".onboard_capabilities_remote_charging_parameters",
    "OnboardCapabilitiesRemoteChargingParametersImmediate": ".onboard_capabilities_remote_charging_parameters_immediate",
    "OnboardCapabilitiesRemoteChargingParametersPreferences": ".onboard_capabilities_remote_charging_parameters_preferences",
    "OnboardCapabilitiesRemoteChargingParametersSchedule": ".onboard_capabilities_remote_charging_parameters_schedule",
    "OnboardCapabilitiesRemoteChargingParametersSchedulePrograms": ".onboard_capabilities_remote_charging_parameters_schedule_programs",
    "OnboardCapabilitiesRemoteChargingScopeName": ".onboard_capabilities_remote_charging_scope_name",
    "OnboardCapabilitiesRemoteDoor": ".onboard_capabilities_remote_door",
    "OnboardCapabilitiesRemoteDoorScopeName": ".onboard_capabilities_remote_door_scope_name",
    "OnboardCapabilitiesRemoteHorn": ".onboard_capabilities_remote_horn",
    "OnboardCapabilitiesRemoteHornScopeName": ".onboard_capabilities_remote_horn_scope_name",
    "OnboardCapabilitiesRemoteLights": ".onboard_capabilities_remote_lights",
    "OnboardCapabilitiesRemoteLightsScopeName": ".onboard_capabilities_remote_lights_scope_name",
    "OnboardCapabilitiesRemoteNavigation": ".onboard_capabilities_remote_navigation",
    "OnboardCapabilitiesRemoteNavigationScopeName": ".onboard_capabilities_remote_navigation_scope_name",
    "OnboardCapabilitiesRemotePreconditioning": ".onboard_capabilities_remote_preconditioning",
    "OnboardCapabilitiesRemotePreconditioningParameters": ".onboard_capabilities_remote_preconditioning_parameters",
    "OnboardCapabilitiesRemotePreconditioningParametersPrograms": ".onboard_capabilities_remote_preconditioning_parameters_programs",
    "OnboardCapabilitiesRemotePreconditioningScopeName": ".onboard_capabilities_remote_preconditioning_scope_name",
    "OnboardCapabilitiesRemoteStolen": ".onboard_capabilities_remote_stolen",
    "OnboardCapabilitiesRemoteWakeup": ".onboard_capabilities_remote_wakeup",
    "OnboardCapabilitiesRemoteWakeupScopeName": ".onboard_capabilities_remote_wakeup_scope_name",
    "Point": ".point",
    "PointType": ".point_type",
    "Position": ".position",
    "PositionBase": ".position_base",
    "PositionBaseProperties": ".position_base_properties",
    "PositionBasePropertiesFixStatus": ".position_base_properties_fix_status",
    "PositionBasePropertiesType": ".position_base_properties_type",
    "PositionBaseType": ".position_base_type",
    "PositionProperties": ".position_properties",
    "PositionPropertiesFixStatus": ".position_properties_fix_status",
    "PositionPropertiesType": ".position_properties_type",
    "PositionType": ".position_type",
    "Powertrain": ".powertrain",
    "PowertrainBase": ".powertrain_base",
    "PowertrainBaseStatus": ".powertrain_base_status",
    "Preconditioning": ".preconditioning",
    "PreconditioningAirConditioning": ".preconditioning_air_conditioning",
    "PreconditioningAirConditioningFailureCause": ".preconditioning_air_conditioning_failure_cause",
    "PreconditioningAirConditioningStartingCause": ".preconditioning_air_conditioning_starting_cause",
    "PreconditioningAirConditioningStatus": ".preconditioning_air_conditioning_status",
    "PreconditioningBase": ".preconditioning_base",
    "PreconditioningBaseAirConditioning": ".preconditioning_base_air_conditioning",
    "PreconditioningBaseAirConditioningFailureCause": ".preconditioning_base_air_conditioning_failure_cause",
    "PreconditioningBaseAirConditioningStartingCause": ".preconditioning_base_air_conditioning_starting_cause",
    "PreconditioningBaseAirConditioningStatus": ".preconditioning_base_air_conditioning_status",
    "PreconditioningProgram": ".preconditioning_program",
    "Privacy": ".privacy",
    "PrivacyBase": ".privacy_base",
    "PrivacyBaseState": ".privacy_base_state",
    "Program": ".program",
    "ProgramOccurence": ".program_occurence",
    "ProgramOccurenceDayItem": ".program_occurence_day_item",
    "ProgramRecurrence": ".program_recurrence",
    "Range": ".range",
    "Remote": ".remote",
    "RemoteAction": ".remote_action",
    "RemoteActionId": ".remote_action_id",
    "RemoteActionLinks": ".remote_action_links",
    "RemoteActionStatus": ".remote_action_status",
    "RemoteActions": ".remote_actions",
    "RemoteActionsEmbedded": ".remote_actions_embedded",
    "RemoteAttribute": ".remote_attribute",
    "RemoteAttributeSet": ".remote_attribute_set",
    "RemoteAttributeValue": ".remote_attribute_value",
    "RemoteAttributeValueOne": ".remote_attribute_value_one",
    "RemoteCallback": ".remote_callback",
    "RemoteCallbackId": ".remote_callback_id",
    "RemoteCallbackLinks": ".remote_callback_links",
    "RemoteCallbackSubscribe": ".remote_callback_subscribe",
    "RemoteCallbackSubscribeCallback": ".remote_callback_subscribe_callback",
    "RemoteCallbackSubscribeCallbackWebhook": ".remote_callback_subscribe_callback_webhook",
    "RemoteCallbackSubscribeRetryPolicy": ".remote_callback_subscribe_retry_policy",
    "RemoteCallbackSubscribeRetryPolicyPolicy": ".remote_callback_subscribe_retry_policy_policy",
    "RemoteCallbacks": ".remote_callbacks",
    "RemoteCallbacksEmbedded": ".remote_callbacks_embedded",
    "RemoteCharging": ".remote_charging",
    "RemoteChargingPreferences": ".remote_charging_preferences",
    "RemoteChargingPreferencesLevel": ".remote_charging_preferences_level",
    "RemoteChargingPreferencesType": ".remote_charging_preferences_type",
    "RemoteChargingSchedule": ".remote_charging_schedule",
    "RemoteChargingScheduleProgramsItem": ".remote_charging_schedule_programs_item",
    "RemoteDoorsState": ".remote_doors_state",
    "RemoteDoorsStateState": ".remote_doors_state_state",
    "RemoteEventFeedbackDetail": ".remote_event_feedback_detail",
    "RemoteFailedEventStatus": ".remote_failed_event_status",
    "RemoteHorn": ".remote_horn",
    "RemoteHornState": ".remote_horn_state",
    "RemoteLights": ".remote_lights",
    "RemoteNavigation": ".remote_navigation",
    "RemotePostResponse": ".remote_post_response",
    "RemotePostResponseLinks": ".remote_post_response_links",
    "RemotePreconditioning": ".remote_preconditioning",
    "RemotePreconditioningAirConditioning": ".remote_preconditioning_air_conditioning",
    "RemotePreconditioningAirConditioningProgramsItem": ".remote_preconditioning_air_conditioning_programs_item",
    "RemotePreconditioningAirConditioningProgramsItemActionsType": ".remote_preconditioning_air_conditioning_programs_item_actions_type",
    "RemoteRef": ".remote_ref",
    "RemoteSetImmobilization": ".remote_set_immobilization",
    "RemoteStolen": ".remote_stolen",
    "RemoteStolenImmobilization": ".remote_stolen_immobilization",
    "RemoteStolenTrackingPeriod": ".remote_stolen_tracking_period",
    "RemoteType": ".remote_type",
    "RemoteTypes": ".remote_types",
    "RemoteWakeUp": ".remote_wake_up",
    "Safety": ".safety",
    "ServiceType": ".service_type",
    "ServiceTypeType": ".service_type_type",
    "Status": ".status",
    "StatusEmbedded": ".status_embedded",
    "StatusLinks": ".status_links",
    "StatusList": ".status_list",
    "StatusListEmbedded": ".status_list_embedded",
    "Stolen": ".stolen",
    "StolenBase": ".stolen_base",
    "StolenBaseEndPosition": ".stolen_base_end_position",
    "StolenBaseEndPositionProperties": ".stolen_base_end_position_properties",
    "StolenBaseEndPositionPropertiesFixStatus": ".stolen_base_end_position_properties_fix_status",
    "StolenBaseEndPositionPropertiesType": ".stolen_base_end_position_properties_type",
    "StolenBaseEndPositionType": ".stolen_base_end_position_type",
    "StolenBaseLinks": ".stolen_base_links",
    "StolenBaseStartPosition": ".stolen_base_start_position",
    "StolenBaseStartPositionProperties": ".stolen_base_start_position_properties",
    "StolenBaseStartPositionPropertiesFixStatus": ".stolen_base_start_position_properties_fix_status",
    "StolenBaseStartPositionPropertiesType": ".stolen_base_start_position_properties_type",
    "StolenBaseStartPositionType": ".stolen_base_start_position_type",
    "StolenCollection": ".stolen_collection",
    "StolenCollectionEmbedded": ".stolen_collection_embedded",
    "StolenObj": ".stolen_obj",
    "TabLinks": ".tab_links",
    "Telemetries": ".telemetries",
    "TelemetriesEmbedded": ".telemetries_embedded",
    "Telemetry": ".telemetry",
    "TelemetryEmbedded": ".telemetry_embedded",
    "TelemetryEnum": ".telemetry_enum",
    "TelemetryEnumItem": ".telemetry_enum_item",
    "TelemetryExtension": ".telemetry_extension",
    "TelemetryExtensionType": ".telemetry_extension_type",
    "TelemetryExtensionTypeItem": ".telemetry_extension_type_item",
    "TelemetryLinks": ".telemetry_links",
    "TelemetryVehicle": ".telemetry_vehicle",
    "TelemetryVehicleOdometer": ".telemetry_vehicle_odometer",
    "TimeTrigger": ".time_trigger",
    "TimeTriggerEntry": ".time_trigger_entry",
    "TimeTriggerEntryOccurence": ".time_trigger_entry_occurence",
    "TimeTriggerEntryOccurenceDayItem": ".time_trigger_entry_occurence_day_item",
    "Transmission": ".transmission",
    "TransmissionGearbox": ".transmission_gearbox",
    "TransmissionGearboxMode": ".transmission_gearbox_mode",
    "TransmissionGearboxRatio": ".transmission_gearbox_ratio",
    "Trip": ".trip",
    "TripFaultsItem": ".trip_faults_item",
    "TripFaultsItemCause": ".trip_faults_item_cause",
    "TripFaultsItemFault": ".trip_faults_item_fault",
    "TripKinetic": ".trip_kinetic",
    "TripLinks": ".trip_links",
    "TripSegment": ".trip_segment",
    "TripSegmentPropulsion": ".trip_segment_propulsion",
    "TripStateEnum": ".trip_state_enum",
    "TripStateEnumArray": ".trip_state_enum_array",
    "Trips": ".trips",
    "TripsEmbedded": ".trips_embedded",
    "UpdatedAtField": ".updated_at_field",
    "Url": ".url",
    "Vehicle": ".vehicle",
    "VehicleBranding": ".vehicle_branding",
    "VehicleBrandingSingle": ".vehicle_branding_single",
    "VehicleCapabilities": ".vehicle_capabilities",
    "VehicleCapabilitiesEmbedded": ".vehicle_capabilities_embedded",
    "VehicleCapabilitiesMotorization": ".vehicle_capabilities_motorization",
    "VehicleEmbedded": ".vehicle_embedded",
    "VehicleExtension": ".vehicle_extension",
    "VehicleExtensionType": ".vehicle_extension_type",
    "VehicleExtensionTypeItem": ".vehicle_extension_type_item",
    "VehicleExtensions": ".vehicle_extensions",
    "VehicleItem": ".vehicle_item",
    "VehicleItemEmbedded": ".vehicle_item_embedded",
    "VehicleItemLinks": ".vehicle_item_links",
    "VehicleItemMotorization": ".vehicle_item_motorization",
    "VehicleLinks": ".vehicle_links",
    "VehicleMotorization": ".vehicle_motorization",
    "VehicleOdometer": ".vehicle_odometer",
    "VehiclePictures": ".vehicle_pictures",
    "VehicleStatusAlarm": ".vehicle_status_alarm",
    "Vehicles": ".vehicles",
    "VehiclesEmbedded": ".vehicles_embedded",
    "VehiclesExtensionType": ".vehicles_extension_type",
    "VehiclesExtensionTypeItem": ".vehicles_extension_type_item",
    "Vin": ".vin",
    "WayPoints": ".way_points",
    "WayPointsEmbedded": ".way_points_embedded",
    "Webhook": ".webhook",
    "WipingBladesState": ".wiping_blades_state",
    "WipingBladesStateBase": ".wiping_blades_state_base",
    "WipingBladesStateBaseSpeed": ".wiping_blades_state_base_speed",
    "XError": ".x_error",
    "ZoneTrigger": ".zone_trigger",
    "ZoneTriggerPlace": ".zone_trigger_place",
    "ZoneTriggerPlaceCenter": ".zone_trigger_place_center",
    "ZoneTriggerTransition": ".zone_trigger_transition",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Adas",
    "AdasArtiv",
    "AdasBsm",
    "AdasLlka",
    "AdasParkAssist",
    "AdasParkAssistFrontItem",
    "AdasParkAssistRearItem",
    "AdasRgi",
    "AdasRlka",
    "Air",
    "AirBase",
    "Alarm",
    "AlarmDetails",
    "AlarmStatus",
    "AlarmTrigger",
    "AlarmTypeEnum",
    "AlarmTypeEnumItem",
    "Alarms",
    "AlarmsEmbedded",
    "Alert",
    "AlertEndPosition",
    "AlertEndPositionProperties",
    "AlertEndPositionPropertiesFixStatus",
    "AlertEndPositionPropertiesType",
    "AlertEndPositionType",
    "AlertLinks",
    "AlertMsgEnum",
    "AlertSeverity",
    "AlertStartPosition",
    "AlertStartPositionProperties",
    "AlertStartPositionPropertiesFixStatus",
    "AlertStartPositionPropertiesType",
    "AlertStartPositionType",
    "Alerts",
    "AlertsEmbedded",
    "Attribute",
    "AttributeSet",
    "AttributeType",
    "AttributeValue",
    "AttributeValueOne",
    "BaseAlarm",
    "BaseAlarmStatus",
    "BaseAlarmStatusActivation",
    "BaseAlarmTrigger",
    "BaseAlarmTriggerPosition",
    "BaseAlarmTriggerPositionProperties",
    "BaseAlarmTriggerPositionPropertiesFixStatus",
    "BaseAlarmTriggerPositionPropertiesType",
    "BaseAlarmTriggerPositionType",
    "BaseAlarmTriggerType",
    "BaseSafety",
    "BaseSafetyAutoECallTriggering",
    "BasicKinetic",
    "BasicProgram",
    "BasicProgramOccurence",
    "BasicProgramOccurenceDayItem",
    "Battery",
    "BatteryBase",
    "BeltStatus",
    "BeltStatusBelt",
    "BeltStatusId",
    "CallbackRef",
    "CallbackRefLinks",
    "CallbackStatus",
    "CallbackSubscribe",
    "CallbackSubscribeBatchNotify",
    "CallbackSubscribeCallback",
    "CallbackSubscribeRetryPolicy",
    "CallbackSubscribeRetryPolicyPolicy",
    "ChargeScheduleProgram",
    "ChargingStatusEnum",
    "CollectionResult",
    "Collision",
    "CollisionDetails",
    "CollisionDetailsSeverity",
    "CollisionDetailsSide",
    "CollisionLinks",
    "CollisionObj",
    "Collisions",
    "CollisionsEmbedded",
    "CompositFuelEnergyConsumption",
    "Consumption",
    "CreatedAtField",
    "DataProfile",
    "DataTrigger",
    "DataTriggerData",
    "DataTriggerOp",
    "DoorsState",
    "DoorsStateBase",
    "DoorsStateBaseLockedStatesItem",
    "DoorsStateBaseOpeningItem",
    "DoorsStateBaseOpeningItemIdentifier",
    "DoorsStateBaseOpeningItemState",
    "DrivingBehavior",
    "DrivingBehaviorBase",
    "DrivingBehaviorBaseMode",
    "ECoaching",
    "ECoachingLinks",
    "ECoachingScoresItem",
    "ECoachingScoresItemCategory",
    "Energy",
    "EnergyBase",
    "EnergyBaseExtension",
    "EnergyBaseExtensionElectric",
    "EnergyBaseExtensionFuel",
    "EnergyBaseSubType",
    "EnergyBaseType",
    "EnergyBattery",
    "EnergyBatteryBase",
    "EnergyBatteryHealth",
    "EnergyBatteryLoad",
    "EnergyCharging",
    "EnergyChargingChargingPowerLevel",
    "EnergyChargingSchedule",
    "EnergyChargingType",
    "EnergyConsumption",
    "EnergyExtension",
    "EnergyExtensionElectric",
    "EnergyExtensionFuel",
    "EnergySubType",
    "EnergyType",
    "Engine",
    "EngineAir",
    "EngineBase",
    "EngineBaseExtension",
    "EngineBaseExtensionThermic",
    "EngineBaseExtensionThermicCoolant",
    "EngineBaseExtensionThermicOil",
    "EngineBaseGmpStatus",
    "EngineBaseType",
    "EngineLiquid",
    "Environment",
    "EnvironmentBase",
    "Extension",
    "Fleet",
    "FleetLinks",
    "Fleets",
    "FleetsEmbedded",
    "Geometry",
    "HealthElectricEnergy",
    "Ignition",
    "IgnitionBase",
    "IgnitionBaseType",
    "IndexRange",
    "Kinetic",
    "LightingBase",
    "LightingBaseLightItem",
    "LightingBaseTurnItem",
    "LightingSystem",
    "LightingSystemBase",
    "Lights",
    "LightsItem",
    "LightsItemDirection",
    "LightsItemPosition",
    "Link",
    "LiteEnergy",
    "LoadElectricEnergy",
    "Luminosity",
    "LuminosityBase",
    "Maintenance",
    "MaintenanceBase",
    "MaintenanceLinks",
    "MaintenanceList",
    "MaintenanceListEmbedded",
    "MaintenanceObj",
    "Monitor",
    "MonitorCallbackSubscribe",
    "MonitorId",
    "MonitorLinks",
    "MonitorParameter",
    "MonitorParameterExtendedEventParamItem",
    "MonitorParameterTriggerParam",
    "MonitorRef",
    "MonitorRefLinks",
    "MonitorStatus",
    "MonitorTrigger",
    "Monitors",
    "MonitorsEmbedded",
    "OnboardCapabilities",
    "OnboardCapabilitiesDataItem",
    "OnboardCapabilitiesRemote",
    "OnboardCapabilitiesRemoteCharging",
    "OnboardCapabilitiesRemoteChargingParameters",
    "OnboardCapabilitiesRemoteChargingParametersImmediate",
    "OnboardCapabilitiesRemoteChargingParametersPreferences",
    "OnboardCapabilitiesRemoteChargingParametersSchedule",
    "OnboardCapabilitiesRemoteChargingParametersSchedulePrograms",
    "OnboardCapabilitiesRemoteChargingScopeName",
    "OnboardCapabilitiesRemoteDoor",
    "OnboardCapabilitiesRemoteDoorScopeName",
    "OnboardCapabilitiesRemoteHorn",
    "OnboardCapabilitiesRemoteHornScopeName",
    "OnboardCapabilitiesRemoteLights",
    "OnboardCapabilitiesRemoteLightsScopeName",
    "OnboardCapabilitiesRemoteNavigation",
    "OnboardCapabilitiesRemoteNavigationScopeName",
    "OnboardCapabilitiesRemotePreconditioning",
    "OnboardCapabilitiesRemotePreconditioningParameters",
    "OnboardCapabilitiesRemotePreconditioningParametersPrograms",
    "OnboardCapabilitiesRemotePreconditioningScopeName",
    "OnboardCapabilitiesRemoteStolen",
    "OnboardCapabilitiesRemoteWakeup",
    "OnboardCapabilitiesRemoteWakeupScopeName",
    "Point",
    "PointType",
    "Position",
    "PositionBase",
    "PositionBaseProperties",
    "PositionBasePropertiesFixStatus",
    "PositionBasePropertiesType",
    "PositionBaseType",
    "PositionProperties",
    "PositionPropertiesFixStatus",
    "PositionPropertiesType",
    "PositionType",
    "Powertrain",
    "PowertrainBase",
    "PowertrainBaseStatus",
    "Preconditioning",
    "PreconditioningAirConditioning",
    "PreconditioningAirConditioningFailureCause",
    "PreconditioningAirConditioningStartingCause",
    "PreconditioningAirConditioningStatus",
    "PreconditioningBase",
    "PreconditioningBaseAirConditioning",
    "PreconditioningBaseAirConditioningFailureCause",
    "PreconditioningBaseAirConditioningStartingCause",
    "PreconditioningBaseAirConditioningStatus",
    "PreconditioningProgram",
    "Privacy",
    "PrivacyBase",
    "PrivacyBaseState",
    "Program",
    "ProgramOccurence",
    "ProgramOccurenceDayItem",
    "ProgramRecurrence",
    "Range",
    "Remote",
    "RemoteAction",
    "RemoteActionId",
    "RemoteActionLinks",
    "RemoteActionStatus",
    "RemoteActions",
    "RemoteActionsEmbedded",
    "RemoteAttribute",
    "RemoteAttributeSet",
    "RemoteAttributeValue",
    "RemoteAttributeValueOne",
    "RemoteCallback",
    "RemoteCallbackId",
    "RemoteCallbackLinks",
    "RemoteCallbackSubscribe",
    "RemoteCallbackSubscribeCallback",
    "RemoteCallbackSubscribeCallbackWebhook",
    "RemoteCallbackSubscribeRetryPolicy",
    "RemoteCallbackSubscribeRetryPolicyPolicy",
    "RemoteCallbacks",
    "RemoteCallbacksEmbedded",
    "RemoteCharging",
    "RemoteChargingPreferences",
    "RemoteChargingPreferencesLevel",
    "RemoteChargingPreferencesType",
    "RemoteChargingSchedule",
    "RemoteChargingScheduleProgramsItem",
    "RemoteDoorsState",
    "RemoteDoorsStateState",
    "RemoteEventFeedbackDetail",
    "RemoteFailedEventStatus",
    "RemoteHorn",
    "RemoteHornState",
    "RemoteLights",
    "RemoteNavigation",
    "RemotePostResponse",
    "RemotePostResponseLinks",
    "RemotePreconditioning",
    "RemotePreconditioningAirConditioning",
    "RemotePreconditioningAirConditioningProgramsItem",
    "RemotePreconditioningAirConditioningProgramsItemActionsType",
    "RemoteRef",
    "RemoteSetImmobilization",
    "RemoteStolen",
    "RemoteStolenImmobilization",
    "RemoteStolenTrackingPeriod",
    "RemoteType",
    "RemoteTypes",
    "RemoteWakeUp",
    "Safety",
    "ServiceType",
    "ServiceTypeType",
    "Status",
    "StatusEmbedded",
    "StatusLinks",
    "StatusList",
    "StatusListEmbedded",
    "Stolen",
    "StolenBase",
    "StolenBaseEndPosition",
    "StolenBaseEndPositionProperties",
    "StolenBaseEndPositionPropertiesFixStatus",
    "StolenBaseEndPositionPropertiesType",
    "StolenBaseEndPositionType",
    "StolenBaseLinks",
    "StolenBaseStartPosition",
    "StolenBaseStartPositionProperties",
    "StolenBaseStartPositionPropertiesFixStatus",
    "StolenBaseStartPositionPropertiesType",
    "StolenBaseStartPositionType",
    "StolenCollection",
    "StolenCollectionEmbedded",
    "StolenObj",
    "TabLinks",
    "Telemetries",
    "TelemetriesEmbedded",
    "Telemetry",
    "TelemetryEmbedded",
    "TelemetryEnum",
    "TelemetryEnumItem",
    "TelemetryExtension",
    "TelemetryExtensionType",
    "TelemetryExtensionTypeItem",
    "TelemetryLinks",
    "TelemetryVehicle",
    "TelemetryVehicleOdometer",
    "TimeTrigger",
    "TimeTriggerEntry",
    "TimeTriggerEntryOccurence",
    "TimeTriggerEntryOccurenceDayItem",
    "Transmission",
    "TransmissionGearbox",
    "TransmissionGearboxMode",
    "TransmissionGearboxRatio",
    "Trip",
    "TripFaultsItem",
    "TripFaultsItemCause",
    "TripFaultsItemFault",
    "TripKinetic",
    "TripLinks",
    "TripSegment",
    "TripSegmentPropulsion",
    "TripStateEnum",
    "TripStateEnumArray",
    "Trips",
    "TripsEmbedded",
    "UpdatedAtField",
    "Url",
    "Vehicle",
    "VehicleBranding",
    "VehicleBrandingSingle",
    "VehicleCapabilities",
    "VehicleCapabilitiesEmbedded",
    "VehicleCapabilitiesMotorization",
    "VehicleEmbedded",
    "VehicleExtension",
    "VehicleExtensionType",
    "VehicleExtensionTypeItem",
    "VehicleExtensions",
    "VehicleItem",
    "VehicleItemEmbedded",
    "VehicleItemLinks",
    "VehicleItemMotorization",
    "VehicleLinks",
    "VehicleMotorization",
    "VehicleOdometer",
    "VehiclePictures",
    "VehicleStatusAlarm",
    "Vehicles",
    "VehiclesEmbedded",
    "VehiclesExtensionType",
    "VehiclesExtensionTypeItem",
    "Vin",
    "WayPoints",
    "WayPointsEmbedded",
    "Webhook",
    "WipingBladesState",
    "WipingBladesStateBase",
    "WipingBladesStateBaseSpeed",
    "XError",
    "ZoneTrigger",
    "ZoneTriggerPlace",
    "ZoneTriggerPlaceCenter",
    "ZoneTriggerTransition",
]
