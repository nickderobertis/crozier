

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreditSessionDocumentIncomeResult(UniversalBaseModel):
    """
    The details of a document income verification in Link
    """

    num_paystubs_uploaded: int = pydantic.Field()
    """
    The number of paystubs uploaded by the user.
    """

    num_w2s_uploaded: int = pydantic.Field()
    """
    The number of w2s uploaded by the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
