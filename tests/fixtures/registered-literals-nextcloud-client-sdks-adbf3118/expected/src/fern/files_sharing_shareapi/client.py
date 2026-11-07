

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.files_sharing_shareapi_create_share200response import FilesSharingShareapiCreateShare200Response
from ..types.files_sharing_shareapi_get_shares200response import FilesSharingShareapiGetShares200Response
from .raw_client import AsyncRawFilesSharingShareapiClient, RawFilesSharingShareapiClient


class FilesSharingShareapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesSharingShareapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesSharingShareapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesSharingShareapiClient
        """
        return self._raw_client

    def get_shares(
        self,
        *,
        shared_with_me: typing.Optional[str] = None,
        reshares: typing.Optional[str] = None,
        subfiles: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        include_tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        shared_with_me : typing.Optional[str]
            Only get shares with the current user

        reshares : typing.Optional[str]
            Only get shares by the current user and reshares

        subfiles : typing.Optional[str]
            Only get all shares in a folder

        path : typing.Optional[str]
            Get shares for a specific path

        include_tags : typing.Optional[str]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response
            Shares returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.get_shares()
        """
        _response = self._raw_client.get_shares(
            shared_with_me=shared_with_me,
            reshares=reshares,
            subfiles=subfiles,
            path=path,
            include_tags=include_tags,
            request_options=request_options,
        )
        return _response.data

    def create_share(
        self,
        *,
        path: typing.Optional[str] = None,
        permissions: typing.Optional[int] = None,
        share_type: typing.Optional[int] = None,
        share_with: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Path of the share

        permissions : typing.Optional[int]
            Permissions for the share

        share_type : typing.Optional[int]
            Type of the share

        share_with : typing.Optional[str]
            The entity this should be shared with

        public_upload : typing.Optional[str]
            If public uploading is allowed

        password : typing.Optional[str]
            Password for the share

        send_password_by_talk : typing.Optional[str]
            Send the password for the share over Talk

        expire_date : typing.Optional[str]
            Expiry date of the share

        note : typing.Optional[str]
            Note for the share

        label : typing.Optional[str]
            Label for the share (only used in link and email)

        attributes : typing.Optional[str]
            Additional attributes for the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.create_share()
        """
        _response = self._raw_client.create_share(
            path=path,
            permissions=permissions,
            share_type=share_type,
            share_with=share_with,
            public_upload=public_upload,
            password=password,
            send_password_by_talk=send_password_by_talk,
            expire_date=expire_date,
            note=note,
            label=label,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    def get_inherited_shares(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        path : str
            Path all shares will be relative to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response
            Shares returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.get_inherited_shares(
            path="path",
        )
        """
        _response = self._raw_client.get_inherited_shares(path=path, request_options=request_options)
        return _response.data

    def pending_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.pending_shares()
        """
        _response = self._raw_client.pending_shares(request_options=request_options)
        return _response.data

    def get_share(
        self,
        id: str,
        *,
        include_tags: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        include_tags : typing.Optional[int]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.get_share(
            id="id",
        )
        """
        _response = self._raw_client.get_share(id, include_tags=include_tags, request_options=request_options)
        return _response.data

    def update_share(
        self,
        id: str,
        *,
        permissions: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        hide_download: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        permissions : typing.Optional[int]
            New permissions

        password : typing.Optional[str]
            New password

        send_password_by_talk : typing.Optional[str]
            New condition if the password should be send over Talk

        public_upload : typing.Optional[str]
            New condition if public uploading is allowed

        expire_date : typing.Optional[str]
            New expiry date

        note : typing.Optional[str]
            New note

        label : typing.Optional[str]
            New label

        hide_download : typing.Optional[str]
            New condition if the download should be hidden

        attributes : typing.Optional[str]
            New additional attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.update_share(
            id="id",
        )
        """
        _response = self._raw_client.update_share(
            id,
            permissions=permissions,
            password=password,
            send_password_by_talk=send_password_by_talk,
            public_upload=public_upload,
            expire_date=expire_date,
            note=note,
            label=label,
            hide_download=hide_download,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    def delete_share(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.delete_share(
            id="id",
        )
        """
        _response = self._raw_client.delete_share(id, request_options=request_options)
        return _response.data

    def accept_share(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share accepted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.files_sharing_shareapi.accept_share(
            id="id",
        )
        """
        _response = self._raw_client.accept_share(id, request_options=request_options)
        return _response.data


class AsyncFilesSharingShareapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesSharingShareapiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesSharingShareapiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesSharingShareapiClient
        """
        return self._raw_client

    async def get_shares(
        self,
        *,
        shared_with_me: typing.Optional[str] = None,
        reshares: typing.Optional[str] = None,
        subfiles: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        include_tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        shared_with_me : typing.Optional[str]
            Only get shares with the current user

        reshares : typing.Optional[str]
            Only get shares by the current user and reshares

        subfiles : typing.Optional[str]
            Only get all shares in a folder

        path : typing.Optional[str]
            Get shares for a specific path

        include_tags : typing.Optional[str]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response
            Shares returned

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
            await client.files_sharing_shareapi.get_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_shares(
            shared_with_me=shared_with_me,
            reshares=reshares,
            subfiles=subfiles,
            path=path,
            include_tags=include_tags,
            request_options=request_options,
        )
        return _response.data

    async def create_share(
        self,
        *,
        path: typing.Optional[str] = None,
        permissions: typing.Optional[int] = None,
        share_type: typing.Optional[int] = None,
        share_with: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Path of the share

        permissions : typing.Optional[int]
            Permissions for the share

        share_type : typing.Optional[int]
            Type of the share

        share_with : typing.Optional[str]
            The entity this should be shared with

        public_upload : typing.Optional[str]
            If public uploading is allowed

        password : typing.Optional[str]
            Password for the share

        send_password_by_talk : typing.Optional[str]
            Send the password for the share over Talk

        expire_date : typing.Optional[str]
            Expiry date of the share

        note : typing.Optional[str]
            Note for the share

        label : typing.Optional[str]
            Label for the share (only used in link and email)

        attributes : typing.Optional[str]
            Additional attributes for the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share created

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
            await client.files_sharing_shareapi.create_share()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_share(
            path=path,
            permissions=permissions,
            share_type=share_type,
            share_with=share_with,
            public_upload=public_upload,
            password=password,
            send_password_by_talk=send_password_by_talk,
            expire_date=expire_date,
            note=note,
            label=label,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    async def get_inherited_shares(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        path : str
            Path all shares will be relative to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response
            Shares returned

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
            await client.files_sharing_shareapi.get_inherited_shares(
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inherited_shares(path=path, request_options=request_options)
        return _response.data

    async def pending_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FilesSharingShareapiGetShares200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiGetShares200Response


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
            await client.files_sharing_shareapi.pending_shares()


        asyncio.run(main())
        """
        _response = await self._raw_client.pending_shares(request_options=request_options)
        return _response.data

    async def get_share(
        self,
        id: str,
        *,
        include_tags: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        include_tags : typing.Optional[int]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share returned

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
            await client.files_sharing_shareapi.get_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_share(id, include_tags=include_tags, request_options=request_options)
        return _response.data

    async def update_share(
        self,
        id: str,
        *,
        permissions: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        hide_download: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FilesSharingShareapiCreateShare200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        permissions : typing.Optional[int]
            New permissions

        password : typing.Optional[str]
            New password

        send_password_by_talk : typing.Optional[str]
            New condition if the password should be send over Talk

        public_upload : typing.Optional[str]
            New condition if public uploading is allowed

        expire_date : typing.Optional[str]
            New expiry date

        note : typing.Optional[str]
            New note

        label : typing.Optional[str]
            New label

        hide_download : typing.Optional[str]
            New condition if the download should be hidden

        attributes : typing.Optional[str]
            New additional attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilesSharingShareapiCreateShare200Response
            Share updated successfully

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
            await client.files_sharing_shareapi.update_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_share(
            id,
            permissions=permissions,
            password=password,
            send_password_by_talk=send_password_by_talk,
            public_upload=public_upload,
            expire_date=expire_date,
            note=note,
            label=label,
            hide_download=hide_download,
            attributes=attributes,
            request_options=request_options,
        )
        return _response.data

    async def delete_share(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share deleted successfully

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
            await client.files_sharing_shareapi.delete_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_share(id, request_options=request_options)
        return _response.data

    async def accept_share(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Share accepted successfully

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
            await client.files_sharing_shareapi.accept_share(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_share(id, request_options=request_options)
        return _response.data
