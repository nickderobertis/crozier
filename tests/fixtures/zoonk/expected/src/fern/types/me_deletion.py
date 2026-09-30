

import typing

from .me_deletion_apple_credentials import MeDeletionAppleCredentials
from .me_deletion_email_credentials import MeDeletionEmailCredentials
from .me_deletion_zero import MeDeletionZero

MeDeletion = typing.Union[MeDeletionZero, MeDeletionAppleCredentials, MeDeletionEmailCredentials]
