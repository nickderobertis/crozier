

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
from ..types.api_paged_response_build_system_shared_dto_activity import ApiPagedResponseBuildSystemSharedDtoActivity
from ..types.build_system_shared_dto_activity import BuildSystemSharedDtoActivity
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getactivities(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoActivity]:
        """
        Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoActivity]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/activities",
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
                    ApiPagedResponseBuildSystemSharedDtoActivity,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoActivity,
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

    def postactivity(
        self,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned
                    on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/activities",
            method="POST",
            json={
                "ActivityID": activity_id,
                "Deleted": deleted,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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

    def getactivity(
        self,
        activity_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildSystemSharedDtoActivity]:
        """
        Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The ID of the Activity to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoActivity]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivity,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivity,
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

    def putactivity(
        self,
        activity_id_: int,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id_ : int
            The id of the activity to update

        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id_)}",
            method="PUT",
            json={
                "ActivityID": activity_id,
                "Deleted": deleted,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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

    def deleteactivity(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The id of the activity to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id)}",
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


class AsyncRawActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getactivities(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoActivity]:
        """
        Gets a collection of Activities. When successful, the response is a PagedResponse of Activities.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoActivity]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/activities",
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
                    ApiPagedResponseBuildSystemSharedDtoActivity,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoActivity,
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

    async def postactivity(
        self,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        Creates an Activity.  The body of the POST is the Activity to create.  The ActivityID will be assigned
                    on creation of the Activity.  When successful, the response is the ActivityID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/activities",
            method="POST",
            json={
                "ActivityID": activity_id,
                "Deleted": deleted,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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

    async def getactivity(
        self,
        activity_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildSystemSharedDtoActivity]:
        """
        Gets an Activity by ID. When successful, the response is the requested Activity.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The ID of the Activity to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted activity, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoActivity]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivity,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivity,
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

    async def putactivity(
        self,
        activity_id_: int,
        *,
        activity_id: typing.Optional[int] = OMIT,
        deleted: typing.Optional[bool] = OMIT,
        name: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates an Activity.  The body of the PUT is the updated Activity.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_id_ : int
            The id of the activity to update

        activity_id : typing.Optional[int]
            The ID of the activity

        deleted : typing.Optional[bool]


        name : typing.Optional[str]
            The name of the activity

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this activity

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            The steps which are performed for this activity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id_)}",
            method="PUT",
            json={
                "ActivityID": activity_id,
                "Deleted": deleted,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
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

    async def deleteactivity(
        self, activity_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes an Activity. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        activity_id : int
            The id of the activity to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/activities/{encode_path_param(activity_id)}",
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
