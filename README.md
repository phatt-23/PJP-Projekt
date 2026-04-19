# PJP Project

Compiler and interpreter for a language in files with extension `.pjp`.

## Compilation

```
python compile.py [input_file] [output_file]
```

This creates an `output_file` with stack instructions for the interpreter / evaluator.

## Evaling

```
python eval.py [file]
```

This will interpret the stack instructions within the file.

