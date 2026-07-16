

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.deleted import Deleted
from ..types.global_jwt_verifier import GlobalJwtVerifier
from ..types.global_jwt_verifier_algo_settings import GlobalJwtVerifierAlgoSettings
from ..types.global_jwt_verifier_source import GlobalJwtVerifierSource
from ..types.global_jwt_verifier_strategy import GlobalJwtVerifierStrategy
from ..types.patch import Patch


OMIT = typing.cast(typing.Any, ...)


class RawJwtVerifiersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_all_global_jwt_verifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GlobalJwtVerifier]]:
        """
        Get all global JWT verifiers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GlobalJwtVerifier]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/verifiers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GlobalJwtVerifier],
                    parse_obj_as(
                        type_=typing.List[GlobalJwtVerifier],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_global_jwt_verifier(
        self,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalJwtVerifier]:
        """
        Create one global JWT verifiers

        Parameters
        ----------
        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/verifiers",
            method="POST",
            json={
                "algoSettings": convert_and_respect_annotation_metadata(
                    object_=algo_settings, annotation=GlobalJwtVerifierAlgoSettings, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "id": id,
                "name": name,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=GlobalJwtVerifierSource, direction="write"
                ),
                "strategy": convert_and_respect_annotation_metadata(
                    object_=strategy, annotation=GlobalJwtVerifierStrategy, direction="write"
                ),
                "strict": strict,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def find_global_jwt_verifiers_by_id(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalJwtVerifier]:
        """
        Get one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_global_jwt_verifier(
        self,
        verifier_id: str,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalJwtVerifier]:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="PUT",
            json={
                "algoSettings": convert_and_respect_annotation_metadata(
                    object_=algo_settings, annotation=GlobalJwtVerifierAlgoSettings, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "id": id,
                "name": name,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=GlobalJwtVerifierSource, direction="write"
                ),
                "strategy": convert_and_respect_annotation_metadata(
                    object_=strategy, annotation=GlobalJwtVerifierStrategy, direction="write"
                ),
                "strict": strict,
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
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_global_jwt_verifier(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
        """
        Delete one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_global_jwt_verifier(
        self, verifier_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalJwtVerifier]:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawJwtVerifiersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_all_global_jwt_verifiers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GlobalJwtVerifier]]:
        """
        Get all global JWT verifiers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GlobalJwtVerifier]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/verifiers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GlobalJwtVerifier],
                    parse_obj_as(
                        type_=typing.List[GlobalJwtVerifier],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_global_jwt_verifier(
        self,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalJwtVerifier]:
        """
        Create one global JWT verifiers

        Parameters
        ----------
        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/verifiers",
            method="POST",
            json={
                "algoSettings": convert_and_respect_annotation_metadata(
                    object_=algo_settings, annotation=GlobalJwtVerifierAlgoSettings, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "id": id,
                "name": name,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=GlobalJwtVerifierSource, direction="write"
                ),
                "strategy": convert_and_respect_annotation_metadata(
                    object_=strategy, annotation=GlobalJwtVerifierStrategy, direction="write"
                ),
                "strict": strict,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def find_global_jwt_verifiers_by_id(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalJwtVerifier]:
        """
        Get one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_global_jwt_verifier(
        self,
        verifier_id: str,
        *,
        algo_settings: GlobalJwtVerifierAlgoSettings,
        desc: str,
        enabled: bool,
        id: str,
        name: str,
        source: GlobalJwtVerifierSource,
        strategy: GlobalJwtVerifierStrategy,
        strict: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalJwtVerifier]:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        algo_settings : GlobalJwtVerifierAlgoSettings

        desc : str
            Verifier description

        enabled : bool
            Is it enabled

        id : str
            Verifier id

        name : str
            Verifier name

        source : GlobalJwtVerifierSource

        strategy : GlobalJwtVerifierStrategy

        strict : bool
            Does it fail if JWT not found

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="PUT",
            json={
                "algoSettings": convert_and_respect_annotation_metadata(
                    object_=algo_settings, annotation=GlobalJwtVerifierAlgoSettings, direction="write"
                ),
                "desc": desc,
                "enabled": enabled,
                "id": id,
                "name": name,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=GlobalJwtVerifierSource, direction="write"
                ),
                "strategy": convert_and_respect_annotation_metadata(
                    object_=strategy, annotation=GlobalJwtVerifierStrategy, direction="write"
                ),
                "strict": strict,
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
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_global_jwt_verifier(
        self, verifier_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_global_jwt_verifier(
        self, verifier_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalJwtVerifier]:
        """
        Update one global JWT verifiers

        Parameters
        ----------
        verifier_id : str
            The jwt verifier id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalJwtVerifier]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/verifiers/{jsonable_encoder(verifier_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalJwtVerifier,
                    parse_obj_as(
                        type_=GlobalJwtVerifier,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
