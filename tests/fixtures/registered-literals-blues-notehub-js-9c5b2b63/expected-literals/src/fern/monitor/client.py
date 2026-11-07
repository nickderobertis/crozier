

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.monitor import Monitor
from ..types.monitor_aggregate_function import MonitorAggregateFunction
from ..types.monitor_alert_routes_item import MonitorAlertRoutesItem
from ..types.monitor_condition_type import MonitorConditionType
from ..types.monitor_source_type import MonitorSourceType
from .raw_client import AsyncRawMonitorClient, RawMonitorClient
from .types.create_monitor_aggregate_function import CreateMonitorAggregateFunction
from .types.create_monitor_alert_routes_item import CreateMonitorAlertRoutesItem
from .types.create_monitor_condition_type import CreateMonitorConditionType
from .types.create_monitor_source_type import CreateMonitorSourceType


OMIT = typing.cast(typing.Any, ...)


class MonitorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMonitorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMonitorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMonitorClient
        """
        return self._raw_client

    def get_monitors(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Monitor]:
        """
        Get list of defined Monitors

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Monitor]
            The response body from GET /monitors

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.get_monitors(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_monitors(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_monitor(
        self,
        project_or_product_uid: str,
        *,
        alert_routes: typing.Sequence[CreateMonitorAlertRoutesItem],
        description: str,
        name: str,
        source_type: CreateMonitorSourceType,
        threshold: int,
        aggregate_function: typing.Optional[CreateMonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        condition_type: typing.Optional[CreateMonitorConditionType] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitor:
        """
        Create a new Monitor

        Parameters
        ----------
        project_or_product_uid : str

        alert_routes : typing.Sequence[CreateMonitorAlertRoutesItem]

        description : str

        name : str

        source_type : CreateMonitorSourceType
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : int
            The type of condition to apply to the value selected by the source_selector

        aggregate_function : typing.Optional[CreateMonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        condition_type : typing.Optional[CreateMonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        from fern import FernApi, SlackWebHookNotification

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.create_monitor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            alert_routes=[SlackWebHookNotification()],
            description="description",
            name="name",
            source_type="event",
            threshold=1,
        )
        """
        _response = self._raw_client.create_monitor(
            project_or_product_uid,
            alert_routes=alert_routes,
            description=description,
            name=name,
            source_type=source_type,
            threshold=threshold,
            aggregate_function=aggregate_function,
            aggregate_window=aggregate_window,
            alert=alert,
            condition_type=condition_type,
            disabled=disabled,
            fleet_filter=fleet_filter,
            last_routed_at=last_routed_at,
            notefile_filter=notefile_filter,
            per_device=per_device,
            routing_cooldown_period=routing_cooldown_period,
            silenced=silenced,
            source_selector=source_selector,
            uid=uid,
            usage_scope=usage_scope,
            usage_type=usage_type,
            usage_window=usage_window,
            request_options=request_options,
        )
        return _response.data

    def get_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Get Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.get_monitor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
        )
        """
        _response = self._raw_client.get_monitor(project_or_product_uid, monitor_uid, request_options=request_options)
        return _response.data

    def update_monitor(
        self,
        project_or_product_uid: str,
        monitor_uid: str,
        *,
        aggregate_function: typing.Optional[MonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        alert_routes: typing.Optional[typing.Sequence[MonitorAlertRoutesItem]] = OMIT,
        condition_type: typing.Optional[MonitorConditionType] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        source_type: typing.Optional[MonitorSourceType] = OMIT,
        threshold: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitor:
        """
        Update Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        aggregate_function : typing.Optional[MonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        alert_routes : typing.Optional[typing.Sequence[MonitorAlertRoutesItem]]

        condition_type : typing.Optional[MonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        name : typing.Optional[str]

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        source_type : typing.Optional[MonitorSourceType]
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : typing.Optional[int]
            The type of condition to apply to the value selected by the source_selector

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.update_monitor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
        )
        """
        _response = self._raw_client.update_monitor(
            project_or_product_uid,
            monitor_uid,
            aggregate_function=aggregate_function,
            aggregate_window=aggregate_window,
            alert=alert,
            alert_routes=alert_routes,
            condition_type=condition_type,
            description=description,
            disabled=disabled,
            fleet_filter=fleet_filter,
            last_routed_at=last_routed_at,
            name=name,
            notefile_filter=notefile_filter,
            per_device=per_device,
            routing_cooldown_period=routing_cooldown_period,
            silenced=silenced,
            source_selector=source_selector,
            source_type=source_type,
            threshold=threshold,
            uid=uid,
            usage_scope=usage_scope,
            usage_type=usage_type,
            usage_window=usage_window,
            request_options=request_options,
        )
        return _response.data

    def delete_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Delete Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.delete_monitor(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
        )
        """
        _response = self._raw_client.delete_monitor(
            project_or_product_uid, monitor_uid, request_options=request_options
        )
        return _response.data


class AsyncMonitorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMonitorClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMonitorClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMonitorClient
        """
        return self._raw_client

    async def get_monitors(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Monitor]:
        """
        Get list of defined Monitors

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Monitor]
            The response body from GET /monitors

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.get_monitors(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_monitors(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_monitor(
        self,
        project_or_product_uid: str,
        *,
        alert_routes: typing.Sequence[CreateMonitorAlertRoutesItem],
        description: str,
        name: str,
        source_type: CreateMonitorSourceType,
        threshold: int,
        aggregate_function: typing.Optional[CreateMonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        condition_type: typing.Optional[CreateMonitorConditionType] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitor:
        """
        Create a new Monitor

        Parameters
        ----------
        project_or_product_uid : str

        alert_routes : typing.Sequence[CreateMonitorAlertRoutesItem]

        description : str

        name : str

        source_type : CreateMonitorSourceType
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : int
            The type of condition to apply to the value selected by the source_selector

        aggregate_function : typing.Optional[CreateMonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        condition_type : typing.Optional[CreateMonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SlackWebHookNotification

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.create_monitor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                alert_routes=[SlackWebHookNotification()],
                description="description",
                name="name",
                source_type="event",
                threshold=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_monitor(
            project_or_product_uid,
            alert_routes=alert_routes,
            description=description,
            name=name,
            source_type=source_type,
            threshold=threshold,
            aggregate_function=aggregate_function,
            aggregate_window=aggregate_window,
            alert=alert,
            condition_type=condition_type,
            disabled=disabled,
            fleet_filter=fleet_filter,
            last_routed_at=last_routed_at,
            notefile_filter=notefile_filter,
            per_device=per_device,
            routing_cooldown_period=routing_cooldown_period,
            silenced=silenced,
            source_selector=source_selector,
            uid=uid,
            usage_scope=usage_scope,
            usage_type=usage_type,
            usage_window=usage_window,
            request_options=request_options,
        )
        return _response.data

    async def get_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Get Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.get_monitor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_monitor(
            project_or_product_uid, monitor_uid, request_options=request_options
        )
        return _response.data

    async def update_monitor(
        self,
        project_or_product_uid: str,
        monitor_uid: str,
        *,
        aggregate_function: typing.Optional[MonitorAggregateFunction] = OMIT,
        aggregate_window: typing.Optional[str] = OMIT,
        alert: typing.Optional[bool] = OMIT,
        alert_routes: typing.Optional[typing.Sequence[MonitorAlertRoutesItem]] = OMIT,
        condition_type: typing.Optional[MonitorConditionType] = OMIT,
        description: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        fleet_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        last_routed_at: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notefile_filter: typing.Optional[typing.Sequence[str]] = OMIT,
        per_device: typing.Optional[bool] = OMIT,
        routing_cooldown_period: typing.Optional[str] = OMIT,
        silenced: typing.Optional[bool] = OMIT,
        source_selector: typing.Optional[str] = OMIT,
        source_type: typing.Optional[MonitorSourceType] = OMIT,
        threshold: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        usage_scope: typing.Optional[str] = OMIT,
        usage_type: typing.Optional[str] = OMIT,
        usage_window: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Monitor:
        """
        Update Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        aggregate_function : typing.Optional[MonitorAggregateFunction]
            Aggregate function to apply to the selected values before applying the condition. [none, sum, average, max, min]

        aggregate_window : typing.Optional[str]
            The time window to aggregate the selected values. It follows the format of a number followed by a time unit

        alert : typing.Optional[bool]
            If true, the monitor is in alert state.

        alert_routes : typing.Optional[typing.Sequence[MonitorAlertRoutesItem]]

        condition_type : typing.Optional[MonitorConditionType]
            A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]

        description : typing.Optional[str]

        disabled : typing.Optional[bool]
            If true, the monitor will not be evaluated.

        fleet_filter : typing.Optional[typing.Sequence[str]]

        last_routed_at : typing.Optional[str]
            The last time the monitor was evaluated and routed.

        name : typing.Optional[str]

        notefile_filter : typing.Optional[typing.Sequence[str]]

        per_device : typing.Optional[bool]
            Only relevant when using an aggregate_function. If true, the monitor will be evaluated per device, | rather than across the set of selected devices. If true then if a single device matches the specified criteria, | and alert will be created, otherwise the aggregate function will be applied across all devices.

        routing_cooldown_period : typing.Optional[str]
            The time period to wait before routing another event after the monitor | has been triggered. It follows the format of a number followed by a time unit.

        silenced : typing.Optional[bool]
            If true, alerts will be created, but no notifications will be sent.

        source_selector : typing.Optional[str]
            A valid JSONata expression that selects the value to monitor from the source. | It should return a single, numeric value.

        source_type : typing.Optional[MonitorSourceType]
            The type of source to monitor. Supported values are "event" and "heartbeat".

        threshold : typing.Optional[int]
            The type of condition to apply to the value selected by the source_selector

        uid : typing.Optional[str]

        usage_scope : typing.Optional[str]
            For usage monitors: the scope of aggregation. Supported values are "device" and "fleet".

        usage_type : typing.Optional[str]
            For usage monitors: the type of data usage to monitor. Supported values are "cellular" and "satellite".

        usage_window : typing.Optional[int]
            For usage monitors: the rolling time window in days to sum usage over (e.g. 30 for 30 days).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.update_monitor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_monitor(
            project_or_product_uid,
            monitor_uid,
            aggregate_function=aggregate_function,
            aggregate_window=aggregate_window,
            alert=alert,
            alert_routes=alert_routes,
            condition_type=condition_type,
            description=description,
            disabled=disabled,
            fleet_filter=fleet_filter,
            last_routed_at=last_routed_at,
            name=name,
            notefile_filter=notefile_filter,
            per_device=per_device,
            routing_cooldown_period=routing_cooldown_period,
            silenced=silenced,
            source_selector=source_selector,
            source_type=source_type,
            threshold=threshold,
            uid=uid,
            usage_scope=usage_scope,
            usage_type=usage_type,
            usage_window=usage_window,
            request_options=request_options,
        )
        return _response.data

    async def delete_monitor(
        self, project_or_product_uid: str, monitor_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Monitor:
        """
        Delete Monitor

        Parameters
        ----------
        project_or_product_uid : str

        monitor_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Monitor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.delete_monitor(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                monitor_uid="monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_monitor(
            project_or_product_uid, monitor_uid, request_options=request_options
        )
        return _response.data
