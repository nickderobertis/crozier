

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_paged_response_build_system_shared_dto_job import ApiPagedResponseBuildSystemSharedDtoJob
from ..types.build_system_shared_dto_job import BuildSystemSharedDtoJob
from ..types.build_system_shared_dto_job_activity import BuildSystemSharedDtoJobActivity
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getjobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoJob]:
        """
        Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.
                    If unsuccessful, an appropriate ApiError is returned.
                    ///

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoJob]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/jobs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoJob,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoJob,
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

    def postjob(
        self,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on
                    creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/jobs",
            method="POST",
            json={
                "Activities": convert_and_respect_annotation_metadata(
                    object_=activities, annotation=typing.Sequence[BuildSystemSharedDtoJobActivity], direction="write"
                ),
                "Deleted": deleted,
                "JobID": job_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
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

    def getjob(
        self,
        job_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildSystemSharedDtoJob]:
        """
        Gets a Job by ID. When successful, the response is the requested Job.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id : int
            The ID of the Job to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoJob]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoJob,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoJob,
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

    def putjob(
        self,
        job_id_: int,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id_ : int
            The id of the job to update

        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id_)}",
            method="PUT",
            json={
                "Activities": convert_and_respect_annotation_metadata(
                    object_=activities, annotation=typing.Sequence[BuildSystemSharedDtoJobActivity], direction="write"
                ),
                "Deleted": deleted,
                "JobID": job_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
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

    def deletejob(self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_id : int
            The id of the job to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id)}",
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getjobs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoJob]:
        """
        Gets a collection of Jobs. When successful, the response is a PagedResponse of Jobs.
                    If unsuccessful, an appropriate ApiError is returned.
                    ///

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoJob]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/jobs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoJob,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoJob,
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

    async def postjob(
        self,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates a Job.  The body of the POST is the Job to create.  The JobID will be assigned on
                    creation of the Job.  When successful, the response is the JobID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/jobs",
            method="POST",
            json={
                "Activities": convert_and_respect_annotation_metadata(
                    object_=activities, annotation=typing.Sequence[BuildSystemSharedDtoJobActivity], direction="write"
                ),
                "Deleted": deleted,
                "JobID": job_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
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

    async def getjob(
        self,
        job_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildSystemSharedDtoJob]:
        """
        Gets a Job by ID. When successful, the response is the requested Job.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id : int
            The ID of the Job to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted job, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoJob]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoJob,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoJob,
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

    async def putjob(
        self,
        job_id_: int,
        *,
        activities: typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates a Job.  The body of the PUT is the updated Job.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_id_ : int
            The id of the job to update

        activities : typing.Optional[typing.Sequence[BuildSystemSharedDtoJobActivity]]
            The activities which are performed for the job

        deleted : typing.Optional[bool]
            Indicates if the job has been deleted.

        job_id : typing.Optional[int]
            The ID of the job

        name : typing.Optional[str]
            The name of the job

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id_)}",
            method="PUT",
            json={
                "Activities": convert_and_respect_annotation_metadata(
                    object_=activities, annotation=typing.Sequence[BuildSystemSharedDtoJobActivity], direction="write"
                ),
                "Deleted": deleted,
                "JobID": job_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
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

    async def deletejob(
        self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a Job. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_id : int
            The id of the job to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/jobs/{encode_path_param(job_id)}",
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
