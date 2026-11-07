

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAlertClient, RawAlertClient
from .types.get_alerts_response import GetAlertsResponse


class AlertClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlertClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlertClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlertClient
        """
        return self._raw_client

    def get_alerts(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        monitor_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAlertsResponse:
        """
        Get list of defined Alerts

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        monitor_uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlertsResponse
            The response body from GET /alerts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.alert.get_alerts(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_alerts(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            monitor_uid=monitor_uid,
            request_options=request_options,
        )
        return _response.data


class AsyncAlertClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlertClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlertClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlertClient
        """
        return self._raw_client

    async def get_alerts(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        monitor_uid: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAlertsResponse:
        """
        Get list of defined Alerts

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        monitor_uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlertsResponse
            The response body from GET /alerts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.alert.get_alerts(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_alerts(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            monitor_uid=monitor_uid,
            request_options=request_options,
        )
        return _response.data
