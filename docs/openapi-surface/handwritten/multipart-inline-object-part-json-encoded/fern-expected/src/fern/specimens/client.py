

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSpecimensClient, RawSpecimensClient
from .types.upload_specimen_request_label import UploadSpecimenRequestLabel


OMIT = typing.cast(typing.Any, ...)


class SpecimensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSpecimensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSpecimensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSpecimensClient
        """
        return self._raw_client

    def upload_specimen(
        self,
        *,
        image: core.File,
        label: UploadSpecimenRequestLabel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        label : UploadSpecimenRequestLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.specimens import UploadSpecimenRequestLabel

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.specimens.upload_specimen(
            label=UploadSpecimenRequestLabel(),
        )
        """
        _response = self._raw_client.upload_specimen(image=image, label=label, request_options=request_options)
        return _response.data


class AsyncSpecimensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSpecimensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSpecimensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSpecimensClient
        """
        return self._raw_client

    async def upload_specimen(
        self,
        *,
        image: core.File,
        label: UploadSpecimenRequestLabel,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        image : core.File
            See core.File for more documentation

        label : UploadSpecimenRequestLabel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.specimens import UploadSpecimenRequestLabel

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.specimens.upload_specimen(
                label=UploadSpecimenRequestLabel(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_specimen(image=image, label=label, request_options=request_options)
        return _response.data
