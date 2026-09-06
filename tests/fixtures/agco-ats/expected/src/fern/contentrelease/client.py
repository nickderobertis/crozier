

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.content_submission_shared_business_entities_content_release_version import (
    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
)
from .raw_client import AsyncRawContentreleaseClient, RawContentreleaseClient


OMIT = typing.cast(typing.Any, ...)


class ContentreleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContentreleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContentreleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContentreleaseClient
        """
        return self._raw_client

    def getcontentreleaseversion(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesContentReleaseVersion:
        """
        Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_release_id : int
            The ID of the ContentReleaseVersion to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentReleaseVersion
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentrelease.getcontentreleaseversion(
            content_release_id=1,
        )
        """
        _response = self._raw_client.getcontentreleaseversion(content_release_id, request_options=request_options)
        return _response.data

    def postcontentrelease(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        content_release_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        publisher_user_id: typing.Optional[int] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        test_report_url: typing.Optional[str] = OMIT,
        updated_date: typing.Optional[dt.datetime] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.
                    The ContentReleaseId will be assigned on creation of the Job.  When successful, the response
                    is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            ContentDefinitionID

        content_release_id : typing.Optional[int]
            ContentReleaseID

        deleted : typing.Optional[bool]
            deleted flag

        publisher_user_id : typing.Optional[int]
            PublisherUser ID

        release_id : typing.Optional[int]
            rele4ase Id

        test_report_url : typing.Optional[str]
            The URL at which test reports for this content can be found

        updated_date : typing.Optional[dt.datetime]
            Updated Date

        version : typing.Optional[int]
            version

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
        client.contentrelease.postcontentrelease()
        """
        _response = self._raw_client.postcontentrelease(
            content_definition_id=content_definition_id,
            content_release_id=content_release_id,
            deleted=deleted,
            publisher_user_id=publisher_user_id,
            release_id=release_id,
            test_report_url=test_report_url,
            updated_date=updated_date,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def putcontentdefinition(
        self,
        content_release_id_: int,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        content_release_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        publisher_user_id: typing.Optional[int] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        test_report_url: typing.Optional[str] = OMIT,
        updated_date: typing.Optional[dt.datetime] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_release_id_ : int
            The ID of the ContentReleaseVersion to update

        content_definition_id : typing.Optional[int]
            ContentDefinitionID

        content_release_id : typing.Optional[int]
            ContentReleaseID

        deleted : typing.Optional[bool]
            deleted flag

        publisher_user_id : typing.Optional[int]
            PublisherUser ID

        release_id : typing.Optional[int]
            rele4ase Id

        test_report_url : typing.Optional[str]
            The URL at which test reports for this content can be found

        updated_date : typing.Optional[dt.datetime]
            Updated Date

        version : typing.Optional[int]
            version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentrelease.putcontentdefinition(
            content_release_id_=1,
        )
        """
        _response = self._raw_client.putcontentdefinition(
            content_release_id_,
            content_definition_id=content_definition_id,
            content_release_id=content_release_id,
            deleted=deleted,
            publisher_user_id=publisher_user_id,
            release_id=release_id,
            test_report_url=test_report_url,
            updated_date=updated_date,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def deletecontentreleaseversionn(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_release_id : int
            The ID of the ContentReleaseVersion to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.contentrelease.deletecontentreleaseversionn(
            content_release_id=1,
        )
        """
        _response = self._raw_client.deletecontentreleaseversionn(content_release_id, request_options=request_options)
        return _response.data


class AsyncContentreleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContentreleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContentreleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContentreleaseClient
        """
        return self._raw_client

    async def getcontentreleaseversion(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesContentReleaseVersion:
        """
        Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_release_id : int
            The ID of the ContentReleaseVersion to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesContentReleaseVersion
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.contentrelease.getcontentreleaseversion(
                content_release_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcontentreleaseversion(content_release_id, request_options=request_options)
        return _response.data

    async def postcontentrelease(
        self,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        content_release_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        publisher_user_id: typing.Optional[int] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        test_report_url: typing.Optional[str] = OMIT,
        updated_date: typing.Optional[dt.datetime] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.
                    The ContentReleaseId will be assigned on creation of the Job.  When successful, the response
                    is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_definition_id : typing.Optional[int]
            ContentDefinitionID

        content_release_id : typing.Optional[int]
            ContentReleaseID

        deleted : typing.Optional[bool]
            deleted flag

        publisher_user_id : typing.Optional[int]
            PublisherUser ID

        release_id : typing.Optional[int]
            rele4ase Id

        test_report_url : typing.Optional[str]
            The URL at which test reports for this content can be found

        updated_date : typing.Optional[dt.datetime]
            Updated Date

        version : typing.Optional[int]
            version

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
            await client.contentrelease.postcontentrelease()


        asyncio.run(main())
        """
        _response = await self._raw_client.postcontentrelease(
            content_definition_id=content_definition_id,
            content_release_id=content_release_id,
            deleted=deleted,
            publisher_user_id=publisher_user_id,
            release_id=release_id,
            test_report_url=test_report_url,
            updated_date=updated_date,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def putcontentdefinition(
        self,
        content_release_id_: int,
        *,
        content_definition_id: typing.Optional[int] = OMIT,
        content_release_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        publisher_user_id: typing.Optional[int] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        test_report_url: typing.Optional[str] = OMIT,
        updated_date: typing.Optional[dt.datetime] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        content_release_id_ : int
            The ID of the ContentReleaseVersion to update

        content_definition_id : typing.Optional[int]
            ContentDefinitionID

        content_release_id : typing.Optional[int]
            ContentReleaseID

        deleted : typing.Optional[bool]
            deleted flag

        publisher_user_id : typing.Optional[int]
            PublisherUser ID

        release_id : typing.Optional[int]
            rele4ase Id

        test_report_url : typing.Optional[str]
            The URL at which test reports for this content can be found

        updated_date : typing.Optional[dt.datetime]
            Updated Date

        version : typing.Optional[int]
            version

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
            await client.contentrelease.putcontentdefinition(
                content_release_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentdefinition(
            content_release_id_,
            content_definition_id=content_definition_id,
            content_release_id=content_release_id,
            deleted=deleted,
            publisher_user_id=publisher_user_id,
            release_id=release_id,
            test_report_url=test_report_url,
            updated_date=updated_date,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def deletecontentreleaseversionn(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        content_release_id : int
            The ID of the ContentReleaseVersion to delete

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
            await client.contentrelease.deletecontentreleaseversionn(
                content_release_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecontentreleaseversionn(
            content_release_id, request_options=request_options
        )
        return _response.data
