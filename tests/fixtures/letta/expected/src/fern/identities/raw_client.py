

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
from ..types.agent_state import AgentState
from ..types.block_response import BlockResponse
from ..types.http_validation_error import HttpValidationError
from ..types.identity import Identity
from ..types.identity_property import IdentityProperty
from ..types.identity_type import IdentityType
from .types.list_agents_for_identity_request_include_item import ListAgentsForIdentityRequestIncludeItem
from .types.list_agents_for_identity_request_order import ListAgentsForIdentityRequestOrder
from .types.list_agents_for_identity_request_order_by import ListAgentsForIdentityRequestOrderBy
from .types.list_blocks_for_identity_request_order import ListBlocksForIdentityRequestOrder
from .types.list_blocks_for_identity_request_order_by import ListBlocksForIdentityRequestOrderBy
from .types.list_identities_request_order import ListIdentitiesRequestOrder
from .types.list_identities_request_order_by import ListIdentitiesRequestOrderBy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIdentitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_identities(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListIdentitiesRequestOrder] = None,
        order_by: typing.Optional[ListIdentitiesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Identity]]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]
            [DEPRECATED: Use X-Project-Id header instead] Filter identities by project ID

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order

        after : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of identities to return

        order : typing.Optional[ListIdentitiesRequestOrder]
            Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListIdentitiesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Identity]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="GET",
            params={
                "name": name,
                "project_id": project_id,
                "identifier_key": identifier_key,
                "identity_type": identity_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Identity],
                    parse_obj_as(
                        type_=typing.List[Identity],
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

    def create_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="POST",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    def upsert_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="PUT",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    def count_identities(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[int]:
        """
        Get count of all identities for a user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/count",
            method="GET",
            request_options=request_options,
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

    def retrieve_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    def delete_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def update_identity(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="PATCH",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
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
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    def upsert_properties_for_identity(
        self,
        identity_id: str,
        *,
        request: typing.Sequence[IdentityProperty],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request : typing.Sequence[IdentityProperty]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/properties",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[IdentityProperty], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def list_agents_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForIdentityRequestOrderBy] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[AgentState]]:
        """
        Get all agents associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForIdentityRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForIdentityRequestOrderBy]
            Field to sort by

        include : typing.Optional[typing.Union[ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
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

    def list_blocks_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBlocksForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListBlocksForIdentityRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[BlockResponse]]:
        """
        Get all blocks associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListBlocksForIdentityRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksForIdentityRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/blocks",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
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


class AsyncRawIdentitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_identities(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListIdentitiesRequestOrder] = None,
        order_by: typing.Optional[ListIdentitiesRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Identity]]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]
            [DEPRECATED: Use X-Project-Id header instead] Filter identities by project ID

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order

        after : typing.Optional[str]
            Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of identities to return

        order : typing.Optional[ListIdentitiesRequestOrder]
            Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListIdentitiesRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Identity]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="GET",
            params={
                "name": name,
                "project_id": project_id,
                "identifier_key": identifier_key,
                "identity_type": identity_type,
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Identity],
                    parse_obj_as(
                        type_=typing.List[Identity],
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

    async def create_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="POST",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    async def upsert_identity(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project : typing.Optional[str]
            The project slug to associate with the identity (cloud only).

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="PUT",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Project": str(project) if project is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    async def count_identities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[int]:
        """
        Get count of all identities for a user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/count",
            method="GET",
            request_options=request_options,
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

    async def retrieve_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    async def delete_identity(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def update_identity(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}",
            method="PATCH",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Optional[typing.Sequence[IdentityProperty]], direction="write"
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
                    Identity,
                    parse_obj_as(
                        type_=Identity,
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

    async def upsert_properties_for_identity(
        self,
        identity_id: str,
        *,
        request: typing.Sequence[IdentityProperty],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        request : typing.Sequence[IdentityProperty]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/properties",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[IdentityProperty], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def list_agents_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAgentsForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListAgentsForIdentityRequestOrderBy] = None,
        include: typing.Optional[
            typing.Union[
                ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]
            ]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[AgentState]]:
        """
        Get all agents associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order

        after : typing.Optional[str]
            Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of agents to return

        order : typing.Optional[ListAgentsForIdentityRequestOrder]
            Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListAgentsForIdentityRequestOrderBy]
            Field to sort by

        include : typing.Optional[typing.Union[ListAgentsForIdentityRequestIncludeItem, typing.Sequence[ListAgentsForIdentityRequestIncludeItem]]]
            Specify which relational fields to include in the response. No relationships are included by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AgentState]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/agents",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
                "include": include,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgentState],
                    parse_obj_as(
                        type_=typing.List[AgentState],
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

    async def list_blocks_for_identity(
        self,
        identity_id: str,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListBlocksForIdentityRequestOrder] = None,
        order_by: typing.Optional[ListBlocksForIdentityRequestOrderBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[BlockResponse]]:
        """
        Get all blocks associated with the specified identity.

        Parameters
        ----------
        identity_id : str
            The ID of the identity in the format 'identity-<uuid4>'

        before : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order

        after : typing.Optional[str]
            Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order

        limit : typing.Optional[int]
            Maximum number of blocks to return

        order : typing.Optional[ListBlocksForIdentityRequestOrder]
            Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first

        order_by : typing.Optional[ListBlocksForIdentityRequestOrderBy]
            Field to sort by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[BlockResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{encode_path_param(identity_id)}/blocks",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[BlockResponse],
                    parse_obj_as(
                        type_=typing.List[BlockResponse],
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
