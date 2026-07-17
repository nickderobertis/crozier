

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_key import ApiKey
from ..types.deleted import Deleted
from ..types.group import Group
from ..types.patch import Patch
from ..types.quotas import Quotas
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApikeysClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def all_api_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_keys_from_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        group_id : str
            The api key group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_api_key_from_group(
        self,
        group_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiKey]:
        """
        Create a new api key for a group

        Parameters
        ----------
        group_id : str
            The api key group id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys",
            method="POST",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKey]:
        """
        Get an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_api_key_from_group(
        self,
        group_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiKey]:
        """
        Update an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
        """
        Delete an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_api_key_from_group(
        self, group_id: str, client_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Quotas]:
        """
        Get the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Quotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reset_api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Quotas]:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Quotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_keys(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        service_id : str
            The api key service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_api_key(
        self,
        service_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiKey]:
        """


        Parameters
        ----------
        service_id : str
            The api key service id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys",
            method="POST",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApiKey]:
        """
        Get an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_api_key(
        self,
        service_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
        """
        Delete an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_api_key(
        self,
        service_id: str,
        client_id: str,
        *,
        request: Patch,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiKey]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_key_group(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Group]:
        """
        Get the group of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Group]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/group",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Quotas]:
        """
        Get the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Quotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def reset_api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Quotas]:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Quotas]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawApikeysClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def all_api_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_keys_from_group(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        group_id : str
            The api key group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_api_key_from_group(
        self,
        group_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Create a new api key for a group

        Parameters
        ----------
        group_id : str
            The api key group id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys",
            method="POST",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Get an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_api_key_from_group(
        self,
        group_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Update an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_api_key_from_group(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete an api key for a specified service group

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_api_key_from_group(
        self, group_id: str, client_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}",
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Quotas]:
        """
        Get the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Quotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reset_api_key_from_group_quotas(
        self, group_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Quotas]:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        group_id : str
            The api key group id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Quotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(group_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_keys(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ApiKey]]:
        """
        Get all api keys for the group of a service

        Parameters
        ----------
        service_id : str
            The api key service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_api_key(
        self,
        service_id: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiKey]:
        """


        Parameters
        ----------
        service_id : str
            The api key service id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys",
            method="POST",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Get an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_api_key(
        self,
        service_id: str,
        client_id_: str,
        *,
        authorized_entities: typing.Sequence[str],
        client_id: str,
        client_name: str,
        client_secret: str,
        enabled: bool,
        daily_quota: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        monthly_quota: typing.Optional[int] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id_ : str
            the api key id

        authorized_entities : typing.Sequence[str]
            The group/service ids (prefixed by group_ or service_ on which the key is authorized

        client_id : str
            The unique id of the Api Key. Usually 16 random alpha numerical characters, but can be anything

        client_name : str
            The name of the api key, for humans ;-)

        client_secret : str
            The secret of the Api Key. Usually 64 random alpha numerical characters, but can be anything

        enabled : bool
            Whether or not the key is enabled. If disabled, resources won't be available to calls using this key

        daily_quota : typing.Optional[int]
            Authorized number of calls per day

        metadata : typing.Optional[typing.Dict[str, str]]
            Bunch of metadata for the key

        monthly_quota : typing.Optional[int]
            Authorized number of calls per month

        throttling_quota : typing.Optional[int]
            Authorized number of calls per second, measured on 10 seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id_)}",
            method="PUT",
            json={
                "authorizedEntities": authorized_entities,
                "clientId": client_id,
                "clientName": client_name,
                "clientSecret": client_secret,
                "dailyQuota": daily_quota,
                "enabled": enabled,
                "metadata": metadata,
                "monthlyQuota": monthly_quota,
                "throttlingQuota": throttling_quota,
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_api_key(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
        """
        Delete an api key for a specified service descriptor

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_api_key(
        self,
        service_id: str,
        client_id: str,
        *,
        request: Patch,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiKey]:
        """
        Update an api key for a specified service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiKey]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}",
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
                    ApiKey,
                    parse_obj_as(
                        type_=ApiKey,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_key_group(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Group]:
        """
        Get the group of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Group]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/group",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Group,
                    parse_obj_as(
                        type_=Group,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Quotas]:
        """
        Get the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Quotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def reset_api_key_quotas(
        self, service_id: str, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Quotas]:
        """
        Reset the quota state of an api key

        Parameters
        ----------
        service_id : str
            The api key service id

        client_id : str
            the api key id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Quotas]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/apikeys/{encode_path_param(client_id)}/quotas",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Quotas,
                    parse_obj_as(
                        type_=Quotas,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
