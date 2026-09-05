

import typing

from .ipsec_crypto import IpsecCrypto
from .ipsec_crypto_profiles import IpsecCryptoProfiles

IpsecTunnelCrypto = typing.Union[IpsecCryptoProfiles, IpsecCrypto]
