

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_node_submit_form_payload_flags import PdfActionNodeSubmitFormPayloadFlags
from .pdf_action_target_ref import PdfActionTargetRef


class PdfActionNodeSubmitFormPayload(UniversalBaseModel):
    url: str
    fields: typing.Optional[typing.List[PdfActionTargetRef]] = None
    flags: PdfActionNodeSubmitFormPayloadFlags
    char_set: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="charSet"), pydantic.Field(alias="charSet")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
