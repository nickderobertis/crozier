

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunCodeRequestLanguage(enum.StrEnum):
    """
    the language or execution mode to run the code
    """

    PYTHON = "python"
    CPP = "cpp"
    NODEJS = "nodejs"
    GO = "go"
    GO_TEST = "go_test"
    JAVA = "java"
    PHP = "php"
    CSHARP = "csharp"
    BASH = "bash"
    TYPESCRIPT = "typescript"
    SQL = "sql"
    RUST = "rust"
    CUDA = "cuda"
    LUA = "lua"
    R = "R"
    PERL = "perl"
    D_UT = "D_ut"
    RUBY = "ruby"
    SCALA = "scala"
    JULIA = "julia"
    PYTEST = "pytest"
    JUNIT = "junit"
    KOTLIN_SCRIPT = "kotlin_script"
    JEST = "jest"
    VERILOG = "verilog"
    PYTHON_GPU = "python_gpu"
    LEAN = "lean"
    SWIFT = "swift"
    RACKET = "racket"

    def visit(
        self,
        python: typing.Callable[[], T_Result],
        cpp: typing.Callable[[], T_Result],
        nodejs: typing.Callable[[], T_Result],
        go: typing.Callable[[], T_Result],
        go_test: typing.Callable[[], T_Result],
        java: typing.Callable[[], T_Result],
        php: typing.Callable[[], T_Result],
        csharp: typing.Callable[[], T_Result],
        bash: typing.Callable[[], T_Result],
        typescript: typing.Callable[[], T_Result],
        sql: typing.Callable[[], T_Result],
        rust: typing.Callable[[], T_Result],
        cuda: typing.Callable[[], T_Result],
        lua: typing.Callable[[], T_Result],
        r: typing.Callable[[], T_Result],
        perl: typing.Callable[[], T_Result],
        d_ut: typing.Callable[[], T_Result],
        ruby: typing.Callable[[], T_Result],
        scala: typing.Callable[[], T_Result],
        julia: typing.Callable[[], T_Result],
        pytest: typing.Callable[[], T_Result],
        junit: typing.Callable[[], T_Result],
        kotlin_script: typing.Callable[[], T_Result],
        jest: typing.Callable[[], T_Result],
        verilog: typing.Callable[[], T_Result],
        python_gpu: typing.Callable[[], T_Result],
        lean: typing.Callable[[], T_Result],
        swift: typing.Callable[[], T_Result],
        racket: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunCodeRequestLanguage.PYTHON:
            return python()
        if self is RunCodeRequestLanguage.CPP:
            return cpp()
        if self is RunCodeRequestLanguage.NODEJS:
            return nodejs()
        if self is RunCodeRequestLanguage.GO:
            return go()
        if self is RunCodeRequestLanguage.GO_TEST:
            return go_test()
        if self is RunCodeRequestLanguage.JAVA:
            return java()
        if self is RunCodeRequestLanguage.PHP:
            return php()
        if self is RunCodeRequestLanguage.CSHARP:
            return csharp()
        if self is RunCodeRequestLanguage.BASH:
            return bash()
        if self is RunCodeRequestLanguage.TYPESCRIPT:
            return typescript()
        if self is RunCodeRequestLanguage.SQL:
            return sql()
        if self is RunCodeRequestLanguage.RUST:
            return rust()
        if self is RunCodeRequestLanguage.CUDA:
            return cuda()
        if self is RunCodeRequestLanguage.LUA:
            return lua()
        if self is RunCodeRequestLanguage.R:
            return r()
        if self is RunCodeRequestLanguage.PERL:
            return perl()
        if self is RunCodeRequestLanguage.D_UT:
            return d_ut()
        if self is RunCodeRequestLanguage.RUBY:
            return ruby()
        if self is RunCodeRequestLanguage.SCALA:
            return scala()
        if self is RunCodeRequestLanguage.JULIA:
            return julia()
        if self is RunCodeRequestLanguage.PYTEST:
            return pytest()
        if self is RunCodeRequestLanguage.JUNIT:
            return junit()
        if self is RunCodeRequestLanguage.KOTLIN_SCRIPT:
            return kotlin_script()
        if self is RunCodeRequestLanguage.JEST:
            return jest()
        if self is RunCodeRequestLanguage.VERILOG:
            return verilog()
        if self is RunCodeRequestLanguage.PYTHON_GPU:
            return python_gpu()
        if self is RunCodeRequestLanguage.LEAN:
            return lean()
        if self is RunCodeRequestLanguage.SWIFT:
            return swift()
        if self is RunCodeRequestLanguage.RACKET:
            return racket()
