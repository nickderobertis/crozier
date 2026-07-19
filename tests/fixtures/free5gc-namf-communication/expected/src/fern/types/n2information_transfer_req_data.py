

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ecgi import Ecgi
from .global_ran_node_id import GlobalRanNodeId
from .n2info_container import N2InfoContainer
from .ncgi import Ncgi
from .rat_selector import RatSelector
from .tai import Tai


class N2InformationTransferReqData(UniversalBaseModel):
    tai_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Tai]], FieldMetadata(alias="taiList"), pydantic.Field(alias="taiList")
    ] = None
    rat_selector: typing_extensions.Annotated[
        typing.Optional[RatSelector], FieldMetadata(alias="ratSelector"), pydantic.Field(alias="ratSelector")
    ] = None
    ecgi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Ecgi]], FieldMetadata(alias="ecgiList"), pydantic.Field(alias="ecgiList")
    ] = None
    ncgi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Ncgi]], FieldMetadata(alias="ncgiList"), pydantic.Field(alias="ncgiList")
    ] = None
    global_ran_node_list: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalRanNodeId]],
        FieldMetadata(alias="globalRanNodeList"),
        pydantic.Field(alias="globalRanNodeList"),
    ] = None
    n2information: typing_extensions.Annotated[
        N2InfoContainer, FieldMetadata(alias="n2Information"), pydantic.Field(alias="n2Information")
    ]
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
