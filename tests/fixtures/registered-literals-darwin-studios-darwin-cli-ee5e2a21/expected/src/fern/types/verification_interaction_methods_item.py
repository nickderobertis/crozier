

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VerificationInteractionMethodsItem(UniversalBaseModel):
    id: str
    label: str
    web_link_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="webLinkRequired"), pydantic.Field(alias="webLinkRequired")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
