

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_purpose_label import AddressPurposeLabel
from .match_summary_code import MatchSummaryCode
from .po_box_status import PoBoxStatus


class KycCheckAddressSummary(UniversalBaseModel):
    """
    Result summary object specifying how the `address` field matched.
    """

    po_box: PoBoxStatus
    summary: MatchSummaryCode
    type: AddressPurposeLabel

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
