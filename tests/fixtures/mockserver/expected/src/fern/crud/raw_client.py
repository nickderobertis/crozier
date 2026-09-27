

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from .types.crud_expectations_definition_id_strategy import CrudExpectationsDefinitionIdStrategy
from .types.put_mockserver_crud_response import PutMockserverCrudResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrudClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_a_generated_crud_data_store(
        self,
        *,
        base_path: str,
        id_field: typing.Optional[str] = OMIT,
        id_strategy: typing.Optional[CrudExpectationsDefinitionIdStrategy] = OMIT,
        initial_data: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutMockserverCrudResponse]:
        """
        Registers a REST resource backed by an in-memory data store that automatically handles list, read, create, update and delete operations under the supplied base path.

        Parameters
        ----------
        base_path : str
            base path the CRUD resource is served under (e.g. /api/users)

        id_field : typing.Optional[str]
            name of the field used as the resource identifier

        id_strategy : typing.Optional[CrudExpectationsDefinitionIdStrategy]
            strategy used to generate identifiers for newly created resources

        initial_data : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            initial records to seed the data store with

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutMockserverCrudResponse]
            CRUD resource registered
        """
        _response = self._client_wrapper.httpx_client.request(
            "mockserver/crud",
            method="PUT",
            json={
                "basePath": base_path,
                "idField": id_field,
                "idStrategy": id_strategy,
                "initialData": initial_data,
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
                    PutMockserverCrudResponse,
                    parse_obj_as(
                        type_=PutMockserverCrudResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCrudClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_a_generated_crud_data_store(
        self,
        *,
        base_path: str,
        id_field: typing.Optional[str] = OMIT,
        id_strategy: typing.Optional[CrudExpectationsDefinitionIdStrategy] = OMIT,
        initial_data: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutMockserverCrudResponse]:
        """
        Registers a REST resource backed by an in-memory data store that automatically handles list, read, create, update and delete operations under the supplied base path.

        Parameters
        ----------
        base_path : str
            base path the CRUD resource is served under (e.g. /api/users)

        id_field : typing.Optional[str]
            name of the field used as the resource identifier

        id_strategy : typing.Optional[CrudExpectationsDefinitionIdStrategy]
            strategy used to generate identifiers for newly created resources

        initial_data : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            initial records to seed the data store with

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutMockserverCrudResponse]
            CRUD resource registered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mockserver/crud",
            method="PUT",
            json={
                "basePath": base_path,
                "idField": id_field,
                "idStrategy": id_strategy,
                "initialData": initial_data,
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
                    PutMockserverCrudResponse,
                    parse_obj_as(
                        type_=PutMockserverCrudResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
