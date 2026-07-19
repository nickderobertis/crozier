

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.feeds_list_feeds_request_offset import FeedsListFeedsRequestOffset
from ..types.feeds_list_subscriptions_request_offset import FeedsListSubscriptionsRequestOffset
from .types.feeds_backfill_subscription_response import FeedsBackfillSubscriptionResponse
from .types.feeds_create_feed_response import FeedsCreateFeedResponse
from .types.feeds_delete_feed_request_body import FeedsDeleteFeedRequestBody
from .types.feeds_delete_feed_response import FeedsDeleteFeedResponse
from .types.feeds_delete_subscription_request_body import FeedsDeleteSubscriptionRequestBody
from .types.feeds_delete_subscription_response import FeedsDeleteSubscriptionResponse
from .types.feeds_get_feed_response import FeedsGetFeedResponse
from .types.feeds_get_message_response import FeedsGetMessageResponse
from .types.feeds_list_feeds_response import FeedsListFeedsResponse
from .types.feeds_list_messages_response import FeedsListMessagesResponse
from .types.feeds_list_subscription_history_response import FeedsListSubscriptionHistoryResponse
from .types.feeds_list_subscriptions_response import FeedsListSubscriptionsResponse
from .types.feeds_publish_messages_request_messages_item import FeedsPublishMessagesRequestMessagesItem
from .types.feeds_publish_messages_response import FeedsPublishMessagesResponse
from .types.feeds_subscribe_agent_response import FeedsSubscribeAgentResponse
from .types.feeds_trigger_subscription_response import FeedsTriggerSubscriptionResponse
from .types.feeds_unsubscribe_agent_response import FeedsUnsubscribeAgentResponse
from .types.feeds_update_all_subscriptions_cron_response import FeedsUpdateAllSubscriptionsCronResponse
from .types.feeds_update_subscription_response import FeedsUpdateSubscriptionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFeedsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listfeeds(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListFeedsRequestOffset] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsListFeedsResponse]:
        """
        List all feeds with optional filters and pagination

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListFeedsRequestOffset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsListFeedsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/feeds",
            method="GET",
            params={
                "project_id": project_id,
                "name": name,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListFeedsResponse,
                    parse_obj_as(
                        type_=FeedsListFeedsResponse,
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

    def createfeed(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsCreateFeedResponse]:
        """
        Create a new feed in a project

        Parameters
        ----------
        project_id : str

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsCreateFeedResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/feeds",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
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
                    FeedsCreateFeedResponse,
                    parse_obj_as(
                        type_=FeedsCreateFeedResponse,
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

    def getfeed(
        self, feed_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeedsGetFeedResponse]:
        """
        Retrieve feed details by ID

        Parameters
        ----------
        feed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsGetFeedResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsGetFeedResponse,
                    parse_obj_as(
                        type_=FeedsGetFeedResponse,
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

    def deletefeed(
        self,
        feed_id: str,
        *,
        request: typing.Optional[FeedsDeleteFeedRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsDeleteFeedResponse]:
        """
        Soft delete a feed and clean up its sequence

        Parameters
        ----------
        feed_id : str

        request : typing.Optional[FeedsDeleteFeedRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsDeleteFeedResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FeedsDeleteFeedRequestBody], direction="write"
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
                    FeedsDeleteFeedResponse,
                    parse_obj_as(
                        type_=FeedsDeleteFeedResponse,
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

    def listmessages(
        self,
        feed_id: str,
        *,
        after_sequence: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsListMessagesResponse]:
        """
        List messages from a feed (for debugging/inspection)

        Parameters
        ----------
        feed_id : str

        after_sequence : typing.Optional[str]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsListMessagesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages",
            method="GET",
            params={
                "after_sequence": after_sequence,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListMessagesResponse,
                    parse_obj_as(
                        type_=FeedsListMessagesResponse,
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

    def publishmessages(
        self,
        feed_id: str,
        *,
        messages: typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsPublishMessagesResponse]:
        """
        Batch insert messages into a feed (up to 10,000 per request)

        Parameters
        ----------
        feed_id : str

        messages : typing.Sequence[FeedsPublishMessagesRequestMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsPublishMessagesResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
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
                _data = typing.cast(
                    FeedsPublishMessagesResponse,
                    parse_obj_as(
                        type_=FeedsPublishMessagesResponse,
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

    def getmessage(
        self, feed_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeedsGetMessageResponse]:
        """
        Get full content of a feed message

        Parameters
        ----------
        feed_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsGetMessageResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsGetMessageResponse,
                    parse_obj_as(
                        type_=FeedsGetMessageResponse,
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

    def subscribeagent(
        self,
        feed_id: str,
        *,
        agent_id: str,
        cron_schedule: str,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsSubscribeAgentResponse]:
        """
        Subscribe an agent to a feed with polling configuration

        Parameters
        ----------
        feed_id : str

        agent_id : str

        cron_schedule : str

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsSubscribeAgentResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscribe",
            method="POST",
            json={
                "agent_id": agent_id,
                "cron_schedule": cron_schedule,
                "prompt_template": prompt_template,
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
                    FeedsSubscribeAgentResponse,
                    parse_obj_as(
                        type_=FeedsSubscribeAgentResponse,
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

    def deletesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        request: typing.Optional[FeedsDeleteSubscriptionRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsDeleteSubscriptionResponse]:
        """
        Remove agent subscription from a feed (by subscription_id)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request : typing.Optional[FeedsDeleteSubscriptionRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsDeleteSubscriptionResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FeedsDeleteSubscriptionRequestBody], direction="write"
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
                    FeedsDeleteSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsDeleteSubscriptionResponse,
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

    def updatesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsUpdateSubscriptionResponse]:
        """
        Update subscription configuration (cron schedule, enable/disable)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsUpdateSubscriptionResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}",
            method="PATCH",
            json={
                "cron_schedule": cron_schedule,
                "prompt_template": prompt_template,
                "disabled": disabled,
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
                    FeedsUpdateSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsUpdateSubscriptionResponse,
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

    def unsubscribeagent(
        self, feed_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeedsUnsubscribeAgentResponse]:
        """
        Remove agent subscription from a feed (by agent_id)

        Parameters
        ----------
        feed_id : str

        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsUnsubscribeAgentResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/unsubscribe",
            method="POST",
            json={
                "agent_id": agent_id,
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
                    FeedsUnsubscribeAgentResponse,
                    parse_obj_as(
                        type_=FeedsUnsubscribeAgentResponse,
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

    def triggersubscription(
        self, feed_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeedsTriggerSubscriptionResponse]:
        """
        Immediately trigger a subscription to process pending messages

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsTriggerSubscriptionResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/trigger",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsTriggerSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsTriggerSubscriptionResponse,
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

    def backfillsubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        from_sequence: typing.Optional[float] = OMIT,
        to_sequence: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsBackfillSubscriptionResponse]:
        """
        Start a background job to send historical messages to an agent subscription. Returns immediately with workflow ID. Does not update last_consumed_sequence.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        from_sequence : typing.Optional[float]

        to_sequence : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsBackfillSubscriptionResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/backfill",
            method="POST",
            json={
                "from_sequence": from_sequence,
                "to_sequence": to_sequence,
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
                    FeedsBackfillSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsBackfillSubscriptionResponse,
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

    def listsubscriptionhistory(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        page_size: typing.Optional[str] = None,
        next_page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsListSubscriptionHistoryResponse]:
        """
        List the run history for a subscription including scheduled runs, manual triggers, and backfills.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        page_size : typing.Optional[str]

        next_page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsListSubscriptionHistoryResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/history",
            method="GET",
            params={
                "page_size": page_size,
                "next_page_token": next_page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListSubscriptionHistoryResponse,
                    parse_obj_as(
                        type_=FeedsListSubscriptionHistoryResponse,
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

    def updateallsubscriptionscron(
        self, feed_id: str, *, cron_schedule: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FeedsUpdateAllSubscriptionsCronResponse]:
        """
        Update the cron schedule for all subscriptions of a feed

        Parameters
        ----------
        feed_id : str

        cron_schedule : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsUpdateAllSubscriptionsCronResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/cron",
            method="PATCH",
            json={
                "cron_schedule": cron_schedule,
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
                    FeedsUpdateAllSubscriptionsCronResponse,
                    parse_obj_as(
                        type_=FeedsUpdateAllSubscriptionsCronResponse,
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

    def listsubscriptions(
        self,
        feed_id: str,
        *,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListSubscriptionsRequestOffset] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedsListSubscriptionsResponse]:
        """
        List all agent subscriptions for a feed

        Parameters
        ----------
        feed_id : str

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListSubscriptionsRequestOffset]

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedsListSubscriptionsResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListSubscriptionsResponse,
                    parse_obj_as(
                        type_=FeedsListSubscriptionsResponse,
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


class AsyncRawFeedsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listfeeds(
        self,
        *,
        project_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListFeedsRequestOffset] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsListFeedsResponse]:
        """
        List all feeds with optional filters and pagination

        Parameters
        ----------
        project_id : typing.Optional[str]

        name : typing.Optional[str]

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListFeedsRequestOffset]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsListFeedsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/feeds",
            method="GET",
            params={
                "project_id": project_id,
                "name": name,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListFeedsResponse,
                    parse_obj_as(
                        type_=FeedsListFeedsResponse,
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

    async def createfeed(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsCreateFeedResponse]:
        """
        Create a new feed in a project

        Parameters
        ----------
        project_id : str

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsCreateFeedResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/feeds",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
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
                    FeedsCreateFeedResponse,
                    parse_obj_as(
                        type_=FeedsCreateFeedResponse,
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

    async def getfeed(
        self, feed_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeedsGetFeedResponse]:
        """
        Retrieve feed details by ID

        Parameters
        ----------
        feed_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsGetFeedResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsGetFeedResponse,
                    parse_obj_as(
                        type_=FeedsGetFeedResponse,
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

    async def deletefeed(
        self,
        feed_id: str,
        *,
        request: typing.Optional[FeedsDeleteFeedRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsDeleteFeedResponse]:
        """
        Soft delete a feed and clean up its sequence

        Parameters
        ----------
        feed_id : str

        request : typing.Optional[FeedsDeleteFeedRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsDeleteFeedResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FeedsDeleteFeedRequestBody], direction="write"
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
                    FeedsDeleteFeedResponse,
                    parse_obj_as(
                        type_=FeedsDeleteFeedResponse,
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

    async def listmessages(
        self,
        feed_id: str,
        *,
        after_sequence: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsListMessagesResponse]:
        """
        List messages from a feed (for debugging/inspection)

        Parameters
        ----------
        feed_id : str

        after_sequence : typing.Optional[str]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsListMessagesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages",
            method="GET",
            params={
                "after_sequence": after_sequence,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListMessagesResponse,
                    parse_obj_as(
                        type_=FeedsListMessagesResponse,
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

    async def publishmessages(
        self,
        feed_id: str,
        *,
        messages: typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsPublishMessagesResponse]:
        """
        Batch insert messages into a feed (up to 10,000 per request)

        Parameters
        ----------
        feed_id : str

        messages : typing.Sequence[FeedsPublishMessagesRequestMessagesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsPublishMessagesResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[FeedsPublishMessagesRequestMessagesItem],
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
                _data = typing.cast(
                    FeedsPublishMessagesResponse,
                    parse_obj_as(
                        type_=FeedsPublishMessagesResponse,
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

    async def getmessage(
        self, feed_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeedsGetMessageResponse]:
        """
        Get full content of a feed message

        Parameters
        ----------
        feed_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsGetMessageResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsGetMessageResponse,
                    parse_obj_as(
                        type_=FeedsGetMessageResponse,
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

    async def subscribeagent(
        self,
        feed_id: str,
        *,
        agent_id: str,
        cron_schedule: str,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsSubscribeAgentResponse]:
        """
        Subscribe an agent to a feed with polling configuration

        Parameters
        ----------
        feed_id : str

        agent_id : str

        cron_schedule : str

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsSubscribeAgentResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscribe",
            method="POST",
            json={
                "agent_id": agent_id,
                "cron_schedule": cron_schedule,
                "prompt_template": prompt_template,
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
                    FeedsSubscribeAgentResponse,
                    parse_obj_as(
                        type_=FeedsSubscribeAgentResponse,
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

    async def deletesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        request: typing.Optional[FeedsDeleteSubscriptionRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsDeleteSubscriptionResponse]:
        """
        Remove agent subscription from a feed (by subscription_id)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request : typing.Optional[FeedsDeleteSubscriptionRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsDeleteSubscriptionResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[FeedsDeleteSubscriptionRequestBody], direction="write"
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
                    FeedsDeleteSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsDeleteSubscriptionResponse,
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

    async def updatesubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsUpdateSubscriptionResponse]:
        """
        Update subscription configuration (cron schedule, enable/disable)

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsUpdateSubscriptionResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}",
            method="PATCH",
            json={
                "cron_schedule": cron_schedule,
                "prompt_template": prompt_template,
                "disabled": disabled,
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
                    FeedsUpdateSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsUpdateSubscriptionResponse,
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

    async def unsubscribeagent(
        self, feed_id: str, *, agent_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeedsUnsubscribeAgentResponse]:
        """
        Remove agent subscription from a feed (by agent_id)

        Parameters
        ----------
        feed_id : str

        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsUnsubscribeAgentResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/unsubscribe",
            method="POST",
            json={
                "agent_id": agent_id,
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
                    FeedsUnsubscribeAgentResponse,
                    parse_obj_as(
                        type_=FeedsUnsubscribeAgentResponse,
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

    async def triggersubscription(
        self, feed_id: str, subscription_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeedsTriggerSubscriptionResponse]:
        """
        Immediately trigger a subscription to process pending messages

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsTriggerSubscriptionResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/trigger",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsTriggerSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsTriggerSubscriptionResponse,
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

    async def backfillsubscription(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        from_sequence: typing.Optional[float] = OMIT,
        to_sequence: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsBackfillSubscriptionResponse]:
        """
        Start a background job to send historical messages to an agent subscription. Returns immediately with workflow ID. Does not update last_consumed_sequence.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        from_sequence : typing.Optional[float]

        to_sequence : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsBackfillSubscriptionResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/backfill",
            method="POST",
            json={
                "from_sequence": from_sequence,
                "to_sequence": to_sequence,
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
                    FeedsBackfillSubscriptionResponse,
                    parse_obj_as(
                        type_=FeedsBackfillSubscriptionResponse,
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

    async def listsubscriptionhistory(
        self,
        feed_id: str,
        subscription_id: str,
        *,
        page_size: typing.Optional[str] = None,
        next_page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsListSubscriptionHistoryResponse]:
        """
        List the run history for a subscription including scheduled runs, manual triggers, and backfills.

        Parameters
        ----------
        feed_id : str

        subscription_id : str

        page_size : typing.Optional[str]

        next_page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsListSubscriptionHistoryResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/{encode_path_param(subscription_id)}/history",
            method="GET",
            params={
                "page_size": page_size,
                "next_page_token": next_page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListSubscriptionHistoryResponse,
                    parse_obj_as(
                        type_=FeedsListSubscriptionHistoryResponse,
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

    async def updateallsubscriptionscron(
        self, feed_id: str, *, cron_schedule: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FeedsUpdateAllSubscriptionsCronResponse]:
        """
        Update the cron schedule for all subscriptions of a feed

        Parameters
        ----------
        feed_id : str

        cron_schedule : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsUpdateAllSubscriptionsCronResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions/cron",
            method="PATCH",
            json={
                "cron_schedule": cron_schedule,
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
                    FeedsUpdateAllSubscriptionsCronResponse,
                    parse_obj_as(
                        type_=FeedsUpdateAllSubscriptionsCronResponse,
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

    async def listsubscriptions(
        self,
        feed_id: str,
        *,
        limit: typing.Optional[str] = None,
        offset: typing.Optional[FeedsListSubscriptionsRequestOffset] = None,
        agent_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedsListSubscriptionsResponse]:
        """
        List all agent subscriptions for a feed

        Parameters
        ----------
        feed_id : str

        limit : typing.Optional[str]

        offset : typing.Optional[FeedsListSubscriptionsRequestOffset]

        agent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedsListSubscriptionsResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/feeds/{encode_path_param(feed_id)}/subscriptions",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "agent_id": agent_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FeedsListSubscriptionsResponse,
                    parse_obj_as(
                        type_=FeedsListSubscriptionsResponse,
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
