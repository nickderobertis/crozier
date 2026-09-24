

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.alarms_list_response import AlarmsListResponse
from .raw_client import AsyncRawAlarmsClient, RawAlarmsClient
from .types.list_alarms_request_status import ListAlarmsRequestStatus


class AlarmsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAlarmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAlarmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAlarmsClient
        """
        return self._raw_client

    def list_alarms(
        self,
        *,
        status: ListAlarmsRequestStatus,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlarmsListResponse:
        """
        List alarms filtered by status

        Parameters
        ----------
        status : ListAlarmsRequestStatus
            Filter alarms by status. Required parameter. Allowed values:
              - ACTIVE
              - DEACTIVE

        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlarmsListResponse
            A list of alarms

        Examples
        --------
        from fern.alarms import ListAlarmsRequestStatus

        from fern import FernApi

        client = FernApi()
        client.alarms.list_alarms(
            status=ListAlarmsRequestStatus.ACTIVE,
        )
        """
        _response = self._raw_client.list_alarms(
            status=status, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def delete_deactive_alarms(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all deactive alarms

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarms.delete_deactive_alarms()
        """
        _response = self._raw_client.delete_deactive_alarms(request_options=request_options)
        return _response.data

    def deactivate_alarm(self, alarm_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deactivate an alarm

        Parameters
        ----------
        alarm_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alarms.deactivate_alarm(
            alarm_id=1,
        )
        """
        _response = self._raw_client.deactivate_alarm(alarm_id, request_options=request_options)
        return _response.data


class AsyncAlarmsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAlarmsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAlarmsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAlarmsClient
        """
        return self._raw_client

    async def list_alarms(
        self,
        *,
        status: ListAlarmsRequestStatus,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AlarmsListResponse:
        """
        List alarms filtered by status

        Parameters
        ----------
        status : ListAlarmsRequestStatus
            Filter alarms by status. Required parameter. Allowed values:
              - ACTIVE
              - DEACTIVE

        page : typing.Optional[int]
            The page number

        page_size : typing.Optional[int]
            The number of items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlarmsListResponse
            A list of alarms

        Examples
        --------
        import asyncio

        from fern.alarms import ListAlarmsRequestStatus

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarms.list_alarms(
                status=ListAlarmsRequestStatus.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_alarms(
            status=status, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def delete_deactive_alarms(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete all deactive alarms

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarms.delete_deactive_alarms()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_deactive_alarms(request_options=request_options)
        return _response.data

    async def deactivate_alarm(self, alarm_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deactivate an alarm

        Parameters
        ----------
        alarm_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alarms.deactivate_alarm(
                alarm_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deactivate_alarm(alarm_id, request_options=request_options)
        return _response.data
