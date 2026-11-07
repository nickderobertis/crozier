

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMonitorClient, RawMonitorClient
from .types.monitor_all_response_item import MonitorAllResponseItem
from .types.monitor_change_active_response import MonitorChangeActiveResponse
from .types.monitor_data_metrics_response import MonitorDataMetricsResponse
from .types.monitor_data_response_item import MonitorDataResponseItem
from .types.monitor_delete_response import MonitorDeleteResponse
from .types.monitor_events_response_item import MonitorEventsResponseItem
from .types.monitor_get_public_info_response_item import MonitorGetPublicInfoResponseItem
from .types.monitor_get_response import MonitorGetResponse
from .types.monitor_get_status_response import MonitorGetStatusResponse
from .types.monitor_public_data_response_item import MonitorPublicDataResponseItem
from .types.monitor_public_summary_response_item import MonitorPublicSummaryResponseItem
from .types.monitor_recent_data_response_item import MonitorRecentDataResponseItem
from .types.monitor_upsert_response import MonitorUpsertResponse
from .types.server_status_public_info_response_value import ServerStatusPublicInfoResponseValue


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

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def get(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MonitorGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MonitorGetResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.get(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.get(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def getpublicinfo(
        self, *, monitor_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorGetPublicInfoResponseItem]:
        """
        Parameters
        ----------
        monitor_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorGetPublicInfoResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.getpublicinfo(
            monitor_ids=["monitorIds"],
        )
        """
        _response = self._raw_client.getpublicinfo(monitor_ids=monitor_ids, request_options=request_options)
        return _response.data

    def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        type: str,
        payload: typing.Dict[str, typing.Any],
        id: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        interval: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        trending_mode: typing.Optional[bool] = OMIT,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        up_message_template: typing.Optional[str] = OMIT,
        down_message_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        type : str

        payload : typing.Dict[str, typing.Any]

        id : typing.Optional[str]

        active : typing.Optional[bool]

        interval : typing.Optional[int]

        max_retries : typing.Optional[int]

        trending_mode : typing.Optional[bool]

        notification_ids : typing.Optional[typing.Sequence[str]]

        up_message_template : typing.Optional[str]

        down_message_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.upsert(
            workspace_id="workspaceId",
            name="name",
            type="type",
            payload={"key": "value"},
        )
        """
        _response = self._raw_client.upsert(
            workspace_id,
            name=name,
            type=type,
            payload=payload,
            id=id,
            active=active,
            interval=interval,
            max_retries=max_retries,
            trending_mode=trending_mode,
            notification_ids=notification_ids,
            up_message_template=up_message_template,
            down_message_template=down_message_template,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonitorDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.delete(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.delete(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def regeneratepushtoken(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.regeneratepushtoken(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.regeneratepushtoken(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def triggermonitor(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.triggermonitor(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.triggermonitor(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def data(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorDataResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.data(
            workspace_id="workspaceId",
            monitor_id="monitorId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.data(
            workspace_id, monitor_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    def changeactive(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorChangeActiveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorChangeActiveResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.changeactive(
            workspace_id="workspaceId",
            monitor_id="monitorId",
            active=True,
        )
        """
        _response = self._raw_client.changeactive(
            workspace_id, monitor_id, active=active, request_options=request_options
        )
        return _response.data

    def recentdata(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        take: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorRecentDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        take : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorRecentDataResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.recentdata(
            workspace_id="workspaceId",
            monitor_id="monitorId",
            take=1.1,
        )
        """
        _response = self._raw_client.recentdata(workspace_id, monitor_id, take=take, request_options=request_options)
        return _response.data

    def publicsummary(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorPublicSummaryResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorPublicSummaryResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.publicsummary(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.publicsummary(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def publicdata(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorPublicDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorPublicDataResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.publicdata(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.publicdata(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def datametrics(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonitorDataMetricsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorDataMetricsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.datametrics(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.datametrics(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    def events(
        self,
        workspace_id: str,
        *,
        monitor_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorEventsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : typing.Optional[str]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorEventsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.events(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.events(
            workspace_id, monitor_id=monitor_id, limit=limit, request_options=request_options
        )
        return _response.data

    def clearevents(
        self, workspace_id: str, *, monitor_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.clearevents(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.clearevents(workspace_id, monitor_id=monitor_id, request_options=request_options)
        return _response.data

    def cleardata(
        self, workspace_id: str, *, monitor_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.cleardata(
            workspace_id="workspaceId",
            monitor_id="monitorId",
        )
        """
        _response = self._raw_client.cleardata(workspace_id, monitor_id=monitor_id, request_options=request_options)
        return _response.data

    def getstatus(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        status_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[MonitorGetStatusResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        status_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MonitorGetStatusResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.getstatus(
            workspace_id="workspaceId",
            monitor_id="monitorId",
            status_name="statusName",
        )
        """
        _response = self._raw_client.getstatus(
            workspace_id, monitor_id, status_name=status_name, request_options=request_options
        )
        return _response.data

    def server_status_public_info(
        self,
        *,
        workspace_id: str,
        server_names: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, ServerStatusPublicInfoResponseValue]:
        """
        Parameters
        ----------
        workspace_id : str

        server_names : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ServerStatusPublicInfoResponseValue]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.monitor.server_status_public_info(
            workspace_id="workspaceId",
            server_names=["serverNames"],
        )
        """
        _response = self._raw_client.server_status_public_info(
            workspace_id=workspace_id, server_names=server_names, request_options=request_options
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

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def get(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[MonitorGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MonitorGetResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.get(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def getpublicinfo(
        self, *, monitor_ids: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorGetPublicInfoResponseItem]:
        """
        Parameters
        ----------
        monitor_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorGetPublicInfoResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.getpublicinfo(
                monitor_ids=["monitorIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicinfo(monitor_ids=monitor_ids, request_options=request_options)
        return _response.data

    async def upsert(
        self,
        workspace_id: str,
        *,
        name: str,
        type: str,
        payload: typing.Dict[str, typing.Any],
        id: typing.Optional[str] = OMIT,
        active: typing.Optional[bool] = OMIT,
        interval: typing.Optional[int] = OMIT,
        max_retries: typing.Optional[int] = OMIT,
        trending_mode: typing.Optional[bool] = OMIT,
        notification_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        up_message_template: typing.Optional[str] = OMIT,
        down_message_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        type : str

        payload : typing.Dict[str, typing.Any]

        id : typing.Optional[str]

        active : typing.Optional[bool]

        interval : typing.Optional[int]

        max_retries : typing.Optional[int]

        trending_mode : typing.Optional[bool]

        notification_ids : typing.Optional[typing.Sequence[str]]

        up_message_template : typing.Optional[str]

        down_message_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.upsert(
                workspace_id="workspaceId",
                name="name",
                type="type",
                payload={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert(
            workspace_id,
            name=name,
            type=type,
            payload=payload,
            id=id,
            active=active,
            interval=interval,
            max_retries=max_retries,
            trending_mode=trending_mode,
            notification_ids=notification_ids,
            up_message_template=up_message_template,
            down_message_template=down_message_template,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonitorDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.delete(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def regeneratepushtoken(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.regeneratepushtoken(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.regeneratepushtoken(
            workspace_id, monitor_id, request_options=request_options
        )
        return _response.data

    async def triggermonitor(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.triggermonitor(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.triggermonitor(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def data(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorDataResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.data(
                workspace_id="workspaceId",
                monitor_id="monitorId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.data(
            workspace_id, monitor_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    async def changeactive(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MonitorChangeActiveResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorChangeActiveResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.changeactive(
                workspace_id="workspaceId",
                monitor_id="monitorId",
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.changeactive(
            workspace_id, monitor_id, active=active, request_options=request_options
        )
        return _response.data

    async def recentdata(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        take: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorRecentDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        take : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorRecentDataResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.recentdata(
                workspace_id="workspaceId",
                monitor_id="monitorId",
                take=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recentdata(
            workspace_id, monitor_id, take=take, request_options=request_options
        )
        return _response.data

    async def publicsummary(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorPublicSummaryResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorPublicSummaryResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.publicsummary(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publicsummary(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def publicdata(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MonitorPublicDataResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorPublicDataResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.publicdata(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publicdata(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def datametrics(
        self, workspace_id: str, monitor_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MonitorDataMetricsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MonitorDataMetricsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.datametrics(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.datametrics(workspace_id, monitor_id, request_options=request_options)
        return _response.data

    async def events(
        self,
        workspace_id: str,
        *,
        monitor_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[MonitorEventsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : typing.Optional[str]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MonitorEventsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.events(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.events(
            workspace_id, monitor_id=monitor_id, limit=limit, request_options=request_options
        )
        return _response.data

    async def clearevents(
        self, workspace_id: str, *, monitor_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.clearevents(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clearevents(
            workspace_id, monitor_id=monitor_id, request_options=request_options
        )
        return _response.data

    async def cleardata(
        self, workspace_id: str, *, monitor_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.cleardata(
                workspace_id="workspaceId",
                monitor_id="monitorId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cleardata(
            workspace_id, monitor_id=monitor_id, request_options=request_options
        )
        return _response.data

    async def getstatus(
        self,
        workspace_id: str,
        monitor_id: str,
        *,
        status_name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[MonitorGetStatusResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        monitor_id : str

        status_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MonitorGetStatusResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.getstatus(
                workspace_id="workspaceId",
                monitor_id="monitorId",
                status_name="statusName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getstatus(
            workspace_id, monitor_id, status_name=status_name, request_options=request_options
        )
        return _response.data

    async def server_status_public_info(
        self,
        *,
        workspace_id: str,
        server_names: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, ServerStatusPublicInfoResponseValue]:
        """
        Parameters
        ----------
        workspace_id : str

        server_names : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, ServerStatusPublicInfoResponseValue]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.monitor.server_status_public_info(
                workspace_id="workspaceId",
                server_names=["serverNames"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.server_status_public_info(
            workspace_id=workspace_id, server_names=server_names, request_options=request_options
        )
        return _response.data
