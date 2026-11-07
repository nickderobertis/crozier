

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customise import Customise
from ..types.info import Info
from ..types.obligation_extended import ObligationExtended
from ..types.obligations_list import ObligationsList
from .raw_client import AsyncRawAdminClient, RawAdminClient


OMIT = typing.cast(typing.Any, ...)


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def get_obligations_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObligationsList:
        """
        Get the list of obligations in the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObligationsList
            The API information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.get_obligations_list()
        """
        _response = self._raw_client.get_obligations_list(request_options=request_options)
        return _response.data

    def get_obligations_data(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObligationExtended:
        """
        Get the details of a particular obligation from the server.

        Parameters
        ----------
        id : int
            Id of the obligation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObligationExtended
            The API information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.get_obligations_data(
            id=1,
        )
        """
        _response = self._raw_client.get_obligations_data(id, request_options=request_options)
        return _response.data

    def delete_obligations_data(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Info]:
        """
        Delete a particular obligation from the server.

        Parameters
        ----------
        id : int
            Id of the obligation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Obligation deleted.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.delete_obligations_data(
            id=1,
        )
        """
        _response = self._raw_client.delete_obligations_data(id, request_options=request_options)
        return _response.data

    def get_all_obligations_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObligationExtended]:
        """
        Get the details of all obligations from the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObligationExtended]
            The API information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.get_all_obligations_data()
        """
        _response = self._raw_client.get_all_obligations_data(request_options=request_options)
        return _response.data

    def get_customise_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Customise]:
        """
        Returns the admin configuration data from the server

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Customise]
            Config data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.get_customise_data()
        """
        _response = self._raw_client.get_customise_data(request_options=request_options)
        return _response.data

    def update_customise_data(
        self,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Updates the admin configuration data.

        Parameters
        ----------
        key : typing.Optional[str]
            Key of the field to be updated

        value : typing.Optional[str]
            Value of the field to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Config data

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.admin.update_customise_data()
        """
        _response = self._raw_client.update_customise_data(key=key, value=value, request_options=request_options)
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def get_obligations_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ObligationsList:
        """
        Get the list of obligations in the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObligationsList
            The API information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.get_obligations_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_obligations_list(request_options=request_options)
        return _response.data

    async def get_obligations_data(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ObligationExtended:
        """
        Get the details of a particular obligation from the server.

        Parameters
        ----------
        id : int
            Id of the obligation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ObligationExtended
            The API information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.get_obligations_data(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_obligations_data(id, request_options=request_options)
        return _response.data

    async def delete_obligations_data(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Info]:
        """
        Delete a particular obligation from the server.

        Parameters
        ----------
        id : int
            Id of the obligation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Obligation deleted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.delete_obligations_data(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_obligations_data(id, request_options=request_options)
        return _response.data

    async def get_all_obligations_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ObligationExtended]:
        """
        Get the details of all obligations from the server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ObligationExtended]
            The API information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.get_all_obligations_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_obligations_data(request_options=request_options)
        return _response.data

    async def get_customise_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Customise]:
        """
        Returns the admin configuration data from the server

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Customise]
            Config data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.get_customise_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_customise_data(request_options=request_options)
        return _response.data

    async def update_customise_data(
        self,
        *,
        key: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Updates the admin configuration data.

        Parameters
        ----------
        key : typing.Optional[str]
            Key of the field to be updated

        value : typing.Optional[str]
            Value of the field to be updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Config data

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.admin.update_customise_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_customise_data(key=key, value=value, request_options=request_options)
        return _response.data
