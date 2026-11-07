

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Model(enum.StrEnum):
    """
    Predefined model type for embeddings.
    """

    POTION_CODE16MV2 = "PotionCode16MV2"
    POTION_BASE32M = "PotionBase32M"
    POTION_MULTILINGUAL128M = "PotionMultilingual128M"
    POTION_RETRIEVAL32M = "PotionRetrieval32M"
    POTION_BASE8M = "PotionBase8M"
    POTION_BASE4M = "PotionBase4M"
    POTION_BASE2M = "PotionBase2M"

    def visit(
        self,
        potion_code16mv2: typing.Callable[[], T_Result],
        potion_base32m: typing.Callable[[], T_Result],
        potion_multilingual128m: typing.Callable[[], T_Result],
        potion_retrieval32m: typing.Callable[[], T_Result],
        potion_base8m: typing.Callable[[], T_Result],
        potion_base4m: typing.Callable[[], T_Result],
        potion_base2m: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Model.POTION_CODE16MV2:
            return potion_code16mv2()
        if self is Model.POTION_BASE32M:
            return potion_base32m()
        if self is Model.POTION_MULTILINGUAL128M:
            return potion_multilingual128m()
        if self is Model.POTION_RETRIEVAL32M:
            return potion_retrieval32m()
        if self is Model.POTION_BASE8M:
            return potion_base8m()
        if self is Model.POTION_BASE4M:
            return potion_base4m()
        if self is Model.POTION_BASE2M:
            return potion_base2m()
