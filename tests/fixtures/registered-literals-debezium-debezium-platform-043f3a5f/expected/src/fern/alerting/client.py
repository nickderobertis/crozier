

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alert_event_response import AlertEventResponse
from ..types.alert_rule_response import AlertRuleResponse
from ..types.alert_status_response import AlertStatusResponse
from ..types.channel_type import ChannelType
from ..types.duration import Duration
from ..types.instant import Instant
from ..types.notification_channel_response import NotificationChannelResponse
from ..types.operator import Operator
from ..types.paged_alert_event_response import PagedAlertEventResponse
from ..types.reduce_function import ReduceFunction
from ..types.severity import Severity
from .raw_client import AsyncRawAlertingClient, RawAlertingClient


OMIT = typing.cast(typing.Any, ...)


class AlertingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlertingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlertingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlertingClient
        """
        return self._raw_client

    def returns_all_available_notification_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationChannelResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationChannelResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_all_available_notification_channels()
        """
        _response = self._raw_client.returns_all_available_notification_channels(request_options=request_options)
        return _response.data

    def creates_a_new_notification_channel(
        self,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse

        Examples
        --------
        from fern import ChannelType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.creates_a_new_notification_channel(
            name="name",
            type=ChannelType.EMAIL,
            config={"key": "value"},
        )
        """
        _response = self._raw_client.creates_a_new_notification_channel(
            name=name, type=type, config=config, enabled=enabled, request_options=request_options
        )
        return _response.data

    def returns_a_notification_channel_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_a_notification_channel_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_notification_channel_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_notification_channel(
        self,
        id: int,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        from fern import ChannelType, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.updates_an_existing_notification_channel(
            id=1000000,
            name="name",
            type=ChannelType.EMAIL,
            config={"key": "value"},
        )
        """
        _response = self._raw_client.updates_an_existing_notification_channel(
            id, name=name, type=type, config=config, enabled=enabled, request_options=request_options
        )
        return _response.data

    def deletes_an_existing_notification_channel(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.deletes_an_existing_notification_channel(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_notification_channel(id, request_options=request_options)
        return _response.data

    def returns_paginated_alert_events(
        self,
        *,
        from_: typing.Optional[Instant] = None,
        page: typing.Optional[int] = None,
        pipeline_id: typing.Optional[str] = None,
        rule_id: typing.Optional[int] = None,
        severity: typing.Optional[Severity] = None,
        size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        to: typing.Optional[Instant] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedAlertEventResponse:
        """
        Parameters
        ----------
        from_ : typing.Optional[Instant]

        page : typing.Optional[int]

        pipeline_id : typing.Optional[str]

        rule_id : typing.Optional[int]

        severity : typing.Optional[Severity]

        size : typing.Optional[int]

        status : typing.Optional[str]

        to : typing.Optional[Instant]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedAlertEventResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_paginated_alert_events()
        """
        _response = self._raw_client.returns_paginated_alert_events(
            from_=from_,
            page=page,
            pipeline_id=pipeline_id,
            rule_id=rule_id,
            severity=severity,
            size=size,
            status=status,
            to=to,
            request_options=request_options,
        )
        return _response.data

    def returns_a_single_alert_event_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertEventResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertEventResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_a_single_alert_event_by_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_a_single_alert_event_by_id(id, request_options=request_options)
        return _response.data

    def returns_all_available_alert_rules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AlertRuleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertRuleResponse]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_all_available_alert_rules()
        """
        _response = self._raw_client.returns_all_available_alert_rules(request_options=request_options)
        return _response.data

    def creates_a_new_alert_rule(
        self,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse

        Examples
        --------
        from fern import FernApi, Operator

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.creates_a_new_alert_rule(
            name="name",
            panel_id="panelId",
            operator=Operator.GREATER_THAN,
            threshold=1.1,
        )
        """
        _response = self._raw_client.creates_a_new_alert_rule(
            name=name,
            panel_id=panel_id,
            operator=operator,
            threshold=threshold,
            description=description,
            for_duration=for_duration,
            reduce_function=reduce_function,
            evaluation_window=evaluation_window,
            severity=severity,
            enabled=enabled,
            channel_ids=channel_ids,
            request_options=request_options,
        )
        return _response.data

    def returns_an_alert_rule_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_an_alert_rule_with_given_id(
            id=1000000,
        )
        """
        _response = self._raw_client.returns_an_alert_rule_with_given_id(id, request_options=request_options)
        return _response.data

    def updates_an_existing_alert_rule(
        self,
        id: int,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        from fern import FernApi, Operator

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.updates_an_existing_alert_rule(
            id=1000000,
            name="name",
            panel_id="panelId",
            operator=Operator.GREATER_THAN,
            threshold=1.1,
        )
        """
        _response = self._raw_client.updates_an_existing_alert_rule(
            id,
            name=name,
            panel_id=panel_id,
            operator=operator,
            threshold=threshold,
            description=description,
            for_duration=for_duration,
            reduce_function=reduce_function,
            evaluation_window=evaluation_window,
            severity=severity,
            enabled=enabled,
            channel_ids=channel_ids,
            request_options=request_options,
        )
        return _response.data

    def deletes_an_existing_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.deletes_an_existing_alert_rule(
            id=1000000,
        )
        """
        _response = self._raw_client.deletes_an_existing_alert_rule(id, request_options=request_options)
        return _response.data

    def disables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.disables_an_alert_rule(
            id=1000000,
        )
        """
        _response = self._raw_client.disables_an_alert_rule(id, request_options=request_options)
        return _response.data

    def enables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.enables_an_alert_rule(
            id=1000000,
        )
        """
        _response = self._raw_client.enables_an_alert_rule(id, request_options=request_options)
        return _response.data

    def returns_current_alert_status_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertStatusResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alerting.returns_current_alert_status_summary()
        """
        _response = self._raw_client.returns_current_alert_status_summary(request_options=request_options)
        return _response.data


class AsyncAlertingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlertingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlertingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlertingClient
        """
        return self._raw_client

    async def returns_all_available_notification_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NotificationChannelResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NotificationChannelResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_all_available_notification_channels()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_notification_channels(request_options=request_options)
        return _response.data

    async def creates_a_new_notification_channel(
        self,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChannelType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.creates_a_new_notification_channel(
                name="name",
                type=ChannelType.EMAIL,
                config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_notification_channel(
            name=name, type=type, config=config, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def returns_a_notification_channel_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_a_notification_channel_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_notification_channel_with_given_id(
            id, request_options=request_options
        )
        return _response.data

    async def updates_an_existing_notification_channel(
        self,
        id: int,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NotificationChannelResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NotificationChannelResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ChannelType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.updates_an_existing_notification_channel(
                id=1000000,
                name="name",
                type=ChannelType.EMAIL,
                config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_notification_channel(
            id, name=name, type=type, config=config, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def deletes_an_existing_notification_channel(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.deletes_an_existing_notification_channel(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_notification_channel(id, request_options=request_options)
        return _response.data

    async def returns_paginated_alert_events(
        self,
        *,
        from_: typing.Optional[Instant] = None,
        page: typing.Optional[int] = None,
        pipeline_id: typing.Optional[str] = None,
        rule_id: typing.Optional[int] = None,
        severity: typing.Optional[Severity] = None,
        size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        to: typing.Optional[Instant] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagedAlertEventResponse:
        """
        Parameters
        ----------
        from_ : typing.Optional[Instant]

        page : typing.Optional[int]

        pipeline_id : typing.Optional[str]

        rule_id : typing.Optional[int]

        severity : typing.Optional[Severity]

        size : typing.Optional[int]

        status : typing.Optional[str]

        to : typing.Optional[Instant]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagedAlertEventResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_paginated_alert_events()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_paginated_alert_events(
            from_=from_,
            page=page,
            pipeline_id=pipeline_id,
            rule_id=rule_id,
            severity=severity,
            size=size,
            status=status,
            to=to,
            request_options=request_options,
        )
        return _response.data

    async def returns_a_single_alert_event_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertEventResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertEventResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_a_single_alert_event_by_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_single_alert_event_by_id(id, request_options=request_options)
        return _response.data

    async def returns_all_available_alert_rules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AlertRuleResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AlertRuleResponse]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_all_available_alert_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_available_alert_rules(request_options=request_options)
        return _response.data

    async def creates_a_new_alert_rule(
        self,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Operator

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.creates_a_new_alert_rule(
                name="name",
                panel_id="panelId",
                operator=Operator.GREATER_THAN,
                threshold=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_alert_rule(
            name=name,
            panel_id=panel_id,
            operator=operator,
            threshold=threshold,
            description=description,
            for_duration=for_duration,
            reduce_function=reduce_function,
            evaluation_window=evaluation_window,
            severity=severity,
            enabled=enabled,
            channel_ids=channel_ids,
            request_options=request_options,
        )
        return _response.data

    async def returns_an_alert_rule_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_an_alert_rule_with_given_id(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_an_alert_rule_with_given_id(id, request_options=request_options)
        return _response.data

    async def updates_an_existing_alert_rule(
        self,
        id: int,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Operator

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.updates_an_existing_alert_rule(
                id=1000000,
                name="name",
                panel_id="panelId",
                operator=Operator.GREATER_THAN,
                threshold=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_an_existing_alert_rule(
            id,
            name=name,
            panel_id=panel_id,
            operator=operator,
            threshold=threshold,
            description=description,
            for_duration=for_duration,
            reduce_function=reduce_function,
            evaluation_window=evaluation_window,
            severity=severity,
            enabled=enabled,
            channel_ids=channel_ids,
            request_options=request_options,
        )
        return _response.data

    async def deletes_an_existing_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : int

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.deletes_an_existing_alert_rule(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletes_an_existing_alert_rule(id, request_options=request_options)
        return _response.data

    async def disables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.disables_an_alert_rule(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disables_an_alert_rule(id, request_options=request_options)
        return _response.data

    async def enables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertRuleResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertRuleResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.enables_an_alert_rule(
                id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enables_an_alert_rule(id, request_options=request_options)
        return _response.data

    async def returns_current_alert_status_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertStatusResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertStatusResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alerting.returns_current_alert_status_summary()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_current_alert_status_summary(request_options=request_options)
        return _response.data
