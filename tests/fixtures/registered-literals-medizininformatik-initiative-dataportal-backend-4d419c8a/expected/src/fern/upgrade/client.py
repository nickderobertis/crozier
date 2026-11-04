

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ccdl import Ccdl
from ..types.data_extraction_query import DataExtractionQuery
from ..types.upgrade_wrapper import UpgradeWrapper
from .raw_client import AsyncRawUpgradeClient, RawUpgradeClient


OMIT = typing.cast(typing.Any, ...)


class UpgradeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpgradeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpgradeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpgradeClient
        """
        return self._raw_client

    def crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpgradeWrapper:
        """
        Some common problems can be automatically fixed by either removing parts of the CRTDL or renaming things. Try to fix as many as possible

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpgradeWrapper
            CRTDL upgrade finished. If any changes were made, they are listed in "annotations"

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.upgrade.crtdl()
        """
        _response = self._raw_client.crtdl(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data


class AsyncUpgradeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpgradeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpgradeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpgradeClient
        """
        return self._raw_client

    async def crtdl(
        self,
        *,
        display: typing.Optional[str] = OMIT,
        cohort_definition: typing.Optional[Ccdl] = OMIT,
        data_extraction: typing.Optional[DataExtractionQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpgradeWrapper:
        """
        Some common problems can be automatically fixed by either removing parts of the CRTDL or renaming things. Try to fix as many as possible

        Parameters
        ----------
        display : typing.Optional[str]

        cohort_definition : typing.Optional[Ccdl]

        data_extraction : typing.Optional[DataExtractionQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpgradeWrapper
            CRTDL upgrade finished. If any changes were made, they are listed in "annotations"

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upgrade.crtdl()


        asyncio.run(main())
        """
        _response = await self._raw_client.crtdl(
            display=display,
            cohort_definition=cohort_definition,
            data_extraction=data_extraction,
            request_options=request_options,
        )
        return _response.data
