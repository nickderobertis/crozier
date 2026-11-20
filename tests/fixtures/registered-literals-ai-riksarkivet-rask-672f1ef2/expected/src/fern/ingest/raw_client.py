

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIngestClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ingest_event(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Optional[str]]]:
        """
        Ingest one OpenLineage event — a ``RunEvent``, or a ``DatasetEvent`` for a change no job performed.

        PARSED HERE RATHER THAN BY THE SIGNATURE, so this door and the bus door share ONE discriminator
        (`models.parse_event`). Declaring the body as `RunEvent` is what made a static event 422 before
        any handler ran: [[LIN-004]] moved catalog DDL onto `DatasetEvent` and taught only the bus. The
        catalog's HTTP emitter is best-effort, so every create it sent lost its provenance in silence —
        measured 2026-09-24, three creates, `{"events":[]}` in the durable feed, and a governance
        assertion reading `expected lineage creator=..., got None`.

        A body that is neither shape raises `RequestValidationError`, which `install_problem_handlers`
        renders exactly as FastAPI's own 422 — the wire answer for a malformed payload is unchanged.

        This is the OpenLineage HTTP-transport default path, so any OpenLineage producer
        (our emitter, Airflow, Spark, dbt, …) configured with ``OPENLINEAGE_URL`` pointed
        here ingests with no glue — the lightweight-Marquez contract.

        When OIDC is enabled the ``CurrentToken`` dependency requires a verified bearer token
        (401 otherwise), :func:`~lineage.api.fga_deps.enforce_author` binds the run author to that
        token's subject (no self-asserted identity), and :func:`~lineage.api.fga_deps.enforce_output_authz`
        requires ``can_write_data`` on every output dataset (a producer can't record provenance for a table
        it can't write). Both are no-ops when auth is off.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Optional[str]]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/lineage",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Optional[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[str]],
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


class AsyncRawIngestClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ingest_event(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Optional[str]]]:
        """
        Ingest one OpenLineage event — a ``RunEvent``, or a ``DatasetEvent`` for a change no job performed.

        PARSED HERE RATHER THAN BY THE SIGNATURE, so this door and the bus door share ONE discriminator
        (`models.parse_event`). Declaring the body as `RunEvent` is what made a static event 422 before
        any handler ran: [[LIN-004]] moved catalog DDL onto `DatasetEvent` and taught only the bus. The
        catalog's HTTP emitter is best-effort, so every create it sent lost its provenance in silence —
        measured 2026-09-24, three creates, `{"events":[]}` in the durable feed, and a governance
        assertion reading `expected lineage creator=..., got None`.

        A body that is neither shape raises `RequestValidationError`, which `install_problem_handlers`
        renders exactly as FastAPI's own 422 — the wire answer for a malformed payload is unchanged.

        This is the OpenLineage HTTP-transport default path, so any OpenLineage producer
        (our emitter, Airflow, Spark, dbt, …) configured with ``OPENLINEAGE_URL`` pointed
        here ingests with no glue — the lightweight-Marquez contract.

        When OIDC is enabled the ``CurrentToken`` dependency requires a verified bearer token
        (401 otherwise), :func:`~lineage.api.fga_deps.enforce_author` binds the run author to that
        token's subject (no self-asserted identity), and :func:`~lineage.api.fga_deps.enforce_output_authz`
        requires ``can_write_data`` on every output dataset (a producer can't record provenance for a table
        it can't write). Both are no-ops when auth is off.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Optional[str]]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/lineage",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Optional[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Optional[str]],
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
