

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_release import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
)
from ..types.content_submission_shared_business_entities_release import ContentSubmissionSharedBusinessEntitiesRelease
from .raw_client import AsyncRawReleaseClient, RawReleaseClient


OMIT = typing.cast(typing.Any, ...)


class ReleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReleaseClient
        """
        return self._raw_client

    def getreleases(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        visible: typing.Optional[bool] = None,
        bundle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease:
        """
        Gets a collection of Release. When successful, the response is a PagedResponse of Release.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        visible : typing.Optional[bool]
            Optional. Filter by visible.

        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.release.getreleases()
        """
        _response = self._raw_client.getreleases(
            limit=limit, offset=offset, visible=visible, bundle_id=bundle_id, request_options=request_options
        )
        return _response.data

    def postrelease(
        self,
        *,
        build_date: typing.Optional[dt.datetime] = OMIT,
        bundle_i_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        release_number: typing.Optional[str] = OMIT,
        visible: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a Release.  The body of the POST is the Release to create.
                    The ReleaseId will be assigned on creation of the Job.  When successful, the response
                    is the Release Id.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        build_date : typing.Optional[dt.datetime]
            Build Date

        bundle_i_ds : typing.Optional[typing.Sequence[str]]
            IDs of AUC Bundles associated with this Release.

        release_date : typing.Optional[dt.datetime]
            Release Date

        release_id : typing.Optional[int]
            Release ID

        release_number : typing.Optional[str]
            Release Number

        visible : typing.Optional[bool]
            Visible

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
        client.release.postrelease()
        """
        _response = self._raw_client.postrelease(
            build_date=build_date,
            bundle_i_ds=bundle_i_ds,
            release_date=release_date,
            release_id=release_id,
            release_number=release_number,
            visible=visible,
            request_options=request_options,
        )
        return _response.data

    def getrelease(
        self, release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesRelease:
        """
        Gets a Release by ID. When successful, the response is the requested Release.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        release_id : int
            The ID of the Release to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesRelease
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.release.getrelease(
            release_id=1,
        )
        """
        _response = self._raw_client.getrelease(release_id, request_options=request_options)
        return _response.data

    def postreleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        release_id : int
            The release identifier.

        bundle_id : str
            The bundle identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.release.postreleasebundle(
            release_id=1,
            bundle_id="BundleId",
        )
        """
        _response = self._raw_client.postreleasebundle(release_id, bundle_id, request_options=request_options)
        return _response.data

    def deletereleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        release_id : int
            The release identifier.

        bundle_id : str
            The bundle identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.release.deletereleasebundle(
            release_id=1,
            bundle_id="BundleId",
        )
        """
        _response = self._raw_client.deletereleasebundle(release_id, bundle_id, request_options=request_options)
        return _response.data

    def putcontentdefinition(
        self,
        release_id_: int,
        *,
        build_date: typing.Optional[dt.datetime] = OMIT,
        bundle_i_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        release_number: typing.Optional[str] = OMIT,
        visible: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Release.  The body of the PUT is the updated Release.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        release_id_ : int
            The ID of the Release to update

        build_date : typing.Optional[dt.datetime]
            Build Date

        bundle_i_ds : typing.Optional[typing.Sequence[str]]
            IDs of AUC Bundles associated with this Release.

        release_date : typing.Optional[dt.datetime]
            Release Date

        release_id : typing.Optional[int]
            Release ID

        release_number : typing.Optional[str]
            Release Number

        visible : typing.Optional[bool]
            Visible

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.release.putcontentdefinition(
            release_id_=1,
        )
        """
        _response = self._raw_client.putcontentdefinition(
            release_id_,
            build_date=build_date,
            bundle_i_ds=bundle_i_ds,
            release_date=release_date,
            release_id=release_id,
            release_number=release_number,
            visible=visible,
            request_options=request_options,
        )
        return _response.data


class AsyncReleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReleaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReleaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReleaseClient
        """
        return self._raw_client

    async def getreleases(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        visible: typing.Optional[bool] = None,
        bundle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease:
        """
        Gets a collection of Release. When successful, the response is a PagedResponse of Release.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        visible : typing.Optional[bool]
            Optional. Filter by visible.

        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.release.getreleases()


        asyncio.run(main())
        """
        _response = await self._raw_client.getreleases(
            limit=limit, offset=offset, visible=visible, bundle_id=bundle_id, request_options=request_options
        )
        return _response.data

    async def postrelease(
        self,
        *,
        build_date: typing.Optional[dt.datetime] = OMIT,
        bundle_i_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        release_number: typing.Optional[str] = OMIT,
        visible: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a Release.  The body of the POST is the Release to create.
                    The ReleaseId will be assigned on creation of the Job.  When successful, the response
                    is the Release Id.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        build_date : typing.Optional[dt.datetime]
            Build Date

        bundle_i_ds : typing.Optional[typing.Sequence[str]]
            IDs of AUC Bundles associated with this Release.

        release_date : typing.Optional[dt.datetime]
            Release Date

        release_id : typing.Optional[int]
            Release ID

        release_number : typing.Optional[str]
            Release Number

        visible : typing.Optional[bool]
            Visible

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
            await client.release.postrelease()


        asyncio.run(main())
        """
        _response = await self._raw_client.postrelease(
            build_date=build_date,
            bundle_i_ds=bundle_i_ds,
            release_date=release_date,
            release_id=release_id,
            release_number=release_number,
            visible=visible,
            request_options=request_options,
        )
        return _response.data

    async def getrelease(
        self, release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContentSubmissionSharedBusinessEntitiesRelease:
        """
        Gets a Release by ID. When successful, the response is the requested Release.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        release_id : int
            The ID of the Release to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContentSubmissionSharedBusinessEntitiesRelease
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.release.getrelease(
                release_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getrelease(release_id, request_options=request_options)
        return _response.data

    async def postreleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        release_id : int
            The release identifier.

        bundle_id : str
            The bundle identifier.

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
            await client.release.postreleasebundle(
                release_id=1,
                bundle_id="BundleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postreleasebundle(release_id, bundle_id, request_options=request_options)
        return _response.data

    async def deletereleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        release_id : int
            The release identifier.

        bundle_id : str
            The bundle identifier.

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
            await client.release.deletereleasebundle(
                release_id=1,
                bundle_id="BundleId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletereleasebundle(release_id, bundle_id, request_options=request_options)
        return _response.data

    async def putcontentdefinition(
        self,
        release_id_: int,
        *,
        build_date: typing.Optional[dt.datetime] = OMIT,
        bundle_i_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        release_id: typing.Optional[int] = OMIT,
        release_number: typing.Optional[str] = OMIT,
        visible: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates a Release.  The body of the PUT is the updated Release.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        release_id_ : int
            The ID of the Release to update

        build_date : typing.Optional[dt.datetime]
            Build Date

        bundle_i_ds : typing.Optional[typing.Sequence[str]]
            IDs of AUC Bundles associated with this Release.

        release_date : typing.Optional[dt.datetime]
            Release Date

        release_id : typing.Optional[int]
            Release ID

        release_number : typing.Optional[str]
            Release Number

        visible : typing.Optional[bool]
            Visible

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
            await client.release.putcontentdefinition(
                release_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putcontentdefinition(
            release_id_,
            build_date=build_date,
            bundle_i_ds=bundle_i_ds,
            release_date=release_date,
            release_id=release_id,
            release_number=release_number,
            visible=visible,
            request_options=request_options,
        )
        return _response.data
