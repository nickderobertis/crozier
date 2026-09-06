

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_bundle import ApiPagedResponseUpdateSystemModelsBundle
from ..types.update_system_models_bundle import UpdateSystemModelsBundle
from .raw_client import AsyncRawBundlesClient, RawBundlesClient


OMIT = typing.cast(typing.Any, ...)


class BundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBundlesClient
        """
        return self._raw_client

    def getbundles(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by UpdateGroup ID.

        active : typing.Optional[bool]
            Optional. Filter by active status.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        bundle_number : typing.Optional[int]
            Optional. If provided, filters by BundleNumber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bundles.getbundles()
        """
        _response = self._raw_client.getbundles(
            update_group_id=update_group_id,
            active=active,
            limit=limit,
            offset=offset,
            bundle_number=bundle_number,
            request_options=request_options,
        )
        return _response.data

    def postbundle(
        self,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bundles.postbundle(
            bundle_number=1,
            description="Description",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.postbundle(
            bundle_number=bundle_number,
            description=description,
            update_group_id=update_group_id,
            active=active,
            bundle_id=bundle_id,
            request_options=request_options,
        )
        return _response.data

    def getbundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsBundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bundles.getbundle(
            id="ID",
        )
        """
        _response = self._raw_client.getbundle(id, request_options=request_options)
        return _response.data

    def putbundle(
        self,
        id: str,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Bundle

        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bundles.putbundle(
            id="ID",
            bundle_number=1,
            description="Description",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.putbundle(
            id,
            bundle_number=bundle_number,
            description=description,
            update_group_id=update_group_id,
            active=active,
            bundle_id=bundle_id,
            request_options=request_options,
        )
        return _response.data

    def deletebundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.bundles.deletebundle(
            id="ID",
        )
        """
        _response = self._raw_client.deletebundle(id, request_options=request_options)
        return _response.data


class AsyncBundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBundlesClient
        """
        return self._raw_client

    async def getbundles(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by UpdateGroup ID.

        active : typing.Optional[bool]
            Optional. Filter by active status.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        bundle_number : typing.Optional[int]
            Optional. If provided, filters by BundleNumber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bundles.getbundles()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbundles(
            update_group_id=update_group_id,
            active=active,
            limit=limit,
            offset=offset,
            bundle_number=bundle_number,
            request_options=request_options,
        )
        return _response.data

    async def postbundle(
        self,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bundles.postbundle(
                bundle_number=1,
                description="Description",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postbundle(
            bundle_number=bundle_number,
            description=description,
            update_group_id=update_group_id,
            active=active,
            bundle_id=bundle_id,
            request_options=request_options,
        )
        return _response.data

    async def getbundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsBundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bundles.getbundle(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbundle(id, request_options=request_options)
        return _response.data

    async def putbundle(
        self,
        id: str,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Bundle

        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bundles.putbundle(
                id="ID",
                bundle_number=1,
                description="Description",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putbundle(
            id,
            bundle_number=bundle_number,
            description=description,
            update_group_id=update_group_id,
            active=active,
            bundle_id=bundle_id,
            request_options=request_options,
        )
        return _response.data

    async def deletebundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.bundles.deletebundle(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletebundle(id, request_options=request_options)
        return _response.data
