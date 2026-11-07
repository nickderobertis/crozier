

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NormCorporateGroup(UniversalBaseModel):
    norm_corporate_group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="normCorporateGroupId"), pydantic.Field(alias="normCorporateGroupId")
    ] = None
    norm_corporate_group_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="normCorporateGroupName"),
        pydantic.Field(alias="normCorporateGroupName"),
    ] = None
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
