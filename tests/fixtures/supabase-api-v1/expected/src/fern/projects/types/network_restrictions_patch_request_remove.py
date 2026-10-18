

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class NetworkRestrictionsPatchRequestRemove(UniversalBaseModel):
    db_allowed_cidrs: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="dbAllowedCidrs"), pydantic.Field(alias="dbAllowedCidrs")
    ] = None
    db_allowed_cidrs_v6: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="dbAllowedCidrsV6"),
        pydantic.Field(alias="dbAllowedCidrsV6"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
