

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.index_range import IndexRange
from ..types.monitor import Monitor
from ..types.monitor_callback_subscribe import MonitorCallbackSubscribe
from ..types.monitor_parameter_extended_event_param_item import MonitorParameterExtendedEventParamItem
from ..types.monitor_parameter_trigger_param import MonitorParameterTriggerParam
from ..types.monitor_ref import MonitorRef
from ..types.monitors import Monitors
from .raw_client import AsyncRawMonitorsClient, RawMonitorsClient
from .types.monitor_status_setter_status import MonitorStatusSetterStatus


OMIT = typing.cast(typing.Any, ...)


class MonitorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonitorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonitorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonitorsClient
        """
        return self._raw_client

    def get_fleet_monitors(
        self,
        fid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitors:
        """
        Returns the list of subscribed Monitors of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitors
            A list of Monitors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.get_fleet_monitors(
            fid="fid",
        )
        """
        _response = self._raw_client.get_fleet_monitors(
            fid, index_range=index_range, page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_fleet_vehicle_monitor(
        self,
        fid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        >Create a Monitor for all Vehicles of the fleet. This is a kind of vehicle monitor that generates an event following the transition state of one of the (monitored) data  of the vehicles. As for example the fuel level, the moving out of a defined geographical area.

        >When the trigger occurs, the built event expressed as a JSON object will be sent over the subscribed callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        from fern import (
            Attribute,
            AttributeType,
            CallbackSubscribeCallback,
            FernApi,
            MonitorCallbackSubscribe,
            MonitorParameterTriggerParam,
            MonitorTrigger,
            Webhook,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.create_fleet_vehicle_monitor(
            fid="fid",
            label="label",
            subscribe_param=MonitorCallbackSubscribe(
                callback=CallbackSubscribeCallback(
                    webhook=Webhook(
                        target="https://my.post.callback",
                        name="My_Webhook",
                        attributes=[
                            Attribute(
                                type=AttributeType.HEADER,
                                key="X-Vehicle_Id",
                                value="$vin",
                            )
                        ],
                    ),
                ),
            ),
            trigger_param=MonitorParameterTriggerParam(
                triggers=[
                    MonitorTrigger(
                        name="name",
                    )
                ],
                bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
            ),
        )
        """
        _response = self._raw_client.create_fleet_vehicle_monitor(
            fid,
            label=label,
            subscribe_param=subscribe_param,
            trigger_param=trigger_param,
            extended_event_param=extended_event_param,
            request_options=request_options,
        )
        return _response.data

    def get_fleet_monitors_status_by_id(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Returns information about a specific Monitor for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Monitor response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.get_fleet_monitors_status_by_id(
            fid="fid",
            mid="mid",
        )
        """
        _response = self._raw_client.get_fleet_monitors_status_by_id(fid, mid, request_options=request_options)
        return _response.data

    def update_fleet_vehicle_monitor(
        self,
        fid: str,
        mid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        Update an existing ```Monitor``` that has been posted (and accepted previously) for this fleet. The monitor object (body) provided should be complete because the aggregation is not supported for the update of the ```monitor```. You can first retrieve this object using the ```GET /monitor/{mid}``` API, then modify it and finally publish it (via this ```PUT API```).

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        from fern import (
            Attribute,
            AttributeType,
            CallbackSubscribeCallback,
            FernApi,
            MonitorCallbackSubscribe,
            MonitorParameterTriggerParam,
            MonitorTrigger,
            Webhook,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.update_fleet_vehicle_monitor(
            fid="fid",
            mid="mid",
            label="label",
            subscribe_param=MonitorCallbackSubscribe(
                callback=CallbackSubscribeCallback(
                    webhook=Webhook(
                        target="https://my.post.callback",
                        name="My_Webhook",
                        attributes=[
                            Attribute(
                                type=AttributeType.HEADER,
                                key="X-Vehicle_Id",
                                value="$vin",
                            )
                        ],
                    ),
                ),
            ),
            trigger_param=MonitorParameterTriggerParam(
                triggers=[
                    MonitorTrigger(
                        name="name",
                    )
                ],
                bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
            ),
        )
        """
        _response = self._raw_client.update_fleet_vehicle_monitor(
            fid,
            mid,
            label=label,
            subscribe_param=subscribe_param,
            trigger_param=trigger_param,
            extended_event_param=extended_event_param,
            request_options=request_options,
        )
        return _response.data

    def delete_fleet_monitor(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stop (disable) an existing Monitor.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.delete_fleet_monitor(
            fid="fid",
            mid="mid",
        )
        """
        _response = self._raw_client.delete_fleet_monitor(fid, mid, request_options=request_options)
        return _response.data

    def set_fleet_vehicle_monitor_status(
        self,
        fid: str,
        mid: str,
        *,
        status: MonitorStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        Set monitor status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        status : MonitorStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        from fern.monitors import MonitorStatusSetterStatus

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.monitors.set_fleet_vehicle_monitor_status(
            fid="fid",
            mid="mid",
            status=MonitorStatusSetterStatus.RUNNING,
        )
        """
        _response = self._raw_client.set_fleet_vehicle_monitor_status(
            fid, mid, status=status, request_options=request_options
        )
        return _response.data


class AsyncMonitorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonitorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonitorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonitorsClient
        """
        return self._raw_client

    async def get_fleet_monitors(
        self,
        fid: str,
        *,
        index_range: typing.Optional[IndexRange] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitors:
        """
        Returns the list of subscribed Monitors of the fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        index_range : typing.Optional[IndexRange]
            Results indexes will be included in this range (see **indexRange** model).

              default: 0-

              example: 0-, 0-5

        page_size : typing.Optional[int]
            The maximum number of results (for a collection results response) to return per page. When not set, at most 60 results will be returned.  The range for this parameter is [1...60]

        page_token : typing.Optional[str]
            Start-Page marker, this token is used (by the backend) for continuing serving from the previous results page to the next one. (_Disclaimer_:  **It is built and used only by the server**).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitors
            A list of Monitors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.get_fleet_monitors(
                fid="fid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_monitors(
            fid, index_range=index_range, page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_fleet_vehicle_monitor(
        self,
        fid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        >Create a Monitor for all Vehicles of the fleet. This is a kind of vehicle monitor that generates an event following the transition state of one of the (monitored) data  of the vehicles. As for example the fuel level, the moving out of a defined geographical area.

        >When the trigger occurs, the built event expressed as a JSON object will be sent over the subscribed callback.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Attribute,
            AttributeType,
            CallbackSubscribeCallback,
            MonitorCallbackSubscribe,
            MonitorParameterTriggerParam,
            MonitorTrigger,
            Webhook,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.create_fleet_vehicle_monitor(
                fid="fid",
                label="label",
                subscribe_param=MonitorCallbackSubscribe(
                    callback=CallbackSubscribeCallback(
                        webhook=Webhook(
                            target="https://my.post.callback",
                            name="My_Webhook",
                            attributes=[
                                Attribute(
                                    type=AttributeType.HEADER,
                                    key="X-Vehicle_Id",
                                    value="$vin",
                                )
                            ],
                        ),
                    ),
                ),
                trigger_param=MonitorParameterTriggerParam(
                    triggers=[
                        MonitorTrigger(
                            name="name",
                        )
                    ],
                    bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_fleet_vehicle_monitor(
            fid,
            label=label,
            subscribe_param=subscribe_param,
            trigger_param=trigger_param,
            extended_event_param=extended_event_param,
            request_options=request_options,
        )
        return _response.data

    async def get_fleet_monitors_status_by_id(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Returns information about a specific Monitor for a given fleet.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Monitor response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.get_fleet_monitors_status_by_id(
                fid="fid",
                mid="mid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_fleet_monitors_status_by_id(fid, mid, request_options=request_options)
        return _response.data

    async def update_fleet_vehicle_monitor(
        self,
        fid: str,
        mid: str,
        *,
        label: str,
        subscribe_param: MonitorCallbackSubscribe,
        trigger_param: MonitorParameterTriggerParam,
        extended_event_param: typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        Update an existing ```Monitor``` that has been posted (and accepted previously) for this fleet. The monitor object (body) provided should be complete because the aggregation is not supported for the update of the ```monitor```. You can first retrieve this object using the ```GET /monitor/{mid}``` API, then modify it and finally publish it (via this ```PUT API```).

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        label : str
            Monitor label (usually its name).

        subscribe_param : MonitorCallbackSubscribe

        trigger_param : MonitorParameterTriggerParam
            Monitor trigger-param that allows to compound triggers by applying a boolean expression to evaluate them.

        extended_event_param : typing.Optional[typing.Sequence[MonitorParameterExtendedEventParamItem]]
            Allow to set extra vehicle data (defined in data model) to add to the monitor event
            when publishing. The possible values are :


            |value|description|Related model |
            |----------|:-------------|------:|
            |vehicle.doorsState|Latest known door state (timestamped) before the eventDate|DoorState|
            |vehicle.status|Latest known vehicle status (timestamped) before the eventDate|Status|
            |vehicle.maintenance|Latest known maintenance(timestamped) before the eventDate|Maintenance|
            |vehicle.position|Last vehicle position (timestamped) before the eventDate|Position|
            |vehicle.telemetry${.TelemetryEnum} |Latest known telemetry (timestamped) before the eventDate filtered with type|Telemetry
            |vehicle.alerts|List of active alerts at the eventDate|Alert|
            |vehicle.collisions|Latest known collisions before the eventDate|Collision|
            |vehicle.trip|Trip related to the event that triggers the notification|Trip|
            |vehicle.stolen|Vehicle Stolen context at the eventDate (only returns when vehicle is reported stolen) |Stolen|


            * For telemetry extension:
              * The suffix ```${.TelemetryEnum}``` can be selected to refine with telemetry type (from the TelemetryEnum list). This value (with suffix) can be selected **_several times_** to included suitable telemetry messages with the extention.
              * Using ```vehicle.telemetry``` without suffix means to include all available telemetries.
            * The set of data will then correspond to the union of extensions used in the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            Attribute,
            AttributeType,
            CallbackSubscribeCallback,
            MonitorCallbackSubscribe,
            MonitorParameterTriggerParam,
            MonitorTrigger,
            Webhook,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.update_fleet_vehicle_monitor(
                fid="fid",
                mid="mid",
                label="label",
                subscribe_param=MonitorCallbackSubscribe(
                    callback=CallbackSubscribeCallback(
                        webhook=Webhook(
                            target="https://my.post.callback",
                            name="My_Webhook",
                            attributes=[
                                Attribute(
                                    type=AttributeType.HEADER,
                                    key="X-Vehicle_Id",
                                    value="$vin",
                                )
                            ],
                        ),
                    ),
                ),
                trigger_param=MonitorParameterTriggerParam(
                    triggers=[
                        MonitorTrigger(
                            name="name",
                        )
                    ],
                    bool_exp="((z1 & t1) | (z2 & !t1) | (f & z1) | (a & (z1|t))  | (o & (z1 | z2)))",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_fleet_vehicle_monitor(
            fid,
            mid,
            label=label,
            subscribe_param=subscribe_param,
            trigger_param=trigger_param,
            extended_event_param=extended_event_param,
            request_options=request_options,
        )
        return _response.data

    async def delete_fleet_monitor(
        self, fid: str, mid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stop (disable) an existing Monitor.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.delete_fleet_monitor(
                fid="fid",
                mid="mid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_fleet_monitor(fid, mid, request_options=request_options)
        return _response.data

    async def set_fleet_vehicle_monitor_status(
        self,
        fid: str,
        mid: str,
        *,
        status: MonitorStatusSetterStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorRef:
        """
        Set monitor status.

        Parameters
        ----------
        fid : str
            Resource is related to this fleet ID only.

        mid : str
            id of the monitor.

        status : MonitorStatusSetterStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorRef
            Monitor created or updated successfully

        Examples
        --------
        import asyncio

        from fern.monitors import MonitorStatusSetterStatus

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.monitors.set_fleet_vehicle_monitor_status(
                fid="fid",
                mid="mid",
                status=MonitorStatusSetterStatus.RUNNING,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_fleet_vehicle_monitor_status(
            fid, mid, status=status, request_options=request_options
        )
        return _response.data
