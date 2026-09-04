

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskSpecParametersItemSourceRef(UniversalBaseModel):
    id: str
    title: typing.Optional[str] = None
    help: typing.Optional[str] = None
    section: typing.Optional[str] = None
    order: typing.Optional[float] = None
    widget: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    accepts: typing.List[str]
    multiple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When true, the parameter takes more than one value: the client sends one staged file per value, listed in `uris` in selection order. When absent or false, it takes a single value. Only labelmap source refs bind plurally today — every group whose parent is the active dataset, in store order; on other type tags the flag has no effect yet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
