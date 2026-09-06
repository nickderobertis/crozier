

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
from ..types.content_submission_shared_business_entities_content_release_version import (
    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContentreleaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcontentreleaseversion(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentSubmissionSharedBusinessEntitiesContentReleaseVersion]:
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
        HttpResponse[ContentSubmissionSharedBusinessEntitiesContentReleaseVersion]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
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
    ) -> HttpResponse[int]:
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
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/ContentReleases",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
                "ContentReleaseID": content_release_id,
                "Deleted": deleted,
                "PublisherUserID": publisher_user_id,
                "ReleaseID": release_id,
                "TestReportUrl": test_report_url,
                "UpdatedDate": updated_date,
                "Version": version,
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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id_)}",
            method="PUT",
            json={
                "ContentDefinitionID": content_definition_id,
                "ContentReleaseID": content_release_id,
                "Deleted": deleted,
                "PublisherUserID": publisher_user_id,
                "ReleaseID": release_id,
                "TestReportUrl": test_report_url,
                "UpdatedDate": updated_date,
                "Version": version,
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

    def deletecontentreleaseversionn(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id)}",
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


class AsyncRawContentreleaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcontentreleaseversion(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentReleaseVersion]:
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
        AsyncHttpResponse[ContentSubmissionSharedBusinessEntitiesContentReleaseVersion]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
                    parse_obj_as(
                        type_=ContentSubmissionSharedBusinessEntitiesContentReleaseVersion,
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
    ) -> AsyncHttpResponse[int]:
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
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/ContentReleases",
            method="POST",
            json={
                "ContentDefinitionID": content_definition_id,
                "ContentReleaseID": content_release_id,
                "Deleted": deleted,
                "PublisherUserID": publisher_user_id,
                "ReleaseID": release_id,
                "TestReportUrl": test_report_url,
                "UpdatedDate": updated_date,
                "Version": version,
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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id_)}",
            method="PUT",
            json={
                "ContentDefinitionID": content_definition_id,
                "ContentReleaseID": content_release_id,
                "Deleted": deleted,
                "PublisherUserID": publisher_user_id,
                "ReleaseID": release_id,
                "TestReportUrl": test_report_url,
                "UpdatedDate": updated_date,
                "Version": version,
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

    async def deletecontentreleaseversionn(
        self, content_release_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/ContentReleases/{encode_path_param(content_release_id)}",
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
