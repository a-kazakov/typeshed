from contextlib import contextmanager
from typing import Generator, Iterable, Optional, Tuple


FORCED_WIDTH: Optional[int]


def measure_table(rows: Iterable[Iterable[str]]) -> Tuple[int, ...]:
    ...


def iter_rows(
    rows: Iterable[Iterable[str]], col_count: int
) -> Generator[Tuple[str, ...], None, None]:
    ...


def wrap_text(
    text: str,
    width: int = 78,
    initial_indent: str = '',
    subsequent_indent: str = '',
    preserve_paragraphs = False
) -> str:
    ...


class HelpFormatter:
    indent_increment: int
    width: Optional[int]
    current_indent: int
    buffer: List[str]

    def __init__(
        self,
        indent_increment: int = 2,
        width: int = None,
        max_width: int = None,
    ) -> None:
        ...

    def write(self, string: str) -> None:
        ...

    def indent(self) -> None:
        ...

    def dedent(self) -> None:
        ...

    def write_usage(
        self,
        prog: str,
        args: str = '',
        prefix: str = 'Usage: ',
    ):
        ...

    def write_heading(self, heading: str) -> None:
        ...

    def write_paragraph(self) -> None:
        ...

    def write_text(self, text: str) -> None:
        ...

    def write_dl(
        self,
        rows: Iterable[Iterable[str]],
        col_max: int = 30,
        col_spacing: int = 2,
    ) -> None:
        ...

    @contextmanager
    def section(self, name) -> Generator[None, None, None]:
        ...

    @contextmanager
    def indentation(self) -> Generator[None, None, None]:
        ...

    def getvalue(self) -> str:
        ...


def join_options(options: List[str]) -> Tuple[str, bool]:
    ...
