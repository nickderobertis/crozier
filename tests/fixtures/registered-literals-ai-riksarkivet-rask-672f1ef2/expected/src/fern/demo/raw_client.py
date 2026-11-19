

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.demo_datasets import DemoDatasets
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


class RawDemoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def demo_datasets(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[DemoDatasets]:
        """
        The medallion datasets as they currently exist on S3 — schema per Lance version + rows.

        GOVERNED (audit: this endpoint reads real medallion schemas/row-counts + gold's lineage JSONB from S3
        with the SERVICE root credentials, so it must not disclose a dataset the caller cannot see). Every
        other lineage read gates on ``can_get_metadata``; this does the same via the shared batch filter —
        ONE ``batch_check`` over the layout, not a per-dataset round-trip loop (F-LIN-13). The ladder is
        unchanged: 401 unauthenticated / 503 FGA unwired propagate; a denied dataset is dropped, not fatal.
        FGA off → pass-through (the dev demo).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DemoDatasets]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "demo/datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DemoDatasets,
                    parse_obj_as(
                        type_=DemoDatasets,
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


class AsyncRawDemoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def demo_datasets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DemoDatasets]:
        """
        The medallion datasets as they currently exist on S3 — schema per Lance version + rows.

        GOVERNED (audit: this endpoint reads real medallion schemas/row-counts + gold's lineage JSONB from S3
        with the SERVICE root credentials, so it must not disclose a dataset the caller cannot see). Every
        other lineage read gates on ``can_get_metadata``; this does the same via the shared batch filter —
        ONE ``batch_check`` over the layout, not a per-dataset round-trip loop (F-LIN-13). The ladder is
        unchanged: 401 unauthenticated / 503 FGA unwired propagate; a denied dataset is dropped, not fatal.
        FGA off → pass-through (the dev demo).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DemoDatasets]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "demo/datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DemoDatasets,
                    parse_obj_as(
                        type_=DemoDatasets,
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
