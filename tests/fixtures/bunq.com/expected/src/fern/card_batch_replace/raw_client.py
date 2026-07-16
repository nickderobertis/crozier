

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
from ..types.card_batch_replace_create import CardBatchReplaceCreate
from ..types.card_batch_replace_entry import CardBatchReplaceEntry
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCardBatchReplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_card_batch_replace_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchReplaceEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardBatchReplaceCreate]:
        """
        Used to replace multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchReplaceEntry]
            The cards that need to be replaced.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardBatchReplaceCreate]
            Used to replace multiple cards in a batch.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card-batch-replace",
            method="POST",
            json={
                "cards": convert_and_respect_annotation_metadata(
                    object_=cards, annotation=typing.Sequence[CardBatchReplaceEntry], direction="write"
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
                    CardBatchReplaceCreate,
                    parse_obj_as(
                        type_=CardBatchReplaceCreate,
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


class AsyncRawCardBatchReplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_card_batch_replace_for_user(
        self,
        user_id: int,
        *,
        cards: typing.Sequence[CardBatchReplaceEntry],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardBatchReplaceCreate]:
        """
        Used to replace multiple cards in a batch.

        Parameters
        ----------
        user_id : int


        cards : typing.Sequence[CardBatchReplaceEntry]
            The cards that need to be replaced.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardBatchReplaceCreate]
            Used to replace multiple cards in a batch.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card-batch-replace",
            method="POST",
            json={
                "cards": convert_and_respect_annotation_metadata(
                    object_=cards, annotation=typing.Sequence[CardBatchReplaceEntry], direction="write"
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
                    CardBatchReplaceCreate,
                    parse_obj_as(
                        type_=CardBatchReplaceCreate,
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
