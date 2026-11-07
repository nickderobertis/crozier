

import typing

from .invalid_scenario import InvalidScenario
from .no_sources import NoSources
from .not_supported_by_sources import NotSupportedBySources
from .user_does_not_have_permission import UserDoesNotHavePermission

NotAvailableReason = typing.Union[InvalidScenario, NoSources, NotSupportedBySources, UserDoesNotHavePermission]
