

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .g_nb_id import GNbId
from .plmn_id import PlmnId


class GlobalRanNodeId(UniversalBaseModel):
    plmn_id: typing_extensions.Annotated[PlmnId, FieldMetadata(alias="plmnId"), pydantic.Field(alias="plmnId")]
    n3iwf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n3IwfId"), pydantic.Field(alias="n3IwfId")
    ] = None
    g_nb_id: typing_extensions.Annotated[
        typing.Optional[GNbId], FieldMetadata(alias="gNbId"), pydantic.Field(alias="gNbId")
    ] = None
    nge_nb_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ngeNbId"), pydantic.Field(alias="ngeNbId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
