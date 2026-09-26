

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.room import Room
from .raw_client import AsyncRawRoomsClient, RawRoomsClient


class RoomsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoomsClient
        """
        return self._raw_client

    def get_rooms_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Optional[Room]]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. school_id is required. Returns an unpaginated list.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[Room]]
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.get_rooms_v3(
            company_id="11111111-1111-4111-8111-111111111111",
            school_id="22222222-2222-4222-8222-222222222222",
        )
        """
        _response = self._raw_client.get_rooms_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    def get_rooms_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The room ID identifies the room; school_id is not required.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Room
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rooms.get_rooms_id_v3(
            id="id",
            company_id="11111111-1111-4111-8111-111111111111",
        )
        """
        _response = self._raw_client.get_rooms_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data


class AsyncRoomsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoomsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoomsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoomsClient
        """
        return self._raw_client

    async def get_rooms_v3(
        self, *, company_id: str, school_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Optional[Room]]:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. school_id is required. Returns an unpaginated list.

        Parameters
        ----------
        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        school_id : str
            School UUID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[Room]]
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.get_rooms_v3(
                company_id="11111111-1111-4111-8111-111111111111",
                school_id="22222222-2222-4222-8222-222222222222",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rooms_v3(
            company_id=company_id, school_id=school_id, request_options=request_options
        )
        return _response.data

    async def get_rooms_id_v3(
        self, id: str, *, company_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Room:
        """
        Scoped to company_id; the handler does not restrict this read to the session school assignments. The room ID identifies the room; school_id is not required.

        Parameters
        ----------
        id : str
            UUID identifying this resource.

        company_id : str
            Company UUID. Must equal the authenticated session company when that session has a company assigned; the equality check is skipped for sessions without one.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Room
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rooms.get_rooms_id_v3(
                id="id",
                company_id="11111111-1111-4111-8111-111111111111",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_rooms_id_v3(id, company_id=company_id, request_options=request_options)
        return _response.data
