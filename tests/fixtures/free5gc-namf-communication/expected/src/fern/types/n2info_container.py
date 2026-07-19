

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2information_class import N2InformationClass
from .n2ran_information import N2RanInformation
from .n2sm_information import N2SmInformation
from .nrppa_information import NrppaInformation
from .pws_information import PwsInformation


class N2InfoContainer(UniversalBaseModel):
    n2information_class: typing_extensions.Annotated[
        N2InformationClass, FieldMetadata(alias="n2InformationClass"), pydantic.Field(alias="n2InformationClass")
    ]
    sm_info: typing_extensions.Annotated[
        typing.Optional[N2SmInformation], FieldMetadata(alias="smInfo"), pydantic.Field(alias="smInfo")
    ] = None
    ran_info: typing_extensions.Annotated[
        typing.Optional[N2RanInformation], FieldMetadata(alias="ranInfo"), pydantic.Field(alias="ranInfo")
    ] = None
    nrppa_info: typing_extensions.Annotated[
        typing.Optional[NrppaInformation], FieldMetadata(alias="nrppaInfo"), pydantic.Field(alias="nrppaInfo")
    ] = None
    pws_info: typing_extensions.Annotated[
        typing.Optional[PwsInformation], FieldMetadata(alias="pwsInfo"), pydantic.Field(alias="pwsInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
