

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExtractionUsageTotals(UniversalBaseModel):
    """
    Aggregated customer retail OpenRouter usage for transparency. `cost_usd` is the
    customer charge, not raw provider list cost. Distinct from the customer
    USD $0.001/page (0.1 credits/page) OCR charge recorded by Eigenpal billing.
    """

    input_tokens: typing.Optional[int] = None
    output_tokens: typing.Optional[int] = None
    cost_usd: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
