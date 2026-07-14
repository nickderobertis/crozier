

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connection import Connection
from ..types.connection_collection import ConnectionCollection
from ..types.connection_test import ConnectionTest
from .raw_client import AsyncRawConnectionClient, RawConnectionClient


OMIT = typing.cast(typing.Any, ...)


class ConnectionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectionClient
        """
        return self._raw_client

    def get_connections(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionCollection:
        """
        Parameters
        ----------
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
        ConnectionCollection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connection.get_connections()
        """
        _response = self._raw_client.get_connections(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    def post_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Connection:
        """
        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connection.post_connection()
        """
        _response = self._raw_client.post_connection(
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    def test_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionTest:
        """
        Test a connection.

        *New in version 2.2.0*

        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionTest
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connection.test_connection()
        """
        _response = self._raw_client.test_connection(
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    def get_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Connection:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connection.get_connection(
            connection_id="connection_id",
        )
        """
        _response = self._raw_client.get_connection(connection_id, request_options=request_options)
        return _response.data

    def delete_connection(self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

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
        client.connection.delete_connection(
            connection_id="connection_id",
        )
        """
        _response = self._raw_client.delete_connection(connection_id, request_options=request_options)
        return _response.data

    def patch_connection(
        self,
        connection_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Connection:
        """
        Parameters
        ----------
        connection_id_ : str
            The connection ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
            Success.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.connection.patch_connection(
            connection_id_="connection_id",
        )
        """
        _response = self._raw_client.patch_connection(
            connection_id_,
            update_mask=update_mask,
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data


class AsyncConnectionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectionClient
        """
        return self._raw_client

    async def get_connections(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionCollection:
        """
        Parameters
        ----------
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
        ConnectionCollection
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
            await client.connection.get_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connections(
            limit=limit, offset=offset, order_by=order_by, request_options=request_options
        )
        return _response.data

    async def post_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Connection:
        """
        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
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
            await client.connection.post_connection()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_connection(
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    async def test_connection(
        self,
        *,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectionTest:
        """
        Test a connection.

        *New in version 2.2.0*

        Parameters
        ----------
        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionTest
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
            await client.connection.test_connection()


        asyncio.run(main())
        """
        _response = await self._raw_client.test_connection(
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    async def get_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Connection:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
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
            await client.connection.get_connection(
                connection_id="connection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_connection(connection_id, request_options=request_options)
        return _response.data

    async def delete_connection(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        connection_id : str
            The connection ID.

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
            await client.connection.delete_connection(
                connection_id="connection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connection(connection_id, request_options=request_options)
        return _response.data

    async def patch_connection(
        self,
        connection_id_: str,
        *,
        update_mask: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        extra: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        conn_type: typing.Optional[str] = OMIT,
        connection_id: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        login: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        schema: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Connection:
        """
        Parameters
        ----------
        connection_id_ : str
            The connection ID.

        update_mask : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The fields to update on the resource. If absent or empty, all modifiable fields are updated.
            A comma-separated list of fully qualified names of fields.

        extra : typing.Optional[str]
            Other values that cannot be put into another field, e.g. RSA keys.

        password : typing.Optional[str]
            Password of the connection.

        conn_type : typing.Optional[str]
            The connection type.

        connection_id : typing.Optional[str]
            The connection ID.

        description : typing.Optional[str]
            The description of the connection.

        host : typing.Optional[str]
            Host of the connection.

        login : typing.Optional[str]
            Login of the connection.

        port : typing.Optional[int]
            Port of the connection.

        schema : typing.Optional[str]
            Schema of the connection.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Connection
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
            await client.connection.patch_connection(
                connection_id_="connection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_connection(
            connection_id_,
            update_mask=update_mask,
            extra=extra,
            password=password,
            conn_type=conn_type,
            connection_id=connection_id,
            description=description,
            host=host,
            login=login,
            port=port,
            schema=schema,
            request_options=request_options,
        )
        return _response.data
