

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dag_warning_collection import DagWarningCollection
from .raw_client import AsyncRawDagWarningClient, RawDagWarningClient


class DagWarningClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDagWarningClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDagWarningClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDagWarningClient
        """
        return self._raw_client

    def get_dag_warnings(
        self,
        *,
        dag_id: typing.Optional[str] = None,
        warning_type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagWarningCollection:
        """
        Parameters
        ----------
        dag_id : typing.Optional[str]
            If set, only return DAG warnings with this dag_id.

        warning_type : typing.Optional[str]
            If set, only return DAG warnings with this type.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagWarningCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.dag_warning.get_dag_warnings()
        """
        _response = self._raw_client.get_dag_warnings(
            dag_id=dag_id,
            warning_type=warning_type,
            limit=limit,
            offset=offset,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data


class AsyncDagWarningClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDagWarningClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDagWarningClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDagWarningClient
        """
        return self._raw_client

    async def get_dag_warnings(
        self,
        *,
        dag_id: typing.Optional[str] = None,
        warning_type: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DagWarningCollection:
        """
        Parameters
        ----------
        dag_id : typing.Optional[str]
            If set, only return DAG warnings with this dag_id.

        warning_type : typing.Optional[str]
            If set, only return DAG warnings with this type.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        order_by : typing.Optional[str]
            The name of the field to order the results by.
            Prefix a field name with `-` to reverse the sort order.

            *New in version 2.1.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DagWarningCollection
            Success.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.dag_warning.get_dag_warnings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dag_warnings(
            dag_id=dag_id,
            warning_type=warning_type,
            limit=limit,
            offset=offset,
            order_by=order_by,
            request_options=request_options,
        )
        return _response.data
