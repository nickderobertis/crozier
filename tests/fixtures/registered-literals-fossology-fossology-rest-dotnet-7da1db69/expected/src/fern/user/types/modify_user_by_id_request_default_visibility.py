

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ModifyUserByIdRequestDefaultVisibility(enum.StrEnum):
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        protected: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModifyUserByIdRequestDefaultVisibility.PUBLIC:
            return public()
        if self is ModifyUserByIdRequestDefaultVisibility.PROTECTED:
            return protected()
        if self is ModifyUserByIdRequestDefaultVisibility.PRIVATE:
            return private()
