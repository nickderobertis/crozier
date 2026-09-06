

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
from ..types.api_paged_response_build_system_shared_dto_step import ApiPagedResponseBuildSystemSharedDtoStep
from ..types.build_system_shared_dto_parameter import BuildSystemSharedDtoParameter
from ..types.build_system_shared_dto_step import BuildSystemSharedDtoStep
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getsteps(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoStep]:
        """
        Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoStep]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/steps",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoStep,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoStep,
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

    def poststep(
        self,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/steps",
            method="POST",
            json={
                "ConfigRequired": config_required,
                "Deleted": deleted,
                "Description": description,
                "ImplementationID": implementation_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "StepID": step_id,
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

    def getstep(
        self,
        step_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BuildSystemSharedDtoStep]:
        """
        Gets a Step by ID. When successful, the response is the requested Step.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        step_id : int
            The ID of the Step to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoStep]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/steps/{encode_path_param(step_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoStep,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoStep,
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

    def putstep(
        self,
        step_id_: int,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        step_id_ : int
            The step ID of the step to update

        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/steps/{encode_path_param(step_id_)}",
            method="PUT",
            json={
                "ConfigRequired": config_required,
                "Deleted": deleted,
                "Description": description,
                "ImplementationID": implementation_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "StepID": step_id,
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


class AsyncRawStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getsteps(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoStep]:
        """
        Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoStep]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/steps",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "includeDeleted": include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoStep,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoStep,
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

    async def poststep(
        self,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/steps",
            method="POST",
            json={
                "ConfigRequired": config_required,
                "Deleted": deleted,
                "Description": description,
                "ImplementationID": implementation_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "StepID": step_id,
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

    async def getstep(
        self,
        step_id: int,
        *,
        is_include_deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BuildSystemSharedDtoStep]:
        """
        Gets a Step by ID. When successful, the response is the requested Step.
                    If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

        Parameters
        ----------
        step_id : int
            The ID of the Step to get.

        is_include_deleted : typing.Optional[bool]
            Does it include deleted step, or not

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoStep]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/steps/{encode_path_param(step_id)}",
            method="GET",
            params={
                "isIncludeDeleted": is_include_deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoStep,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoStep,
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

    async def putstep(
        self,
        step_id_: int,
        *,
        config_required: bool,
        implementation_id: str,
        name: str,
        deleted: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]] = OMIT,
        step_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        step_id_ : int
            The step ID of the step to update

        config_required : bool
            Indicates if the step requires configuration values to be provided by the build agent

        implementation_id : str
            The implementation ID used to lookup the step implementation when it is executed

        name : str
            The name of the step

        deleted : typing.Optional[bool]
            Read Only.  Indicates if the record is deleted.

        description : typing.Optional[str]
            A description of the step to be presented to a user

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameter]]
            The parameters for this step

        step_id : typing.Optional[int]
            The ID of the step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/steps/{encode_path_param(step_id_)}",
            method="PUT",
            json={
                "ConfigRequired": config_required,
                "Deleted": deleted,
                "Description": description,
                "ImplementationID": implementation_id,
                "Name": name,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters, annotation=typing.Sequence[BuildSystemSharedDtoParameter], direction="write"
                ),
                "StepID": step_id,
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
