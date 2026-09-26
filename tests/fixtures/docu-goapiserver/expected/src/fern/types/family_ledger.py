

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .family_transaction import FamilyTransaction


class FamilyLedger(UniversalBaseModel):
    """
    Family Ledger.
    """

    family_id: str = pydantic.Field()
    """
    Family id.
    """

    student_ids: typing.Optional[typing.List[str]] = None
    transactions: typing.Optional[typing.List[FamilyTransaction]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
