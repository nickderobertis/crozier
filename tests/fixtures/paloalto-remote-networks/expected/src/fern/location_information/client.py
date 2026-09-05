

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.location import Location
from ..types.location_information_response import LocationInformationResponse
from ..types.uuid_response import UuidResponse
from .raw_client import AsyncRawLocationInformationClient, RawLocationInformationClient


OMIT = typing.cast(typing.Any, ...)


class LocationInformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLocationInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLocationInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLocationInformationClient
        """
        return self._raw_client

    def get_v1location_informations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LocationInformationResponse:
        """
        Get the location information status of the given request ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationInformationResponse
            List of location mapped information and configurations.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.location_information.get_v1location_informations(
            id="id",
        )
        """
        _response = self._raw_client.get_v1location_informations(id=id, request_options=request_options)
        return _response.data

    def post_v1location_informations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        info_type: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Retrieve location-mapped information or configuration through a POST request and returns the request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        info_type : typing.Optional[str]
            Information type. For example, region information.

        description : typing.Optional[str]
            optional user description

        locations : typing.Optional[typing.Sequence[Location]]
            locations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.location_information.post_v1location_informations()
        """
        _response = self._raw_client.post_v1location_informations(
            sub_tenant_name=sub_tenant_name,
            info_type=info_type,
            description=description,
            locations=locations,
            request_options=request_options,
        )
        return _response.data


class AsyncLocationInformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLocationInformationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLocationInformationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLocationInformationClient
        """
        return self._raw_client

    async def get_v1location_informations(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> LocationInformationResponse:
        """
        Get the location information status of the given request ID.

        Parameters
        ----------
        id : str
            UUID for the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LocationInformationResponse
            List of location mapped information and configurations.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.location_information.get_v1location_informations(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1location_informations(id=id, request_options=request_options)
        return _response.data

    async def post_v1location_informations(
        self,
        *,
        sub_tenant_name: typing.Optional[str] = None,
        info_type: typing.Optional[str] = None,
        description: typing.Optional[str] = OMIT,
        locations: typing.Optional[typing.Sequence[Location]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UuidResponse:
        """
        Retrieve location-mapped information or configuration through a POST request and returns the request ID.

        Parameters
        ----------
        sub_tenant_name : typing.Optional[str]
            Sub-tenant name in a panorama multi-tenancy setup.

        info_type : typing.Optional[str]
            Information type. For example, region information.

        description : typing.Optional[str]
            optional user description

        locations : typing.Optional[typing.Sequence[Location]]
            locations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.location_information.post_v1location_informations()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1location_informations(
            sub_tenant_name=sub_tenant_name,
            info_type=info_type,
            description=description,
            locations=locations,
            request_options=request_options,
        )
        return _response.data
