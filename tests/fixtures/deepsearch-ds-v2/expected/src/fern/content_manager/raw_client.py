

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
from ..types.api_server_fastapi_server_public_models_data_indices_upload_models_identifier import (
    ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier,
)
from ..types.document_description import DocumentDescription
from ..types.document_statistics import DocumentStatistics
from ..types.http_validation_error import HttpValidationError
from ..types.project_agents import ProjectAgents
from ..types.project_document import ProjectDocument
from ..types.project_document_url import ProjectDocumentUrl
from ..types.project_documents import ProjectDocuments
from ..types.response_document_artifacts import ResponseDocumentArtifacts
from ..types.response_grouped_documents import ResponseGroupedDocuments
from ..types.response_upload_jobs import ResponseUploadJobs
from ..types.status_filter import StatusFilter
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContentManagerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_agents(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectAgents]:
        """
        Get project agents.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectAgents]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/documents/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectAgents,
                    parse_obj_as(
                        type_=ProjectAgents,
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

    def get_project_documents_by_transaction(
        self,
        proj_key: str,
        index_key: str,
        transaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocuments]:
        """
        Get project documents by transaction ID.

        Parameters
        ----------
        proj_key : str

        index_key : str

        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/transactions/{encode_path_param(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    def get_all_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocuments]:
        """
        Get all project documents

        Parameters
        ----------
        proj_key : str

        index_key : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    def get_project_conversion_statistics(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DocumentStatistics]:
        """
        Get project conversion statistics.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DocumentStatistics]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentStatistics,
                    parse_obj_as(
                        type_=DocumentStatistics,
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

    def get_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocuments]:
        """
        Get project documents, can be filter by status.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/agent/{encode_path_param(agent_name)}",
            method="GET",
            params={
                "status": status,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    def get_project_data_index_grouped_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseGroupedDocuments]:
        """
        Get project documents grouped by upload.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseGroupedDocuments]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/agent/{encode_path_param(agent_name)}/grouped",
            method="GET",
            params={
                "status": status,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseGroupedDocuments,
                    parse_obj_as(
                        type_=ResponseGroupedDocuments,
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

    def get_project_index_upload_jobs(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponseUploadJobs]:
        """
        Get project upload jobs.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseUploadJobs]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/upload_jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseUploadJobs,
                    parse_obj_as(
                        type_=ResponseUploadJobs,
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

    def get_project_data_index_document_markdown(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocumentUrl]:
        """
        Get project document Markdown.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocumentUrl]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/Markdown",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocumentUrl,
                    parse_obj_as(
                        type_=ProjectDocumentUrl,
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

    def get_project_data_index_pdf_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocumentUrl]:
        """
        Get project PDF document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocumentUrl]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/PDF",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocumentUrl,
                    parse_obj_as(
                        type_=ProjectDocumentUrl,
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

    def get_project_data_index_json_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get project JSON document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/JSON",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def get_project_data_index_document_artifacts(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseDocumentArtifacts]:
        """
        Get project document artifacts.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseDocumentArtifacts]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/artifacts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseDocumentArtifacts,
                    parse_obj_as(
                        type_=ResponseDocumentArtifacts,
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

    def get_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDocument]:
        """
        Get project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDocument]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocument,
                    parse_obj_as(
                        type_=ProjectDocument,
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

    def add_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        filename: typing.Optional[str] = OMIT,
        description: typing.Optional[DocumentDescription] = OMIT,
        identifiers: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Insert project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        filename : typing.Optional[str]

        description : typing.Optional[DocumentDescription]

        identifiers : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/metadata",
            method="POST",
            json={
                "filename": filename,
                "description": convert_and_respect_annotation_metadata(
                    object_=description, annotation=typing.Optional[DocumentDescription], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
                    ],
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
                return HttpResponse(response=_response, data=None)
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

    def get_project_data_index_document_events(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        agent_name: typing.Optional[str] = None,
        status: typing.Optional[StatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get events of a project document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        agent_name : typing.Optional[str]

        status : typing.Optional[StatusFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/doc_events",
            method="GET",
            params={
                "agent_name": agent_name,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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


class AsyncRawContentManagerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_agents(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectAgents]:
        """
        Get project agents.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectAgents]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/documents/agents",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectAgents,
                    parse_obj_as(
                        type_=ProjectAgents,
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

    async def get_project_documents_by_transaction(
        self,
        proj_key: str,
        index_key: str,
        transaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocuments]:
        """
        Get project documents by transaction ID.

        Parameters
        ----------
        proj_key : str

        index_key : str

        transaction_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/transactions/{encode_path_param(transaction_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    async def get_all_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocuments]:
        """
        Get all project documents

        Parameters
        ----------
        proj_key : str

        index_key : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/",
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    async def get_project_conversion_statistics(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DocumentStatistics]:
        """
        Get project conversion statistics.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DocumentStatistics]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/statistics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DocumentStatistics,
                    parse_obj_as(
                        type_=DocumentStatistics,
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

    async def get_project_data_index_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocuments]:
        """
        Get project documents, can be filter by status.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocuments]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/agent/{encode_path_param(agent_name)}",
            method="GET",
            params={
                "status": status,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocuments,
                    parse_obj_as(
                        type_=ProjectDocuments,
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

    async def get_project_data_index_grouped_documents(
        self,
        proj_key: str,
        index_key: str,
        agent_name: str,
        *,
        status: typing.Optional[StatusFilter] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseGroupedDocuments]:
        """
        Get project documents grouped by upload.

        Parameters
        ----------
        proj_key : str

        index_key : str

        agent_name : str

        status : typing.Optional[StatusFilter]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseGroupedDocuments]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/agent/{encode_path_param(agent_name)}/grouped",
            method="GET",
            params={
                "status": status,
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseGroupedDocuments,
                    parse_obj_as(
                        type_=ResponseGroupedDocuments,
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

    async def get_project_index_upload_jobs(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponseUploadJobs]:
        """
        Get project upload jobs.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseUploadJobs]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/upload_jobs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseUploadJobs,
                    parse_obj_as(
                        type_=ResponseUploadJobs,
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

    async def get_project_data_index_document_markdown(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocumentUrl]:
        """
        Get project document Markdown.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocumentUrl]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/Markdown",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocumentUrl,
                    parse_obj_as(
                        type_=ProjectDocumentUrl,
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

    async def get_project_data_index_pdf_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocumentUrl]:
        """
        Get project PDF document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocumentUrl]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/PDF",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocumentUrl,
                    parse_obj_as(
                        type_=ProjectDocumentUrl,
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

    async def get_project_data_index_json_document(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get project JSON document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/JSON",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def get_project_data_index_document_artifacts(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseDocumentArtifacts]:
        """
        Get project document artifacts.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseDocumentArtifacts]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/artifacts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseDocumentArtifacts,
                    parse_obj_as(
                        type_=ResponseDocumentArtifacts,
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

    async def get_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDocument]:
        """
        Get project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDocument]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDocument,
                    parse_obj_as(
                        type_=ProjectDocument,
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

    async def add_project_data_index_document_metadata(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        filename: typing.Optional[str] = OMIT,
        description: typing.Optional[DocumentDescription] = OMIT,
        identifiers: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Insert project document metadata.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        filename : typing.Optional[str]

        description : typing.Optional[DocumentDescription]

        identifiers : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/metadata",
            method="POST",
            json={
                "filename": filename,
                "description": convert_and_respect_annotation_metadata(
                    object_=description, annotation=typing.Optional[DocumentDescription], direction="write"
                ),
                "identifiers": convert_and_respect_annotation_metadata(
                    object_=identifiers,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsIdentifier]
                    ],
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
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_project_data_index_document_events(
        self,
        proj_key: str,
        index_key: str,
        document_hash: str,
        *,
        agent_name: typing.Optional[str] = None,
        status: typing.Optional[StatusFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Get events of a project document.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hash : str

        agent_name : typing.Optional[str]

        status : typing.Optional[StatusFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(document_hash)}/doc_events",
            method="GET",
            params={
                "agent_name": agent_name,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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
