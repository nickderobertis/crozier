

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.v1project_advisors_response_output import V1ProjectAdvisorsResponseOutput
from .types.v1get_security_advisors_request_lint_type import V1GetSecurityAdvisorsRequestLintType
from pydantic import ValidationError


class RawAdvisorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1get_performance_advisors(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1ProjectAdvisorsResponseOutput]:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1ProjectAdvisorsResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/advisors/performance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1ProjectAdvisorsResponseOutput,
                    parse_obj_as(
                        type_=V1ProjectAdvisorsResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def v1get_security_advisors(
        self,
        ref: str,
        *,
        lint_type: typing.Optional[V1GetSecurityAdvisorsRequestLintType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1ProjectAdvisorsResponseOutput]:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        lint_type : typing.Optional[V1GetSecurityAdvisorsRequestLintType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1ProjectAdvisorsResponseOutput]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/advisors/security",
            method="GET",
            params={
                "lint_type": lint_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1ProjectAdvisorsResponseOutput,
                    parse_obj_as(
                        type_=V1ProjectAdvisorsResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawAdvisorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1get_performance_advisors(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1ProjectAdvisorsResponseOutput]:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1ProjectAdvisorsResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/advisors/performance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1ProjectAdvisorsResponseOutput,
                    parse_obj_as(
                        type_=V1ProjectAdvisorsResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def v1get_security_advisors(
        self,
        ref: str,
        *,
        lint_type: typing.Optional[V1GetSecurityAdvisorsRequestLintType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1ProjectAdvisorsResponseOutput]:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        lint_type : typing.Optional[V1GetSecurityAdvisorsRequestLintType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1ProjectAdvisorsResponseOutput]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(ref)}/advisors/security",
            method="GET",
            params={
                "lint_type": lint_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1ProjectAdvisorsResponseOutput,
                    parse_obj_as(
                        type_=V1ProjectAdvisorsResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
