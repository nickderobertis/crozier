

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.verification_email_response import VerificationEmailResponse
from .raw_client import AsyncRawManagementV1Client, RawManagementV1Client


OMIT = typing.cast(typing.Any, ...)


class ManagementV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementV1Client
        """
        return self._raw_client

    def send_verification_email(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerificationEmailResponse:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationEmailResponse
            Ok

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management_v1.send_verification_email(
            user_id="userId",
        )
        """
        _response = self._raw_client.send_verification_email(user_id=user_id, request_options=request_options)
        return _response.data


class AsyncManagementV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementV1Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementV1Client
        """
        return self._raw_client

    async def send_verification_email(
        self, *, user_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> VerificationEmailResponse:
        """
        Parameters
        ----------
        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerificationEmailResponse
            Ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management_v1.send_verification_email(
                user_id="userId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_verification_email(user_id=user_id, request_options=request_options)
        return _response.data
