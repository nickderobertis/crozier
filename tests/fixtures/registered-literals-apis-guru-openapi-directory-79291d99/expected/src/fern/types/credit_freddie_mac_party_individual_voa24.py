

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_individual_name_voa24 import CreditFreddieMacIndividualNameVoa24


class CreditFreddieMacPartyIndividualVoa24(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    name: typing_extensions.Annotated[
        CreditFreddieMacIndividualNameVoa24, FieldMetadata(alias="NAME"), pydantic.Field(alias="NAME")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
