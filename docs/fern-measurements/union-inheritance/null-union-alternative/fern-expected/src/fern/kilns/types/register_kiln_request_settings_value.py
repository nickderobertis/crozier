

import typing

from .register_kiln_request_settings_value_one_item import RegisterKilnRequestSettingsValueOneItem
from .register_kiln_request_settings_value_zero import RegisterKilnRequestSettingsValueZero

RegisterKilnRequestSettingsValue = typing.Union[
    typing.Optional[RegisterKilnRequestSettingsValueZero],
    typing.List[typing.Optional[RegisterKilnRequestSettingsValueOneItem]],
]
