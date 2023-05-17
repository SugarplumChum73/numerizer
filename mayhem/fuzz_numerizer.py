#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from numerizer import numerize

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    num = RandomString(fdp, 10, 100)

    numerize(num)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()