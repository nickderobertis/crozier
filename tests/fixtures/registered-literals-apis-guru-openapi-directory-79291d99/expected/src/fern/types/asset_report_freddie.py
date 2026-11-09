

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .loans import Loans
from .parties import Parties
from .services import Services


class AssetReportFreddie(UniversalBaseModel):
    """
    An object representing an Asset Report with Freddie Mac schema.
    """

    loans: typing_extensions.Annotated[Loans, FieldMetadata(alias="LOANS"), pydantic.Field(alias="LOANS")]
    parties: typing_extensions.Annotated[Parties, FieldMetadata(alias="PARTIES"), pydantic.Field(alias="PARTIES")]
    services: typing_extensions.Annotated[Services, FieldMetadata(alias="SERVICES"), pydantic.Field(alias="SERVICES")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
