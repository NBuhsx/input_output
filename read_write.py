import json

from pathlib import Path
from more_itertools import islice_extended
from typing import Callable, Generator, Any, Iterable, Optional, Literal


def read_rows(
        pathfile: str | Path,
        templete: Optional[Callable[[str], Any]] = None,
        mode: Literal['r', 'rb'] = 'r',
        islice: slice = slice(0, None, 1),
        encoding: str = 'utf-8') -> Generator[str | Any, None, None]:
    """Возращает генератор по строчно"""
    with open(file=pathfile, mode=mode, encoding=encoding) as file:
        for row in islice_extended(file)[islice]:
            try:
                yield templete(row) if templete else row
            except GeneratorExit:
                break


def write_rows(
        pathfile: str | Path,
        write: Iterable | str,
        mode: Literal['a', 'w', 'wb'] = 'a',
        encoding: str = 'utf-8',
        addN: bool = False) -> None:
    """ Записывает в файл"""
    with open(file=pathfile, mode=mode, encoding=encoding) as file:
        if isinstance(write, str):
            file.write(write + '\n') if addN else file.write(write)
        else:
            file.writelines(f"{elem}\n" for elem in write) \
                if addN else file.writelines(write)
