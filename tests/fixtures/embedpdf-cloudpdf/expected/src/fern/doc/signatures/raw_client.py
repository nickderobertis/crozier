

import typing
from json.decoder import JSONDecodeError

from ... import core
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.http_response import AsyncHttpResponse, HttpResponse
from ...core.jsonable_encoder import encode_path_param
from ...core.parse_error import ParsingError
from ...core.pydantic_utilities import parse_obj_as
from ...core.request_options import RequestOptions
from ...core.serialization import convert_and_respect_annotation_metadata
from ...errors.bad_request_error import BadRequestError
from ...errors.conflict_error import ConflictError
from ...errors.not_found_error import NotFoundError
from ...types.doc_signatures_abort200response import DocSignaturesAbort200Response
from ...types.doc_signatures_analysis200response import DocSignaturesAnalysis200Response
from ...types.doc_signatures_complete200response import DocSignaturesComplete200Response
from ...types.doc_signatures_list200response import DocSignaturesList200Response
from ...types.doc_signatures_prepare200response import DocSignaturesPrepare200Response
from .types.analysis_signatures_request_level import AnalysisSignaturesRequestLevel
from .types.doc_signatures_complete_request_expected_version import DocSignaturesCompleteRequestExpectedVersion
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSignaturesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocSignaturesList200Response]:
        """
        Describes the bytes the layer is over: the base version's signatures plus the layer's own edits as the last revision. Signed bytes (contents, digests, revision prefixes) are served per base version under /versions.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocSignaturesList200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesList200Response,
                    parse_obj_as(
                        type_=DocSignaturesList200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def abort(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocSignaturesAbort200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocSignaturesAbort200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/{encode_path_param(signing_id)}",
            method="DELETE",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesAbort200Response,
                    parse_obj_as(
                        type_=DocSignaturesAbort200Response,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def complete(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        cms: str,
        expected_version: DocSignaturesCompleteRequestExpectedVersion,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocSignaturesComplete200Response]:
        """
        `cms` is the detached CMS over the prepared digest, base64. `expectedVersion` must be what prepare returned. Idempotent by signing id: the same CMS again answers `already-completed`. Every layer of the document then sits over the new version; refetch the manifest after a completion.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        cms : str

        expected_version : DocSignaturesCompleteRequestExpectedVersion

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocSignaturesComplete200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/{encode_path_param(signing_id)}/complete",
            method="POST",
            json={
                "cms": cms,
                "expectedVersion": convert_and_respect_annotation_metadata(
                    object_=expected_version, annotation=DocSignaturesCompleteRequestExpectedVersion, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesComplete200Response,
                    parse_obj_as(
                        type_=DocSignaturesComplete200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def analysis(
        self,
        doc_id: str,
        layer_name: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisSignaturesRequestLevel] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocSignaturesAnalysis200Response]:
        """
        Exactly one of `since.signature=<index>` or `since.revision=<index>`; the layer's pending edits are the end. `level=fill|annotate|lta|none` evaluates exploratorily and never becomes a verdict. For history between two base revisions use the version analysis.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisSignaturesRequestLevel]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocSignaturesAnalysis200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/analysis",
            method="GET",
            params={
                "since.signature": since_signature,
                "since.revision": since_revision,
                "level": level,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesAnalysis200Response,
                    parse_obj_as(
                        type_=DocSignaturesAnalysis200Response,
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

    def prepare(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DocSignaturesPrepare200Response]:
        """
        The multipart envelope: a JSON `body` part (field, subFilter, digest, contentsSize, signer, certify, lock, appearance) and an optional `resource:<key>` PDF part the body's `appearance.resource` names. A certification (`certify.permission`) additionally requires `doc.sign.certify`. The layer is read-only until the signing completes, is aborted, or expires (15 minutes). A layer behind the document head cannot sign (StaleBase).

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocSignaturesPrepare200Response]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/prepare",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesPrepare200Response,
                    parse_obj_as(
                        type_=DocSignaturesPrepare200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncRawSignaturesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocSignaturesList200Response]:
        """
        Describes the bytes the layer is over: the base version's signatures plus the layer's own edits as the last revision. Signed bytes (contents, digests, revision prefixes) are served per base version under /versions.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocSignaturesList200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures",
            method="GET",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesList200Response,
                    parse_obj_as(
                        type_=DocSignaturesList200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def abort(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocSignaturesAbort200Response]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocSignaturesAbort200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/{encode_path_param(signing_id)}",
            method="DELETE",
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesAbort200Response,
                    parse_obj_as(
                        type_=DocSignaturesAbort200Response,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def complete(
        self,
        doc_id: str,
        layer_name: str,
        signing_id: str,
        *,
        cms: str,
        expected_version: DocSignaturesCompleteRequestExpectedVersion,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocSignaturesComplete200Response]:
        """
        `cms` is the detached CMS over the prepared digest, base64. `expectedVersion` must be what prepare returned. Idempotent by signing id: the same CMS again answers `already-completed`. Every layer of the document then sits over the new version; refetch the manifest after a completion.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        signing_id : str

        cms : str

        expected_version : DocSignaturesCompleteRequestExpectedVersion

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocSignaturesComplete200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/{encode_path_param(signing_id)}/complete",
            method="POST",
            json={
                "cms": cms,
                "expectedVersion": convert_and_respect_annotation_metadata(
                    object_=expected_version, annotation=DocSignaturesCompleteRequestExpectedVersion, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesComplete200Response,
                    parse_obj_as(
                        type_=DocSignaturesComplete200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def analysis(
        self,
        doc_id: str,
        layer_name: str,
        *,
        since_signature: typing.Optional[int] = None,
        since_revision: typing.Optional[int] = None,
        level: typing.Optional[AnalysisSignaturesRequestLevel] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocSignaturesAnalysis200Response]:
        """
        Exactly one of `since.signature=<index>` or `since.revision=<index>`; the layer's pending edits are the end. `level=fill|annotate|lta|none` evaluates exploratorily and never becomes a verdict. For history between two base revisions use the version analysis.

        Parameters
        ----------
        doc_id : str

        layer_name : str

        since_signature : typing.Optional[int]

        since_revision : typing.Optional[int]

        level : typing.Optional[AnalysisSignaturesRequestLevel]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocSignaturesAnalysis200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/analysis",
            method="GET",
            params={
                "since.signature": since_signature,
                "since.revision": since_revision,
                "level": level,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesAnalysis200Response,
                    parse_obj_as(
                        type_=DocSignaturesAnalysis200Response,
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

    async def prepare(
        self,
        doc_id: str,
        layer_name: str,
        *,
        file: core.File,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DocSignaturesPrepare200Response]:
        """
        The multipart envelope: a JSON `body` part (field, subFilter, digest, contentsSize, signer, certify, lock, appearance) and an optional `resource:<key>` PDF part the body's `appearance.resource` names. A certification (`certify.permission`) additionally requires `doc.sign.certify`. The layer is read-only until the signing completes, is aborted, or expires (15 minutes). A layer behind the document head cannot sign (StaleBase).

        Parameters
        ----------
        doc_id : str

        layer_name : str

        file : core.File
            See core.File for more documentation

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocSignaturesPrepare200Response]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/docs/{encode_path_param(doc_id)}/layers/{encode_path_param(layer_name)}/signatures/prepare",
            method="POST",
            data={},
            files={
                "file": file,
            },
            headers={
                "X-Document-Password": str(document_password) if document_password is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocSignaturesPrepare200Response,
                    parse_obj_as(
                        type_=DocSignaturesPrepare200Response,
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
            if _response.status_code == 409:
                raise ConflictError(
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
