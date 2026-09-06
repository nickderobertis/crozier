

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_content_submission_shared_business_entities_release import (
    ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
)
from ..types.content_submission_shared_business_entities_release import ContentSubmissionSharedBusinessEntitiesRelease
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawReleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getreleases(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        visible: typing.Optional[bool] = None,
        bundle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease]:
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
        HttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Releases",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "visible": visible,
                "bundleID": bundle_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[int]:
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
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Releases",
            method="POST",
            json={
                "BuildDate": build_date,
                "BundleIDs": bundle_i_ds,
                "ReleaseDate": release_date,
                "ReleaseID": release_id,
                "ReleaseNumber": release_number,
                "Visible": visible,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getrelease(
        self, release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesRelease]:
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
        HttpResponse[ContentSubmissionSharedBusinessEntitiesRelease]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesRelease,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesRelease,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def postreleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}/Bundle/{encode_path_param(bundle_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletereleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}/Bundle/{encode_path_param(bundle_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id_)}",
            method="PUT",
            json={
                "BuildDate": build_date,
                "BundleIDs": bundle_i_ds,
                "ReleaseDate": release_date,
                "ReleaseID": release_id,
                "ReleaseNumber": release_number,
                "Visible": visible,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawReleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getreleases(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        visible: typing.Optional[bool] = None,
        bundle_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease]:
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
        AsyncHttpResponse[ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Releases",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "visible": visible,
                "bundleID": bundle_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
                    parse_obj_as(
                        type_=ApiPagedResponseContentSubmissionSharedBusinessEntitiesRelease,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[int]:
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
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Releases",
            method="POST",
            json={
                "BuildDate": build_date,
                "BundleIDs": bundle_i_ds,
                "ReleaseDate": release_date,
                "ReleaseID": release_id,
                "ReleaseNumber": release_number,
                "Visible": visible,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getrelease(
        self, release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesRelease]:
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
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesRelease]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesRelease,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesRelease,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def postreleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}/Bundle/{encode_path_param(bundle_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletereleasebundle(
        self, release_id: int, bundle_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id)}/Bundle/{encode_path_param(bundle_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Releases/{encode_path_param(release_id_)}",
            method="PUT",
            json={
                "BuildDate": build_date,
                "BundleIDs": bundle_i_ds,
                "ReleaseDate": release_date,
                "ReleaseID": release_id,
                "ReleaseNumber": release_number,
                "Visible": visible,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
