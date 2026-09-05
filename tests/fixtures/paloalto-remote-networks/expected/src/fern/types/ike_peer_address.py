

import typing

from .ike_peer_address_dynamic import IkePeerAddressDynamic
from .ike_peer_address_fqdn import IkePeerAddressFqdn
from .ike_peer_address_ip import IkePeerAddressIp

IkePeerAddress = typing.Union[IkePeerAddressIp, IkePeerAddressFqdn, IkePeerAddressDynamic]
