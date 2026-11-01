

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.assignment import Assignment
from ..types.contribution import Contribution
from ..types.error_response import ErrorResponse
from ..types.export import Export
from ..types.export_summary import ExportSummary
from ..types.flag import Flag
from ..types.media_usage import MediaUsage
from ..types.moderation_action import ModerationAction
from ..types.moderation_history_item import ModerationHistoryItem
from ..types.place import Place
from ..types.via import Via
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContributionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_valid_contribution_refinement_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            An array of refinement types. These are the possible values of the get contribution refinements parameter.
        """
        _response = self._client_wrapper.httpx_client.request(
            "contribution-refinement-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def list_contribution_refinement_options(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        refinements: typing.Optional[str] = None,
        refinement_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.List[str]]]:
        """
        Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        refinements : typing.Optional[str]
            Comma seperated list of refinement names.

        refinement_size : typing.Optional[float]
            Number of refinement options to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.List[str]]]
            A map of refinement names to lists of options
        """
        _response = self._client_wrapper.httpx_client.request(
            "contribution-refinements",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "refinements": refinements,
                "refinementSize": refinement_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[str]],
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

    def list_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_day: typing.Optional[dt.date] = None,
        created_month: typing.Optional[str] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Contribution]]:
        """
        Retrieve contributions.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        created_day : typing.Optional[dt.date]
            Limit results to contributions created on this day.

        created_month : typing.Optional[str]
            Limit results to contributions created during this month.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        ids : typing.Optional[str]
            Restrict results to a list of specific contributions identified by a comma seperated list of ids.

        format : typing.Optional[str]
            Select output format. 'json' or 'rss'. Defaults to JSON.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Contribution]]
            A list of contributions
        """
        _response = self._client_wrapper.httpx_client.request(
            "contributions",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "createdDay": str(created_day) if created_day is not None else None,
                "createdMonth": created_month,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "ids": ids,
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Contribution],
                    parse_obj_as(
                        type_=typing.List[Contribution],
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

    def create_a_new_contribution(
        self,
        *,
        assignment: typing.Optional[Assignment] = OMIT,
        attribution: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_usages: typing.Optional[typing.Sequence[MediaUsage]] = OMIT,
        moderation_history: typing.Optional[typing.Sequence[ModerationHistoryItem]] = OMIT,
        place: typing.Optional[Place] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        via: typing.Optional[Via] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Contribution]:
        """
        Parameters
        ----------
        assignment : typing.Optional[Assignment]

        attribution : typing.Optional[str]
            The public attribution for this contribution. This will be the display name of the registered user or the contributor's first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.

        body : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        id : typing.Optional[str]

        media_usages : typing.Optional[typing.Sequence[MediaUsage]]

        moderation_history : typing.Optional[typing.Sequence[ModerationHistoryItem]]

        place : typing.Optional[Place]

        url_words : typing.Optional[str]

        via : typing.Optional[Via]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Contribution]
            Contribution created
        """
        _response = self._client_wrapper.httpx_client.request(
            "contributions",
            method="POST",
            json={
                "assignment": convert_and_respect_annotation_metadata(
                    object_=assignment, annotation=Assignment, direction="write"
                ),
                "attribution": attribution,
                "body": body,
                "created": created,
                "headline": headline,
                "id": id,
                "mediaUsages": convert_and_respect_annotation_metadata(
                    object_=media_usages, annotation=typing.Sequence[MediaUsage], direction="write"
                ),
                "moderationHistory": convert_and_respect_annotation_metadata(
                    object_=moderation_history, annotation=typing.Sequence[ModerationHistoryItem], direction="write"
                ),
                "place": convert_and_respect_annotation_metadata(object_=place, annotation=Place, direction="write"),
                "urlWords": url_words,
                "via": convert_and_respect_annotation_metadata(object_=via, annotation=Via, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
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

    def get_a_single_contribution_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Contribution]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Contribution]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
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

    def delete_this_contribution(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Contribution]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Contribution]
            The deletion request has been accepted and will be processed in the background.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def raise_a_flag_against_this_contribution(
        self,
        id_: str,
        *,
        date: typing.Optional[dt.datetime] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Flag]:
        """
        Allows end users to bring potential issues with publicly visible content to the attention of moderators.

        Parameters
        ----------
        id_ : str
            Id of the contribution to flag

        date : typing.Optional[dt.datetime]

        email : typing.Optional[str]

        id : typing.Optional[str]

        notes : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Flag]
            Flag created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id_)}/flag",
            method="POST",
            json={
                "date": date,
                "email": email,
                "id": id,
                "notes": notes,
                "type": type,
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
                    Flag,
                    parse_obj_as(
                        type_=Flag,
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

    def allows_a_user_to_mark_a_contribution_as_liked(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[float]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[float]
            The updated like count for this contribution.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/like",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    float,
                    parse_obj_as(
                        type_=float,
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

    def list_users_who_have_liked_this_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Returns a list of user ids of users who have liked this conribution

        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            A list of user ids.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/likes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def perform_a_moderation_action_on_this_contribution(
        self,
        id: str,
        *,
        action: typing.Optional[ModerationAction] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Allows the contribution to approved of rejected.

        Parameters
        ----------
        id : str
            Id of the contribution to moderate

        action : typing.Optional[ModerationAction]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            The moderation action was successfully applied
        """
        _response = self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/moderate",
            method="POST",
            json={
                "action": convert_and_respect_annotation_metadata(
                    object_=action, annotation=ModerationAction, direction="write"
                ),
                "notes": notes,
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
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def export_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        tagged: typing.Optional[bool] = None,
        combined: typing.Optional[bool] = None,
        individual: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        json: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Export]:
        """
        Begin an export job. Returns a export job which can be polled to follow the progress of an export.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        tagged : typing.Optional[bool]
            Should exported media files be tagged with metadata. Deprecated; use format instead.

        combined : typing.Optional[bool]
            Included a combined file with all contribution text.

        individual : typing.Optional[bool]
            Include individual text files for each contribution.

        format : typing.Optional[str]
            Media format to export; none, fullsize, tagged or original.

        json : typing.Optional[bool]
            Include raw JSON for each contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Export]
            An export job describing the state of an export job.
        """
        _response = self._client_wrapper.httpx_client.request(
            "export",
            method="POST",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "tagged": tagged,
                "combined": combined,
                "individual": individual,
                "format": format,
                "json": json,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Export,
                    parse_obj_as(
                        type_=Export,
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

    def export_contributions_preflight_summary(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportSummary]:
        """
        Provide a preflight summary of an export request.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportSummary]
            A summary of the number of contributions, media files and approximate total size of media files.
        """
        _response = self._client_wrapper.httpx_client.request(
            "export-summary",
            method="POST",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportSummary,
                    parse_obj_as(
                        type_=ExportSummary,
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

    def get_a_single_export_job_poll_to_follow_export_progress(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Export]:
        """
        Parameters
        ----------
        id : str
            Id of the export job to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Export]
            Successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"exports/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Export,
                    parse_obj_as(
                        type_=Export,
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


class AsyncRawContributionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_valid_contribution_refinement_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            An array of refinement types. These are the possible values of the get contribution refinements parameter.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contribution-refinement-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def list_contribution_refinement_options(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        refinements: typing.Optional[str] = None,
        refinement_size: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.List[str]]]:
        """
        Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        refinements : typing.Optional[str]
            Comma seperated list of refinement names.

        refinement_size : typing.Optional[float]
            Number of refinement options to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.List[str]]]
            A map of refinement names to lists of options
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contribution-refinements",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "refinements": refinements,
                "refinementSize": refinement_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.List[str]],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.List[str]],
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

    async def list_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_day: typing.Optional[dt.date] = None,
        created_month: typing.Optional[str] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Contribution]]:
        """
        Retrieve contributions.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        created_day : typing.Optional[dt.date]
            Limit results to contributions created on this day.

        created_month : typing.Optional[str]
            Limit results to contributions created during this month.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        ids : typing.Optional[str]
            Restrict results to a list of specific contributions identified by a comma seperated list of ids.

        format : typing.Optional[str]
            Select output format. 'json' or 'rss'. Defaults to JSON.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Contribution]]
            A list of contributions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contributions",
            method="GET",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "createdDay": str(created_day) if created_day is not None else None,
                "createdMonth": created_month,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "ids": ids,
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Contribution],
                    parse_obj_as(
                        type_=typing.List[Contribution],
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

    async def create_a_new_contribution(
        self,
        *,
        assignment: typing.Optional[Assignment] = OMIT,
        attribution: typing.Optional[str] = OMIT,
        body: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        headline: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        media_usages: typing.Optional[typing.Sequence[MediaUsage]] = OMIT,
        moderation_history: typing.Optional[typing.Sequence[ModerationHistoryItem]] = OMIT,
        place: typing.Optional[Place] = OMIT,
        url_words: typing.Optional[str] = OMIT,
        via: typing.Optional[Via] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Contribution]:
        """
        Parameters
        ----------
        assignment : typing.Optional[Assignment]

        attribution : typing.Optional[str]
            The public attribution for this contribution. This will be the display name of the registered user or the contributor's first and last name if they provided them while making a non authenticated contribution. A blank attribution field indicates and anonymous contribution.

        body : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        headline : typing.Optional[str]

        id : typing.Optional[str]

        media_usages : typing.Optional[typing.Sequence[MediaUsage]]

        moderation_history : typing.Optional[typing.Sequence[ModerationHistoryItem]]

        place : typing.Optional[Place]

        url_words : typing.Optional[str]

        via : typing.Optional[Via]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Contribution]
            Contribution created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "contributions",
            method="POST",
            json={
                "assignment": convert_and_respect_annotation_metadata(
                    object_=assignment, annotation=Assignment, direction="write"
                ),
                "attribution": attribution,
                "body": body,
                "created": created,
                "headline": headline,
                "id": id,
                "mediaUsages": convert_and_respect_annotation_metadata(
                    object_=media_usages, annotation=typing.Sequence[MediaUsage], direction="write"
                ),
                "moderationHistory": convert_and_respect_annotation_metadata(
                    object_=moderation_history, annotation=typing.Sequence[ModerationHistoryItem], direction="write"
                ),
                "place": convert_and_respect_annotation_metadata(object_=place, annotation=Place, direction="write"),
                "urlWords": url_words,
                "via": convert_and_respect_annotation_metadata(object_=via, annotation=Via, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
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

    async def get_a_single_contribution_by_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Contribution]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Contribution]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
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

    async def delete_this_contribution(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Contribution]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Contribution]
            The deletion request has been accepted and will be processed in the background.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contribution,
                    parse_obj_as(
                        type_=Contribution,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def raise_a_flag_against_this_contribution(
        self,
        id_: str,
        *,
        date: typing.Optional[dt.datetime] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Flag]:
        """
        Allows end users to bring potential issues with publicly visible content to the attention of moderators.

        Parameters
        ----------
        id_ : str
            Id of the contribution to flag

        date : typing.Optional[dt.datetime]

        email : typing.Optional[str]

        id : typing.Optional[str]

        notes : typing.Optional[str]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Flag]
            Flag created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id_)}/flag",
            method="POST",
            json={
                "date": date,
                "email": email,
                "id": id,
                "notes": notes,
                "type": type,
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
                    Flag,
                    parse_obj_as(
                        type_=Flag,
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

    async def allows_a_user_to_mark_a_contribution_as_liked(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[float]:
        """
        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[float]
            The updated like count for this contribution.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/like",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    float,
                    parse_obj_as(
                        type_=float,
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

    async def list_users_who_have_liked_this_contributions(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Returns a list of user ids of users who have liked this conribution

        Parameters
        ----------
        id : str
            Id of the contribution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            A list of user ids.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/likes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def perform_a_moderation_action_on_this_contribution(
        self,
        id: str,
        *,
        action: typing.Optional[ModerationAction] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Allows the contribution to approved of rejected.

        Parameters
        ----------
        id : str
            Id of the contribution to moderate

        action : typing.Optional[ModerationAction]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            The moderation action was successfully applied
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"contributions/{encode_path_param(id)}/moderate",
            method="POST",
            json={
                "action": convert_and_respect_annotation_metadata(
                    object_=action, annotation=ModerationAction, direction="write"
                ),
                "notes": notes,
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
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def export_contributions(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        tagged: typing.Optional[bool] = None,
        combined: typing.Optional[bool] = None,
        individual: typing.Optional[bool] = None,
        format: typing.Optional[str] = None,
        json: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Export]:
        """
        Begin an export job. Returns a export job which can be polled to follow the progress of an export.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        tagged : typing.Optional[bool]
            Should exported media files be tagged with metadata. Deprecated; use format instead.

        combined : typing.Optional[bool]
            Included a combined file with all contribution text.

        individual : typing.Optional[bool]
            Include individual text files for each contribution.

        format : typing.Optional[str]
            Media format to export; none, fullsize, tagged or original.

        json : typing.Optional[bool]
            Include raw JSON for each contribution.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Export]
            An export job describing the state of an export job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "export",
            method="POST",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
                "tagged": tagged,
                "combined": combined,
                "individual": individual,
                "format": format,
                "json": json,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Export,
                    parse_obj_as(
                        type_=Export,
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

    async def export_contributions_preflight_summary(
        self,
        *,
        assignment: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        created_before: typing.Optional[dt.datetime] = None,
        created_after: typing.Optional[dt.datetime] = None,
        geohash: typing.Optional[str] = None,
        has_location: typing.Optional[bool] = None,
        lat_long: typing.Optional[str] = None,
        radius: typing.Optional[float] = None,
        media_type: typing.Optional[str] = None,
        owned_by: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        url_words: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportSummary]:
        """
        Provide a preflight summary of an export request.

        Parameters
        ----------
        assignment : typing.Optional[str]
            Restrict results to contributions submitted to this assignment.

        country : typing.Optional[str]
            Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).

        created_before : typing.Optional[dt.datetime]
            Limit results to contributions created before this date time.

        created_after : typing.Optional[dt.datetime]
            Limit results to contributions created after this date time.

        geohash : typing.Optional[str]
            Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)

        has_location : typing.Optional[bool]
            Restrict results to contributions which have a publicly visible location.

        lat_long : typing.Optional[str]
            Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius

        radius : typing.Optional[float]
            When limiting result by location with the latLong parameter, specify the radius in kilometers.

        media_type : typing.Optional[str]
            Restrict results to contributions which include a media file of the given type (ie. image / video)

        owned_by : typing.Optional[str]
            Restrict results to contributions which are fall under the jurisdiction by this user.

        q : typing.Optional[str]
            Restrict results to contributions whose headline text matches this keyword.

        url_words : typing.Optional[str]
            Locate a specific contribution by URL words

        user : typing.Optional[str]
            Restrict results to contributions by this user identified by id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportSummary]
            A summary of the number of contributions, media files and approximate total size of media files.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "export-summary",
            method="POST",
            params={
                "assignment": assignment,
                "country": country,
                "createdBefore": serialize_datetime(created_before) if created_before is not None else None,
                "createdAfter": serialize_datetime(created_after) if created_after is not None else None,
                "geohash": geohash,
                "hasLocation": has_location,
                "latLong": lat_long,
                "radius": radius,
                "mediaType": media_type,
                "ownedBy": owned_by,
                "q": q,
                "urlWords": url_words,
                "user": user,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportSummary,
                    parse_obj_as(
                        type_=ExportSummary,
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

    async def get_a_single_export_job_poll_to_follow_export_progress(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Export]:
        """
        Parameters
        ----------
        id : str
            Id of the export job to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Export]
            Successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"exports/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Export,
                    parse_obj_as(
                        type_=Export,
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
