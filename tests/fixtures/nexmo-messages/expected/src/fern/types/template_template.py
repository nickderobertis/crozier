

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .template_parameters import TemplateParameters


class TemplateTemplate(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the template. For WhatsApp use your WhatsApp namespace (available via Facebook Business Manager), followed by a colon : and the name of the template to use.
    """

    parameters: typing.Optional[TemplateParameters] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
