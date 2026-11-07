

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.profile_data_list import ProfileDataList
from .raw_client import AsyncRawDseClient, RawDseClient


class DseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDseClient
        """
        return self._raw_client

    def get_profile_data(self, *, ids: str, request_options: typing.Optional[RequestOptions] = None) -> ProfileDataList:
        """
        Get profile data for all submitted ids. If a profile is not found, an error message will be supplied.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (here - mostly URLs) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileDataList
            Success, returning profiles - may contain profiles with error messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dse.get_profile_data(
            ids="https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab,https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/Procedure",
        )
        """
        _response = self._raw_client.get_profile_data(ids=ids, request_options=request_options)
        return _response.data


class AsyncDseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDseClient
        """
        return self._raw_client

    async def get_profile_data(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProfileDataList:
        """
        Get profile data for all submitted ids. If a profile is not found, an error message will be supplied.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (here - mostly URLs) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileDataList
            Success, returning profiles - may contain profiles with error messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dse.get_profile_data(
                ids="https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab,https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/Procedure",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_profile_data(ids=ids, request_options=request_options)
        return _response.data
