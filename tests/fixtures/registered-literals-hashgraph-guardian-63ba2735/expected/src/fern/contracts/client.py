

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contract_dto import ContractDto
from ..types.date import Date
from ..types.retire_pool_dto import RetirePoolDto
from ..types.retire_request_dto import RetireRequestDto
from ..types.wiper_request_dto import WiperRequestDto
from .raw_client import AsyncRawContractsClient, RawContractsClient
from .types.contracts_api_get_contracts_request_type import ContractsApiGetContractsRequestType


OMIT = typing.cast(typing.Any, ...)


class ContractsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawContractsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawContractsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawContractsClient
        """
        return self._raw_client

    def contracts_api_get_contracts(
        self,
        *,
        type: typing.Optional[ContractsApiGetContractsRequestType] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ContractDto]:
        """
        Returns all contracts.

        Parameters
        ----------
        type : typing.Optional[ContractsApiGetContractsRequestType]
            Contract type

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContractDto]
            Contracts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_get_contracts()
        """
        _response = self._raw_client.contracts_api_get_contracts(
            type=type, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    def contracts_api_create_contract(
        self, *, description: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ContractDto:
        """
        Create smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractDto
            Created contract.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_create_contract()
        """
        _response = self._raw_client.contracts_api_create_contract(
            description=description, request_options=request_options
        )
        return _response.data

    def contracts_api_import_contract(
        self,
        *,
        contract_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContractDto:
        """
        Import smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Hedera Identifier

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractDto
            Imported contract.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_import_contract(
            contract_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_import_contract(
            contract_id=contract_id, description=description, request_options=request_options
        )
        return _response.data

    def contracts_api_contract_permissions(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Get smart-contract permissions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Contract permissions.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_contract_permissions(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_contract_permissions(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_remove_contract(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Remove smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_remove_contract(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_remove_contract(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_get_wipe_requests(
        self,
        *,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WiperRequestDto]:
        """
        Returns all wipe requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WiperRequestDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_get_wipe_requests(
            contract_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_get_wipe_requests(
            contract_id=contract_id, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    def contracts_api_enable_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_enable_wipe_requests(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_enable_wipe_requests(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_disable_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_disable_wipe_requests(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_disable_wipe_requests(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_approve_wipe_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Approve wipe contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_approve_wipe_request(
            request_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_approve_wipe_request(request_id, request_options=request_options)
        return _response.data

    def contracts_api_reject_wipe_request(
        self,
        request_id: str,
        *,
        ban: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reject wipe contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        ban : typing.Optional[bool]
            Reject and ban

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_reject_wipe_request(
            request_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_reject_wipe_request(
            request_id, ban=ban, request_options=request_options
        )
        return _response.data

    def contracts_api_clear_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Clear wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_clear_wipe_requests(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_clear_wipe_requests(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_wipe_add_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_add_admin(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_add_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_wipe_remove_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_remove_admin(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_remove_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_wipe_add_manager(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract manager. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_add_manager(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_add_manager(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_wipe_remove_manager(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_remove_manager(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_remove_manager(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_wipe_add_wiper(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract wiper. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_add_wiper(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_add_wiper(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_wipe_remove_wiper(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_wipe_remove_wiper(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_wipe_remove_wiper(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_retire_sync_pools(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Date:
        """
        Sync retire contract pools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Date
            Sync date.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_retire_sync_pools(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_retire_sync_pools(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_get_retire_requests(
        self,
        *,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RetireRequestDto]:
        """
        Returns all retire requests.

        Parameters
        ----------
        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetireRequestDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_get_retire_requests(
            contract_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_get_retire_requests(
            contract_id=contract_id, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    def contracts_api_get_retire_pools(
        self,
        *,
        tokens: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RetirePoolDto]:
        """
        Returns all retire pools.

        Parameters
        ----------
        tokens : typing.Optional[str]
            Tokens

        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetirePoolDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_get_retire_pools(
            tokens="0.0.1,0.0.2,0.0.3",
            contract_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_get_retire_pools(
            tokens=tokens,
            contract_id=contract_id,
            page_size=page_size,
            page_index=page_index,
            request_options=request_options,
        )
        return _response.data

    def contracts_api_clear_retire_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear retire contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_clear_retire_requests(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_clear_retire_requests(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_set_retire_pool(
        self, contract_id: str, *, token: str, count: float, request_options: typing.Optional[RequestOptions] = None
    ) -> RetirePoolDto:
        """
        Set retire contract pool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        token : str

        count : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetirePoolDto
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_set_retire_pool(
            contract_id="652745597a7b53526de37c05",
            token="token",
            count=1.1,
        )
        """
        _response = self._raw_client.contracts_api_set_retire_pool(
            contract_id, token=token, count=count, request_options=request_options
        )
        return _response.data

    def contracts_api_clear_retire_pools(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear retire contract pools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_clear_retire_pools(
            contract_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_clear_retire_pools(contract_id, request_options=request_options)
        return _response.data

    def contracts_api_unset_retire_pool(
        self, pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Unset retire contract pool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        pool_id : str
            Pool Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_unset_retire_pool(
            pool_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_unset_retire_pool(pool_id, request_options=request_options)
        return _response.data

    def contracts_api_unset_retire_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Unset retire contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_unset_retire_request(
            request_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_unset_retire_request(request_id, request_options=request_options)
        return _response.data

    def contracts_api_retire(
        self,
        pool_id: str,
        *,
        token: str,
        count: float,
        serials: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Retire tokens.

        Parameters
        ----------
        pool_id : str
            Pool Identifier

        token : str

        count : float

        serials : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_retire(
            pool_id="652745597a7b53526de37c05",
            token="token",
            count=1.1,
            serials=["serials"],
        )
        """
        _response = self._raw_client.contracts_api_retire(
            pool_id, token=token, count=count, serials=serials, request_options=request_options
        )
        return _response.data

    def contracts_api_approve_retire(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Approve retire contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_approve_retire(
            request_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_approve_retire(request_id, request_options=request_options)
        return _response.data

    def contracts_api_cancel_retire_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancel retire contract request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_cancel_retire_request(
            request_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.contracts_api_cancel_retire_request(request_id, request_options=request_options)
        return _response.data

    def contracts_api_retire_add_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add retire contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_retire_add_admin(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_retire_add_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_retire_remove_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_retire_remove_admin(
            contract_id="652745597a7b53526de37c05",
            hedera_id="0.0.1",
        )
        """
        _response = self._raw_client.contracts_api_retire_remove_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    def contracts_api_get_retire_v_cs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns all retire vcs.

        Parameters
        ----------
        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.contracts.contracts_api_get_retire_v_cs()
        """
        _response = self._raw_client.contracts_api_get_retire_v_cs(
            page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data


class AsyncContractsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawContractsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawContractsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawContractsClient
        """
        return self._raw_client

    async def contracts_api_get_contracts(
        self,
        *,
        type: typing.Optional[ContractsApiGetContractsRequestType] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ContractDto]:
        """
        Returns all contracts.

        Parameters
        ----------
        type : typing.Optional[ContractsApiGetContractsRequestType]
            Contract type

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ContractDto]
            Contracts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_get_contracts()


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_get_contracts(
            type=type, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    async def contracts_api_create_contract(
        self, *, description: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> ContractDto:
        """
        Create smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractDto
            Created contract.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_create_contract()


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_create_contract(
            description=description, request_options=request_options
        )
        return _response.data

    async def contracts_api_import_contract(
        self,
        *,
        contract_id: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContractDto:
        """
        Import smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Hedera Identifier

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContractDto
            Imported contract.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_import_contract(
                contract_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_import_contract(
            contract_id=contract_id, description=description, request_options=request_options
        )
        return _response.data

    async def contracts_api_contract_permissions(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Get smart-contract permissions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Contract permissions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_contract_permissions(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_contract_permissions(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_remove_contract(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Remove smart-contract. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_remove_contract(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_remove_contract(contract_id, request_options=request_options)
        return _response.data

    async def contracts_api_get_wipe_requests(
        self,
        *,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WiperRequestDto]:
        """
        Returns all wipe requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WiperRequestDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_get_wipe_requests(
                contract_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_get_wipe_requests(
            contract_id=contract_id, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    async def contracts_api_enable_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Enable wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_enable_wipe_requests(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_enable_wipe_requests(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_disable_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disable wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_disable_wipe_requests(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_disable_wipe_requests(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_approve_wipe_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Approve wipe contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_approve_wipe_request(
                request_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_approve_wipe_request(
            request_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_reject_wipe_request(
        self,
        request_id: str,
        *,
        ban: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reject wipe contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        ban : typing.Optional[bool]
            Reject and ban

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_reject_wipe_request(
                request_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_reject_wipe_request(
            request_id, ban=ban, request_options=request_options
        )
        return _response.data

    async def contracts_api_clear_wipe_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Clear wipe contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_clear_wipe_requests(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_clear_wipe_requests(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_add_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_add_admin(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_add_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_remove_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_remove_admin(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_remove_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_add_manager(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract manager. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_add_manager(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_add_manager(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_remove_manager(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_remove_manager(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_remove_manager(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_add_wiper(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add wipe contract wiper. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_add_wiper(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_add_wiper(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_wipe_remove_wiper(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_wipe_remove_wiper(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_wipe_remove_wiper(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_retire_sync_pools(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Date:
        """
        Sync retire contract pools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Date
            Sync date.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_retire_sync_pools(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_retire_sync_pools(contract_id, request_options=request_options)
        return _response.data

    async def contracts_api_get_retire_requests(
        self,
        *,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RetireRequestDto]:
        """
        Returns all retire requests.

        Parameters
        ----------
        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetireRequestDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_get_retire_requests(
                contract_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_get_retire_requests(
            contract_id=contract_id, page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data

    async def contracts_api_get_retire_pools(
        self,
        *,
        tokens: typing.Optional[str] = None,
        contract_id: typing.Optional[str] = None,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[RetirePoolDto]:
        """
        Returns all retire pools.

        Parameters
        ----------
        tokens : typing.Optional[str]
            Tokens

        contract_id : typing.Optional[str]
            Contract identifier

        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RetirePoolDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_get_retire_pools(
                tokens="0.0.1,0.0.2,0.0.3",
                contract_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_get_retire_pools(
            tokens=tokens,
            contract_id=contract_id,
            page_size=page_size,
            page_index=page_index,
            request_options=request_options,
        )
        return _response.data

    async def contracts_api_clear_retire_requests(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear retire contract requests. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_clear_retire_requests(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_clear_retire_requests(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_set_retire_pool(
        self, contract_id: str, *, token: str, count: float, request_options: typing.Optional[RequestOptions] = None
    ) -> RetirePoolDto:
        """
        Set retire contract pool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        token : str

        count : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetirePoolDto
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_set_retire_pool(
                contract_id="652745597a7b53526de37c05",
                token="token",
                count=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_set_retire_pool(
            contract_id, token=token, count=count, request_options=request_options
        )
        return _response.data

    async def contracts_api_clear_retire_pools(
        self, contract_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Clear retire contract pools. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_clear_retire_pools(
                contract_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_clear_retire_pools(
            contract_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_unset_retire_pool(
        self, pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Unset retire contract pool. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        pool_id : str
            Pool Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_unset_retire_pool(
                pool_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_unset_retire_pool(pool_id, request_options=request_options)
        return _response.data

    async def contracts_api_unset_retire_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Unset retire contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_unset_retire_request(
                request_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_unset_retire_request(
            request_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_retire(
        self,
        pool_id: str,
        *,
        token: str,
        count: float,
        serials: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Retire tokens.

        Parameters
        ----------
        pool_id : str
            Pool Identifier

        token : str

        count : float

        serials : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_retire(
                pool_id="652745597a7b53526de37c05",
                token="token",
                count=1.1,
                serials=["serials"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_retire(
            pool_id, token=token, count=count, serials=serials, request_options=request_options
        )
        return _response.data

    async def contracts_api_approve_retire(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Approve retire contract request. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_approve_retire(
                request_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_approve_retire(request_id, request_options=request_options)
        return _response.data

    async def contracts_api_cancel_retire_request(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Cancel retire contract request.

        Parameters
        ----------
        request_id : str
            Request identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_cancel_retire_request(
                request_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_cancel_retire_request(
            request_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_retire_add_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add retire contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_retire_add_admin(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_retire_add_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_retire_remove_admin(
        self, contract_id: str, hedera_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove wipe contract admin. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        contract_id : str
            Contract identifier

        hedera_id : str
            Hedera identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_retire_remove_admin(
                contract_id="652745597a7b53526de37c05",
                hedera_id="0.0.1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_retire_remove_admin(
            contract_id, hedera_id, request_options=request_options
        )
        return _response.data

    async def contracts_api_get_retire_v_cs(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_index: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns all retire vcs.

        Parameters
        ----------
        page_size : typing.Optional[float]
            The numbers of items to return

        page_index : typing.Optional[float]
            The number of pages to skip before starting to collect the result set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.contracts.contracts_api_get_retire_v_cs()


        asyncio.run(main())
        """
        _response = await self._raw_client.contracts_api_get_retire_v_cs(
            page_size=page_size, page_index=page_index, request_options=request_options
        )
        return _response.data
