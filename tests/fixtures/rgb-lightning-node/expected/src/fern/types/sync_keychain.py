

import typing

from .sync_keychain_vanilla import SyncKeychainVanilla
from .sync_keychain_zero import SyncKeychainZero

SyncKeychain = typing.Union[SyncKeychainZero, SyncKeychainVanilla]
