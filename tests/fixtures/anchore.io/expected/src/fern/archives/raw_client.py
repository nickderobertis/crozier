

import datetime as dt
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
from ..errors.internal_server_error import InternalServerError
from ..types.add_analysis_archive_result import AddAnalysisArchiveResult
from ..types.analysis_archive_rules import AnalysisArchiveRules
from ..types.analysis_archive_transition_rule import AnalysisArchiveTransitionRule
from ..types.analysis_archive_transition_rule_exclude import AnalysisArchiveTransitionRuleExclude
from ..types.analysis_archive_transition_rule_transition import AnalysisArchiveTransitionRuleTransition
from ..types.archive_summary import ArchiveSummary
from ..types.archived_analyses import ArchivedAnalyses
from ..types.archived_analysis import ArchivedAnalysis
from ..types.image_analysis_references import ImageAnalysisReferences
from ..types.image_selector import ImageSelector
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawArchivesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_archives(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ArchiveSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArchiveSummary]
            Archive summary listing
        """
        _response = self._client_wrapper.httpx_client.request(
            "archives",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchiveSummary,
                    parse_obj_as(
                        type_=ArchiveSummary,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def list_analysis_archive(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ArchivedAnalyses]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArchivedAnalyses]
            Image analysis archive listing for the requesting account (not the whole system)
        """
        _response = self._client_wrapper.httpx_client.request(
            "archives/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivedAnalyses,
                    parse_obj_as(
                        type_=ArchivedAnalyses,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def archive_image_analysis(
        self, *, request: ImageAnalysisReferences, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddAnalysisArchiveResult]:
        """
        Parameters
        ----------
        request : ImageAnalysisReferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddAnalysisArchiveResult]
            Archive statuses
        """
        _response = self._client_wrapper.httpx_client.request(
            "archives/images",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddAnalysisArchiveResult,
                    parse_obj_as(
                        type_=AddAnalysisArchiveResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_archived_analysis(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ArchivedAnalysis]:
        """
        Returns the archive metadata record identifying the image and tags for the analysis in the archive.

        Parameters
        ----------
        image_digest : str
            The image digest to identify the image analysis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ArchivedAnalysis]
            Archived Image
        """
        _response = self._client_wrapper.httpx_client.request(
            f"archives/images/{encode_path_param(image_digest)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivedAnalysis,
                    parse_obj_as(
                        type_=ArchivedAnalysis,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_archived_analysis(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Performs a synchronous archive deletion

        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"archives/images/{encode_path_param(image_digest)}",
            method="DELETE",
            params={
                "force": force,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def list_analysis_archive_rules(
        self, *, system_global: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AnalysisArchiveRules]:
        """
        Parameters
        ----------
        system_global : typing.Optional[bool]
            If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnalysisArchiveRules]
            Archive transition rules
        """
        _response = self._client_wrapper.httpx_client.request(
            "archives/rules",
            method="GET",
            params={
                "system_global": system_global,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveRules,
                    parse_obj_as(
                        type_=AnalysisArchiveRules,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create_analysis_archive_rule(
        self,
        *,
        transition: AnalysisArchiveTransitionRuleTransition,
        analysis_age_days: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        exclude: typing.Optional[AnalysisArchiveTransitionRuleExclude] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_images_per_account: typing.Optional[int] = OMIT,
        rule_id: typing.Optional[str] = OMIT,
        selector: typing.Optional[ImageSelector] = OMIT,
        system_global: typing.Optional[bool] = OMIT,
        tag_versions_newer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnalysisArchiveTransitionRule]:
        """
        Parameters
        ----------
        transition : AnalysisArchiveTransitionRuleTransition
            The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.

        analysis_age_days : typing.Optional[int]
            Matches if the analysis is strictly older than this number of days

        created_at : typing.Optional[dt.datetime]

        exclude : typing.Optional[AnalysisArchiveTransitionRuleExclude]

        last_updated : typing.Optional[dt.datetime]

        max_images_per_account : typing.Optional[int]
            This is the maximum number of image analyses an account can have. Can only be set on system_global rules

        rule_id : typing.Optional[str]
            Unique identifier for archive rule

        selector : typing.Optional[ImageSelector]

        system_global : typing.Optional[bool]
            True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them

        tag_versions_newer : typing.Optional[int]
            Number of images mapped to the tag that are newer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnalysisArchiveTransitionRule]
            Archive transition rule
        """
        _response = self._client_wrapper.httpx_client.request(
            "archives/rules",
            method="POST",
            json={
                "analysis_age_days": analysis_age_days,
                "created_at": created_at,
                "exclude": convert_and_respect_annotation_metadata(
                    object_=exclude, annotation=AnalysisArchiveTransitionRuleExclude, direction="write"
                ),
                "last_updated": last_updated,
                "max_images_per_account": max_images_per_account,
                "rule_id": rule_id,
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ImageSelector, direction="write"
                ),
                "system_global": system_global,
                "tag_versions_newer": tag_versions_newer,
                "transition": transition,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveTransitionRule,
                    parse_obj_as(
                        type_=AnalysisArchiveTransitionRule,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AnalysisArchiveTransitionRule]:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnalysisArchiveTransitionRule]
            Archive transition rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"archives/rules/{encode_path_param(rule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveTransitionRule,
                    parse_obj_as(
                        type_=AnalysisArchiveTransitionRule,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def delete_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"archives/rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawArchivesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_archives(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArchiveSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArchiveSummary]
            Archive summary listing
        """
        _response = await self._client_wrapper.httpx_client.request(
            "archives",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchiveSummary,
                    parse_obj_as(
                        type_=ArchiveSummary,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def list_analysis_archive(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArchivedAnalyses]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArchivedAnalyses]
            Image analysis archive listing for the requesting account (not the whole system)
        """
        _response = await self._client_wrapper.httpx_client.request(
            "archives/images",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivedAnalyses,
                    parse_obj_as(
                        type_=ArchivedAnalyses,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def archive_image_analysis(
        self, *, request: ImageAnalysisReferences, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddAnalysisArchiveResult]:
        """
        Parameters
        ----------
        request : ImageAnalysisReferences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddAnalysisArchiveResult]
            Archive statuses
        """
        _response = await self._client_wrapper.httpx_client.request(
            "archives/images",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddAnalysisArchiveResult,
                    parse_obj_as(
                        type_=AddAnalysisArchiveResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_archived_analysis(
        self, image_digest: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ArchivedAnalysis]:
        """
        Returns the archive metadata record identifying the image and tags for the analysis in the archive.

        Parameters
        ----------
        image_digest : str
            The image digest to identify the image analysis

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ArchivedAnalysis]
            Archived Image
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"archives/images/{encode_path_param(image_digest)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArchivedAnalysis,
                    parse_obj_as(
                        type_=ArchivedAnalysis,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_archived_analysis(
        self,
        image_digest: str,
        *,
        force: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Performs a synchronous archive deletion

        Parameters
        ----------
        image_digest : str

        force : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"archives/images/{encode_path_param(image_digest)}",
            method="DELETE",
            params={
                "force": force,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def list_analysis_archive_rules(
        self, *, system_global: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AnalysisArchiveRules]:
        """
        Parameters
        ----------
        system_global : typing.Optional[bool]
            If true include system global rules (owned by admin) even for non-admin users. Defaults to true if not set. Can be set to false to exclude globals

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnalysisArchiveRules]
            Archive transition rules
        """
        _response = await self._client_wrapper.httpx_client.request(
            "archives/rules",
            method="GET",
            params={
                "system_global": system_global,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveRules,
                    parse_obj_as(
                        type_=AnalysisArchiveRules,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create_analysis_archive_rule(
        self,
        *,
        transition: AnalysisArchiveTransitionRuleTransition,
        analysis_age_days: typing.Optional[int] = OMIT,
        created_at: typing.Optional[dt.datetime] = OMIT,
        exclude: typing.Optional[AnalysisArchiveTransitionRuleExclude] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_images_per_account: typing.Optional[int] = OMIT,
        rule_id: typing.Optional[str] = OMIT,
        selector: typing.Optional[ImageSelector] = OMIT,
        system_global: typing.Optional[bool] = OMIT,
        tag_versions_newer: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnalysisArchiveTransitionRule]:
        """
        Parameters
        ----------
        transition : AnalysisArchiveTransitionRuleTransition
            The type of transition to make. If "archive", then archive an image from the working set and remove it from the working set. If "delete", then match against archived images and delete from the archive if match.

        analysis_age_days : typing.Optional[int]
            Matches if the analysis is strictly older than this number of days

        created_at : typing.Optional[dt.datetime]

        exclude : typing.Optional[AnalysisArchiveTransitionRuleExclude]

        last_updated : typing.Optional[dt.datetime]

        max_images_per_account : typing.Optional[int]
            This is the maximum number of image analyses an account can have. Can only be set on system_global rules

        rule_id : typing.Optional[str]
            Unique identifier for archive rule

        selector : typing.Optional[ImageSelector]

        system_global : typing.Optional[bool]
            True if the rule applies to all accounts in the system. This is only available to admin users to update/modify, but all users with permission to list rules can see them

        tag_versions_newer : typing.Optional[int]
            Number of images mapped to the tag that are newer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnalysisArchiveTransitionRule]
            Archive transition rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            "archives/rules",
            method="POST",
            json={
                "analysis_age_days": analysis_age_days,
                "created_at": created_at,
                "exclude": convert_and_respect_annotation_metadata(
                    object_=exclude, annotation=AnalysisArchiveTransitionRuleExclude, direction="write"
                ),
                "last_updated": last_updated,
                "max_images_per_account": max_images_per_account,
                "rule_id": rule_id,
                "selector": convert_and_respect_annotation_metadata(
                    object_=selector, annotation=ImageSelector, direction="write"
                ),
                "system_global": system_global,
                "tag_versions_newer": tag_versions_newer,
                "transition": transition,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveTransitionRule,
                    parse_obj_as(
                        type_=AnalysisArchiveTransitionRule,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AnalysisArchiveTransitionRule]:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnalysisArchiveTransitionRule]
            Archive transition rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"archives/rules/{encode_path_param(rule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnalysisArchiveTransitionRule,
                    parse_obj_as(
                        type_=AnalysisArchiveTransitionRule,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def delete_analysis_archive_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        rule_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"archives/rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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
