

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.object import Object
from ..types.objects_instances_post import ObjectsInstancesPost
from ..types.url_label_list import UrlLabelList
from .raw_client import AsyncRawObjectsClient, RawObjectsClient


OMIT = typing.cast(typing.Any, ...)


class ObjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObjectsClient
        """
        return self._raw_client

    def get_objects(
        self,
        object_id: str,
        *,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[str] = None,
        presigned: typing.Optional[bool] = None,
        flow_tag_name: typing.Optional[str] = None,
        flow_tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Object:
        """
        Contains Flows that references the Media Object and other information.

        The paging query parameters and headers are required for the list of Flow references in the Media Object.
        Service implementations should return a complete list of Flow references within reason and API clients should expect paging to happen in some rare cases where a Media Object is used in many Flows.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls`.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Media Object `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[str]
            A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        flow_tag_name : typing.Optional[str]
            Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.

        flow_tag_exists_name : typing.Optional[bool]
            Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Object


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.objects.get_objects(
            object_id="objectId",
        )
        """
        _response = self._raw_client.get_objects(
            object_id,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            flow_tag_name=flow_tag_name,
            flow_tag_exists_name=flow_tag_exists_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def head_objects(
        self,
        object_id: str,
        *,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[str] = None,
        presigned: typing.Optional[bool] = None,
        flow_tag_name: typing.Optional[str] = None,
        flow_tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow references and other information about Media Objects.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls`.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Media Object `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[str]
            A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        flow_tag_name : typing.Optional[str]
            Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.

        flow_tag_exists_name : typing.Optional[bool]
            Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.objects.head_objects(
            object_id="objectId",
        )
        """
        _response = self._raw_client.head_objects(
            object_id,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            flow_tag_name=flow_tag_name,
            flow_tag_exists_name=flow_tag_exists_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    def post_objects_instances(
        self, object_id: str, *, request: ObjectsInstancesPost, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Request the service to create an Object instance on a new Storage Backend. Or add a new uncontrolled URL to `get_urls`.

        To request the duplication of the Object to a new Storage Backend, clients POST a `storage_id` to this endpoint that does not currently have an instance of the Object. The API will then:

        - Allocate storage for Media Object `objectId` on Storage Backend `storage_id`
        - Copy the Media Object from an existing location to the newly allocated storage
        - Start advertising the new copy in `get_urls` once ready

        The API instances SHOULD be capable of handling the case where the only existant instances are uncontrolled.

        Where a client has written a new uncontrolled Object instance, the client is responsible for ensuring that the Object written is complete and correct before registering it with this method.

        All instances of an Object MUST be identical.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        request : ObjectsInstancesPost

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, ObjectsInstancesPostStorageId

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.objects.post_objects_instances(
            object_id="objectId",
            request=ObjectsInstancesPostStorageId(
                storage_id="storage_id",
            ),
        )
        """
        _response = self._raw_client.post_objects_instances(object_id, request=request, request_options=request_options)
        return _response.data

    def delete_objects_instances(
        self,
        object_id: str,
        *,
        storage_id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an instance of a Media Object.

        One of `storage_id` or `label` MUST be specified in the query parameters. `storage_id` SHOULD be used where `controlled` is `True` for the instance.

        API instances should remove the Media Object instance from the `get_urls` list and then, if the instance is controlled, delete the Object instance from storage.

        API instances SHOULD prevent clients from deleting all Object instances. Additionally, API instances MAY prevent clients from deleting all controlled Object instances. Where clients wish to remove all copies of an Object from the store, they should do so by deleting all Flows or Flow Segments which reference the Object.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        storage_id : typing.Optional[str]
            The storage_id identifying the Media Object instance to be deleted.

        label : typing.Optional[str]
            The label identifying the Media Object instance to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.objects.delete_objects_instances(
            object_id="objectId",
        )
        """
        _response = self._raw_client.delete_objects_instances(
            object_id, storage_id=storage_id, label=label, request_options=request_options
        )
        return _response.data


class AsyncObjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObjectsClient
        """
        return self._raw_client

    async def get_objects(
        self,
        object_id: str,
        *,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[str] = None,
        presigned: typing.Optional[bool] = None,
        flow_tag_name: typing.Optional[str] = None,
        flow_tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Object:
        """
        Contains Flows that references the Media Object and other information.

        The paging query parameters and headers are required for the list of Flow references in the Media Object.
        Service implementations should return a complete list of Flow references within reason and API clients should expect paging to happen in some rare cases where a Media Object is used in many Flows.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls`.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Media Object `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[str]
            A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        flow_tag_name : typing.Optional[str]
            Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.

        flow_tag_exists_name : typing.Optional[bool]
            Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Object


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.objects.get_objects(
                object_id="objectId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_objects(
            object_id,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            flow_tag_name=flow_tag_name,
            flow_tag_exists_name=flow_tag_exists_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def head_objects(
        self,
        object_id: str,
        *,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[str] = None,
        presigned: typing.Optional[bool] = None,
        flow_tag_name: typing.Optional[str] = None,
        flow_tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow references and other information about Media Objects.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls`.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Media Object `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Media Object `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[str]
            A comma separated list of `storage_id`s of Media Object `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Media Object `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the `service/storage-backends` endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to
            generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        flow_tag_name : typing.Optional[str]
            Filter `referenced_by_flows` on tag values. This option is the same as the `tag.{name}` query parameter on the `/flows/` API endpoint.

        flow_tag_exists_name : typing.Optional[bool]
            Filter `referenced_by_flows` on tag names. This option is the same as the `tag_exists.{name}` query parameter on the `/flows/` API endpoint.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.objects.head_objects(
                object_id="objectId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_objects(
            object_id,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            flow_tag_name=flow_tag_name,
            flow_tag_exists_name=flow_tag_exists_name,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers

    async def post_objects_instances(
        self, object_id: str, *, request: ObjectsInstancesPost, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Request the service to create an Object instance on a new Storage Backend. Or add a new uncontrolled URL to `get_urls`.

        To request the duplication of the Object to a new Storage Backend, clients POST a `storage_id` to this endpoint that does not currently have an instance of the Object. The API will then:

        - Allocate storage for Media Object `objectId` on Storage Backend `storage_id`
        - Copy the Media Object from an existing location to the newly allocated storage
        - Start advertising the new copy in `get_urls` once ready

        The API instances SHOULD be capable of handling the case where the only existant instances are uncontrolled.

        Where a client has written a new uncontrolled Object instance, the client is responsible for ensuring that the Object written is complete and correct before registering it with this method.

        All instances of an Object MUST be identical.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        request : ObjectsInstancesPost

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ObjectsInstancesPostStorageId

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.objects.post_objects_instances(
                object_id="objectId",
                request=ObjectsInstancesPostStorageId(
                    storage_id="storage_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_objects_instances(
            object_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_objects_instances(
        self,
        object_id: str,
        *,
        storage_id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete an instance of a Media Object.

        One of `storage_id` or `label` MUST be specified in the query parameters. `storage_id` SHOULD be used where `controlled` is `True` for the instance.

        API instances should remove the Media Object instance from the `get_urls` list and then, if the instance is controlled, delete the Object instance from storage.

        API instances SHOULD prevent clients from deleting all Object instances. Additionally, API instances MAY prevent clients from deleting all controlled Object instances. Where clients wish to remove all copies of an Object from the store, they should do so by deleting all Flows or Flow Segments which reference the Object.

        Parameters
        ----------
        object_id : str
            The Media Object identifier. The Object ID may include special characters such as `/` which should be URL encoded.

        storage_id : typing.Optional[str]
            The storage_id identifying the Media Object instance to be deleted.

        label : typing.Optional[str]
            The label identifying the Media Object instance to be deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.objects.delete_objects_instances(
                object_id="objectId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_objects_instances(
            object_id, storage_id=storage_id, label=label, request_options=request_options
        )
        return _response.data
