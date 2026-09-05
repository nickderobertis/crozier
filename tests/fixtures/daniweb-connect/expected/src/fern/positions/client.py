

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_delete_positions_id import EndpointDeletePositionsId
from ..types.endpoint_patch_positions_id import EndpointPatchPositionsId
from ..types.endpoint_post_positions import EndpointPostPositions
from .raw_client import AsyncRawPositionsClient, RawPositionsClient
from .types.patch_positions_id_request_category import PatchPositionsIdRequestCategory
from .types.patch_positions_id_request_organization_size import PatchPositionsIdRequestOrganizationSize
from .types.patch_positions_id_request_position import PatchPositionsIdRequestPosition
from .types.post_positions_request_category import PostPositionsRequestCategory
from .types.post_positions_request_organization_size import PostPositionsRequestOrganizationSize
from .types.post_positions_request_position import PostPositionsRequestPosition


OMIT = typing.cast(typing.Any, ...)


class PositionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPositionsClient
        """
        return self._raw_client

    def post_positions(
        self,
        *,
        category: PostPositionsRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PostPositionsRequestOrganizationSize] = OMIT,
        position: typing.Optional[PostPositionsRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostPositions:
        """
        Update the OAuth'ed end user's Curriculum Vitae by adding a position.

        Parameters
        ----------
        category : PostPositionsRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PostPositionsRequestOrganizationSize]

        position : typing.Optional[PostPositionsRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostPositions
            Valid Response

        Examples
        --------
        from fern.positions import PostPositionsRequestCategory

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.positions.post_positions(
            category=PostPositionsRequestCategory.EXPERIENCE,
            organization="organization",
            role="role",
            start_date="start_date",
        )
        """
        _response = self._raw_client.post_positions(
            category=category,
            organization=organization,
            role=role,
            start_date=start_date,
            end_date=end_date,
            organization_size=organization_size,
            position=position,
            summary=summary,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def delete_positions_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointDeletePositionsId:
        """
        Remove an item from the OAuth'ed end user's Curriculum Vitae.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointDeletePositionsId
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.positions.delete_positions_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_positions_id(id, request_options=request_options)
        return _response.data

    def patch_positions_id(
        self,
        id: int,
        *,
        category: PatchPositionsIdRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PatchPositionsIdRequestOrganizationSize] = OMIT,
        position: typing.Optional[PatchPositionsIdRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchPositionsId:
        """
        Update the OAuth'ed end user's Curriculum Vitae by modifying an existing position.

        Parameters
        ----------
        id : int

        category : PatchPositionsIdRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PatchPositionsIdRequestOrganizationSize]

        position : typing.Optional[PatchPositionsIdRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchPositionsId
            Valid Response

        Examples
        --------
        from fern.positions import PatchPositionsIdRequestCategory

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.positions.patch_positions_id(
            id=1,
            category=PatchPositionsIdRequestCategory.EXPERIENCE,
            organization="organization",
            role="role",
            start_date="start_date",
        )
        """
        _response = self._raw_client.patch_positions_id(
            id,
            category=category,
            organization=organization,
            role=role,
            start_date=start_date,
            end_date=end_date,
            organization_size=organization_size,
            position=position,
            summary=summary,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncPositionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPositionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPositionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPositionsClient
        """
        return self._raw_client

    async def post_positions(
        self,
        *,
        category: PostPositionsRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PostPositionsRequestOrganizationSize] = OMIT,
        position: typing.Optional[PostPositionsRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostPositions:
        """
        Update the OAuth'ed end user's Curriculum Vitae by adding a position.

        Parameters
        ----------
        category : PostPositionsRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PostPositionsRequestOrganizationSize]

        position : typing.Optional[PostPositionsRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostPositions
            Valid Response

        Examples
        --------
        import asyncio

        from fern.positions import PostPositionsRequestCategory

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.positions.post_positions(
                category=PostPositionsRequestCategory.EXPERIENCE,
                organization="organization",
                role="role",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_positions(
            category=category,
            organization=organization,
            role=role,
            start_date=start_date,
            end_date=end_date,
            organization_size=organization_size,
            position=position,
            summary=summary,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def delete_positions_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointDeletePositionsId:
        """
        Remove an item from the OAuth'ed end user's Curriculum Vitae.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointDeletePositionsId
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.positions.delete_positions_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_positions_id(id, request_options=request_options)
        return _response.data

    async def patch_positions_id(
        self,
        id: int,
        *,
        category: PatchPositionsIdRequestCategory,
        organization: str,
        role: str,
        start_date: str,
        end_date: typing.Optional[str] = OMIT,
        organization_size: typing.Optional[PatchPositionsIdRequestOrganizationSize] = OMIT,
        position: typing.Optional[PatchPositionsIdRequestPosition] = OMIT,
        summary: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPatchPositionsId:
        """
        Update the OAuth'ed end user's Curriculum Vitae by modifying an existing position.

        Parameters
        ----------
        id : int

        category : PatchPositionsIdRequestCategory

        organization : str

        role : str

        start_date : str

        end_date : typing.Optional[str]

        organization_size : typing.Optional[PatchPositionsIdRequestOrganizationSize]

        position : typing.Optional[PatchPositionsIdRequestPosition]

        summary : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPatchPositionsId
            Valid Response

        Examples
        --------
        import asyncio

        from fern.positions import PatchPositionsIdRequestCategory

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.positions.patch_positions_id(
                id=1,
                category=PatchPositionsIdRequestCategory.EXPERIENCE,
                organization="organization",
                role="role",
                start_date="start_date",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_positions_id(
            id,
            category=category,
            organization=organization,
            role=role,
            start_date=start_date,
            end_date=end_date,
            organization_size=organization_size,
            position=position,
            summary=summary,
            url=url,
            request_options=request_options,
        )
        return _response.data
