

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..types.scoped_secret_result_body import ScopedSecretResultBody
from ..types.secret_filter_body import SecretFilterBody
from ..types.secret_scope import SecretScope
from ..types.secret_type import SecretType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSecretsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_api_v1secrets(
        self, *, plan_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ScopedSecretResultBody]]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ScopedSecretResultBody]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/Secrets",
            method="GET",
            params={
                "planId": plan_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScopedSecretResultBody],
                    parse_obj_as(
                        type_=typing.List[ScopedSecretResultBody],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_api_v1secrets(
        self,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        type: typing.Optional[SecretType] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        type : typing.Optional[SecretType]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScopedSecretResultBody]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/Secrets",
            method="POST",
            params={
                "planId": plan_id,
            },
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Optional[typing.Sequence[SecretFilterBody]], direction="write"
                ),
                "notes": notes,
                "scope": scope,
                "secretName": secret_name,
                "type": type,
                "value": value,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScopedSecretResultBody,
                    parse_obj_as(
                        type_=ScopedSecretResultBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScopedSecretResultBody]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Secrets/{encode_path_param(secret_id)}",
            method="PUT",
            params={
                "planId": plan_id,
            },
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Optional[typing.Sequence[SecretFilterBody]], direction="write"
                ),
                "notes": notes,
                "scope": scope,
                "secretName": secret_name,
                "value": value,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScopedSecretResultBody,
                    parse_obj_as(
                        type_=ScopedSecretResultBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        scope: typing.Optional[SecretScope] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/Secrets/{encode_path_param(secret_id)}",
            method="DELETE",
            params={
                "planId": plan_id,
                "scope": scope,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSecretsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_api_v1secrets(
        self, *, plan_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ScopedSecretResultBody]]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ScopedSecretResultBody]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/Secrets",
            method="GET",
            params={
                "planId": plan_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ScopedSecretResultBody],
                    parse_obj_as(
                        type_=typing.List[ScopedSecretResultBody],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_api_v1secrets(
        self,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        type: typing.Optional[SecretType] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        type : typing.Optional[SecretType]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScopedSecretResultBody]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/Secrets",
            method="POST",
            params={
                "planId": plan_id,
            },
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Optional[typing.Sequence[SecretFilterBody]], direction="write"
                ),
                "notes": notes,
                "scope": scope,
                "secretName": secret_name,
                "type": type,
                "value": value,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScopedSecretResultBody,
                    parse_obj_as(
                        type_=ScopedSecretResultBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        filters: typing.Optional[typing.Sequence[SecretFilterBody]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        scope: typing.Optional[SecretScope] = OMIT,
        secret_name: typing.Optional[str] = OMIT,
        value: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScopedSecretResultBody]:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[SecretFilterBody]]

        notes : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        secret_name : typing.Optional[str]

        value : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScopedSecretResultBody]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Secrets/{encode_path_param(secret_id)}",
            method="PUT",
            params={
                "planId": plan_id,
            },
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=typing.Optional[typing.Sequence[SecretFilterBody]], direction="write"
                ),
                "notes": notes,
                "scope": scope,
                "secretName": secret_name,
                "value": value,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScopedSecretResultBody,
                    parse_obj_as(
                        type_=ScopedSecretResultBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_api_v1secrets_secret_id(
        self,
        secret_id: str,
        *,
        plan_id: typing.Optional[str] = None,
        scope: typing.Optional[SecretScope] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        secret_id : str

        plan_id : typing.Optional[str]

        scope : typing.Optional[SecretScope]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/Secrets/{encode_path_param(secret_id)}",
            method="DELETE",
            params={
                "planId": plan_id,
                "scope": scope,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
