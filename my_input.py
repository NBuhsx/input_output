from typing import Callable, Generator, Any, Optional


class my_input1:
    def __init__(self, end: str = '',
                 inside_string: Optional[Callable[[str], Any]] = None,
                 execute_with_element: Optional[Callable[[str], Any]] = None) -> None:

        print('\033[92m' + "---> " + '\033[1m', end='')
        self.rows = list(iter(input, end))
        self.__index = 0
        self.inside_string = inside_string
        self.exec_elem = execute_with_element

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.inside_string:
                for item_strok in self.inside_string(self.rows[self.__index]):
                    self.__index += 1
                    return self.exec_elem(item_strok) if self.exec_elem else item_strok
            else:
                ret = self.exec_elem(
                    self.rows[self.__index]) if self.exec_elem else self.rows[self.__index]
                self.__index += 1
                return ret
        except IndexError:
            raise StopIteration()


def my_input2(end: str = '',
              inside_string: Optional[Callable[[str], Any]] = None,
              execute_with_element: Callable[[str], Any] = lambda n: n) -> Generator[str | Any, None, None]:

    print('\033[92m' + "---> " + '\033[1m', end='')
    for row in list(iter(input, end)):
        if inside_string:
            for item_strok in inside_string(row):
                yield execute_with_element(item_strok)
        else:
            yield execute_with_element(row)
