

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.connector_response import ConnectorResponse
from ..types.paginated_result_connector_preset_response import PaginatedResultConnectorPresetResponse
from ..types.paginated_result_connector_response import PaginatedResultConnectorResponse
from .raw_client import AsyncRawConnectorsClient, RawConnectorsClient


OMIT = typing.cast(typing.Any, ...)


class ConnectorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConnectorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConnectorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConnectorsClient
        """
        return self._raw_client

    def list_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultConnectorPresetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultConnectorPresetResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.list_presets()
        """
        _response = self._raw_client.list_presets(request_options=request_options)
        return _response.data

    def list_connectors(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultConnectorResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultConnectorResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.list_connectors()
        """
        _response = self._raw_client.list_connectors(request_options=request_options)
        return _response.data

    def create_connector(
        self,
        *,
        url: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        match_preset: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        url : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        match_preset : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.create_connector(
            url="url",
        )
        """
        _response = self._raw_client.create_connector(
            url=url,
            client_id=client_id,
            client_secret=client_secret,
            metadata=metadata,
            match_preset=match_preset,
            request_options=request_options,
        )
        return _response.data

    def read_connector(
        self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.read_connector(
            connector_id="connector_id",
        )
        """
        _response = self._raw_client.read_connector(connector_id, request_options=request_options)
        return _response.data

    def delete_connector(self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        connector_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.delete_connector(
            connector_id="connector_id",
        )
        """
        _response = self._raw_client.delete_connector(connector_id, request_options=request_options)
        return _response.data

    def connect_connector(
        self,
        connector_id: str,
        *,
        redirect_url: typing.Optional[str] = OMIT,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        redirect_url : typing.Optional[str]

        access_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.connect_connector(
            connector_id="connector_id",
        )
        """
        _response = self._raw_client.connect_connector(
            connector_id, redirect_url=redirect_url, access_token=access_token, request_options=request_options
        )
        return _response.data

    def disconnect_connector(
        self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.disconnect_connector(
            connector_id="connector_id",
        )
        """
        _response = self._raw_client.disconnect_connector(connector_id, request_options=request_options)
        return _response.data

    def mcp(self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.mcp(
            connector_id="connector_id",
        )
        """
        _response = self._raw_client.mcp(connector_id, request_options=request_options)
        return _response.data

    def oauth_callback(
        self,
        *,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        state : str

        error : typing.Optional[str]

        error_description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.connectors.oauth_callback(
            state="state",
        )
        """
        _response = self._raw_client.oauth_callback(
            state=state, error=error, error_description=error_description, request_options=request_options
        )
        return _response.data


class AsyncConnectorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConnectorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConnectorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConnectorsClient
        """
        return self._raw_client

    async def list_presets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultConnectorPresetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultConnectorPresetResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.list_presets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_presets(request_options=request_options)
        return _response.data

    async def list_connectors(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PaginatedResultConnectorResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResultConnectorResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.list_connectors()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connectors(request_options=request_options)
        return _response.data

    async def create_connector(
        self,
        *,
        url: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        match_preset: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        url : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        match_preset : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.create_connector(
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_connector(
            url=url,
            client_id=client_id,
            client_secret=client_secret,
            metadata=metadata,
            match_preset=match_preset,
            request_options=request_options,
        )
        return _response.data

    async def read_connector(
        self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.read_connector(
                connector_id="connector_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_connector(connector_id, request_options=request_options)
        return _response.data

    async def delete_connector(
        self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        connector_id : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.delete_connector(
                connector_id="connector_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_connector(connector_id, request_options=request_options)
        return _response.data

    async def connect_connector(
        self,
        connector_id: str,
        *,
        redirect_url: typing.Optional[str] = OMIT,
        access_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        redirect_url : typing.Optional[str]

        access_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.connect_connector(
                connector_id="connector_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_connector(
            connector_id, redirect_url=redirect_url, access_token=access_token, request_options=request_options
        )
        return _response.data

    async def disconnect_connector(
        self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectorResponse:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectorResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.disconnect_connector(
                connector_id="connector_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect_connector(connector_id, request_options=request_options)
        return _response.data

    async def mcp(self, connector_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        connector_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.mcp(
                connector_id="connector_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mcp(connector_id, request_options=request_options)
        return _response.data

    async def oauth_callback(
        self,
        *,
        state: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        state : str

        error : typing.Optional[str]

        error_description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.connectors.oauth_callback(
                state="state",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.oauth_callback(
            state=state, error=error, error_description=error_description, request_options=request_options
        )
        return _response.data
