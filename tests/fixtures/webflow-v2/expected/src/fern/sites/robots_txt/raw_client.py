

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from .types.delete_robots_txt_request_rules_item import DeleteRobotsTxtRequestRulesItem
from .types.delete_robots_txt_response import DeleteRobotsTxtResponse
from .types.get_robots_txt_response import GetRobotsTxtResponse
from .types.patch_robots_txt_request_rules_item import PatchRobotsTxtRequestRulesItem
from .types.patch_robots_txt_response import PatchRobotsTxtResponse
from .types.put_robots_txt_request_rules_item import PutRobotsTxtRequestRulesItem
from .types.put_robots_txt_response import PutRobotsTxtResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRobotsTxtClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRobotsTxtResponse]:
        """
        Retrieve the robots.txt configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRobotsTxtResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRobotsTxtResponse,
                    parse_obj_as(
                        type_=GetRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def put(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutRobotsTxtResponse]:
        """
        Replace the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutRobotsTxtResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PutRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    PutRobotsTxtResponse,
                    parse_obj_as(
                        type_=PutRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteRobotsTxtResponse]:
        """
        Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.

        **Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteRobotsTxtResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[DeleteRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    DeleteRobotsTxtResponse,
                    parse_obj_as(
                        type_=DeleteRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    def patch(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PatchRobotsTxtResponse]:
        """
        Update the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PatchRobotsTxtResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PatchRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    PatchRobotsTxtResponse,
                    parse_obj_as(
                        type_=PatchRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawRobotsTxtClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRobotsTxtResponse]:
        """
        Retrieve the robots.txt configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRobotsTxtResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRobotsTxtResponse,
                    parse_obj_as(
                        type_=GetRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def put(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutRobotsTxtResponse]:
        """
        Replace the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PutRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutRobotsTxtResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="PUT",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PutRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    PutRobotsTxtResponse,
                    parse_obj_as(
                        type_=PutRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteRobotsTxtResponse]:
        """
        Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.

        **Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope: `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[DeleteRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteRobotsTxtResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[DeleteRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    DeleteRobotsTxtResponse,
                    parse_obj_as(
                        type_=DeleteRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def patch(
        self,
        site_id: str,
        *,
        rules: typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]] = OMIT,
        sitemap: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PatchRobotsTxtResponse]:
        """
        Update the `robots.txt` configuration for various user agents.

        <Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

        Required scope | `site_config:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        rules : typing.Optional[typing.Sequence[PatchRobotsTxtRequestRulesItem]]
            List of rules for user agents.

        sitemap : typing.Optional[str]
            URL to the sitemap.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PatchRobotsTxtResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/robots_txt",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules, annotation=typing.Sequence[PatchRobotsTxtRequestRulesItem], direction="write"
                ),
                "sitemap": sitemap,
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
                    PatchRobotsTxtResponse,
                    parse_obj_as(
                        type_=PatchRobotsTxtResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            if _response.status_code == 500:
                raise InternalServerError(
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
