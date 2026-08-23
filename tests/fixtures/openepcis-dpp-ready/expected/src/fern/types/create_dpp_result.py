

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identifier import Identifier


class CreateDppResult(UniversalBaseModel):
    """
    Result of CreateDPP (EN 18222 clause 4.6) — the new DPP ID.
    """

    digital_product_passport_id: typing_extensions.Annotated[
        Identifier, FieldMetadata(alias="digitalProductPassportId"), pydantic.Field(alias="digitalProductPassportId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
