

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SmContextRetrievedData(UniversalBaseModel):
    ue_eps_pdn_connection: typing_extensions.Annotated[
        str, FieldMetadata(alias="ueEpsPdnConnection"), pydantic.Field(alias="ueEpsPdnConnection")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
