

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.email_settings import EmailSettings
from ..types.ereader_device_object import EreaderDeviceObject
from ..types.ereader_name import EreaderName
from ..types.library_item_id import LibraryItemId
from .raw_client import AsyncRawEmailClient, RawEmailClient
from .types.update_e_reader_devices_response import UpdateEReaderDevicesResponse


OMIT = typing.cast(typing.Any, ...)


class EmailClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmailClient
        """
        return self._raw_client

    def get_email_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmailSettings:
        """
        Get email settings for sending e-books to e-readers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailSettings
            Successful response - Email

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.email.get_email_settings()
        """
        _response = self._raw_client.get_email_settings(request_options=request_options)
        return _response.data

    def update_email_settings(
        self,
        *,
        id: str,
        port: int,
        secure: bool,
        ereader_devices: typing.Sequence[EreaderDeviceObject],
        host: typing.Optional[str] = OMIT,
        reject_unauthorized: typing.Optional[bool] = OMIT,
        user: typing.Optional[str] = OMIT,
        pass_: typing.Optional[str] = OMIT,
        test_address: typing.Optional[str] = OMIT,
        from_address: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailSettings:
        """
        Parameters
        ----------
        id : str
            The unique identifier for the email settings. Currently this is always `email-settings`

        port : int
            The port number for the SMTP server.

        secure : bool
            Indicates if the connection should use SSL/TLS.

        ereader_devices : typing.Sequence[EreaderDeviceObject]
            List of configured e-reader devices.

        host : typing.Optional[str]
            The SMTP host address.

        reject_unauthorized : typing.Optional[bool]
            Indicates if unauthorized SSL/TLS certificates should be rejected.

        user : typing.Optional[str]
            The username for SMTP authentication.

        pass_ : typing.Optional[str]
            The password for SMTP authentication.

        test_address : typing.Optional[str]
            The test email address used for sending test emails.

        from_address : typing.Optional[str]
            The default "from" email address for outgoing emails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailSettings
            Successful response - Email

        Examples
        --------
        from fern import (
            EreaderDeviceObject,
            EreaderDeviceObjectAvailabilityOption,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.email.update_email_settings(
            id="email-settings",
            port=465,
            secure=True,
            ereader_devices=[
                EreaderDeviceObject(
                    name="name",
                    email="email",
                    availability_option=EreaderDeviceObjectAvailabilityOption.ADMIN_OR_UP,
                )
            ],
        )
        """
        _response = self._raw_client.update_email_settings(
            id=id,
            port=port,
            secure=secure,
            ereader_devices=ereader_devices,
            host=host,
            reject_unauthorized=reject_unauthorized,
            user=user,
            pass_=pass_,
            test_address=test_address,
            from_address=from_address,
            request_options=request_options,
        )
        return _response.data

    def send_test_email(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.email.send_test_email()
        """
        _response = self._raw_client.send_test_email(request_options=request_options)
        return _response.data

    def update_e_reader_devices(
        self,
        *,
        ereader_devices: typing.Optional[typing.Sequence[EreaderDeviceObject]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateEReaderDevicesResponse:
        """
        Parameters
        ----------
        ereader_devices : typing.Optional[typing.Sequence[EreaderDeviceObject]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateEReaderDevicesResponse
            Successful response - Ereader

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.email.update_e_reader_devices()
        """
        _response = self._raw_client.update_e_reader_devices(
            ereader_devices=ereader_devices, request_options=request_options
        )
        return _response.data

    def send_e_book_to_device(
        self,
        *,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        device_name: typing.Optional[EreaderName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        library_item_id : typing.Optional[LibraryItemId]

        device_name : typing.Optional[EreaderName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.email.send_e_book_to_device()
        """
        _response = self._raw_client.send_e_book_to_device(
            library_item_id=library_item_id, device_name=device_name, request_options=request_options
        )
        return _response.data


class AsyncEmailClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmailClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmailClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmailClient
        """
        return self._raw_client

    async def get_email_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> EmailSettings:
        """
        Get email settings for sending e-books to e-readers.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailSettings
            Successful response - Email

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.email.get_email_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_email_settings(request_options=request_options)
        return _response.data

    async def update_email_settings(
        self,
        *,
        id: str,
        port: int,
        secure: bool,
        ereader_devices: typing.Sequence[EreaderDeviceObject],
        host: typing.Optional[str] = OMIT,
        reject_unauthorized: typing.Optional[bool] = OMIT,
        user: typing.Optional[str] = OMIT,
        pass_: typing.Optional[str] = OMIT,
        test_address: typing.Optional[str] = OMIT,
        from_address: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmailSettings:
        """
        Parameters
        ----------
        id : str
            The unique identifier for the email settings. Currently this is always `email-settings`

        port : int
            The port number for the SMTP server.

        secure : bool
            Indicates if the connection should use SSL/TLS.

        ereader_devices : typing.Sequence[EreaderDeviceObject]
            List of configured e-reader devices.

        host : typing.Optional[str]
            The SMTP host address.

        reject_unauthorized : typing.Optional[bool]
            Indicates if unauthorized SSL/TLS certificates should be rejected.

        user : typing.Optional[str]
            The username for SMTP authentication.

        pass_ : typing.Optional[str]
            The password for SMTP authentication.

        test_address : typing.Optional[str]
            The test email address used for sending test emails.

        from_address : typing.Optional[str]
            The default "from" email address for outgoing emails.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmailSettings
            Successful response - Email

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            EreaderDeviceObject,
            EreaderDeviceObjectAvailabilityOption,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.email.update_email_settings(
                id="email-settings",
                port=465,
                secure=True,
                ereader_devices=[
                    EreaderDeviceObject(
                        name="name",
                        email="email",
                        availability_option=EreaderDeviceObjectAvailabilityOption.ADMIN_OR_UP,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_email_settings(
            id=id,
            port=port,
            secure=secure,
            ereader_devices=ereader_devices,
            host=host,
            reject_unauthorized=reject_unauthorized,
            user=user,
            pass_=pass_,
            test_address=test_address,
            from_address=from_address,
            request_options=request_options,
        )
        return _response.data

    async def send_test_email(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.email.send_test_email()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_test_email(request_options=request_options)
        return _response.data

    async def update_e_reader_devices(
        self,
        *,
        ereader_devices: typing.Optional[typing.Sequence[EreaderDeviceObject]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateEReaderDevicesResponse:
        """
        Parameters
        ----------
        ereader_devices : typing.Optional[typing.Sequence[EreaderDeviceObject]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateEReaderDevicesResponse
            Successful response - Ereader

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.email.update_e_reader_devices()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_e_reader_devices(
            ereader_devices=ereader_devices, request_options=request_options
        )
        return _response.data

    async def send_e_book_to_device(
        self,
        *,
        library_item_id: typing.Optional[LibraryItemId] = OMIT,
        device_name: typing.Optional[EreaderName] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        library_item_id : typing.Optional[LibraryItemId]

        device_name : typing.Optional[EreaderName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.email.send_e_book_to_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_e_book_to_device(
            library_item_id=library_item_id, device_name=device_name, request_options=request_options
        )
        return _response.data
