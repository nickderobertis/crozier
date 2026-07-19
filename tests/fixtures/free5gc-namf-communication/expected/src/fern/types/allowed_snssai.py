

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_information import NsiInformation
from .snssai import Snssai


class AllowedSnssai(UniversalBaseModel):
    allowed_snssai: typing_extensions.Annotated[
        Snssai, FieldMetadata(alias="allowedSnssai"), pydantic.Field(alias="allowedSnssai")
    ]
    nsi_information_list: typing_extensions.Annotated[
        typing.Optional[typing.List[NsiInformation]],
        FieldMetadata(alias="nsiInformationList"),
        pydantic.Field(alias="nsiInformationList"),
    ] = None
    mapped_home_snssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="mappedHomeSnssai"), pydantic.Field(alias="mappedHomeSnssai")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
