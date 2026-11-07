

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
from ..errors.bad_request_error import BadRequestError
from ..types.alert_event_response import AlertEventResponse
from ..types.alert_rule_response import AlertRuleResponse
from ..types.alert_status_response import AlertStatusResponse
from ..types.channel_type import ChannelType
from ..types.duration import Duration
from ..types.instant import Instant
from ..types.notification_channel_response import NotificationChannelResponse
from ..types.operator import Operator
from ..types.paged_alert_event_response import PagedAlertEventResponse
from ..types.reduce_function import ReduceFunction
from ..types.severity import Severity
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAlertingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def returns_all_available_notification_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotificationChannelResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotificationChannelResponse]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/channels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationChannelResponse],
                    parse_obj_as(
                        type_=typing.List[NotificationChannelResponse],
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

    def creates_a_new_notification_channel(
        self,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationChannelResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/channels",
            method="POST",
            json={
                "name": name,
                "type": type,
                "config": config,
                "enabled": enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    def returns_a_notification_channel_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationChannelResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    def updates_an_existing_notification_channel(
        self,
        id: int,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotificationChannelResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "type": type,
                "config": config,
                "enabled": enabled,
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
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    def deletes_an_existing_notification_channel(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_paginated_alert_events(
        self,
        *,
        from_: typing.Optional[Instant] = None,
        page: typing.Optional[int] = None,
        pipeline_id: typing.Optional[str] = None,
        rule_id: typing.Optional[int] = None,
        severity: typing.Optional[Severity] = None,
        size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        to: typing.Optional[Instant] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagedAlertEventResponse]:
        """
        Parameters
        ----------
        from_ : typing.Optional[Instant]

        page : typing.Optional[int]

        pipeline_id : typing.Optional[str]

        rule_id : typing.Optional[int]

        severity : typing.Optional[Severity]

        size : typing.Optional[int]

        status : typing.Optional[str]

        to : typing.Optional[Instant]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagedAlertEventResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/events",
            method="GET",
            params={
                "from": serialize_datetime(from_) if from_ is not None else None,
                "page": page,
                "pipelineId": pipeline_id,
                "ruleId": rule_id,
                "severity": severity,
                "size": size,
                "status": status,
                "to": serialize_datetime(to) if to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedAlertEventResponse,
                    parse_obj_as(
                        type_=PagedAlertEventResponse,
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

    def returns_a_single_alert_event_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AlertEventResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertEventResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/events/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertEventResponse,
                    parse_obj_as(
                        type_=AlertEventResponse,
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

    def returns_all_available_alert_rules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AlertRuleResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AlertRuleResponse]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AlertRuleResponse],
                    parse_obj_as(
                        type_=typing.List[AlertRuleResponse],
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

    def creates_a_new_alert_rule(
        self,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertRuleResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/rules",
            method="POST",
            json={
                "name": name,
                "description": description,
                "panelId": panel_id,
                "operator": operator,
                "threshold": threshold,
                "forDuration": for_duration,
                "reduceFunction": reduce_function,
                "evaluationWindow": evaluation_window,
                "severity": severity,
                "enabled": enabled,
                "channelIds": channel_ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    def returns_an_alert_rule_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertRuleResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    def updates_an_existing_alert_rule(
        self,
        id: int,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertRuleResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "panelId": panel_id,
                "operator": operator,
                "threshold": threshold,
                "forDuration": for_duration,
                "reduceFunction": reduce_function,
                "evaluationWindow": evaluation_window,
                "severity": severity,
                "enabled": enabled,
                "channelIds": channel_ids,
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
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    def deletes_an_existing_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def disables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertRuleResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}/disable",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    def enables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertRuleResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}/enable",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    def returns_current_alert_status_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AlertStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AlertStatusResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/alerts/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertStatusResponse,
                    parse_obj_as(
                        type_=AlertStatusResponse,
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


class AsyncRawAlertingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def returns_all_available_notification_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotificationChannelResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotificationChannelResponse]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/channels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotificationChannelResponse],
                    parse_obj_as(
                        type_=typing.List[NotificationChannelResponse],
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

    async def creates_a_new_notification_channel(
        self,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationChannelResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/channels",
            method="POST",
            json={
                "name": name,
                "type": type,
                "config": config,
                "enabled": enabled,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    async def returns_a_notification_channel_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationChannelResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    async def updates_an_existing_notification_channel(
        self,
        id: int,
        *,
        name: str,
        type: ChannelType,
        config: typing.Dict[str, typing.Any],
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotificationChannelResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        type : ChannelType

        config : typing.Dict[str, typing.Any]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotificationChannelResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "type": type,
                "config": config,
                "enabled": enabled,
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
                    NotificationChannelResponse,
                    parse_obj_as(
                        type_=NotificationChannelResponse,
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

    async def deletes_an_existing_notification_channel(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/channels/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_paginated_alert_events(
        self,
        *,
        from_: typing.Optional[Instant] = None,
        page: typing.Optional[int] = None,
        pipeline_id: typing.Optional[str] = None,
        rule_id: typing.Optional[int] = None,
        severity: typing.Optional[Severity] = None,
        size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
        to: typing.Optional[Instant] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagedAlertEventResponse]:
        """
        Parameters
        ----------
        from_ : typing.Optional[Instant]

        page : typing.Optional[int]

        pipeline_id : typing.Optional[str]

        rule_id : typing.Optional[int]

        severity : typing.Optional[Severity]

        size : typing.Optional[int]

        status : typing.Optional[str]

        to : typing.Optional[Instant]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagedAlertEventResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/events",
            method="GET",
            params={
                "from": serialize_datetime(from_) if from_ is not None else None,
                "page": page,
                "pipelineId": pipeline_id,
                "ruleId": rule_id,
                "severity": severity,
                "size": size,
                "status": status,
                "to": serialize_datetime(to) if to is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagedAlertEventResponse,
                    parse_obj_as(
                        type_=PagedAlertEventResponse,
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

    async def returns_a_single_alert_event_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AlertEventResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertEventResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/events/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertEventResponse,
                    parse_obj_as(
                        type_=AlertEventResponse,
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

    async def returns_all_available_alert_rules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AlertRuleResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AlertRuleResponse]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AlertRuleResponse],
                    parse_obj_as(
                        type_=typing.List[AlertRuleResponse],
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

    async def creates_a_new_alert_rule(
        self,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertRuleResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/rules",
            method="POST",
            json={
                "name": name,
                "description": description,
                "panelId": panel_id,
                "operator": operator,
                "threshold": threshold,
                "forDuration": for_duration,
                "reduceFunction": reduce_function,
                "evaluationWindow": evaluation_window,
                "severity": severity,
                "enabled": enabled,
                "channelIds": channel_ids,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    async def returns_an_alert_rule_with_given_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertRuleResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    async def updates_an_existing_alert_rule(
        self,
        id: int,
        *,
        name: str,
        panel_id: str,
        operator: Operator,
        threshold: float,
        description: typing.Optional[str] = OMIT,
        for_duration: typing.Optional[Duration] = OMIT,
        reduce_function: typing.Optional[ReduceFunction] = OMIT,
        evaluation_window: typing.Optional[Duration] = OMIT,
        severity: typing.Optional[Severity] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        channel_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        panel_id : str

        operator : Operator

        threshold : float

        description : typing.Optional[str]

        for_duration : typing.Optional[Duration]
            ISO-8601 duration for how long the condition must hold before firing. Default: PT0S (immediate). Max: PT1H

        reduce_function : typing.Optional[ReduceFunction]

        evaluation_window : typing.Optional[Duration]
            ISO-8601 duration for the evaluation window used with reduce functions other than LAST. Default: PT5M. Range: PT1M to PT1H

        severity : typing.Optional[Severity]

        enabled : typing.Optional[bool]

        channel_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertRuleResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "panelId": panel_id,
                "operator": operator,
                "threshold": threshold,
                "forDuration": for_duration,
                "reduceFunction": reduce_function,
                "evaluationWindow": evaluation_window,
                "severity": severity,
                "enabled": enabled,
                "channelIds": channel_ids,
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
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    async def deletes_an_existing_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def disables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertRuleResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}/disable",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    async def enables_an_alert_rule(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AlertRuleResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertRuleResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alerts/rules/{encode_path_param(id)}/enable",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertRuleResponse,
                    parse_obj_as(
                        type_=AlertRuleResponse,
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

    async def returns_current_alert_status_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AlertStatusResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AlertStatusResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/alerts/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AlertStatusResponse,
                    parse_obj_as(
                        type_=AlertStatusResponse,
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
