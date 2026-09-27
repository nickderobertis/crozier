

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_template_response_modifier import HttpTemplateResponseModifier
from .http_template_template_type import HttpTemplateTemplateType


class HttpTemplate(UniversalBaseModel):
    """
    template to generate response / request
    """

    delay: typing.Optional[Delay] = None
    template_type: typing_extensions.Annotated[
        typing.Optional[HttpTemplateTemplateType],
        FieldMetadata(alias="templateType"),
        pydantic.Field(alias="templateType"),
    ] = None
    template: typing.Optional[str] = None
    template_file: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="templateFile"), pydantic.Field(alias="templateFile")
    ] = None
    response_override: typing_extensions.Annotated[
        typing.Optional["HttpResponse"],
        FieldMetadata(alias="responseOverride"),
        pydantic.Field(alias="responseOverride"),
    ] = None
    response_modifier: typing_extensions.Annotated[
        typing.Optional[HttpTemplateResponseModifier],
        FieldMetadata(alias="responseModifier"),
        pydantic.Field(alias="responseModifier"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .http_response import HttpResponse
from .recover_after import RecoverAfter

update_forward_refs(HttpTemplate, HttpResponse=HttpResponse, RecoverAfter=RecoverAfter)
