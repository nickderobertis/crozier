

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLockerClient, RawLockerClient


OMIT = typing.cast(typing.Any, ...)


class LockerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLockerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLockerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLockerClient
        """
        return self._raw_client

    def save_state(
        self,
        *,
        data: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        data : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Saved.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locker.save_state()
        """
        _response = self._raw_client.save_state(data=data, directory=directory, request_options=request_options)
        return _response.data

    def update_annotations(
        self,
        *,
        locker_id: str,
        data: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        locker_id : str

        data : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locker.update_annotations()
        """
        _response = self._raw_client.update_annotations(
            locker_id=locker_id, data=data, directory=directory, request_options=request_options
        )
        return _response.data

    def answer_control(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Answered.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locker.answer_control()
        """
        _response = self._raw_client.answer_control(
            request=request, directory=directory, request_options=request_options
        )
        return _response.data

    def create_workspace(
        self,
        *,
        kind: str,
        branch: typing.Optional[str] = OMIT,
        extra: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        kind : str

        branch : typing.Optional[str]

        extra : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.locker.create_workspace(
            kind="kind",
        )
        """
        _response = self._raw_client.create_workspace(
            kind=kind, branch=branch, extra=extra, request_options=request_options
        )
        return _response.data


class AsyncLockerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLockerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLockerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLockerClient
        """
        return self._raw_client

    async def save_state(
        self,
        *,
        data: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        data : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Saved.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locker.save_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.save_state(data=data, directory=directory, request_options=request_options)
        return _response.data

    async def update_annotations(
        self,
        *,
        locker_id: str,
        data: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        locker_id : str

        data : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locker.update_annotations()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_annotations(
            locker_id=locker_id, data=data, directory=directory, request_options=request_options
        )
        return _response.data

    async def answer_control(
        self,
        *,
        request: typing.Any,
        directory: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Any

        directory : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Answered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locker.answer_control()


        asyncio.run(main())
        """
        _response = await self._raw_client.answer_control(
            request=request, directory=directory, request_options=request_options
        )
        return _response.data

    async def create_workspace(
        self,
        *,
        kind: str,
        branch: typing.Optional[str] = OMIT,
        extra: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        kind : str

        branch : typing.Optional[str]

        extra : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.locker.create_workspace(
                kind="kind",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_workspace(
            kind=kind, branch=branch, extra=extra, request_options=request_options
        )
        return _response.data
