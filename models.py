from dataclasses import dataclass

@dataclass
class AddInput:
    a: int
    b: int

@dataclass
class AddOutput:
    result: int

@dataclass
class SqrtInput:
    a: float

@dataclass
class SqrtOutput:
    result: float

@dataclass
class StringsToIntsInput:
    string: str

@dataclass
class StringsToIntsOutput:
    ascii_values: list[int]

@dataclass
class ExpSumInput:
    int_list: list[int]

@dataclass
class ExpSumOutput:
    result: float