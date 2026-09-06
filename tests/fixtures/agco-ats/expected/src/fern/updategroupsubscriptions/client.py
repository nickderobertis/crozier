

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_update_group_subscription import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription,
)
from ..types.update_system_models_update_group_subscription import UpdateSystemModelsUpdateGroupSubscription
from .raw_client import AsyncRawUpdategroupsubscriptionsClient, RawUpdategroupsubscriptionsClient


OMIT = typing.cast(typing.Any, ...)


class UpdategroupsubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpdategroupsubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpdategroupsubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpdategroupsubscriptionsClient
        """
        return self._raw_client

    def getupdategroupsubscriptions(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID.

        package_type_id : typing.Optional[str]
            Optional. Filter by Package Type ID.

        client_id : typing.Optional[str]
            Optional. Filter by Client ID.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupsubscriptions.getupdategroupsubscriptions()
        """
        _response = self._raw_client.getupdategroupsubscriptions(
            update_group_id=update_group_id,
            package_type_id=package_type_id,
            client_id=client_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def postupdategroupsubscription(
        self,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupsubscriptions.postupdategroupsubscription(
            client_id="ClientID",
            include=True,
            package_type_id="PackageTypeID",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.postupdategroupsubscription(
            client_id=client_id,
            include=include,
            package_type_id=package_type_id,
            update_group_id=update_group_id,
            update_group_subscription_id=update_group_subscription_id,
            request_options=request_options,
        )
        return _response.data

    def postupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, UpdateSystemModelsUpdateGroupSubscription

        client = FernApi()
        client.updategroupsubscriptions.postupdategroupsubscriptions(
            request=[
                UpdateSystemModelsUpdateGroupSubscription(
                    client_id="ClientID",
                    include=True,
                    package_type_id="PackageTypeID",
                    update_group_id="UpdateGroupID",
                )
            ],
        )
        """
        _response = self._raw_client.postupdategroupsubscriptions(request=request, request_options=request_options)
        return _response.data

    def putupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, UpdateSystemModelsUpdateGroupSubscription

        client = FernApi()
        client.updategroupsubscriptions.putupdategroupsubscriptions(
            request=[
                UpdateSystemModelsUpdateGroupSubscription(
                    client_id="ClientID",
                    include=True,
                    package_type_id="PackageTypeID",
                    update_group_id="UpdateGroupID",
                )
            ],
        )
        """
        _response = self._raw_client.putupdategroupsubscriptions(request=request, request_options=request_options)
        return _response.data

    def getupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupsubscriptions.getupdategroupsubscription(
            update_group_subscription_id=1,
        )
        """
        _response = self._raw_client.getupdategroupsubscription(
            update_group_subscription_id, request_options=request_options
        )
        return _response.data

    def putupdategroupsubscription(
        self,
        update_group_subscription_id_: int,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id_ : int
            The Update Group Subscription ID

        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupsubscriptions.putupdategroupsubscription(
            update_group_subscription_id_=1,
            client_id="ClientID",
            include=True,
            package_type_id="PackageTypeID",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.putupdategroupsubscription(
            update_group_subscription_id_,
            client_id=client_id,
            include=include,
            package_type_id=package_type_id,
            update_group_id=update_group_id,
            update_group_subscription_id=update_group_subscription_id,
            request_options=request_options,
        )
        return _response.data

    def deleteupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupsubscriptions.deleteupdategroupsubscription(
            update_group_subscription_id=1,
        )
        """
        _response = self._raw_client.deleteupdategroupsubscription(
            update_group_subscription_id, request_options=request_options
        )
        return _response.data


class AsyncUpdategroupsubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpdategroupsubscriptionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpdategroupsubscriptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpdategroupsubscriptionsClient
        """
        return self._raw_client

    async def getupdategroupsubscriptions(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID.

        package_type_id : typing.Optional[str]
            Optional. Filter by Package Type ID.

        client_id : typing.Optional[str]
            Optional. Filter by Client ID.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupsubscriptions.getupdategroupsubscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getupdategroupsubscriptions(
            update_group_id=update_group_id,
            package_type_id=package_type_id,
            client_id=client_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def postupdategroupsubscription(
        self,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupsubscriptions.postupdategroupsubscription(
                client_id="ClientID",
                include=True,
                package_type_id="PackageTypeID",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postupdategroupsubscription(
            client_id=client_id,
            include=include,
            package_type_id=package_type_id,
            update_group_id=update_group_id,
            update_group_subscription_id=update_group_subscription_id,
            request_options=request_options,
        )
        return _response.data

    async def postupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateSystemModelsUpdateGroupSubscription

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupsubscriptions.postupdategroupsubscriptions(
                request=[
                    UpdateSystemModelsUpdateGroupSubscription(
                        client_id="ClientID",
                        include=True,
                        package_type_id="PackageTypeID",
                        update_group_id="UpdateGroupID",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postupdategroupsubscriptions(
            request=request, request_options=request_options
        )
        return _response.data

    async def putupdategroupsubscriptions(
        self,
        *,
        request: typing.Sequence[UpdateSystemModelsUpdateGroupSubscription],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        request : typing.Sequence[UpdateSystemModelsUpdateGroupSubscription]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateSystemModelsUpdateGroupSubscription

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupsubscriptions.putupdategroupsubscriptions(
                request=[
                    UpdateSystemModelsUpdateGroupSubscription(
                        client_id="ClientID",
                        include=True,
                        package_type_id="PackageTypeID",
                        update_group_id="UpdateGroupID",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putupdategroupsubscriptions(request=request, request_options=request_options)
        return _response.data

    async def getupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsUpdateGroupSubscription:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroupSubscription
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupsubscriptions.getupdategroupsubscription(
                update_group_subscription_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getupdategroupsubscription(
            update_group_subscription_id, request_options=request_options
        )
        return _response.data

    async def putupdategroupsubscription(
        self,
        update_group_subscription_id_: int,
        *,
        client_id: str,
        include: bool,
        package_type_id: str,
        update_group_id: str,
        update_group_subscription_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id_ : int
            The Update Group Subscription ID

        client_id : str
            The ClientID.

        include : bool
            True to receive content of type indicated by PackageTypeID.

        package_type_id : str
            The PackageType to set subscription status for

        update_group_id : str
            The Update Group this subscription is relevant for.

        update_group_subscription_id : typing.Optional[int]
            The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.

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
            await client.updategroupsubscriptions.putupdategroupsubscription(
                update_group_subscription_id_=1,
                client_id="ClientID",
                include=True,
                package_type_id="PackageTypeID",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putupdategroupsubscription(
            update_group_subscription_id_,
            client_id=client_id,
            include=include,
            package_type_id=package_type_id,
            update_group_id=update_group_id,
            update_group_subscription_id=update_group_subscription_id,
            request_options=request_options,
        )
        return _response.data

    async def deleteupdategroupsubscription(
        self, update_group_subscription_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_subscription_id : int
            The Update Group Subscription ID to delete

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
            await client.updategroupsubscriptions.deleteupdategroupsubscription(
                update_group_subscription_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteupdategroupsubscription(
            update_group_subscription_id, request_options=request_options
        )
        return _response.data
