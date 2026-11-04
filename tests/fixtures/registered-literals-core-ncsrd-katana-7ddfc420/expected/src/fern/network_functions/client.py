

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.net_func import NetFunc
from .raw_client import AsyncRawNetworkFunctionsClient, RawNetworkFunctionsClient


class NetworkFunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNetworkFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNetworkFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNetworkFunctionsClient
        """
        return self._raw_client

    def returns_a_list_of_the_network_function_on_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NetFunc]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NetFunc]
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network_functions.returns_a_list_of_the_network_function_on_the_platform()
        """
        _response = self._raw_client.returns_a_list_of_the_network_function_on_the_platform(
            request_options=request_options
        )
        return _response.data

    def add_a_network_function_on_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
        client.network_functions.add_a_network_function_on_the_platform()
        """
        _response = self._raw_client.add_a_network_function_on_the_platform(request_options=request_options)
        return _response.data

    def return_info_about_a_specific_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetFunc:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetFunc
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network_functions.return_info_about_a_specific_network_function_on_the_platform(
            func_id="func_id",
        )
        """
        _response = self._raw_client.return_info_about_a_specific_network_function_on_the_platform(
            func_id, request_options=request_options
        )
        return _response.data

    def add_or_update_a_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network_functions.add_or_update_a_network_function_on_the_platform(
            func_id="func_id",
        )
        """
        _response = self._raw_client.add_or_update_a_network_function_on_the_platform(
            func_id, request_options=request_options
        )
        return _response.data

    def delete_a_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.network_functions.delete_a_network_function_on_the_platform(
            func_id="func_id",
        )
        """
        _response = self._raw_client.delete_a_network_function_on_the_platform(func_id, request_options=request_options)
        return _response.data


class AsyncNetworkFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNetworkFunctionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNetworkFunctionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNetworkFunctionsClient
        """
        return self._raw_client

    async def returns_a_list_of_the_network_function_on_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[NetFunc]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[NetFunc]
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.network_functions.returns_a_list_of_the_network_function_on_the_platform()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_the_network_function_on_the_platform(
            request_options=request_options
        )
        return _response.data

    async def add_a_network_function_on_the_platform(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
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
            await client.network_functions.add_a_network_function_on_the_platform()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_a_network_function_on_the_platform(request_options=request_options)
        return _response.data

    async def return_info_about_a_specific_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetFunc:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetFunc
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.network_functions.return_info_about_a_specific_network_function_on_the_platform(
                func_id="func_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_info_about_a_specific_network_function_on_the_platform(
            func_id, request_options=request_options
        )
        return _response.data

    async def add_or_update_a_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

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
            await client.network_functions.add_or_update_a_network_function_on_the_platform(
                func_id="func_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_or_update_a_network_function_on_the_platform(
            func_id, request_options=request_options
        )
        return _response.data

    async def delete_a_network_function_on_the_platform(
        self, func_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        func_id : str
            ID of Network Function

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
            await client.network_functions.delete_a_network_function_on_the_platform(
                func_id="func_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_network_function_on_the_platform(
            func_id, request_options=request_options
        )
        return _response.data
