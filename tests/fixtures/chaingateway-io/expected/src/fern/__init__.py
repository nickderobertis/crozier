



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Address,
        Cipherparams,
        ClearAddress,
        Content,
        Crypto,
        DeleteAddress,
        ExportAddress,
        FailedIpn,
        GetBlock,
        GetEthereumBalance,
        GetExchangeRate,
        GetGasPrice,
        GetLastBlockNumber,
        GetToken,
        GetTokenBalance,
        GetTransactions,
        ImportAddress,
        Ipn,
        Kdfparams,
        ListAddresses,
        ListFailedIpNs,
        ListSubscribedAddresses,
        NewAddress,
        ResendFailedIpn,
        SendEthereum,
        SendToken,
        SubscribeAddress,
        Transaction,
        UnsubscribeAddress,
    )
    from . import address_requests, info_requests, subscription_ipn_requests, transaction_requests
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".types",
    "AsyncFernApi": ".client",
    "Cipherparams": ".types",
    "ClearAddress": ".types",
    "Content": ".types",
    "Crypto": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeleteAddress": ".types",
    "ExportAddress": ".types",
    "FailedIpn": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetBlock": ".types",
    "GetEthereumBalance": ".types",
    "GetExchangeRate": ".types",
    "GetGasPrice": ".types",
    "GetLastBlockNumber": ".types",
    "GetToken": ".types",
    "GetTokenBalance": ".types",
    "GetTransactions": ".types",
    "ImportAddress": ".types",
    "Ipn": ".types",
    "Kdfparams": ".types",
    "ListAddresses": ".types",
    "ListFailedIpNs": ".types",
    "ListSubscribedAddresses": ".types",
    "NewAddress": ".types",
    "ResendFailedIpn": ".types",
    "SendEthereum": ".types",
    "SendToken": ".types",
    "SubscribeAddress": ".types",
    "Transaction": ".types",
    "UnsubscribeAddress": ".types",
    "__version__": ".version",
    "address_requests": ".address_requests",
    "info_requests": ".info_requests",
    "subscription_ipn_requests": ".subscription_ipn_requests",
    "transaction_requests": ".transaction_requests",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Address",
    "AsyncFernApi",
    "Cipherparams",
    "ClearAddress",
    "Content",
    "Crypto",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeleteAddress",
    "ExportAddress",
    "FailedIpn",
    "FernApi",
    "FernApiEnvironment",
    "GetBlock",
    "GetEthereumBalance",
    "GetExchangeRate",
    "GetGasPrice",
    "GetLastBlockNumber",
    "GetToken",
    "GetTokenBalance",
    "GetTransactions",
    "ImportAddress",
    "Ipn",
    "Kdfparams",
    "ListAddresses",
    "ListFailedIpNs",
    "ListSubscribedAddresses",
    "NewAddress",
    "ResendFailedIpn",
    "SendEthereum",
    "SendToken",
    "SubscribeAddress",
    "Transaction",
    "UnsubscribeAddress",
    "__version__",
    "address_requests",
    "info_requests",
    "subscription_ipn_requests",
    "transaction_requests",
]
