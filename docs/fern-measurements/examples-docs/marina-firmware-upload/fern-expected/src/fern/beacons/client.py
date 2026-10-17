

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBeaconsClient, RawBeaconsClient


OMIT = typing.cast(typing.Any, ...)


class BeaconsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeaconsClient
        """
        return self._raw_client

    def upload_firmware(
        self,
        *,
        firmware_manifest_version: str,
        image: str,
        version: typing.Optional[str] = None,
        signed: typing.Optional[str] = None,
        firmware_manifest_signed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        firmware_manifest_version : str

        image : str

        version : typing.Optional[str]

        signed : typing.Optional[str]

        firmware_manifest_signed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.upload_firmware(
            version="2.4.1",
            firmware_manifest_version="version",
            image="image",
        )
        """
        _response = self._raw_client.upload_firmware(
            firmware_manifest_version=firmware_manifest_version,
            image=image,
            version=version,
            signed=signed,
            firmware_manifest_signed=firmware_manifest_signed,
            request_options=request_options,
        )
        return _response.data

    def update_firmware(
        self,
        beacon_id: str,
        *,
        channel: typing.Optional[str] = None,
        firmware_patch_channel: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        beacon_id : str

        channel : typing.Optional[str]

        firmware_patch_channel : typing.Optional[str]

        image : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.beacons.update_firmware(
            beacon_id="beacon_id",
        )
        """
        _response = self._raw_client.update_firmware(
            beacon_id,
            channel=channel,
            firmware_patch_channel=firmware_patch_channel,
            image=image,
            request_options=request_options,
        )
        return _response.data


class AsyncBeaconsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeaconsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBeaconsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeaconsClient
        """
        return self._raw_client

    async def upload_firmware(
        self,
        *,
        firmware_manifest_version: str,
        image: str,
        version: typing.Optional[str] = None,
        signed: typing.Optional[str] = None,
        firmware_manifest_signed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        firmware_manifest_version : str

        image : str

        version : typing.Optional[str]

        signed : typing.Optional[str]

        firmware_manifest_signed : typing.Optional[bool]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.upload_firmware(
                version="2.4.1",
                firmware_manifest_version="version",
                image="image",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_firmware(
            firmware_manifest_version=firmware_manifest_version,
            image=image,
            version=version,
            signed=signed,
            firmware_manifest_signed=firmware_manifest_signed,
            request_options=request_options,
        )
        return _response.data

    async def update_firmware(
        self,
        beacon_id: str,
        *,
        channel: typing.Optional[str] = None,
        firmware_patch_channel: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        beacon_id : str

        channel : typing.Optional[str]

        firmware_patch_channel : typing.Optional[str]

        image : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.beacons.update_firmware(
                beacon_id="beacon_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_firmware(
            beacon_id,
            channel=channel,
            firmware_patch_channel=firmware_patch_channel,
            image=image,
            request_options=request_options,
        )
        return _response.data
