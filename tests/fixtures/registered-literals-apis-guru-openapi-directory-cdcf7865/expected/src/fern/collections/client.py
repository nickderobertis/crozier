

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient
from .types.collections_detail_response_item import CollectionsDetailResponseItem
from .types.collections_list_response_item import CollectionsListResponseItem


OMIT = typing.cast(typing.Any, ...)


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionsListResponseItem]:
        """
        Retrieves a list collections, either public or related to the user
        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionsListResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves a list collections, either public or related to the user
        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.create(
            request={
                "data": {
                    "attributes": {"title": "An Excellent Collection Title"},
                    "type": "collections",
                }
            },
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    def detail(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionsDetailResponseItem]:
        """
        Retrieves a collection, if the user has appropriate permissions.

        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionsDetailResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.detail(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.detail(collection_id, request_options=request_options)
        return _response.data

    def delete(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a collection, if the user has appropriate permissions.
        #### Permissions
        Users must have write permissions on a collection in order to delete it
        #### Returns
        Nothing is returned in the body

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.delete(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.delete(collection_id, request_options=request_options)
        return _response.data

    def metadata_registrations_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        In order to view this metadata it must be public or a user must have read permissions for collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_registrations_list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.metadata_registrations_list(collection_id, request_options=request_options)
        return _response.data

    def add_metadata(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        To edit this collection a user must have collections write permissions
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.add_metadata(
            collection_id="collection_id",
            request={
                "application/json": {
                    "data": {
                        "attributes": {
                            "guid": "test0",
                            "subjects": "5fd228b7e64e1300aa99ee15",
                            "volume": "test",
                        },
                        "type": "collected-metadata",
                    }
                }
            },
        )
        """
        _response = self._raw_client.add_metadata(collection_id, request=request, request_options=request_options)
        return _response.data

    def metadata_registrations_detail(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        #### Permissions
        In order to view this metadata it must be public or a user must have read permissions for collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_registrations_detail(
            collection_id="collection_id",
            cgm_id="cgm_id",
        )
        """
        _response = self._raw_client.metadata_registrations_detail(
            collection_id, cgm_id, request_options=request_options
        )
        return _response.data

    def metadata_detail(
        self,
        collection_id: str,
        cgm_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        To edit this collection a user must have collections write permissions
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_detail(
            collection_id="collection_id",
            cgm_id="cgm_id",
            request={
                "application/json": {
                    "data": {
                        "attributes": {
                            "guid": "test0",
                            "subjects": "5fd228b7e64e1300aa99ee15",
                            "volume": "test",
                        },
                        "type": "collected-metadata",
                    }
                }
            },
        )
        """
        _response = self._raw_client.metadata_detail(
            collection_id, cgm_id, request=request, request_options=request_options
        )
        return _response.data

    def metadata_delete(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        #### Permissions
        Only a user with collection admin permissions can delete collected metadata
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_delete(
            collection_id="collection_id",
            cgm_id="cgm_id",
        )
        """
        _response = self._raw_client.metadata_delete(collection_id, cgm_id, request_options=request_options)
        return _response.data

    def metadata_subjects_relationships(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """

        #### Permissions
        This is public for a logged out user when an entity is public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_subjects_relationships(
            collection_id="collection_id",
            cgm_id="cgm_id",
        )
        """
        _response = self._raw_client.metadata_subjects_relationships(
            collection_id, cgm_id, request_options=request_options
        )
        return _response.data

    def metadata_subjects_relationships_update(
        self,
        collection_id: str,
        cgm_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        #### Permissions
        This is editable for a user with a write permission for this collection.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.metadata_subjects_relationships_update(
            collection_id="collection_id",
            cgm_id="cgm_id",
            request={
                "application/json": {
                    "data": {"id": "5fd228b7e64e1300aa99ee15", "type": "subjects"}
                }
            },
        )
        """
        _response = self._raw_client.metadata_subjects_relationships_update(
            collection_id, cgm_id, request=request, request_options=request_options
        )
        return _response.data

    def collected_metadata(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """

        #### Permissions
        In order to view these subject it must be a public collection or a user must have read permissions for collection.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error, other then permissions errors.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.collected_metadata(
            collection_id="collection_id",
            cgm_id="cgm_id",
        )
        """
        _response = self._raw_client.collected_metadata(collection_id, cgm_id, request_options=request_options)
        return _response.data

    def linked_nodes_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all nodes linked to the given collection.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_nodes_list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.linked_nodes_list(collection_id, request_options=request_options)
        return _response.data

    def linked_nodes_relationships_create(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all the node ids linked to the given collection.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_nodes_relationships_create(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.linked_nodes_relationships_create(collection_id, request_options=request_options)
        return _response.data

    def linked_nodes_relationships(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint allow users to a add a node to a collection by issuing a POST request.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_nodes_relationships(
            collection_id="collection_id",
            request={
                "data": [
                    {"id": "guid0", "type": "linked_nodes"},
                    {"id": "newid", "type": "linked_nodes"},
                    {"id": "test2", "type": "linked_nodes"},
                    {"id": "guid4", "type": "linked_nodes"},
                ]
            },
        )
        """
        _response = self._raw_client.linked_nodes_relationships(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    def linked_nodes_relationships_delete(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """

        This removes associated nodes from a collection
        #### Permissions
        Any user with write permissions on this collection should be to remove nodes from this collection.
        #### Returns
        Nothing in the response body.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_nodes_relationships_delete(
            collection_id="collection_id",
            request={
                "data": [
                    {"id": "guid0", "type": "linked_nodes"},
                    {"id": "newid", "type": "linked_nodes"},
                    {"id": "test2", "type": "linked_nodes"},
                    {"id": "guid4", "type": "linked_nodes"},
                ]
            },
        )
        """
        _response = self._raw_client.linked_nodes_relationships_delete(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    def linked_preprints_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all preprints linked to the given collection.
        #### Permissions
        This returns all public preprints associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_preprints_list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.linked_preprints_list(collection_id, request_options=request_options)
        return _response.data

    def linked_registrations_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all registrations linked to the given collection.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_registrations_list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.linked_registrations_list(collection_id, request_options=request_options)
        return _response.data

    def linked_registrations_relationships_create(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all the registration ids linked to the given collection.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_registrations_relationships_create(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.linked_registrations_relationships_create(
            collection_id, request_options=request_options
        )
        return _response.data

    def linked_registrations_relationships(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint allow users to a add a registration to a collection by issuing a POST request.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_registrations_relationships(
            collection_id="collection_id",
            request={
                "data": [
                    {"id": "guid0", "type": "linked_registrations"},
                    {"id": "newid", "type": "linked_registrations"},
                    {"id": "test2", "type": "linked_registrations"},
                    {"id": "guid4", "type": "linked_registrations"},
                ]
            },
        )
        """
        _response = self._raw_client.linked_registrations_relationships(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    def linked_registrations_relationships_delete(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """

        This removes associated registrations from a collection
        #### Permissions
        Any user with write permissions on this collection should be to remove registrations from this collection.
        #### Returns
        Nothing in the response body.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.collections.linked_registrations_relationships_delete(
            collection_id="collection_id",
            request={
                "data": [
                    {"id": "guid0", "type": "linked_registrations"},
                    {"id": "newid", "type": "linked_registrations"},
                    {"id": "test2", "type": "linked_registrations"},
                    {"id": "guid4", "type": "linked_registrations"},
                ]
            },
        )
        """
        _response = self._raw_client.linked_registrations_relationships_delete(
            collection_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionsListResponseItem]:
        """
        Retrieves a list collections, either public or related to the user
        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionsListResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Retrieves a list collections, either public or related to the user
        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.

        Comments on private nodes are only visible to contributors and administrators on the parent node.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.create(
                request={
                    "data": {
                        "attributes": {"title": "An Excellent Collection Title"},
                        "type": "collections",
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    async def detail(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[CollectionsDetailResponseItem]:
        """
        Retrieves a collection, if the user has appropriate permissions.

        #### Permissions
        Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CollectionsDetailResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.detail(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.detail(collection_id, request_options=request_options)
        return _response.data

    async def delete(self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a collection, if the user has appropriate permissions.
        #### Permissions
        Users must have write permissions on a collection in order to delete it
        #### Returns
        Nothing is returned in the body

        Parameters
        ----------
        collection_id : str
            A short id for that collection

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
            await client.collections.delete(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(collection_id, request_options=request_options)
        return _response.data

    async def metadata_registrations_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        In order to view this metadata it must be public or a user must have read permissions for collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.metadata_registrations_list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_registrations_list(collection_id, request_options=request_options)
        return _response.data

    async def add_metadata(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        To edit this collection a user must have collections write permissions
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

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
            await client.collections.add_metadata(
                collection_id="collection_id",
                request={
                    "application/json": {
                        "data": {
                            "attributes": {
                                "guid": "test0",
                                "subjects": "5fd228b7e64e1300aa99ee15",
                                "volume": "test",
                            },
                            "type": "collected-metadata",
                        }
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_metadata(collection_id, request=request, request_options=request_options)
        return _response.data

    async def metadata_registrations_detail(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        #### Permissions
        In order to view this metadata it must be public or a user must have read permissions for collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

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
            await client.collections.metadata_registrations_detail(
                collection_id="collection_id",
                cgm_id="cgm_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_registrations_detail(
            collection_id, cgm_id, request_options=request_options
        )
        return _response.data

    async def metadata_detail(
        self,
        collection_id: str,
        cgm_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        List of user created metadata for entities within a collection.
        #### Permissions
        To edit this collection a user must have collections write permissions
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request : typing.Dict[str, typing.Any]

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
            await client.collections.metadata_detail(
                collection_id="collection_id",
                cgm_id="cgm_id",
                request={
                    "application/json": {
                        "data": {
                            "attributes": {
                                "guid": "test0",
                                "subjects": "5fd228b7e64e1300aa99ee15",
                                "volume": "test",
                            },
                            "type": "collected-metadata",
                        }
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_detail(
            collection_id, cgm_id, request=request, request_options=request_options
        )
        return _response.data

    async def metadata_delete(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """

        #### Permissions
        Only a user with collection admin permissions can delete collected metadata
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

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
            await client.collections.metadata_delete(
                collection_id="collection_id",
                cgm_id="cgm_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_delete(collection_id, cgm_id, request_options=request_options)
        return _response.data

    async def metadata_subjects_relationships(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """

        #### Permissions
        This is public for a logged out user when an entity is public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.metadata_subjects_relationships(
                collection_id="collection_id",
                cgm_id="cgm_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_subjects_relationships(
            collection_id, cgm_id, request_options=request_options
        )
        return _response.data

    async def metadata_subjects_relationships_update(
        self,
        collection_id: str,
        cgm_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        #### Permissions
        This is editable for a user with a write permission for this collection.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request : typing.Dict[str, typing.Any]

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
            await client.collections.metadata_subjects_relationships_update(
                collection_id="collection_id",
                cgm_id="cgm_id",
                request={
                    "application/json": {
                        "data": {"id": "5fd228b7e64e1300aa99ee15", "type": "subjects"}
                    }
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metadata_subjects_relationships_update(
            collection_id, cgm_id, request=request, request_options=request_options
        )
        return _response.data

    async def collected_metadata(
        self, collection_id: str, cgm_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """

        #### Permissions
        In order to view these subject it must be a public collection or a user must have read permissions for collection.

        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error, other then permissions errors.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        cgm_id : str
            A short id for that piece of metadata

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.collected_metadata(
                collection_id="collection_id",
                cgm_id="cgm_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.collected_metadata(collection_id, cgm_id, request_options=request_options)
        return _response.data

    async def linked_nodes_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all nodes linked to the given collection.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_nodes_list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_nodes_list(collection_id, request_options=request_options)
        return _response.data

    async def linked_nodes_relationships_create(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all the node ids linked to the given collection.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_nodes_relationships_create(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_nodes_relationships_create(
            collection_id, request_options=request_options
        )
        return _response.data

    async def linked_nodes_relationships(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint allow users to a add a node to a collection by issuing a POST request.
        #### Permissions
        This returns all public nodes associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_nodes_relationships(
                collection_id="collection_id",
                request={
                    "data": [
                        {"id": "guid0", "type": "linked_nodes"},
                        {"id": "newid", "type": "linked_nodes"},
                        {"id": "test2", "type": "linked_nodes"},
                        {"id": "guid4", "type": "linked_nodes"},
                    ]
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_nodes_relationships(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    async def linked_nodes_relationships_delete(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """

        This removes associated nodes from a collection
        #### Permissions
        Any user with write permissions on this collection should be to remove nodes from this collection.
        #### Returns
        Nothing in the response body.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_nodes_relationships_delete(
                collection_id="collection_id",
                request={
                    "data": [
                        {"id": "guid0", "type": "linked_nodes"},
                        {"id": "newid", "type": "linked_nodes"},
                        {"id": "test2", "type": "linked_nodes"},
                        {"id": "guid4", "type": "linked_nodes"},
                    ]
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_nodes_relationships_delete(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    async def linked_preprints_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all preprints linked to the given collection.
        #### Permissions
        This returns all public preprints associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_preprints_list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_preprints_list(collection_id, request_options=request_options)
        return _response.data

    async def linked_registrations_list(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all registrations linked to the given collection.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_registrations_list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_registrations_list(collection_id, request_options=request_options)
        return _response.data

    async def linked_registrations_relationships_create(
        self, collection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        List of all the registration ids linked to the given collection.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of nodes ids.
        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_registrations_relationships_create(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_registrations_relationships_create(
            collection_id, request_options=request_options
        )
        return _response.data

    async def linked_registrations_relationships(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        This endpoint allow users to a add a registration to a collection by issuing a POST request.
        #### Permissions
        This returns all public registrations associated with this collection.
        #### Returns
        Returns a JSON object containing `data` and `links` keys.

        The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.

        The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_registrations_relationships(
                collection_id="collection_id",
                request={
                    "data": [
                        {"id": "guid0", "type": "linked_registrations"},
                        {"id": "newid", "type": "linked_registrations"},
                        {"id": "test2", "type": "linked_registrations"},
                        {"id": "guid4", "type": "linked_registrations"},
                    ]
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_registrations_relationships(
            collection_id, request=request, request_options=request_options
        )
        return _response.data

    async def linked_registrations_relationships_delete(
        self,
        collection_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """

        This removes associated registrations from a collection
        #### Permissions
        Any user with write permissions on this collection should be to remove registrations from this collection.
        #### Returns
        Nothing in the response body.

        Parameters
        ----------
        collection_id : str
            A short id for that collection

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.collections.linked_registrations_relationships_delete(
                collection_id="collection_id",
                request={
                    "data": [
                        {"id": "guid0", "type": "linked_registrations"},
                        {"id": "newid", "type": "linked_registrations"},
                        {"id": "test2", "type": "linked_registrations"},
                        {"id": "guid4", "type": "linked_registrations"},
                    ]
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.linked_registrations_relationships_delete(
            collection_id, request=request, request_options=request_options
        )
        return _response.data
