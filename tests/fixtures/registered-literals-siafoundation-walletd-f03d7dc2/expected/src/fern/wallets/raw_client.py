

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
from ..errors.not_found_error import NotFoundError
from ..types.address import Address
from ..types.balance import Balance
from ..types.currency import Currency
from ..types.event import Event
from ..types.hash256 import Hash256
from ..types.siacoin_output import SiacoinOutput
from ..types.siafund_output import SiafundOutput
from ..types.spend_policy import SpendPolicy
from ..types.transaction import Transaction
from ..types.unspent_siacoin_elements_response import UnspentSiacoinElementsResponse
from ..types.unspent_siafund_elements_response import UnspentSiafundElementsResponse
from ..types.wallet import Wallet
from ..types.wallet_address import WalletAddress
from ..types.wallet_construct_response import WalletConstructResponse
from ..types.wallet_construct_v2response import WalletConstructV2Response
from ..types.wallet_fund_response import WalletFundResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWalletsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Wallet]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Wallet]]
            Wallets registered with walletd.
        """
        _response = self._client_wrapper.httpx_client.request(
            "wallets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Wallet],
                    parse_obj_as(
                        type_=typing.List[Wallet],
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

    def post_wallet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Wallet]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Wallet]
            Wallet created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "wallets",
            method="POST",
            json={
                "name": name,
                "description": description,
                "metadata": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Wallet,
                    parse_obj_as(
                        type_=Wallet,
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

    def post_wallet_by_id(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Wallet]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Wallet]
            Wallet updated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}",
            method="POST",
            json={
                "name": name,
                "description": description,
                "metadata": metadata,
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
                    Wallet,
                    parse_obj_as(
                        type_=Wallet,
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

    def delete_wallet_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def get_wallet_addresses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WalletAddress]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WalletAddress]]
            Addresses assigned to the wallet.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WalletAddress],
                    parse_obj_as(
                        type_=typing.List[WalletAddress],
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

    def put_wallet_address(
        self,
        id: int,
        *,
        address: Address,
        description: str,
        spend_policy: typing.Optional[SpendPolicy] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        address : Address

        description : str

        spend_policy : typing.Optional[SpendPolicy]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses",
            method="PUT",
            json={
                "address": address,
                "description": description,
                "spendPolicy": convert_and_respect_annotation_metadata(
                    object_=spend_policy, annotation=SpendPolicy, direction="write"
                ),
                "metadata": metadata,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_wallet_batch_addresses(
        self,
        id: int,
        *,
        request: typing.Sequence[WalletAddress],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request : typing.Sequence[WalletAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/batch/addresses",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[WalletAddress], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def delete_wallet_address(
        self, id: int, addr: Address, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        addr : Address
            Sia address (unlock hash).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses/{encode_path_param(addr)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def get_wallet_balance(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Balance]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Balance]
            Wallet balance with immature breakdown.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Balance,
                    parse_obj_as(
                        type_=Balance,
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

    def get_wallet_events(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 500).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Event]]
            Events relevant to the wallet.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/events",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    def get_wallet_events_unconfirmed(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Event]]
            Unconfirmed events referencing the wallet.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/events/unconfirmed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    def get_wallet_siacoin_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnspentSiacoinElementsResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnspentSiacoinElementsResponse]
            Unspent siacoin elements tracked by the wallet.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/outputs/siacoin",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnspentSiacoinElementsResponse,
                    parse_obj_as(
                        type_=UnspentSiacoinElementsResponse,
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

    def get_wallet_siafund_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnspentSiafundElementsResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnspentSiafundElementsResponse]
            Unspent siafund elements tracked by the wallet.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/outputs/siafund",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnspentSiafundElementsResponse,
                    parse_obj_as(
                        type_=UnspentSiafundElementsResponse,
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

    def post_wallet_reserve(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/reserve",
            method="POST",
            json={
                "siacoinOutputs": siacoin_outputs,
                "siafundOutputs": siafund_outputs,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_wallet_release(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/release",
            method="POST",
            json={
                "siacoinOutputs": siacoin_outputs,
                "siafundOutputs": siafund_outputs,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_wallet_fund(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: Currency,
        change_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WalletFundResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : Currency

        change_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WalletFundResponse]
            Transaction funded and inputs listed for signing.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/fund",
            method="POST",
            json={
                "transaction": convert_and_respect_annotation_metadata(
                    object_=transaction, annotation=Transaction, direction="write"
                ),
                "amount": amount,
                "changeAddress": change_address,
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
                    WalletFundResponse,
                    parse_obj_as(
                        type_=WalletFundResponse,
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

    def post_wallet_fund_siafunds(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: int,
        change_address: typing.Optional[Address] = OMIT,
        claim_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WalletFundResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : int

        change_address : typing.Optional[Address]

        claim_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WalletFundResponse]
            Transaction funded with siafund inputs.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/fundsf",
            method="POST",
            json={
                "transaction": convert_and_respect_annotation_metadata(
                    object_=transaction, annotation=Transaction, direction="write"
                ),
                "amount": amount,
                "changeAddress": change_address,
                "claimAddress": claim_address,
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
                    WalletFundResponse,
                    parse_obj_as(
                        type_=WalletFundResponse,
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

    def post_wallet_construct_transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WalletConstructResponse]:
        """
        Selects wallet-managed UTXOs, adds change outputs as needed, and returns a fully-formed v1 transaction with signature placeholders.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WalletConstructResponse]
            Constructed v1 transaction and metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/construct/transaction",
            method="POST",
            json={
                "siacoins": convert_and_respect_annotation_metadata(
                    object_=siacoins, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "siafunds": convert_and_respect_annotation_metadata(
                    object_=siafunds, annotation=typing.Sequence[SiafundOutput], direction="write"
                ),
                "changeAddress": change_address,
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
                    WalletConstructResponse,
                    parse_obj_as(
                        type_=WalletConstructResponse,
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

    def post_wallet_construct_v2transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WalletConstructV2Response]:
        """
        Builds a v2 transaction using wallet-managed UTXOs and optional outputs. Walletd fills in satisfied spend policies and updates proofs to the latest basis.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WalletConstructV2Response]
            Constructed v2 transaction and metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/construct/v2/transaction",
            method="POST",
            json={
                "siacoins": convert_and_respect_annotation_metadata(
                    object_=siacoins, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "siafunds": convert_and_respect_annotation_metadata(
                    object_=siafunds, annotation=typing.Sequence[SiafundOutput], direction="write"
                ),
                "changeAddress": change_address,
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
                    WalletConstructV2Response,
                    parse_obj_as(
                        type_=WalletConstructV2Response,
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


class AsyncRawWalletsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Wallet]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Wallet]]
            Wallets registered with walletd.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wallets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Wallet],
                    parse_obj_as(
                        type_=typing.List[Wallet],
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

    async def post_wallet(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Wallet]:
        """
        Parameters
        ----------
        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Wallet]
            Wallet created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "wallets",
            method="POST",
            json={
                "name": name,
                "description": description,
                "metadata": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Wallet,
                    parse_obj_as(
                        type_=Wallet,
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

    async def post_wallet_by_id(
        self,
        id: int,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Wallet]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        name : typing.Optional[str]

        description : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Wallet]
            Wallet updated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}",
            method="POST",
            json={
                "name": name,
                "description": description,
                "metadata": metadata,
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
                    Wallet,
                    parse_obj_as(
                        type_=Wallet,
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

    async def delete_wallet_by_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_wallet_addresses(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WalletAddress]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WalletAddress]]
            Addresses assigned to the wallet.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WalletAddress],
                    parse_obj_as(
                        type_=typing.List[WalletAddress],
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

    async def put_wallet_address(
        self,
        id: int,
        *,
        address: Address,
        description: str,
        spend_policy: typing.Optional[SpendPolicy] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        address : Address

        description : str

        spend_policy : typing.Optional[SpendPolicy]

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses",
            method="PUT",
            json={
                "address": address,
                "description": description,
                "spendPolicy": convert_and_respect_annotation_metadata(
                    object_=spend_policy, annotation=SpendPolicy, direction="write"
                ),
                "metadata": metadata,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_wallet_batch_addresses(
        self,
        id: int,
        *,
        request: typing.Sequence[WalletAddress],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request : typing.Sequence[WalletAddress]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/batch/addresses",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[WalletAddress], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def delete_wallet_address(
        self, id: int, addr: Address, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        addr : Address
            Sia address (unlock hash).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/addresses/{encode_path_param(addr)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_wallet_balance(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Balance]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Balance]
            Wallet balance with immature breakdown.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/balance",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Balance,
                    parse_obj_as(
                        type_=Balance,
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

    async def get_wallet_events(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 500).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Event]]
            Events relevant to the wallet.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/events",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    async def get_wallet_events_unconfirmed(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Event]]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Event]]
            Unconfirmed events referencing the wallet.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/events/unconfirmed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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

    async def get_wallet_siacoin_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnspentSiacoinElementsResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnspentSiacoinElementsResponse]
            Unspent siacoin elements tracked by the wallet.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/outputs/siacoin",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnspentSiacoinElementsResponse,
                    parse_obj_as(
                        type_=UnspentSiacoinElementsResponse,
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

    async def get_wallet_siafund_outputs(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnspentSiafundElementsResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        offset : typing.Optional[int]
            Number of items to skip.

        limit : typing.Optional[int]
            Maximum number of items to return (default 1000).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnspentSiafundElementsResponse]
            Unspent siafund elements tracked by the wallet.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/outputs/siafund",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnspentSiafundElementsResponse,
                    parse_obj_as(
                        type_=UnspentSiafundElementsResponse,
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

    async def post_wallet_reserve(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/reserve",
            method="POST",
            json={
                "siacoinOutputs": siacoin_outputs,
                "siafundOutputs": siafund_outputs,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_wallet_release(
        self,
        id: int,
        *,
        siacoin_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[Hash256]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        siacoin_outputs : typing.Optional[typing.Sequence[Hash256]]

        siafund_outputs : typing.Optional[typing.Sequence[Hash256]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/release",
            method="POST",
            json={
                "siacoinOutputs": siacoin_outputs,
                "siafundOutputs": siafund_outputs,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_wallet_fund(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: Currency,
        change_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WalletFundResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : Currency

        change_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WalletFundResponse]
            Transaction funded and inputs listed for signing.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/fund",
            method="POST",
            json={
                "transaction": convert_and_respect_annotation_metadata(
                    object_=transaction, annotation=Transaction, direction="write"
                ),
                "amount": amount,
                "changeAddress": change_address,
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
                    WalletFundResponse,
                    parse_obj_as(
                        type_=WalletFundResponse,
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

    async def post_wallet_fund_siafunds(
        self,
        id: int,
        *,
        transaction: Transaction,
        amount: int,
        change_address: typing.Optional[Address] = OMIT,
        claim_address: typing.Optional[Address] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WalletFundResponse]:
        """
        Parameters
        ----------
        id : int
            Wallet identifier.

        transaction : Transaction

        amount : int

        change_address : typing.Optional[Address]

        claim_address : typing.Optional[Address]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WalletFundResponse]
            Transaction funded with siafund inputs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/fundsf",
            method="POST",
            json={
                "transaction": convert_and_respect_annotation_metadata(
                    object_=transaction, annotation=Transaction, direction="write"
                ),
                "amount": amount,
                "changeAddress": change_address,
                "claimAddress": claim_address,
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
                    WalletFundResponse,
                    parse_obj_as(
                        type_=WalletFundResponse,
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

    async def post_wallet_construct_transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WalletConstructResponse]:
        """
        Selects wallet-managed UTXOs, adds change outputs as needed, and returns a fully-formed v1 transaction with signature placeholders.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WalletConstructResponse]
            Constructed v1 transaction and metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/construct/transaction",
            method="POST",
            json={
                "siacoins": convert_and_respect_annotation_metadata(
                    object_=siacoins, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "siafunds": convert_and_respect_annotation_metadata(
                    object_=siafunds, annotation=typing.Sequence[SiafundOutput], direction="write"
                ),
                "changeAddress": change_address,
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
                    WalletConstructResponse,
                    parse_obj_as(
                        type_=WalletConstructResponse,
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

    async def post_wallet_construct_v2transaction(
        self,
        id: int,
        *,
        change_address: Address,
        siacoins: typing.Optional[typing.Sequence[SiacoinOutput]] = OMIT,
        siafunds: typing.Optional[typing.Sequence[SiafundOutput]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WalletConstructV2Response]:
        """
        Builds a v2 transaction using wallet-managed UTXOs and optional outputs. Walletd fills in satisfied spend policies and updates proofs to the latest basis.

        Parameters
        ----------
        id : int
            Wallet identifier.

        change_address : Address

        siacoins : typing.Optional[typing.Sequence[SiacoinOutput]]

        siafunds : typing.Optional[typing.Sequence[SiafundOutput]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WalletConstructV2Response]
            Constructed v2 transaction and metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wallets/{encode_path_param(id)}/construct/v2/transaction",
            method="POST",
            json={
                "siacoins": convert_and_respect_annotation_metadata(
                    object_=siacoins, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "siafunds": convert_and_respect_annotation_metadata(
                    object_=siafunds, annotation=typing.Sequence[SiafundOutput], direction="write"
                ),
                "changeAddress": change_address,
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
                    WalletConstructV2Response,
                    parse_obj_as(
                        type_=WalletConstructV2Response,
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
