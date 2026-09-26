

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AttributeValueOne(enum.StrEnum):
    """
    A value  that will be associated with the provided key as is if expressed as literal value or  contextually valued if prefixed with the dollar sign ($).

    * Disclaimer: if the var "vin" is used as a query parameter, the batchnotify will be no more possible and each event will be sent through a separated request!.
    * example: Having a vin=VIN123456, the following attribute set:
            ```"attributes": [
                {
                  "type": "Header",
                  "key": "X-vehicle-id"
                  "value":"$vin"
                }
              ]```
      will be valued as http header extension:

      *"X-vehicle-id: VIN123456"*
    """

    VIN = "vin"
    MONITOR_ID = "monitorID"
    FLEET_ID = "fleetID"
    VID = "vid"

    def visit(
        self,
        vin: typing.Callable[[], T_Result],
        monitor_id: typing.Callable[[], T_Result],
        fleet_id: typing.Callable[[], T_Result],
        vid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AttributeValueOne.VIN:
            return vin()
        if self is AttributeValueOne.MONITOR_ID:
            return monitor_id()
        if self is AttributeValueOne.FLEET_ID:
            return fleet_id()
        if self is AttributeValueOne.VID:
            return vid()
