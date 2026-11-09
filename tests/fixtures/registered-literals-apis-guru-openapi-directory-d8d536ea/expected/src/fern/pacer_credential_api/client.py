

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.pacer_credential import PacerCredential
from ..types.pacer_credential_list_response import PacerCredentialListResponse
from ..types.success import Success
from .raw_client import AsyncRawPacerCredentialApiClient, RawPacerCredentialApiClient


OMIT = typing.cast(typing.Any, ...)


class PacerCredentialApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPacerCredentialApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPacerCredentialApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPacerCredentialApiClient
        """
        return self._raw_client

    def get_pacer_credential(
        self, *, page_number: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PacerCredentialListResponse:
        """
        List registered PACER credentials.

        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the PACER credentials to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacerCredentialListResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pacer_credential_api.get_pacer_credential(
            page_number=1,
        )
        """
        _response = self._raw_client.get_pacer_credential(page_number=page_number, request_options=request_options)
        return _response.data

    def add_pacer_credential(
        self,
        *,
        pacer_user_id: str,
        password: str,
        default_pacer_client_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        Register PACER credentials with UniCourt.

        Parameters
        ----------
        pacer_user_id : str
            Pacer User Id.

        password : str
            Password.

        default_pacer_client_code : typing.Optional[str]
            Pacer Client Code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pacer_credential_api.add_pacer_credential(
            default_pacer_client_code="Test UniCourt API",
            pacer_user_id="URKYwer3tyh5r56gq2",
            password="your password",
        )
        """
        _response = self._raw_client.add_pacer_credential(
            pacer_user_id=pacer_user_id,
            password=password,
            default_pacer_client_code=default_pacer_client_code,
            request_options=request_options,
        )
        return _response.data

    def get_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PacerCredential:
        """
        Retrieve the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacerCredential
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pacer_credential_api.get_pacer_credential_by_id(
            pacer_user_id="URKYwer3tyh5r56gq2",
        )
        """
        _response = self._raw_client.get_pacer_credential_by_id(pacer_user_id, request_options=request_options)
        return _response.data

    def remove_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        De-register the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.pacer_credential_api.remove_pacer_credential_by_id(
            pacer_user_id="URKYwer3tyh5r56gq2",
        )
        """
        _response = self._raw_client.remove_pacer_credential_by_id(pacer_user_id, request_options=request_options)
        return _response.data


class AsyncPacerCredentialApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPacerCredentialApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPacerCredentialApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPacerCredentialApiClient
        """
        return self._raw_client

    async def get_pacer_credential(
        self, *, page_number: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> PacerCredentialListResponse:
        """
        List registered PACER credentials.

        Parameters
        ----------
        page_number : typing.Optional[int]
            The page number of the PACER credentials to be retrieved.<br>
              - Minimum: 1

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacerCredentialListResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pacer_credential_api.get_pacer_credential(
                page_number=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pacer_credential(
            page_number=page_number, request_options=request_options
        )
        return _response.data

    async def add_pacer_credential(
        self,
        *,
        pacer_user_id: str,
        password: str,
        default_pacer_client_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Success:
        """
        Register PACER credentials with UniCourt.

        Parameters
        ----------
        pacer_user_id : str
            Pacer User Id.

        password : str
            Password.

        default_pacer_client_code : typing.Optional[str]
            Pacer Client Code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pacer_credential_api.add_pacer_credential(
                default_pacer_client_code="Test UniCourt API",
                pacer_user_id="URKYwer3tyh5r56gq2",
                password="your password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_pacer_credential(
            pacer_user_id=pacer_user_id,
            password=password,
            default_pacer_client_code=default_pacer_client_code,
            request_options=request_options,
        )
        return _response.data

    async def get_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PacerCredential:
        """
        Retrieve the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PacerCredential
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pacer_credential_api.get_pacer_credential_by_id(
                pacer_user_id="URKYwer3tyh5r56gq2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pacer_credential_by_id(pacer_user_id, request_options=request_options)
        return _response.data

    async def remove_pacer_credential_by_id(
        self, pacer_user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Success:
        """
        De-register the PACER credentials for the specified PACER username.

        Parameters
        ----------
        pacer_user_id : str
            The PACER username for which PACER credentials are to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Success
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.pacer_credential_api.remove_pacer_credential_by_id(
                pacer_user_id="URKYwer3tyh5r56gq2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_pacer_credential_by_id(pacer_user_id, request_options=request_options)
        return _response.data
