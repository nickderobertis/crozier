

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
from ..types.envelope_annotated_union_registered_project_function_get_registered_solver_function_get_field_info_annotation_none_type_required_true_discriminator_function_class import (
    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
)
from ..types.envelope_dict_new_type_function_group_access_rights_get import (
    EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
)
from ..types.envelope_function_group_access_rights_get import EnvelopeFunctionGroupAccessRightsGet
from ..types.envelope_list_annotated_union_registered_project_function_get_registered_solver_function_get_field_info_annotation_none_type_required_true_discriminator_function_class import (
    EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
)
from ..types.group_id_int import GroupIdInt
from .types.register_function_request import RegisterFunctionRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_functions(
        self,
        *,
        include_extras: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[
        EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        include_extras : typing.Optional[bool]

        search : typing.Optional[str]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/functions",
            method="GET",
            params={
                "include_extras": include_extras,
                "search": search,
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    def register_function(
        self, *, request: RegisterFunctionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        request : RegisterFunctionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/functions",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RegisterFunctionRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    def get_function(
        self,
        function_id: str,
        *,
        include_extras: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        function_id : str

        include_extras : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="GET",
            params={
                "include_extras": include_extras,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    def delete_function(
        self,
        function_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        function_id : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="DELETE",
            params={
                "force": force,
            },
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

    def update_function(
        self,
        function_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        function_id : str

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="PATCH",
            json={
                "title": title,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    def get_function_groups(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeDictNewTypeFunctionGroupAccessRightsGet]:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeDictNewTypeFunctionGroupAccessRightsGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
                    parse_obj_as(
                        type_=EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
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

    def create_or_update_function_group(
        self,
        function_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        execute: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeFunctionGroupAccessRightsGet]:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        execute : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeFunctionGroupAccessRightsGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "execute": execute,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeFunctionGroupAccessRightsGet,
                    parse_obj_as(
                        type_=EnvelopeFunctionGroupAccessRightsGet,
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

    def delete_function_group(
        self, function_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups/{encode_path_param(group_id)}",
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


class AsyncRawFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_functions(
        self,
        *,
        include_extras: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        filters: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[
        EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        include_extras : typing.Optional[bool]

        search : typing.Optional[str]

        filters : typing.Optional[str]

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/functions",
            method="GET",
            params={
                "include_extras": include_extras,
                "search": search,
                "filters": filters,
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeListAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    async def register_function(
        self, *, request: RegisterFunctionRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        request : RegisterFunctionRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/functions",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=RegisterFunctionRequest, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    async def get_function(
        self,
        function_id: str,
        *,
        include_extras: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        function_id : str

        include_extras : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="GET",
            params={
                "include_extras": include_extras,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    async def delete_function(
        self,
        function_id: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        function_id : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="DELETE",
            params={
                "force": force,
            },
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

    async def update_function(
        self,
        function_id: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[
        EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass
    ]:
        """
        Parameters
        ----------
        function_id : str

        title : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}",
            method="PATCH",
            json={
                "title": title,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
                    parse_obj_as(
                        type_=EnvelopeAnnotatedUnionRegisteredProjectFunctionGetRegisteredSolverFunctionGetFieldInfoAnnotationNoneTypeRequiredTrueDiscriminatorFunctionClass,
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

    async def get_function_groups(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeDictNewTypeFunctionGroupAccessRightsGet]:
        """
        Parameters
        ----------
        function_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeDictNewTypeFunctionGroupAccessRightsGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
                    parse_obj_as(
                        type_=EnvelopeDictNewTypeFunctionGroupAccessRightsGet,
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

    async def create_or_update_function_group(
        self,
        function_id: str,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        execute: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeFunctionGroupAccessRightsGet]:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        read : bool

        write : bool

        execute : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeFunctionGroupAccessRightsGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "execute": execute,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeFunctionGroupAccessRightsGet,
                    parse_obj_as(
                        type_=EnvelopeFunctionGroupAccessRightsGet,
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

    async def delete_function_group(
        self, function_id: str, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        function_id : str

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/functions/{encode_path_param(function_id)}/groups/{encode_path_param(group_id)}",
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
