

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TestConfigLanguage(enum.StrEnum):
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
        if self is TestConfigLanguage.PYTHON:
            return python()
        if self is TestConfigLanguage.CPP:
            return cpp()
        if self is TestConfigLanguage.NODEJS:
            return nodejs()
        if self is TestConfigLanguage.GO:
            return go()
        if self is TestConfigLanguage.GO_TEST:
            return go_test()
        if self is TestConfigLanguage.JAVA:
            return java()
        if self is TestConfigLanguage.PHP:
            return php()
        if self is TestConfigLanguage.CSHARP:
            return csharp()
        if self is TestConfigLanguage.BASH:
            return bash()
        if self is TestConfigLanguage.TYPESCRIPT:
            return typescript()
        if self is TestConfigLanguage.SQL:
            return sql()
        if self is TestConfigLanguage.RUST:
            return rust()
        if self is TestConfigLanguage.CUDA:
            return cuda()
        if self is TestConfigLanguage.LUA:
            return lua()
        if self is TestConfigLanguage.R:
            return r()
        if self is TestConfigLanguage.PERL:
            return perl()
        if self is TestConfigLanguage.D_UT:
            return d_ut()
        if self is TestConfigLanguage.RUBY:
            return ruby()
        if self is TestConfigLanguage.SCALA:
            return scala()
        if self is TestConfigLanguage.JULIA:
            return julia()
        if self is TestConfigLanguage.PYTEST:
            return pytest()
        if self is TestConfigLanguage.JUNIT:
            return junit()
        if self is TestConfigLanguage.KOTLIN_SCRIPT:
            return kotlin_script()
        if self is TestConfigLanguage.JEST:
            return jest()
        if self is TestConfigLanguage.VERILOG:
            return verilog()
        if self is TestConfigLanguage.PYTHON_GPU:
            return python_gpu()
        if self is TestConfigLanguage.LEAN:
            return lean()
        if self is TestConfigLanguage.SWIFT:
            return swift()
        if self is TestConfigLanguage.RACKET:
            return racket()
