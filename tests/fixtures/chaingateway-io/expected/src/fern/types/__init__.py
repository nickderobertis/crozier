



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .cipherparams import Cipherparams
    from .clear_address import ClearAddress
    from .content import Content
    from .crypto import Crypto
    from .delete_address import DeleteAddress
    from .export_address import ExportAddress
    from .failed_ipn import FailedIpn
    from .get_block import GetBlock
    from .get_ethereum_balance import GetEthereumBalance
    from .get_exchange_rate import GetExchangeRate
    from .get_gas_price import GetGasPrice
    from .get_last_block_number import GetLastBlockNumber
    from .get_token import GetToken
    from .get_token_balance import GetTokenBalance
    from .get_transactions import GetTransactions
    from .import_address import ImportAddress
    from .ipn import Ipn
    from .kdfparams import Kdfparams
    from .list_addresses import ListAddresses
    from .list_failed_ip_ns import ListFailedIpNs
    from .list_subscribed_addresses import ListSubscribedAddresses
    from .new_address import NewAddress
    from .resend_failed_ipn import ResendFailedIpn
    from .send_ethereum import SendEthereum
    from .send_token import SendToken
    from .subscribe_address import SubscribeAddress
    from .transaction import Transaction
    from .unsubscribe_address import UnsubscribeAddress
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "Cipherparams": ".cipherparams",
    "ClearAddress": ".clear_address",
    "Content": ".content",
    "Crypto": ".crypto",
    "DeleteAddress": ".delete_address",
    "ExportAddress": ".export_address",
    "FailedIpn": ".failed_ipn",
    "GetBlock": ".get_block",
    "GetEthereumBalance": ".get_ethereum_balance",
    "GetExchangeRate": ".get_exchange_rate",
    "GetGasPrice": ".get_gas_price",
    "GetLastBlockNumber": ".get_last_block_number",
    "GetToken": ".get_token",
    "GetTokenBalance": ".get_token_balance",
    "GetTransactions": ".get_transactions",
    "ImportAddress": ".import_address",
    "Ipn": ".ipn",
    "Kdfparams": ".kdfparams",
    "ListAddresses": ".list_addresses",
    "ListFailedIpNs": ".list_failed_ip_ns",
    "ListSubscribedAddresses": ".list_subscribed_addresses",
    "NewAddress": ".new_address",
    "ResendFailedIpn": ".resend_failed_ipn",
    "SendEthereum": ".send_ethereum",
    "SendToken": ".send_token",
    "SubscribeAddress": ".subscribe_address",
    "Transaction": ".transaction",
    "UnsubscribeAddress": ".unsubscribe_address",
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
    "Cipherparams",
    "ClearAddress",
    "Content",
    "Crypto",
    "DeleteAddress",
    "ExportAddress",
    "FailedIpn",
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
]
