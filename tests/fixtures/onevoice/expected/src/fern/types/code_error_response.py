

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeErrorResponse(UniversalBaseModel):
    """
    Machine-routable error envelope; emitted by writeJSONCodeError.
    Frontend resolves `code` to a localized message via i18n catalog.
    """

    code: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
