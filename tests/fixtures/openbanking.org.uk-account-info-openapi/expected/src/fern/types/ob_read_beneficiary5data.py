

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_beneficiary5 import ObBeneficiary5


class ObReadBeneficiary5Data(UniversalBaseModel):
    beneficiary: typing_extensions.Annotated[
        typing.Optional[typing.List[ObBeneficiary5]],
        FieldMetadata(alias="Beneficiary"),
        pydantic.Field(alias="Beneficiary"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
