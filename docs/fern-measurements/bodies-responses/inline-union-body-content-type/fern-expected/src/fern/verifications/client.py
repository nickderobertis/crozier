

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVerificationsClient, RawVerificationsClient
from .types.add_contact_request import AddContactRequest
from .types.add_tagged_contact_request import AddTaggedContactRequest
from .types.add_verification_request import AddVerificationRequest
from .types.recheck_verification_request import RecheckVerificationRequest
from .types.send_notice_request import SendNoticeRequest
from .types.send_reminder_request import SendReminderRequest


OMIT = typing.cast(typing.Any, ...)


class VerificationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVerificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVerificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVerificationsClient
        """
        return self._raw_client

    def add_verification(
        self, *, request: AddVerificationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddVerificationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import AddVerificationRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.add_verification(
            request=AddVerificationRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.add_verification(request=request, request_options=request_options)
        return _response.data

    def recheck_verification(
        self, *, request: RecheckVerificationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : RecheckVerificationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import RecheckVerificationRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.recheck_verification(
            request=RecheckVerificationRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.recheck_verification(request=request, request_options=request_options)
        return _response.data

    def send_reminder(
        self, *, request: SendReminderRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : SendReminderRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import SendReminderRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.send_reminder(
            request=SendReminderRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.send_reminder(request=request, request_options=request_options)
        return _response.data

    def send_notice(
        self, *, request: SendNoticeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : SendNoticeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import SendNoticeRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.send_notice(
            request=SendNoticeRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.send_notice(request=request, request_options=request_options)
        return _response.data

    def add_contact(
        self, *, request: AddContactRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddContactRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import AddContactRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.add_contact(
            request=AddContactRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.add_contact(request=request, request_options=request_options)
        return _response.data

    def add_tagged_contact(
        self, *, request: AddTaggedContactRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddTaggedContactRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.verifications import AddTaggedContactRequest_Email

        from fern import FernApi

        client = FernApi()
        client.verifications.add_tagged_contact(
            request=AddTaggedContactRequest_Email(
                email="email",
            ),
        )
        """
        _response = self._raw_client.add_tagged_contact(request=request, request_options=request_options)
        return _response.data


class AsyncVerificationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVerificationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVerificationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVerificationsClient
        """
        return self._raw_client

    async def add_verification(
        self, *, request: AddVerificationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddVerificationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import AddVerificationRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.add_verification(
                request=AddVerificationRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_verification(request=request, request_options=request_options)
        return _response.data

    async def recheck_verification(
        self, *, request: RecheckVerificationRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : RecheckVerificationRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import RecheckVerificationRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.recheck_verification(
                request=RecheckVerificationRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.recheck_verification(request=request, request_options=request_options)
        return _response.data

    async def send_reminder(
        self, *, request: SendReminderRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : SendReminderRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import SendReminderRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.send_reminder(
                request=SendReminderRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_reminder(request=request, request_options=request_options)
        return _response.data

    async def send_notice(
        self, *, request: SendNoticeRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : SendNoticeRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import SendNoticeRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.send_notice(
                request=SendNoticeRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_notice(request=request, request_options=request_options)
        return _response.data

    async def add_contact(
        self, *, request: AddContactRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddContactRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import AddContactRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.add_contact(
                request=AddContactRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_contact(request=request, request_options=request_options)
        return _response.data

    async def add_tagged_contact(
        self, *, request: AddTaggedContactRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : AddTaggedContactRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.verifications import AddTaggedContactRequest_Email

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.verifications.add_tagged_contact(
                request=AddTaggedContactRequest_Email(
                    email="email",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_tagged_contact(request=request, request_options=request_options)
        return _response.data
