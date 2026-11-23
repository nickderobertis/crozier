

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.action_result import ActionResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_action(
        self,
        *,
        action: str,
        kiln_token: typing.Optional[str] = None,
        run_action_request_kiln_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ActionResult]:
        """
        Parameters
        ----------
        action : str

        kiln_token : typing.Optional[str]

        run_action_request_kiln_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionResult]
            Ran.
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/run",
            method="POST",
            json={
                "action": action,
                "kilnToken": run_action_request_kiln_token,
            },
            headers={
                "content-type": "application/json",
                "kilnToken": str(kiln_token) if kiln_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    def queue_action(
        self,
        *,
        batch_label: str,
        action: str,
        queue_action_request_batch_label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ActionResult]:
        """
        Parameters
        ----------
        batch_label : str

        action : str

        queue_action_request_batch_label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionResult]
            Queued.
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/queue",
            method="POST",
            json={
                "action": action,
                "batchLabel": queue_action_request_batch_label,
            },
            headers={
                "content-type": "application/json",
                "batchLabel": str(batch_label) if batch_label is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    def run_action_batch(
        self,
        *,
        actions: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        action_batch_request_idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ActionResult]:
        """
        Parameters
        ----------
        actions : typing.Sequence[str]

        idempotency_key : typing.Optional[str]

        action_batch_request_idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionResult]
            Ran.
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/batch",
            method="POST",
            json={
                "actions": actions,
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    def preview_action_batch(
        self,
        *,
        actions: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ActionResult]:
        """
        Parameters
        ----------
        actions : typing.Sequence[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActionResult]
            Previewed.
        """
        _response = self._client_wrapper.httpx_client.request(
            "actions/batch/preview",
            method="POST",
            json={
                "actions": actions,
                "idempotency_key": idempotency_key,
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
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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


class AsyncRawActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_action(
        self,
        *,
        action: str,
        kiln_token: typing.Optional[str] = None,
        run_action_request_kiln_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ActionResult]:
        """
        Parameters
        ----------
        action : str

        kiln_token : typing.Optional[str]

        run_action_request_kiln_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionResult]
            Ran.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/run",
            method="POST",
            json={
                "action": action,
                "kilnToken": run_action_request_kiln_token,
            },
            headers={
                "content-type": "application/json",
                "kilnToken": str(kiln_token) if kiln_token is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    async def queue_action(
        self,
        *,
        batch_label: str,
        action: str,
        queue_action_request_batch_label: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ActionResult]:
        """
        Parameters
        ----------
        batch_label : str

        action : str

        queue_action_request_batch_label : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionResult]
            Queued.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/queue",
            method="POST",
            json={
                "action": action,
                "batchLabel": queue_action_request_batch_label,
            },
            headers={
                "content-type": "application/json",
                "batchLabel": str(batch_label) if batch_label is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    async def run_action_batch(
        self,
        *,
        actions: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = None,
        action_batch_request_idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ActionResult]:
        """
        Parameters
        ----------
        actions : typing.Sequence[str]

        idempotency_key : typing.Optional[str]

        action_batch_request_idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionResult]
            Ran.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/batch",
            method="POST",
            json={
                "actions": actions,
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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

    async def preview_action_batch(
        self,
        *,
        actions: typing.Sequence[str],
        idempotency_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ActionResult]:
        """
        Parameters
        ----------
        actions : typing.Sequence[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActionResult]
            Previewed.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "actions/batch/preview",
            method="POST",
            json={
                "actions": actions,
                "idempotency_key": idempotency_key,
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
                    ActionResult,
                    parse_obj_as(
                        type_=ActionResult,
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
