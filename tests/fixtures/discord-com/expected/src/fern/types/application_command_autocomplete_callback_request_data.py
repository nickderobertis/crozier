

import typing

from .interaction_application_command_autocomplete_callback_integer_data import (
    InteractionApplicationCommandAutocompleteCallbackIntegerData,
)
from .interaction_application_command_autocomplete_callback_number_data import (
    InteractionApplicationCommandAutocompleteCallbackNumberData,
)
from .interaction_application_command_autocomplete_callback_string_data import (
    InteractionApplicationCommandAutocompleteCallbackStringData,
)

ApplicationCommandAutocompleteCallbackRequestData = typing.Union[
    InteractionApplicationCommandAutocompleteCallbackIntegerData,
    InteractionApplicationCommandAutocompleteCallbackNumberData,
    InteractionApplicationCommandAutocompleteCallbackStringData,
]
