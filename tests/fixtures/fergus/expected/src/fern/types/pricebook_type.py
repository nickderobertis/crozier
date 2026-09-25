

import typing

from .pricebook_type_one import PricebookTypeOne
from .pricebook_type_two import PricebookTypeTwo
from .pricebook_type_zero import PricebookTypeZero

PricebookType = typing.Union[PricebookTypeZero, PricebookTypeOne, PricebookTypeTwo]
