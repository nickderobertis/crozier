

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawWebhookEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def webhook_event_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        This is a documentation-only endpoint describing the webhook event payloads.

        When you subscribe to webhook events, Timely will send HTTP POST requests to your configured URL with the following payloads:

        | Event | Payload Schema |
        |-------|----------------|
        | `hours:created` | Hour |
        | `hours:updated` | Hour |
        | `hours:deleted` | Hour |
        | `projects:created` | Project |
        | `projects:updated` | Project |
        | `projects:deleted` | Project |
        | `labels:created` | Label |
        | `labels:updated` | Label |
        | `labels:deleted` | Label |
        | `forecasts:created` | Forecast |
        | `forecasts:updated` | Forecast |
        | `forecasts:deleted` | Forecast |

        See the webhook events below for the exact payload schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhook-events",
            method="GET",
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


class AsyncRawWebhookEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def webhook_event_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        This is a documentation-only endpoint describing the webhook event payloads.

        When you subscribe to webhook events, Timely will send HTTP POST requests to your configured URL with the following payloads:

        | Event | Payload Schema |
        |-------|----------------|
        | `hours:created` | Hour |
        | `hours:updated` | Hour |
        | `hours:deleted` | Hour |
        | `projects:created` | Project |
        | `projects:updated` | Project |
        | `projects:deleted` | Project |
        | `labels:created` | Label |
        | `labels:updated` | Label |
        | `labels:deleted` | Label |
        | `forecasts:created` | Forecast |
        | `forecasts:updated` | Forecast |
        | `forecasts:deleted` | Forecast |

        See the webhook events below for the exact payload schemas.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhook-events",
            method="GET",
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
