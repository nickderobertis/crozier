

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.artefact_matching_rule_base import ArtefactMatchingRuleBase
from ..types.http_validation_error import HttpValidationError
from ..types.permission import Permission
from ..types.team_response import TeamResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_teams(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TeamResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TeamResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/teams",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TeamResponse],
                    parse_obj_as(
                        type_=typing.List[TeamResponse],
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

    def create_team(
        self,
        *,
        name: str,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TeamResponse]:
        """
        Create a new team

        Parameters
        ----------
        name : str

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/teams",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "artefact_matching_rules": convert_and_respect_annotation_metadata(
                    object_=artefact_matching_rules,
                    annotation=typing.Sequence[ArtefactMatchingRuleBase],
                    direction="write",
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
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_team(
        self, team_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TeamResponse]:
        """
        Parameters
        ----------
        team_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_team(
        self,
        team_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TeamResponse]:
        """
        Parameters
        ----------
        team_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}",
            method="PATCH",
            json={
                "permissions": permissions,
                "artefact_matching_rules": convert_and_respect_annotation_metadata(
                    object_=artefact_matching_rules,
                    annotation=typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]],
                    direction="write",
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
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def add_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TeamResponse]:
        """
        Add a user to a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}/members/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def remove_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TeamResponse]:
        """
        Remove a user from a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TeamResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_teams(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TeamResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TeamResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/teams",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TeamResponse],
                    parse_obj_as(
                        type_=typing.List[TeamResponse],
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

    async def create_team(
        self,
        *,
        name: str,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TeamResponse]:
        """
        Create a new team

        Parameters
        ----------
        name : str

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/teams",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "artefact_matching_rules": convert_and_respect_annotation_metadata(
                    object_=artefact_matching_rules,
                    annotation=typing.Sequence[ArtefactMatchingRuleBase],
                    direction="write",
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
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_team(
        self, team_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TeamResponse]:
        """
        Parameters
        ----------
        team_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_team(
        self,
        team_id: int,
        *,
        permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        artefact_matching_rules: typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TeamResponse]:
        """
        Parameters
        ----------
        team_id : int

        permissions : typing.Optional[typing.Sequence[Permission]]

        artefact_matching_rules : typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}",
            method="PATCH",
            json={
                "permissions": permissions,
                "artefact_matching_rules": convert_and_respect_annotation_metadata(
                    object_=artefact_matching_rules,
                    annotation=typing.Optional[typing.Sequence[ArtefactMatchingRuleBase]],
                    direction="write",
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
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def add_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TeamResponse]:
        """
        Add a user to a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}/members/{encode_path_param(user_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def remove_team_member(
        self, team_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TeamResponse]:
        """
        Remove a user from a team

        Parameters
        ----------
        team_id : int

        user_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TeamResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/teams/{encode_path_param(team_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TeamResponse,
                    parse_obj_as(
                        type_=TeamResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
