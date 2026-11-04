

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cloud_federation_api_add_share import CloudFederationApiAddShare
from .raw_client import AsyncRawCloudFederationApiRequestHandlerClient, RawCloudFederationApiRequestHandlerClient


class CloudFederationApiRequestHandlerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCloudFederationApiRequestHandlerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCloudFederationApiRequestHandlerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCloudFederationApiRequestHandlerClient
        """
        return self._raw_client

    def add_share(
        self,
        *,
        share_with: str,
        name: str,
        provider_id: str,
        owner: str,
        protocol: str,
        share_type: str,
        resource_type: str,
        description: typing.Optional[str] = None,
        owner_display_name: typing.Optional[str] = None,
        shared_by: typing.Optional[str] = None,
        shared_by_display_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudFederationApiAddShare:
        """
        Parameters
        ----------
        share_with : str
            The user who the share will be shared with

        name : str
            The resource name (e.g. document.odt)

        provider_id : str
            Resource UID on the provider side

        owner : str
            Provider specific UID of the user who owns the resource

        protocol : str
            e,.g. ['name' => 'webdav', 'options' => ['username' => 'john', 'permissions' => 31]]

        share_type : str
            'group' or 'user' share

        resource_type : str
            'file', 'calendar',...

        description : typing.Optional[str]
            Share description

        owner_display_name : typing.Optional[str]
            Display name of the user who shared the item

        shared_by : typing.Optional[str]
            Provider specific UID of the user who shared the resource

        shared_by_display_name : typing.Optional[str]
            Display name of the user who shared the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudFederationApiAddShare
            The notification was successfully received. The display name of the recipient might be returned in the body

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.cloud_federation_api_request_handler.add_share(
            share_with="shareWith",
            name="name",
            provider_id="providerId",
            owner="owner",
            protocol="protocol",
            share_type="shareType",
            resource_type="resourceType",
        )
        """
        _response = self._raw_client.add_share(
            share_with=share_with,
            name=name,
            provider_id=provider_id,
            owner=owner,
            protocol=protocol,
            share_type=share_type,
            resource_type=resource_type,
            description=description,
            owner_display_name=owner_display_name,
            shared_by=shared_by,
            shared_by_display_name=shared_by_display_name,
            request_options=request_options,
        )
        return _response.data

    def receive_notification(
        self,
        *,
        notification_type: str,
        resource_type: str,
        provider_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        notification_type : str
            Notification type, e.g. SHARE_ACCEPTED

        resource_type : str
            calendar, file, contact,...

        provider_id : typing.Optional[str]
            ID of the share

        notification : typing.Optional[str]
            The actual payload of the notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            The notification was successfully received

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.cloud_federation_api_request_handler.receive_notification(
            notification_type="notificationType",
            resource_type="resourceType",
        )
        """
        _response = self._raw_client.receive_notification(
            notification_type=notification_type,
            resource_type=resource_type,
            provider_id=provider_id,
            notification=notification,
            request_options=request_options,
        )
        return _response.data


class AsyncCloudFederationApiRequestHandlerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCloudFederationApiRequestHandlerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCloudFederationApiRequestHandlerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCloudFederationApiRequestHandlerClient
        """
        return self._raw_client

    async def add_share(
        self,
        *,
        share_with: str,
        name: str,
        provider_id: str,
        owner: str,
        protocol: str,
        share_type: str,
        resource_type: str,
        description: typing.Optional[str] = None,
        owner_display_name: typing.Optional[str] = None,
        shared_by: typing.Optional[str] = None,
        shared_by_display_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CloudFederationApiAddShare:
        """
        Parameters
        ----------
        share_with : str
            The user who the share will be shared with

        name : str
            The resource name (e.g. document.odt)

        provider_id : str
            Resource UID on the provider side

        owner : str
            Provider specific UID of the user who owns the resource

        protocol : str
            e,.g. ['name' => 'webdav', 'options' => ['username' => 'john', 'permissions' => 31]]

        share_type : str
            'group' or 'user' share

        resource_type : str
            'file', 'calendar',...

        description : typing.Optional[str]
            Share description

        owner_display_name : typing.Optional[str]
            Display name of the user who shared the item

        shared_by : typing.Optional[str]
            Provider specific UID of the user who shared the resource

        shared_by_display_name : typing.Optional[str]
            Display name of the user who shared the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CloudFederationApiAddShare
            The notification was successfully received. The display name of the recipient might be returned in the body

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.cloud_federation_api_request_handler.add_share(
                share_with="shareWith",
                name="name",
                provider_id="providerId",
                owner="owner",
                protocol="protocol",
                share_type="shareType",
                resource_type="resourceType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_share(
            share_with=share_with,
            name=name,
            provider_id=provider_id,
            owner=owner,
            protocol=protocol,
            share_type=share_type,
            resource_type=resource_type,
            description=description,
            owner_display_name=owner_display_name,
            shared_by=shared_by,
            shared_by_display_name=shared_by_display_name,
            request_options=request_options,
        )
        return _response.data

    async def receive_notification(
        self,
        *,
        notification_type: str,
        resource_type: str,
        provider_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        notification_type : str
            Notification type, e.g. SHARE_ACCEPTED

        resource_type : str
            calendar, file, contact,...

        provider_id : typing.Optional[str]
            ID of the share

        notification : typing.Optional[str]
            The actual payload of the notification

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            The notification was successfully received

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.cloud_federation_api_request_handler.receive_notification(
                notification_type="notificationType",
                resource_type="resourceType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.receive_notification(
            notification_type=notification_type,
            resource_type=resource_type,
            provider_id=provider_id,
            notification=notification,
            request_options=request_options,
        )
        return _response.data
