

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateUserRequestDefaultVisibility(enum.StrEnum):
    PUBLIC = "public"
    PROTECTED = "protected"
    PRIVATE = "private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        protected: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateUserRequestDefaultVisibility.PUBLIC:
            return public()
        if self is CreateUserRequestDefaultVisibility.PROTECTED:
            return protected()
        if self is CreateUserRequestDefaultVisibility.PRIVATE:
            return private()
