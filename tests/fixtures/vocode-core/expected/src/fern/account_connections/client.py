

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_connection_page import AccountConnectionPage
from ..types.account_connection_params_request import AccountConnectionParamsRequest
from ..types.account_connection_response_model import AccountConnectionResponseModel
from ..types.account_connection_update_params_request import AccountConnectionUpdateParamsRequest
from ..types.add_to_steering_pool_request import AddToSteeringPoolRequest
from .raw_client import AsyncRawAccountConnectionsClient, RawAccountConnectionsClient


OMIT = typing.cast(typing.Any, ...)


class AccountConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAccountConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAccountConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAccountConnectionsClient
        """
        return self._raw_client

    def get_account_connection(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account_connections.get_account_connection(
            id="id",
        )
        """
        _response = self._raw_client.get_account_connection(id=id, request_options=request_options)
        return _response.data

    def list_account_connections(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountConnectionPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account_connections.list_account_connections()
        """
        _response = self._raw_client.list_account_connections(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def create_account_connection(
        self, *, request: AccountConnectionParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        request : AccountConnectionParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        from fern import (
            AccountConnectionParamsRequest_AccountConnectionOpenai,
            FernApi,
            OpenAiCredentials,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account_connections.create_account_connection(
            request=AccountConnectionParamsRequest_AccountConnectionOpenai(
                credentials=OpenAiCredentials(
                    openai_api_key="openai_api_key",
                ),
            ),
        )
        """
        _response = self._raw_client.create_account_connection(request=request, request_options=request_options)
        return _response.data

    def update_account_connection(
        self,
        *,
        id: str,
        request: AccountConnectionUpdateParamsRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        id : str

        request : AccountConnectionUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        from fern import (
            AccountConnectionUpdateParamsRequest_AccountConnectionOpenai,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account_connections.update_account_connection(
            id="id",
            request=AccountConnectionUpdateParamsRequest_AccountConnectionOpenai(),
        )
        """
        _response = self._raw_client.update_account_connection(id=id, request=request, request_options=request_options)
        return _response.data

    def add_to_steering_pool(
        self,
        *,
        id: str,
        request: typing.Optional[AddToSteeringPoolRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request : typing.Optional[AddToSteeringPoolRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import AddToSteeringPoolRequest, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.account_connections.add_to_steering_pool(
            id="id",
            request=AddToSteeringPoolRequest(),
        )
        """
        _response = self._raw_client.add_to_steering_pool(id=id, request=request, request_options=request_options)
        return _response.data

    def remove_from_steering_pool(
        self, *, id: str, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        phone_number : str

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
            token="YOUR_TOKEN",
        )
        client.account_connections.remove_from_steering_pool(
            id="id",
            phone_number="phone_number",
        )
        """
        _response = self._raw_client.remove_from_steering_pool(
            id=id, phone_number=phone_number, request_options=request_options
        )
        return _response.data


class AsyncAccountConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAccountConnectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAccountConnectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAccountConnectionsClient
        """
        return self._raw_client

    async def get_account_connection(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.get_account_connection(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_connection(id=id, request_options=request_options)
        return _response.data

    async def list_account_connections(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountConnectionPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.list_account_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_account_connections(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def create_account_connection(
        self, *, request: AccountConnectionParamsRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        request : AccountConnectionParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AccountConnectionParamsRequest_AccountConnectionOpenai,
            AsyncFernApi,
            OpenAiCredentials,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.create_account_connection(
                request=AccountConnectionParamsRequest_AccountConnectionOpenai(
                    credentials=OpenAiCredentials(
                        openai_api_key="openai_api_key",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_account_connection(request=request, request_options=request_options)
        return _response.data

    async def update_account_connection(
        self,
        *,
        id: str,
        request: AccountConnectionUpdateParamsRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountConnectionResponseModel:
        """
        Parameters
        ----------
        id : str

        request : AccountConnectionUpdateParamsRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountConnectionResponseModel
            Successful Response

        Examples
        --------
        import asyncio

        from fern import (
            AccountConnectionUpdateParamsRequest_AccountConnectionOpenai,
            AsyncFernApi,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.update_account_connection(
                id="id",
                request=AccountConnectionUpdateParamsRequest_AccountConnectionOpenai(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account_connection(
            id=id, request=request, request_options=request_options
        )
        return _response.data

    async def add_to_steering_pool(
        self,
        *,
        id: str,
        request: typing.Optional[AddToSteeringPoolRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        request : typing.Optional[AddToSteeringPoolRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AddToSteeringPoolRequest, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.add_to_steering_pool(
                id="id",
                request=AddToSteeringPoolRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_to_steering_pool(id=id, request=request, request_options=request_options)
        return _response.data

    async def remove_from_steering_pool(
        self, *, id: str, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        id : str

        phone_number : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.account_connections.remove_from_steering_pool(
                id="id",
                phone_number="phone_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_from_steering_pool(
            id=id, phone_number=phone_number, request_options=request_options
        )
        return _response.data
