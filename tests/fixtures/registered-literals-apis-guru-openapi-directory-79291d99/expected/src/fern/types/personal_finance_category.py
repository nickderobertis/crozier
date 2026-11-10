

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PersonalFinanceCategory(UniversalBaseModel):
    """
    Information describing the intent of the transaction. Most relevant for personal finance use cases, but not limited to such use cases.

    See the [`taxonomy csv file`](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.
    """

    detailed: str = pydantic.Field()
    """
    A granular category conveying the transaction's intent. This field can also be used as a unique identifier for the category.
    """

    primary: str = pydantic.Field()
    """
    A high level category that communicates the broad category of the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
