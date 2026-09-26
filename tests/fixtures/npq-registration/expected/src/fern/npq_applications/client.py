

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.application_response import ApplicationResponse
from ..types.applications_response import ApplicationsResponse
from ..types.id_attribute import IdAttribute
from ..types.list_applications_filter import ListApplicationsFilter
from ..types.pagination_filter import PaginationFilter
from ..types.sorting_options import SortingOptions
from .raw_client import AsyncRawNpqApplicationsClient, RawNpqApplicationsClient
from .types.application_accept_request_data import ApplicationAcceptRequestData
from .types.application_change_funded_place_request_data import ApplicationChangeFundedPlaceRequestData


OMIT = typing.cast(typing.Any, ...)


class NpqApplicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNpqApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNpqApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNpqApplicationsClient
        """
        return self._raw_client

    def retrieve_multiple_npq_applications(
        self,
        *,
        filter: typing.Optional[ListApplicationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListApplicationsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationsResponse
            A list of NPQ applications

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_applications.retrieve_multiple_npq_applications()
        """
        _response = self._raw_client.retrieve_multiple_npq_applications(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data

    def retrieve_a_single_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            A single NPQ application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_applications.retrieve_a_single_npq_application(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.retrieve_a_single_npq_application(id, request_options=request_options)
        return _response.data

    def accept_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationAcceptRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationAcceptRequestData
            A NPQ application acceptance request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application being accepted

        Examples
        --------
        from fern.npq_applications import ApplicationAcceptRequestData

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_applications.accept_an_npq_application(
            id="id",
            data=ApplicationAcceptRequestData(
                type="type",
                attributes={"key": "value"},
            ),
        )
        """
        _response = self._raw_client.accept_an_npq_application(id, data=data, request_options=request_options)
        return _response.data

    def reject_an_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application being rejected

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_applications.reject_an_npq_application(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
        )
        """
        _response = self._raw_client.reject_an_npq_application(id, request_options=request_options)
        return _response.data

    def change_funded_place_value_of_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationChangeFundedPlaceRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationChangeFundedPlaceRequestData
            A NPQ application change funded place request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application after changing the funded place

        Examples
        --------
        from fern.npq_applications import (
            ApplicationChangeFundedPlaceRequestData,
            ApplicationChangeFundedPlaceRequestDataAttributes,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.npq_applications.change_funded_place_value_of_an_npq_application(
            id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            data=ApplicationChangeFundedPlaceRequestData(
                type="npq-application-change-funded-place",
                attributes=ApplicationChangeFundedPlaceRequestDataAttributes(
                    funded_place=True,
                ),
            ),
        )
        """
        _response = self._raw_client.change_funded_place_value_of_an_npq_application(
            id, data=data, request_options=request_options
        )
        return _response.data


class AsyncNpqApplicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNpqApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNpqApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNpqApplicationsClient
        """
        return self._raw_client

    async def retrieve_multiple_npq_applications(
        self,
        *,
        filter: typing.Optional[ListApplicationsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        sort: typing.Optional[SortingOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationsResponse:
        """
        Parameters
        ----------
        filter : typing.Optional[ListApplicationsFilter]

        page : typing.Optional[PaginationFilter]

        sort : typing.Optional[SortingOptions]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationsResponse
            A list of NPQ applications

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_applications.retrieve_multiple_npq_applications()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_multiple_npq_applications(
            filter=filter, page=page, sort=sort, request_options=request_options
        )
        return _response.data

    async def retrieve_a_single_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            A single NPQ application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_applications.retrieve_a_single_npq_application(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_single_npq_application(id, request_options=request_options)
        return _response.data

    async def accept_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationAcceptRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationAcceptRequestData
            A NPQ application acceptance request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application being accepted

        Examples
        --------
        import asyncio

        from fern.npq_applications import ApplicationAcceptRequestData

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_applications.accept_an_npq_application(
                id="id",
                data=ApplicationAcceptRequestData(
                    type="type",
                    attributes={"key": "value"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_an_npq_application(id, data=data, request_options=request_options)
        return _response.data

    async def reject_an_npq_application(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application being rejected

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_applications.reject_an_npq_application(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reject_an_npq_application(id, request_options=request_options)
        return _response.data

    async def change_funded_place_value_of_an_npq_application(
        self,
        id: IdAttribute,
        *,
        data: ApplicationChangeFundedPlaceRequestData,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationResponse:
        """
        Parameters
        ----------
        id : IdAttribute

        data : ApplicationChangeFundedPlaceRequestData
            A NPQ application change funded place request data

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationResponse
            The NPQ application after changing the funded place

        Examples
        --------
        import asyncio

        from fern.npq_applications import (
            ApplicationChangeFundedPlaceRequestData,
            ApplicationChangeFundedPlaceRequestDataAttributes,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.npq_applications.change_funded_place_value_of_an_npq_application(
                id="d0b4a32e-a272-489e-b30a-cb17131457fc",
                data=ApplicationChangeFundedPlaceRequestData(
                    type="npq-application-change-funded-place",
                    attributes=ApplicationChangeFundedPlaceRequestDataAttributes(
                        funded_place=True,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.change_funded_place_value_of_an_npq_application(
            id, data=data, request_options=request_options
        )
        return _response.data
