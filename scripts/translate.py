#!/usr/bin/env python3
"""
AUTO-TRANSLATOR: Converts Kotlin solutions to Java, Python, Rust, C++.
This runs as part of the build process to generate ALL language variants.
"""
import os, re

DATA_DIR = "_data/code"

# Simple Kotlin-to-X translation rules
KOTLIN_TO_JAVA = {
    r'\bfun\b': 'public static',  # Simplified
    r'\bIntArray\b': 'int[]',
    r'\bval\b': 'final var',
    r'\bvar\b': 'var',
    r'\bif\s*\((.+?)\)\s*->\s*(.+?)\b': 'if ($1) { $2 }',
    r'\belse\s*->\s*(.+?)\b': 'else { $1 }',
    r'\.lastIndex': '.length - 1',
    r'\bmaxOf\b': 'Math.max',
    r'\bminOf\b': 'Math.min',
    r'\bprintln\b': 'System.out.println',
    r'\bnull\b': 'null',
    r'\bList<(.+?)>\b': 'List<$1>',
    r'\bMutableList<(.+?)>\b': 'List<$1>',
    r'\bArray<(.+?)>\b': '$1[]',
    r'\bIntArray\b': 'int[]',
    r'\bStringBuilder\b': 'StringBuilder',
}

KOTLIN_TO_PYTHON = {
    r'\bfun\b': 'def',
    r'\bval\b': '',
    r'\bvar\b': '',
    r'\bIntArray\b': 'list[int]',
    r'\bBoolean\b': 'bool',
    r'\bInt\b': 'int',
    r'\bString\b': 'str',
    r'\bmaxOf\b': 'max',
    r'\bminOf\b': 'min',
    r'\bprintln\b': 'print',
    r'\bnull\b': 'None',
    r'\btrue\b': 'True',
    r'\bfalse\b': 'False',
    r'\bif\s*\((.+?)\)\s*->\s*(.+?)\b': 'if $1: $2',
    r'\belse\s*->\s*(.+?)\b': 'else: $1',
}

def kotlin_to_java(kt: str) -> str:
    """Basic Kotlin to Java translation."""
    java = kt
    java = re.sub(r'package\s+\S+', '', java)
    java = re.sub(r'import\s+.*', '', java)
    java = re.sub(r'fun\s+(\w+)\(', 'public static void $1(', java)
    java = re.sub(r'fun\s+(\w+)\(', 'public static $1(', java)
    java = re.sub(r':\s*Int\b', '', java)
    java = re.sub(r':\s*Boolean\b', '', java)
    java = re.sub(r':\s*String\b', '', java)
    java = re.sub(r':\s*Unit\b', '', java)
    java = re.sub(r'=\s*(\w+)\.toList\(\)\.subList\(', ' = Arrays.asList($1).subList(', java)
    java = re.sub(r'import java\.util\.\*', '', java)
    return java.strip()

def kotlin_to_python(kt: str) -> str:
    """Basic Kotlin to Python translation."""
    py = kt
    py = re.sub(r'package\s+\S+', '', py)
    py = re.sub(r'import\s+.*', '', py)
    py = re.sub(r'fun\s+(\w+)\(', 'def $1(', py)
    py = re.sub(r':\s*Int\b', ': int', py)
    py = re.sub(r':\s*Boolean\b', ': bool', py)
    py = re.sub(r':\s*String\b', ': str', py)
    py = re.sub(r':\s*Unit\b', '', py)
    py = re.sub(r'\bval\s+(\w+)\s*=\s*', '$1 = ', py)
    py = re.sub(r'\bvar\s+(\w+)\s*=\s*', '$1 = ', py)
    py = re.sub(r'\bval\s+\((\w+),\s*(\w+)\)\s*=\s*', '($1, $2) = ', py)
    py = re.sub(r'\bmaxOf\b', 'max', py)
    py = re.sub(r'\bminOf\b', 'min', py)
    py = re.sub(r'\bprintln\b', 'print', py)
    py = re.sub(r'\bnull\b', 'None', py)
    py = re.sub(r'\btrue\b', 'True', py)
    py = re.sub(r'\bfalse\b', 'False', py)
    py = re.sub(r'\bIntArray\b', 'list[int]', py)
    return py.strip()

def kotlin_to_rust(kt: str) -> str:
    """Basic Kotlin to Rust translation."""
    rs = kt
    rs = re.sub(r'package\s+\S+', '', rs)
    rs = re.sub(r'import\s+.*', '', rs)
    rs = re.sub(r'fun\s+(\w+)\(', 'fn $1(', rs)
    rs = re.sub(r':\s*Int\b', ' -> i32', rs)
    rs = re.sub(r':\s*Boolean\b', ' -> bool', rs)
    rs = re.sub(r':\s*String\b', ' -> String', rs)
    rs = re.sub(r':\s*Unit\b', '', rs)
    rs = re.sub(r'\bIntArray\b', 'Vec<i32>', rs)
    rs = re.sub(r'\.lastIndex', '.len() - 1', rs)
    rs = re.sub(r'\bmaxOf\b', 'max', rs)
    rs = re.sub(r'\bminOf\b', 'min', rs)
    rs = re.sub(r'\bprintln\b', 'println!', rs)
    rs = re.sub(r'\bnull\b', 'None', rs)
    return rs.strip()

def kotlin_to_cpp(kt: str) -> str:
    """Basic Kotlin to C++ translation."""
    cpp = kt
    cpp = re.sub(r'package\s+\S+', '', cpp)
    cpp = re.sub(r'import\s+.*', '', cpp)
    cpp = re.sub(r'fun\s+(\w+)\(', '$1(', cpp)
    cpp = re.sub(r':\s*Int\b', '', cpp)
    cpp = re.sub(r':\s*Boolean\b', '', cpp)
    cpp = re.sub(r':\s*String\b', '', cpp)
    cpp = re.sub(r':\s*Unit\b', '', cpp)
    cpp = re.sub(r'\bIntArray\b', 'vector<int>', cpp)
    cpp = re.sub(r'\bval\s+(\w+)\s*=\s*', 'auto $1 = ', cpp)
    cpp = re.sub(r'\bvar\s+(\w+)\s*=\s*', 'auto $1 = ', cpp)
    cpp = re.sub(r'\bmaxOf\b', 'max', cpp)
    cpp = re.sub(r'\bminOf\b', 'min', cpp)
    cpp = re.sub(r'\bprintln\b', 'cout <<', cpp)
    cpp = re.sub(r'\bnull\b', 'nullptr', cpp)
    cpp = re.sub(r'\.lastIndex', '.size() - 1', cpp)
    return cpp.strip()

# Process all problem directories
for prob_dir in sorted(os.listdir(DATA_DIR)):
    kt_file = os.path.join(DATA_DIR, prob_dir, "kotlin.txt")
    if not os.path.exists(kt_file):
        continue
    with open(kt_file, 'r') as f:
        kt_code = f.read()
    
    with open(os.path.join(DATA_DIR, prob_dir, "java.txt"), 'w') as f:
        f.write(kotlin_to_java(kt_code))
    with open(os.path.join(DATA_DIR, prob_dir, "python.txt"), 'w') as f:
        f.write(kotlin_to_python(kt_code))
    with open(os.path.join(DATA_DIR, prob_dir, "rust.txt"), 'w') as f:
        f.write(kotlin_to_rust(kt_code))
    with open(os.path.join(DATA_DIR, prob_dir, "cpp.txt"), 'w') as f:
        f.write(kotlin_to_cpp(kt_code))

print("Translations generated for all problems!")
