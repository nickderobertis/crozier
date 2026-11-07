

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.key_entry_v2 import KeyEntryV2
from .raw_client import AsyncRawKeysClient, RawKeysClient
from .types.lookup_key_response import LookupKeyResponse
from .types.rotate_key_response import RotateKeyResponse


OMIT = typing.cast(typing.Any, ...)


class KeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeysClient
        """
        return self._raw_client

    def lookup_key(self, kid: str, *, request_options: typing.Optional[RequestOptions] = None) -> LookupKeyResponse:
        """
        Parameters
        ----------
        kid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LookupKeyResponse
            Key found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.keys.lookup_key(
            kid="kid",
        )
        """
        _response = self._raw_client.lookup_key(kid, request_options=request_options)
        return _response.data

    def rotate_key(
        self,
        *,
        old_kid: str,
        new_key: KeyEntryV2,
        proof_of_possession: typing.Dict[str, typing.Any],
        authorization_sig: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RotateKeyResponse:
        """
        Parameters
        ----------
        old_kid : str

        new_key : KeyEntryV2

        proof_of_possession : typing.Dict[str, typing.Any]

        authorization_sig : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RotateKeyResponse
            Key rotated

        Examples
        --------
        from fern import FernApi, KeyEntryV2

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.keys.rotate_key(
            old_kid="old_kid",
            new_key=KeyEntryV2(),
            proof_of_possession={"key": "value"},
        )
        """
        _response = self._raw_client.rotate_key(
            old_kid=old_kid,
            new_key=new_key,
            proof_of_possession=proof_of_possession,
            authorization_sig=authorization_sig,
            request_options=request_options,
        )
        return _response.data


class AsyncKeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeysClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeysClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeysClient
        """
        return self._raw_client

    async def lookup_key(
        self, kid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LookupKeyResponse:
        """
        Parameters
        ----------
        kid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LookupKeyResponse
            Key found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.keys.lookup_key(
                kid="kid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.lookup_key(kid, request_options=request_options)
        return _response.data

    async def rotate_key(
        self,
        *,
        old_kid: str,
        new_key: KeyEntryV2,
        proof_of_possession: typing.Dict[str, typing.Any],
        authorization_sig: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RotateKeyResponse:
        """
        Parameters
        ----------
        old_kid : str

        new_key : KeyEntryV2

        proof_of_possession : typing.Dict[str, typing.Any]

        authorization_sig : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RotateKeyResponse
            Key rotated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, KeyEntryV2

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.keys.rotate_key(
                old_kid="old_kid",
                new_key=KeyEntryV2(),
                proof_of_possession={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate_key(
            old_kid=old_kid,
            new_key=new_key,
            proof_of_possession=proof_of_possession,
            authorization_sig=authorization_sig,
            request_options=request_options,
        )
        return _response.data
