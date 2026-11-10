

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_party_voa24 import CreditFreddieMacPartyVoa24


class CreditFreddieMacPartiesVoa24(UniversalBaseModel):
    """
    A collection of objects that define specific parties to a deal. This includes the direct participating parties, such as borrower and seller and the indirect parties such as the credit report provider.
    """

    party: typing_extensions.Annotated[
        typing.List[CreditFreddieMacPartyVoa24], FieldMetadata(alias="PARTY"), pydantic.Field(alias="PARTY")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
