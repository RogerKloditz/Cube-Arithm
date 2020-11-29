# Cube-Arithm
Do arithmetics on cube-files

A script for transforming the scalar fields in cube-files
It can perform all kinds of operations on cube-files with numbers or
other cube-files.

Usage:

./cube-arithm.py <Cube-File1> plus 5 (Add 5 to all entries)

./cube-arithm.py <Cube-File1> times <Cube-File2>
(Multiply all entries of the first file with the corresponding entry in the second file)

Operations:
plus  (+)
minus (-)
times (*)
over  (/)
pow   (**)
fdiv  (floordiv)
mod   (modulo)

Note:

If two cube-files are used, the fields have to be exactly the same and the header of
the first file is used for the resulting cube-file.
