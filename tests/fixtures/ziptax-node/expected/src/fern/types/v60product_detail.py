

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60taxability_code import V60TaxabilityCode


class V60ProductDetail(UniversalBaseModel):
    taxability_code: typing_extensions.Annotated[
        V60TaxabilityCode,
        FieldMetadata(alias="taxabilityCode"),
        pydantic.Field(
            alias="taxabilityCode",
            description="Resolved taxability code details and the product rate rules that apply in this jurisdiction.",
        ),
    ]
    """
    Resolved taxability code details and the product rate rules that apply in this jurisdiction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
