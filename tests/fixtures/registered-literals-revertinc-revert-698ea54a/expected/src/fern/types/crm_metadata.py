

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .crm_status import CrmStatus


class CrmMetadata(UniversalBaseModel):
    integration_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="integrationId"), pydantic.Field(alias="integrationId")
    ]
    name: str
    image_src: typing_extensions.Annotated[str, FieldMetadata(alias="imageSrc"), pydantic.Field(alias="imageSrc")]
    status: CrmStatus
    client_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")
    ] = None
    scopes: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
