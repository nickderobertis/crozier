

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteAttributeValueOne(enum.StrEnum):
    """
    Set of variables that will be contextually valued and used as attribute value. To reference the variable, prefix its name with the dollar sign ($)

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
    CALLBACK_ID = "callbackID"
    REMOTE_TYPE = "remoteType"
    FLEET_ID = "fleetID"

    def visit(
        self,
        vin: typing.Callable[[], T_Result],
        callback_id: typing.Callable[[], T_Result],
        remote_type: typing.Callable[[], T_Result],
        fleet_id: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteAttributeValueOne.VIN:
            return vin()
        if self is RemoteAttributeValueOne.CALLBACK_ID:
            return callback_id()
        if self is RemoteAttributeValueOne.REMOTE_TYPE:
            return remote_type()
        if self is RemoteAttributeValueOne.FLEET_ID:
            return fleet_id()
