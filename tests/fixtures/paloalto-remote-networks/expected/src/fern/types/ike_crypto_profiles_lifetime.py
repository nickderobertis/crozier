

import typing

from .ike_crypto_profiles_lifetime_days import IkeCryptoProfilesLifetimeDays
from .ike_crypto_profiles_lifetime_hours import IkeCryptoProfilesLifetimeHours
from .ike_crypto_profiles_lifetime_minutes import IkeCryptoProfilesLifetimeMinutes
from .ike_crypto_profiles_lifetime_seconds import IkeCryptoProfilesLifetimeSeconds

IkeCryptoProfilesLifetime = typing.Union[
    IkeCryptoProfilesLifetimeSeconds,
    IkeCryptoProfilesLifetimeMinutes,
    IkeCryptoProfilesLifetimeHours,
    IkeCryptoProfilesLifetimeDays,
]
