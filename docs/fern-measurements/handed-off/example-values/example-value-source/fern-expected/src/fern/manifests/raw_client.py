

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.import_manifest_request_task import ImportManifestRequestTask
from .types.import_manifest_response import ImportManifestResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManifestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def import_manifest(
        self,
        *,
        sheet: core.File,
        task: ImportManifestRequestTask,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImportManifestResponse]:
        """
        A multipart object part whose property declares an example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        task : ImportManifestRequestTask

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImportManifestResponse]
            Imported
        """
        _response = self._client_wrapper.httpx_client.request(
            "manifests/import",
            method="POST",
            data={
                "task": json.dumps(jsonable_encoder(task)),
            },
            files={
                "sheet": sheet,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportManifestResponse,
                    parse_obj_as(
                        type_=ImportManifestResponse,
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


class AsyncRawManifestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def import_manifest(
        self,
        *,
        sheet: core.File,
        task: ImportManifestRequestTask,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImportManifestResponse]:
        """
        A multipart object part whose property declares an example.

        Parameters
        ----------
        sheet : core.File
            See core.File for more documentation

        task : ImportManifestRequestTask

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImportManifestResponse]
            Imported
        """
        _response = await self._client_wrapper.httpx_client.request(
            "manifests/import",
            method="POST",
            data={
                "task": json.dumps(jsonable_encoder(task)),
            },
            files={
                "sheet": sheet,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImportManifestResponse,
                    parse_obj_as(
                        type_=ImportManifestResponse,
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
