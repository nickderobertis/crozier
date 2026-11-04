

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.forbidden_error_body import ForbiddenErrorBody
from ..types.unauthorized_error_body import UnauthorizedErrorBody
from .types.get_v3val_viewer_response import GetV3ValViewerResponse
from pydantic import ValidationError


class RawValClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_v3val_viewer(
        self, *, val_town_user: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetV3ValViewerResponse]:
        """
        Look up the identity of the viewer of an app-authenticated (intranet) val, given the X-Val-Town-User header value that Fastify forwarded to the val. Authenticated with the val's own API token (bearer auth). The projectId inside the signed header must match the caller's own project.

        Parameters
        ----------
        val_town_user : str
            The signed X-Val-Town-User header value Fastify forwarded to the val.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetV3ValViewerResponse]
            Public identity of the viewer derived from a verified X-Val-Town-User header. Only safe, public profile fields are returned — no email or tier.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v3/val/viewer",
            method="GET",
            headers={
                "x-val-town-user": str(val_town_user) if val_town_user is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV3ValViewerResponse,
                    parse_obj_as(
                        type_=GetV3ValViewerResponse,
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawValClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_v3val_viewer(
        self, *, val_town_user: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetV3ValViewerResponse]:
        """
        Look up the identity of the viewer of an app-authenticated (intranet) val, given the X-Val-Town-User header value that Fastify forwarded to the val. Authenticated with the val's own API token (bearer auth). The projectId inside the signed header must match the caller's own project.

        Parameters
        ----------
        val_town_user : str
            The signed X-Val-Town-User header value Fastify forwarded to the val.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetV3ValViewerResponse]
            Public identity of the viewer derived from a verified X-Val-Town-User header. Only safe, public profile fields are returned — no email or tier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v3/val/viewer",
            method="GET",
            headers={
                "x-val-town-user": str(val_town_user) if val_town_user is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetV3ValViewerResponse,
                    parse_obj_as(
                        type_=GetV3ValViewerResponse,
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
                        UnauthorizedErrorBody,
                        parse_obj_as(
                            type_=UnauthorizedErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ForbiddenErrorBody,
                        parse_obj_as(
                            type_=ForbiddenErrorBody,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
