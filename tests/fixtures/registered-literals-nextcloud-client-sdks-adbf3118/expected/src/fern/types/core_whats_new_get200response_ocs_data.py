

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_whats_new_get200response_ocs_data_whats_new import CoreWhatsNewGet200ResponseOcsDataWhatsNew


class CoreWhatsNewGet200ResponseOcsData(UniversalBaseModel):
    changelog_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="changelogURL"), pydantic.Field(alias="changelogURL")
    ]
    product: str
    version: str
    whats_new: typing_extensions.Annotated[
        CoreWhatsNewGet200ResponseOcsDataWhatsNew, FieldMetadata(alias="whatsNew"), pydantic.Field(alias="whatsNew")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
