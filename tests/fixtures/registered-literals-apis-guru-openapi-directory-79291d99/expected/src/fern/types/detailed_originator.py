

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_diligence_status import TransferDiligenceStatus


class DetailedOriginator(UniversalBaseModel):
    """
    Originator and their status.
    """

    client_id: str = pydantic.Field()
    """
    Originator’s client ID.
    """

    company_name: str
    transfer_diligence_status: TransferDiligenceStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
