

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.algorithm_advisory import AlgorithmAdvisory
from ..types.error_response import ErrorResponse
from .types.auto_apply_advisories_response import AutoApplyAdvisoriesResponse
from .types.check_advisories_response import CheckAdvisoriesResponse
from .types.get_algorithm_advisories_response import GetAlgorithmAdvisoriesResponse
from .types.publish_advisory_response import PublishAdvisoryResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAdvisoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_algorithm_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAlgorithmAdvisoriesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAlgorithmAdvisoriesResponse]
            Published algorithm advisories
        """
        _response = self._client_wrapper.httpx_client.request(
            ".well-known/algorithm-advisories.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAlgorithmAdvisoriesResponse,
                    parse_obj_as(
                        type_=GetAlgorithmAdvisoriesResponse,
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

    def publish_advisory(
        self, *, advisory: AlgorithmAdvisory, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PublishAdvisoryResponse]:
        """
        Publishes a governance-signed algorithm advisory (deprecate/warn/revoke).

        Parameters
        ----------
        advisory : AlgorithmAdvisory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PublishAdvisoryResponse]
            Advisory published
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/advisory/publish",
            method="POST",
            json={
                "advisory": convert_and_respect_annotation_metadata(
                    object_=advisory, annotation=AlgorithmAdvisory, direction="write"
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
                _data = typing.cast(
                    PublishAdvisoryResponse,
                    parse_obj_as(
                        type_=PublishAdvisoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def check_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckAdvisoriesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckAdvisoriesResponse]
            Active advisory status
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/advisory/check",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckAdvisoriesResponse,
                    parse_obj_as(
                        type_=CheckAdvisoriesResponse,
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

    def auto_apply_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AutoApplyAdvisoriesResponse]:
        """
        Scans active advisories and automatically updates the verifier policy
        by removing deprecated/revoked algorithms and adding replacements.
        May auto-switch to pq_only mode if all classical algorithms are removed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AutoApplyAdvisoriesResponse]
            Advisory auto-apply result
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/advisory/auto-apply",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutoApplyAdvisoriesResponse,
                    parse_obj_as(
                        type_=AutoApplyAdvisoriesResponse,
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


class AsyncRawAdvisoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_algorithm_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAlgorithmAdvisoriesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAlgorithmAdvisoriesResponse]
            Published algorithm advisories
        """
        _response = await self._client_wrapper.httpx_client.request(
            ".well-known/algorithm-advisories.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAlgorithmAdvisoriesResponse,
                    parse_obj_as(
                        type_=GetAlgorithmAdvisoriesResponse,
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

    async def publish_advisory(
        self, *, advisory: AlgorithmAdvisory, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PublishAdvisoryResponse]:
        """
        Publishes a governance-signed algorithm advisory (deprecate/warn/revoke).

        Parameters
        ----------
        advisory : AlgorithmAdvisory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PublishAdvisoryResponse]
            Advisory published
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/advisory/publish",
            method="POST",
            json={
                "advisory": convert_and_respect_annotation_metadata(
                    object_=advisory, annotation=AlgorithmAdvisory, direction="write"
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
                _data = typing.cast(
                    PublishAdvisoryResponse,
                    parse_obj_as(
                        type_=PublishAdvisoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def check_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckAdvisoriesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckAdvisoriesResponse]
            Active advisory status
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/advisory/check",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckAdvisoriesResponse,
                    parse_obj_as(
                        type_=CheckAdvisoriesResponse,
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

    async def auto_apply_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AutoApplyAdvisoriesResponse]:
        """
        Scans active advisories and automatically updates the verifier policy
        by removing deprecated/revoked algorithms and adding replacements.
        May auto-switch to pq_only mode if all classical algorithms are removed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AutoApplyAdvisoriesResponse]
            Advisory auto-apply result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/advisory/auto-apply",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AutoApplyAdvisoriesResponse,
                    parse_obj_as(
                        type_=AutoApplyAdvisoriesResponse,
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
