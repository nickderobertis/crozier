

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.x_com import XCom
from ..types.x_com_collection import XComCollection
from .raw_client import AsyncRawXComClient, RawXComClient


class XComClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawXComClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawXComClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawXComClient
        """
        return self._raw_client

    def get_xcom_entries(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> XComCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        XComCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.x_com.get_xcom_entries(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
        )
        """
        _response = self._raw_client.get_xcom_entries(
            dag_id, dag_run_id, task_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def get_xcom_entry(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        xcom_key: str,
        *,
        deserialize: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> XCom:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        xcom_key : str
            The XCom key.

        deserialize : typing.Optional[bool]
            Whether to deserialize an XCom value when using a custom XCom backend.

            The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value
            that is potentially expensive to deserialize in the web server. Setting this to true overrides
            the consideration, and calls `deserialize_value` instead.

            This parameter is not meaningful when using the default XCom backend.

            *New in version 2.4.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        XCom
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.x_com.get_xcom_entry(
            dag_id="dag_id",
            dag_run_id="dag_run_id",
            task_id="task_id",
            xcom_key="xcom_key",
        )
        """
        _response = self._raw_client.get_xcom_entry(
            dag_id, dag_run_id, task_id, xcom_key, deserialize=deserialize, request_options=request_options
        )
        return _response.data


class AsyncXComClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawXComClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawXComClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawXComClient
        """
        return self._raw_client

    async def get_xcom_entries(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> XComCollection:
        """
        This endpoint allows specifying `~` as the dag_id, dag_run_id, task_id to retrieve XCOM entries for for all DAGs, DAG runs and task instances. XCom values won't be returned as they can be large. Use this endpoint to get a list of XCom entries and then fetch individual entry to get value.

        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        limit : typing.Optional[int]
            The numbers of items to return.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        XComCollection
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
            await client.x_com.get_xcom_entries(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_xcom_entries(
            dag_id, dag_run_id, task_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_xcom_entry(
        self,
        dag_id: str,
        dag_run_id: str,
        task_id: str,
        xcom_key: str,
        *,
        deserialize: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> XCom:
        """
        Parameters
        ----------
        dag_id : str
            The DAG ID.

        dag_run_id : str
            The DAG run ID.

        task_id : str
            The task ID.

        xcom_key : str
            The XCom key.

        deserialize : typing.Optional[bool]
            Whether to deserialize an XCom value when using a custom XCom backend.

            The XCom API endpoint calls `orm_deserialize_value` by default since an XCom may contain value
            that is potentially expensive to deserialize in the web server. Setting this to true overrides
            the consideration, and calls `deserialize_value` instead.

            This parameter is not meaningful when using the default XCom backend.

            *New in version 2.4.0*

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        XCom
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
            await client.x_com.get_xcom_entry(
                dag_id="dag_id",
                dag_run_id="dag_run_id",
                task_id="task_id",
                xcom_key="xcom_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_xcom_entry(
            dag_id, dag_run_id, task_id, xcom_key, deserialize=deserialize, request_options=request_options
        )
        return _response.data
