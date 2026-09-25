

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_trigger_data import DataTriggerData
from .data_trigger_op import DataTriggerOp


class DataTrigger(UniversalBaseModel):
    """
    A monitor for triggering the vehicle data change event.
    """

    data: DataTriggerData = pydantic.Field()
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

    op: DataTriggerOp = pydantic.Field()
    """
    The operator of the trigger function.
    """

    value: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The right operand of the trigger function. It can be a uniq ```value``` or a list of value ```values```. The choice of one or the other depends on ```OP```  which in the case of ```includedIn``` must be a list.
      * _Disclaimer_: If the op field is not set to ```includeIn``` then only the first item will be used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
