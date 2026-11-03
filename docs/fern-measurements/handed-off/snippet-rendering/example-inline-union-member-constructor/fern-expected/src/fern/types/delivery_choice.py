

import typing

from .delivery_choice_one import DeliveryChoiceOne
from .delivery_choice_zero import DeliveryChoiceZero

DeliveryChoice = typing.Union[DeliveryChoiceZero, DeliveryChoiceOne]
