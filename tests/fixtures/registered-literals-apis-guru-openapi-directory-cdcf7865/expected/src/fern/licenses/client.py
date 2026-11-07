

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLicensesClient, RawLicensesClient
from .types.license_list_response_item import LicenseListResponseItem
from .types.licenses_read_response import LicensesReadResponse


class LicensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLicensesClient
        """
        return self._raw_client

    def read(self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> LicensesReadResponse:
        """
        Retrieves the details of a license.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested license, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        license_id : str
            The unique identifier of the license.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LicensesReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.read(
            license_id="license_id",
        )
        """
        _response = self._raw_client.read(license_id, request_options=request_options)
        return _response.data

    def license_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseListResponseItem]:
        """
        A paginated list of licenses. The returned licenses are sorted by their name.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 licenses. Each resource in the array is a separate license object and contains the full representation of the license, meaning additional requests to a license's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include licenses that match your filters by utilizing the `filter` query parameter, e.g. [https://api.osf.io/v2/licenses/?filter[name]=apache](https://api.osf.io/v2/licenses/?filter[name]=apache).

        Licenses may be filtered by their `id`, and `name`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.licenses.license_list()
        """
        _response = self._raw_client.license_list(request_options=request_options)
        return _response.data


class AsyncLicensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLicensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLicensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLicensesClient
        """
        return self._raw_client

    async def read(
        self, license_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LicensesReadResponse:
        """
        Retrieves the details of a license.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested license, if the request is successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        license_id : str
            The unique identifier of the license.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LicensesReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.read(
                license_id="license_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(license_id, request_options=request_options)
        return _response.data

    async def license_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseListResponseItem]:
        """
        A paginated list of licenses. The returned licenses are sorted by their name.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `data` key contains an array of 10 licenses. Each resource in the array is a separate license object and contains the full representation of the license, meaning additional requests to a license's detail view are not necessary.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        This request should never return an error.
        #### Filtering
        You can optionally request that the response only include licenses that match your filters by utilizing the `filter` query parameter, e.g. [https://api.osf.io/v2/licenses/?filter[name]=apache](https://api.osf.io/v2/licenses/?filter[name]=apache).

        Licenses may be filtered by their `id`, and `name`.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.licenses.license_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.license_list(request_options=request_options)
        return _response.data
