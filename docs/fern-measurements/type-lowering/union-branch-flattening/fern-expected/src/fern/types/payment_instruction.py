

import typing

from .ach_instruction import AchInstruction
from .iban_instruction import IbanInstruction

PaymentInstruction = typing.Union[IbanInstruction, AchInstruction]
