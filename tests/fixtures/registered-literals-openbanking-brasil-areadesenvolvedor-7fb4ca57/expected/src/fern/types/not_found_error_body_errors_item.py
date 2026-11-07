

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NotFoundErrorBodyErrorsItem(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    Código de erro específico do endpoint
    """

    title: str = pydantic.Field()
    """
    Título legível por humanos deste erro específico
    """

    detail: str = pydantic.Field()
    """
    Descrição legível por humanos deste erro específico
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
