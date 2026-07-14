

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class XComCollectionItem(UniversalBaseModel):
    """
    XCom entry collection item.

    The value field is only available when reading a single object due to the size of the value.
    """

    dag_id: typing.Optional[str] = None
    execution_date: typing.Optional[str] = None
    key: typing.Optional[str] = None
    task_id: typing.Optional[str] = None
    timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
