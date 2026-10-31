

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
from ..types.artefact_build_environment_review_decision import ArtefactBuildEnvironmentReviewDecision
from ..types.artefact_build_environment_review_response import ArtefactBuildEnvironmentReviewResponse
from ..types.artefact_build_response import ArtefactBuildResponse
from ..types.artefact_history_response import ArtefactHistoryResponse
from ..types.artefact_response import ArtefactResponse
from ..types.artefact_search_response import ArtefactSearchResponse
from ..types.artefact_status import ArtefactStatus
from ..types.artefact_version_response import ArtefactVersionResponse
from ..types.environment_review_patch import EnvironmentReviewPatch
from ..types.expected_environment_input import ExpectedEnvironmentInput
from ..types.family_name import FamilyName
from ..types.http_validation_error import HttpValidationError
from ..types.stage_name import StageName
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawArtefactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_artefacts(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtefactResponse]]:
        """
        Get latest artefacts optionally by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtefactResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/artefacts",
            method="GET",
            params={
                "family": family,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactResponse],
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

    def search_artefacts(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtefactSearchResponse]:
        """
        Search for artefacts by name with pagination support.

        Returns a list of distinct artefact names that match the search query.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for artefact names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtefactSearchResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/artefacts/search",
            method="GET",
            params={
                "q": q,
                "families": families,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactSearchResponse,
                    parse_obj_as(
                        type_=ArtefactSearchResponse,
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

    def get_artefact_history(
        self,
        *,
        name: str,
        family: FamilyName,
        track: typing.Optional[str] = None,
        stage: typing.Optional[StageName] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtefactHistoryResponse]:
        """
        Get the versioning history of an artefact for a given name, family, and track,
        optionally filtered by stage, with pagination support.

        Returns a list of artefact versions along with their creation date.

        Parameters
        ----------
        name : str
            Artefact name

        family : FamilyName
            Artefact family

        track : typing.Optional[str]
            Artefact track

        stage : typing.Optional[StageName]
            Filter by stage

        limit : typing.Optional[int]
            Maximum number of results (defaults to 10 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtefactHistoryResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/artefacts/history",
            method="GET",
            params={
                "name": name,
                "family": family,
                "track": track,
                "stage": stage,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactHistoryResponse,
                    parse_obj_as(
                        type_=ArtefactHistoryResponse,
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

    def get_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ArtefactResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtefactResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactResponse,
                    parse_obj_as(
                        type_=ArtefactResponse,
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

    def delete_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="DELETE",
            request_options=request_options,
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

    def patch_artefact(
        self,
        artefact_id: int,
        *,
        status: typing.Optional[ArtefactStatus] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        stage: typing.Optional[StageName] = OMIT,
        comment: typing.Optional[str] = OMIT,
        jira_issue: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        expected_environments: typing.Optional[typing.Sequence[ExpectedEnvironmentInput]] = OMIT,
        assignee_id: typing.Optional[int] = OMIT,
        assignee_email: typing.Optional[str] = OMIT,
        reviewer_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        reviewer_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtefactResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        status : typing.Optional[ArtefactStatus]

        archived : typing.Optional[bool]

        stage : typing.Optional[StageName]

        comment : typing.Optional[str]

        jira_issue : typing.Optional[str]

        attributes : typing.Optional[typing.Dict[str, typing.Any]]

        expected_environments : typing.Optional[typing.Sequence[ExpectedEnvironmentInput]]
            Expected environments, replacing the current set. Each environment is identified by name and architecture.

        assignee_id : typing.Optional[int]
            Legacy field. Mapped to reviewer_ids as a single-element list when reviewer_ids/reviewer_emails are not provided.

        assignee_email : typing.Optional[str]
            Legacy field. Mapped to reviewer_emails as a single-element list when reviewer_ids/reviewer_emails are not provided.

        reviewer_ids : typing.Optional[typing.Sequence[int]]
            Reviewer user IDs. Preferred over legacy assignee_id/assignee_email for setting assignees.

        reviewer_emails : typing.Optional[typing.Sequence[str]]
            Reviewer emails. Preferred over legacy assignee_id/assignee_email for setting assignees.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtefactResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="PATCH",
            json={
                "status": status,
                "archived": archived,
                "stage": stage,
                "comment": comment,
                "jira_issue": jira_issue,
                "attributes": attributes,
                "expected_environments": convert_and_respect_annotation_metadata(
                    object_=expected_environments,
                    annotation=typing.Optional[typing.Sequence[ExpectedEnvironmentInput]],
                    direction="write",
                ),
                "assignee_id": assignee_id,
                "assignee_email": assignee_email,
                "reviewer_ids": reviewer_ids,
                "reviewer_emails": reviewer_emails,
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
                    ArtefactResponse,
                    parse_obj_as(
                        type_=ArtefactResponse,
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

    def get_artefact_versions(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtefactVersionResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtefactVersionResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactVersionResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactVersionResponse],
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

    def get_environment_reviews(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildEnvironmentReviewResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildEnvironmentReviewResponse],
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

    def bulk_update_environment_reviews(
        self,
        artefact_id: int,
        *,
        request: typing.Sequence[EnvironmentReviewPatch],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request : typing.Sequence[EnvironmentReviewPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[EnvironmentReviewPatch], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildEnvironmentReviewResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildEnvironmentReviewResponse],
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

    def update_environment_review(
        self,
        artefact_id: int,
        review_id: int,
        *,
        id: typing.Optional[int] = OMIT,
        review_decision: typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]] = OMIT,
        review_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        review_id : int

        id : typing.Optional[int]

        review_decision : typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]]

        review_comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArtefactBuildEnvironmentReviewResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews/{encode_path_param(review_id)}",
            method="PATCH",
            json={
                "id": id,
                "review_decision": review_decision,
                "review_comment": review_comment,
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
                    ArtefactBuildEnvironmentReviewResponse,
                    parse_obj_as(
                        type_=ArtefactBuildEnvironmentReviewResponse,
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

    def get_artefact_builds(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtefactBuildResponse]]:
        """
        Get latest artefact builds of an artefact together with their test executions

        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ArtefactBuildResponse]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/builds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildResponse],
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


class AsyncRawArtefactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_artefacts(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtefactResponse]]:
        """
        Get latest artefacts optionally by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtefactResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/artefacts",
            method="GET",
            params={
                "family": family,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactResponse],
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

    async def search_artefacts(
        self,
        *,
        q: typing.Optional[str] = None,
        families: typing.Optional[typing.Sequence[FamilyName]] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtefactSearchResponse]:
        """
        Search for artefacts by name with pagination support.

        Returns a list of distinct artefact names that match the search query.

        Parameters
        ----------
        q : typing.Optional[str]
            Search term for artefact names

        families : typing.Optional[typing.Sequence[FamilyName]]
            Filter by artefact families

        limit : typing.Optional[int]
            Maximum number of results (defaults to 50 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtefactSearchResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/artefacts/search",
            method="GET",
            params={
                "q": q,
                "families": families,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactSearchResponse,
                    parse_obj_as(
                        type_=ArtefactSearchResponse,
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

    async def get_artefact_history(
        self,
        *,
        name: str,
        family: FamilyName,
        track: typing.Optional[str] = None,
        stage: typing.Optional[StageName] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtefactHistoryResponse]:
        """
        Get the versioning history of an artefact for a given name, family, and track,
        optionally filtered by stage, with pagination support.

        Returns a list of artefact versions along with their creation date.

        Parameters
        ----------
        name : str
            Artefact name

        family : FamilyName
            Artefact family

        track : typing.Optional[str]
            Artefact track

        stage : typing.Optional[StageName]
            Filter by stage

        limit : typing.Optional[int]
            Maximum number of results (defaults to 10 if not specified)

        offset : typing.Optional[int]
            Number of results to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtefactHistoryResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/artefacts/history",
            method="GET",
            params={
                "name": name,
                "family": family,
                "track": track,
                "stage": stage,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactHistoryResponse,
                    parse_obj_as(
                        type_=ArtefactHistoryResponse,
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

    async def get_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArtefactResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtefactResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtefactResponse,
                    parse_obj_as(
                        type_=ArtefactResponse,
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

    async def delete_artefact(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def patch_artefact(
        self,
        artefact_id: int,
        *,
        status: typing.Optional[ArtefactStatus] = OMIT,
        archived: typing.Optional[bool] = OMIT,
        stage: typing.Optional[StageName] = OMIT,
        comment: typing.Optional[str] = OMIT,
        jira_issue: typing.Optional[str] = OMIT,
        attributes: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        expected_environments: typing.Optional[typing.Sequence[ExpectedEnvironmentInput]] = OMIT,
        assignee_id: typing.Optional[int] = OMIT,
        assignee_email: typing.Optional[str] = OMIT,
        reviewer_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        reviewer_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtefactResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        status : typing.Optional[ArtefactStatus]

        archived : typing.Optional[bool]

        stage : typing.Optional[StageName]

        comment : typing.Optional[str]

        jira_issue : typing.Optional[str]

        attributes : typing.Optional[typing.Dict[str, typing.Any]]

        expected_environments : typing.Optional[typing.Sequence[ExpectedEnvironmentInput]]
            Expected environments, replacing the current set. Each environment is identified by name and architecture.

        assignee_id : typing.Optional[int]
            Legacy field. Mapped to reviewer_ids as a single-element list when reviewer_ids/reviewer_emails are not provided.

        assignee_email : typing.Optional[str]
            Legacy field. Mapped to reviewer_emails as a single-element list when reviewer_ids/reviewer_emails are not provided.

        reviewer_ids : typing.Optional[typing.Sequence[int]]
            Reviewer user IDs. Preferred over legacy assignee_id/assignee_email for setting assignees.

        reviewer_emails : typing.Optional[typing.Sequence[str]]
            Reviewer emails. Preferred over legacy assignee_id/assignee_email for setting assignees.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtefactResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}",
            method="PATCH",
            json={
                "status": status,
                "archived": archived,
                "stage": stage,
                "comment": comment,
                "jira_issue": jira_issue,
                "attributes": attributes,
                "expected_environments": convert_and_respect_annotation_metadata(
                    object_=expected_environments,
                    annotation=typing.Optional[typing.Sequence[ExpectedEnvironmentInput]],
                    direction="write",
                ),
                "assignee_id": assignee_id,
                "assignee_email": assignee_email,
                "reviewer_ids": reviewer_ids,
                "reviewer_emails": reviewer_emails,
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
                    ArtefactResponse,
                    parse_obj_as(
                        type_=ArtefactResponse,
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

    async def get_artefact_versions(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtefactVersionResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtefactVersionResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/versions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactVersionResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactVersionResponse],
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

    async def get_environment_reviews(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildEnvironmentReviewResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildEnvironmentReviewResponse],
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

    async def bulk_update_environment_reviews(
        self,
        artefact_id: int,
        *,
        request: typing.Sequence[EnvironmentReviewPatch],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]:
        """
        Parameters
        ----------
        artefact_id : int

        request : typing.Sequence[EnvironmentReviewPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtefactBuildEnvironmentReviewResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[EnvironmentReviewPatch], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildEnvironmentReviewResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildEnvironmentReviewResponse],
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

    async def update_environment_review(
        self,
        artefact_id: int,
        review_id: int,
        *,
        id: typing.Optional[int] = OMIT,
        review_decision: typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]] = OMIT,
        review_comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtefactBuildEnvironmentReviewResponse]:
        """
        Parameters
        ----------
        artefact_id : int

        review_id : int

        id : typing.Optional[int]

        review_decision : typing.Optional[typing.Sequence[ArtefactBuildEnvironmentReviewDecision]]

        review_comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArtefactBuildEnvironmentReviewResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/environment-reviews/{encode_path_param(review_id)}",
            method="PATCH",
            json={
                "id": id,
                "review_decision": review_decision,
                "review_comment": review_comment,
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
                    ArtefactBuildEnvironmentReviewResponse,
                    parse_obj_as(
                        type_=ArtefactBuildEnvironmentReviewResponse,
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

    async def get_artefact_builds(
        self, artefact_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtefactBuildResponse]]:
        """
        Get latest artefact builds of an artefact together with their test executions

        Parameters
        ----------
        artefact_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ArtefactBuildResponse]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/artefacts/{encode_path_param(artefact_id)}/builds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtefactBuildResponse],
                    parse_obj_as(
                        type_=typing.List[ArtefactBuildResponse],
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
