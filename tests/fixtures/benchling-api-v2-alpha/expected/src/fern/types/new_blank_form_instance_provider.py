

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .new_blank_form_instance_provider_type import NewBlankFormInstanceProviderType


class NewBlankFormInstanceProvider(UniversalBaseModel):
    type: typing.Optional[NewBlankFormInstanceProviderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
