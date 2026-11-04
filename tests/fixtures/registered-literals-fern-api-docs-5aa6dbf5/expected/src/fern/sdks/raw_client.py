

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.analyze_commit_diff_response import AnalyzeCommitDiffResponse
from ..types.http_validation_error import HttpValidationError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSdksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def analyze_commit_diff(
        self,
        *,
        diff: str,
        language: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[str] = OMIT,
        prior_changelog: typing.Optional[str] = OMIT,
        spec_commit_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnalyzeCommitDiffResponse]:
        """
        Analyzes a git diff and generates an AI-powered commit message with version bump recommendation.

        Parameters
        ----------
        diff : str
            The git diff to analyze for generating a commit message

        language : typing.Optional[str]
            The SDK programming language, e.g. 'typescript', 'python', 'java'. When provided, enables language-specific breaking change rules and behavioral analysis.

        previous_version : typing.Optional[str]
            The current published version before this change, e.g. '1.2.3'. Provided for context only — not included in the commit message.

        prior_changelog : typing.Optional[str]
            The last 3 changelog entries for this SDK. Used to match existing commit message style. Empty string or null if none.

        spec_commit_message : typing.Optional[str]
            The commit message from the API spec repository that triggered this SDK generation. Used as a hint for the intent of the change. Empty string or null if unavailable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnalyzeCommitDiffResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "sdks/analyze-commit-diff",
            method="POST",
            json={
                "diff": diff,
                "language": language,
                "previous_version": previous_version,
                "prior_changelog": prior_changelog,
                "spec_commit_message": spec_commit_message,
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
                    AnalyzeCommitDiffResponse,
                    parse_obj_as(
                        type_=AnalyzeCommitDiffResponse,
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


class AsyncRawSdksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def analyze_commit_diff(
        self,
        *,
        diff: str,
        language: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[str] = OMIT,
        prior_changelog: typing.Optional[str] = OMIT,
        spec_commit_message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnalyzeCommitDiffResponse]:
        """
        Analyzes a git diff and generates an AI-powered commit message with version bump recommendation.

        Parameters
        ----------
        diff : str
            The git diff to analyze for generating a commit message

        language : typing.Optional[str]
            The SDK programming language, e.g. 'typescript', 'python', 'java'. When provided, enables language-specific breaking change rules and behavioral analysis.

        previous_version : typing.Optional[str]
            The current published version before this change, e.g. '1.2.3'. Provided for context only — not included in the commit message.

        prior_changelog : typing.Optional[str]
            The last 3 changelog entries for this SDK. Used to match existing commit message style. Empty string or null if none.

        spec_commit_message : typing.Optional[str]
            The commit message from the API spec repository that triggered this SDK generation. Used as a hint for the intent of the change. Empty string or null if unavailable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnalyzeCommitDiffResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sdks/analyze-commit-diff",
            method="POST",
            json={
                "diff": diff,
                "language": language,
                "previous_version": previous_version,
                "prior_changelog": prior_changelog,
                "spec_commit_message": spec_commit_message,
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
                    AnalyzeCommitDiffResponse,
                    parse_obj_as(
                        type_=AnalyzeCommitDiffResponse,
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
