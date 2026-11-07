

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetTestMetadataResponseItemsItem(UniversalBaseModel):
    message: str = pydantic.Field()
    """
    The failure message associated with the test.
    """

    source: str = pydantic.Field()
    """
    The program that generated the test results
    """

    run_time: float = pydantic.Field()
    """
    The time it took to run the test in seconds
    """

    file: str = pydantic.Field()
    """
    The file in which the test is defined.
    """

    result: str = pydantic.Field()
    """
    Indication of whether the test succeeded.
    """

    name: str = pydantic.Field()
    """
    The name of the test.
    """

    classname: str = pydantic.Field()
    """
    The programmatic location of the test.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
