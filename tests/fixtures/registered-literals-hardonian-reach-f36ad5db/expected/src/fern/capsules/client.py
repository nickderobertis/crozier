

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.capsule import Capsule
from ..types.verification_result import VerificationResult
from .raw_client import AsyncRawCapsulesClient, RawCapsulesClient


OMIT = typing.cast(typing.Any, ...)


class CapsulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCapsulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCapsulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCapsulesClient
        """
        return self._raw_client

    def create_capsule(self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None) -> Capsule:
        """
        Create a time capsule (immutable artifact) from a completed run

        Parameters
        ----------
        run_id : str
            The run ID to create a capsule from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capsule
            Capsule created successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capsules.create_capsule(
            run_id="run-abc123",
        )
        """
        _response = self._raw_client.create_capsule(run_id=run_id, request_options=request_options)
        return _response.data

    def verify_capsule(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerificationResult:
        """
        Verify the integrity of a capsule file

        Parameters
        ----------
        path : str
            Path to the capsule file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.capsules.verify_capsule(
            path="path",
        )
        """
        _response = self._raw_client.verify_capsule(path=path, request_options=request_options)
        return _response.data


class AsyncCapsulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCapsulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCapsulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCapsulesClient
        """
        return self._raw_client

    async def create_capsule(self, *, run_id: str, request_options: typing.Optional[RequestOptions] = None) -> Capsule:
        """
        Create a time capsule (immutable artifact) from a completed run

        Parameters
        ----------
        run_id : str
            The run ID to create a capsule from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Capsule
            Capsule created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capsules.create_capsule(
                run_id="run-abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_capsule(run_id=run_id, request_options=request_options)
        return _response.data

    async def verify_capsule(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerificationResult:
        """
        Verify the integrity of a capsule file

        Parameters
        ----------
        path : str
            Path to the capsule file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationResult
            Verification result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.capsules.verify_capsule(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_capsule(path=path, request_options=request_options)
        return _response.data
