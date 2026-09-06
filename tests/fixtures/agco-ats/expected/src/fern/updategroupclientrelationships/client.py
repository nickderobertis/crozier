

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_update_group_client_relationship import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
)
from ..types.update_system_models_update_group_client_relationship import (
    UpdateSystemModelsUpdateGroupClientRelationship,
)
from .raw_client import AsyncRawUpdategroupclientrelationshipsClient, RawUpdategroupclientrelationshipsClient


OMIT = typing.cast(typing.Any, ...)


class UpdategroupclientrelationshipsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpdategroupclientrelationshipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpdategroupclientrelationshipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpdategroupclientrelationshipsClient
        """
        return self._raw_client

    def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        active : typing.Optional[bool]
            Optional. Filter by Active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupclientrelationships.getsubscriptions()
        """
        _response = self._raw_client.getsubscriptions(
            client_id=client_id,
            update_group_id=update_group_id,
            limit=limit,
            offset=offset,
            active=active,
            request_options=request_options,
        )
        return _response.data

    def postsubscription(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

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
        client.updategroupclientrelationships.postsubscription(
            client_id="ClientID",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.postsubscription(
            client_id=client_id,
            update_group_id=update_group_id,
            active=active,
            last_checkin=last_checkin,
            relationship_id=relationship_id,
            request_options=request_options,
        )
        return _response.data

    def putsubscriptionbyclientidupdategroupid(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID.  This can be a client ID that has not been registered yet.

        update_group_id : str
            The Update Group ID

        active : bool
            Subscribe the client to the Update Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupclientrelationships.putsubscriptionbyclientidupdategroupid(
            client_id="ClientID",
            update_group_id="UpdateGroupID",
            active=True,
        )
        """
        _response = self._raw_client.putsubscriptionbyclientidupdategroupid(
            client_id=client_id, update_group_id=update_group_id, active=active, request_options=request_options
        )
        return _response.data

    def getsubscription(
        self, relationship_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id : str
            The RelationshipID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupclientrelationships.getsubscription(
            relationship_id="RelationshipID",
        )
        """
        _response = self._raw_client.getsubscription(relationship_id, request_options=request_options)
        return _response.data

    def putsubscription(
        self,
        relationship_id_: str,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id_ : str
            The relationship id of the UpdateGroupClientRelationship

        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroupclientrelationships.putsubscription(
            relationship_id_="RelationshipID",
            client_id="ClientID",
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.putsubscription(
            relationship_id_,
            client_id=client_id,
            update_group_id=update_group_id,
            active=active,
            last_checkin=last_checkin,
            relationship_id=relationship_id,
            request_options=request_options,
        )
        return _response.data


class AsyncUpdategroupclientrelationshipsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpdategroupclientrelationshipsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpdategroupclientrelationshipsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpdategroupclientrelationshipsClient
        """
        return self._raw_client

    async def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        active : typing.Optional[bool]
            Optional. Filter by Active

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupclientrelationships.getsubscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsubscriptions(
            client_id=client_id,
            update_group_id=update_group_id,
            limit=limit,
            offset=offset,
            active=active,
            request_options=request_options,
        )
        return _response.data

    async def postsubscription(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

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
            await client.updategroupclientrelationships.postsubscription(
                client_id="ClientID",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postsubscription(
            client_id=client_id,
            update_group_id=update_group_id,
            active=active,
            last_checkin=last_checkin,
            relationship_id=relationship_id,
            request_options=request_options,
        )
        return _response.data

    async def putsubscriptionbyclientidupdategroupid(
        self,
        *,
        client_id: str,
        update_group_id: str,
        active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID.  This can be a client ID that has not been registered yet.

        update_group_id : str
            The Update Group ID

        active : bool
            Subscribe the client to the Update Group.

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
            await client.updategroupclientrelationships.putsubscriptionbyclientidupdategroupid(
                client_id="ClientID",
                update_group_id="UpdateGroupID",
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putsubscriptionbyclientidupdategroupid(
            client_id=client_id, update_group_id=update_group_id, active=active, request_options=request_options
        )
        return _response.data

    async def getsubscription(
        self, relationship_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id : str
            The RelationshipID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroupclientrelationships.getsubscription(
                relationship_id="RelationshipID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsubscription(relationship_id, request_options=request_options)
        return _response.data

    async def putsubscription(
        self,
        relationship_id_: str,
        *,
        client_id: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        last_checkin: typing.Optional[dt.datetime] = OMIT,
        relationship_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        relationship_id_ : str
            The relationship id of the UpdateGroupClientRelationship

        client_id : str
            Read Only after creation. The client id of the subscriber.

        update_group_id : str
            Read Only after creation. The update group to subscribe to.

        active : typing.Optional[bool]
            The subscription status.  The status is active by default.

        last_checkin : typing.Optional[dt.datetime]
            ReadOnly. The timestamp of the last checkin.

        relationship_id : typing.Optional[str]
            Read Only after creation. The relationship id.  A relationship id will be assigned if not provided on creation.

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
            await client.updategroupclientrelationships.putsubscription(
                relationship_id_="RelationshipID",
                client_id="ClientID",
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putsubscription(
            relationship_id_,
            client_id=client_id,
            update_group_id=update_group_id,
            active=active,
            last_checkin=last_checkin,
            relationship_id=relationship_id,
            request_options=request_options,
        )
        return _response.data
