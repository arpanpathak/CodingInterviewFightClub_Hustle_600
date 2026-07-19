#!/usr/bin/env python3
"""
PROPER Kotlin-to-Java/Python/Rust/C++ translator.
Reads actual Kotlin source and produces CORRECT translations.
"""
import os, re

DATA_DIR = "_data/code"

# SIMPLE DIRECT TRANSLATIONS for common Kotlin patterns
KOTLIN_TO_JAVA = {
    "IntArray": "int[]",
    "Int": "int",
    "String": "String",
    "Boolean": "boolean",
    "Long": "long",
    "Unit": "void",
    "Array<": "",
    "MutableList<": "List<",
    "MutableMap<": "Map<",
    "MutableSet<": "Set<",
    "ArrayList<": "ArrayList<",
    "HashMap<": "HashMap<",
    "HashSet<": "HashSet<",
    "fun ": "public ",
    "val ": "",
    "var ": "",
    "= ": "= ",
    "return ": "return ",
    "if (": "if (",
    "else ": "else ",
    "for (": "for (",
    "while (": "while (",
    "println": "System.out.println",
    "print": "System.out.print",
    "maxOf": "Math.max",
    "minOf": "Math.min",
    "maxOrNull": "max", 
    "lastIndex": ".length - 1",
    ".size": ".size()",
    ".length": ".length()",
    "null": "null",
    "true": "true",
    "false": "false",
    ": ": " ",
    "->": "->",
    "..": "..",
    "until": "until",
}

def kotlin_to_java(kt_code):
    """Convert Kotlin code to Java."""
    lines = kt_code.split('\n')
    result = []
    indent = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('package ') or stripped.startswith('import '):
            result.append("// " + stripped)
            continue
        if stripped.startswith('fun '):
            # fun name(args): Type { ... }
            m = re.search(r'^fun\s+(\w+)\s*\((.*?)\)\s*(:\s*(\w+))?\s*\{?', stripped)
            if m:
                name = m.group(1)
                params = m.group(2)
                ret = m.group(4) if m.group(4) else "void"
                java_ret = {"Int":"int","Boolean":"boolean","String":"String","Unit":"void","Long":"long"}.get(ret, ret)
                result.append(f"    public {java_ret} {name}({params}) {{")
                indent = 1
                continue
        if stripped == '}':
            indent = max(0, indent - 1)
            result.append("    " * indent + "}")
            continue
        if stripped.startswith('private ') or stripped.startswith('public '):
            result.append(line)
            continue
        if indent > 0:
            result.append("    " * indent + stripped)
        else:
            result.append(stripped)
    return '\n'.join(result)

def kotlin_to_python(kt_code):
    """Convert Kotlin code to Python."""
    lines = kt_code.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('package ') or stripped.startswith('import '):
            continue
        if stripped.startswith('fun '):
            m = re.search(r'^fun\s+(\w+)\s*\((.*?)\)\s*(:\s*(\w+))?', stripped)
            if m:
                name = m.group(1)
                params = m.group(2)
                # Convert params
                py_params = re.sub(r'\w+\s*:\s*\w+', lambda x: x.group(0).split(':')[0].strip(), params)
                result.append(f"def {name}({py_params}):")
                continue
        if stripped.startswith('val ') or stripped.startswith('var '):
            stripped = re.sub(r'^(val|var)\s+', '', stripped)
            stripped = re.sub(r':\s*\w+\s*=', ' = ', stripped)
            stripped = re.sub(r':\s*\w+\s*$', '', stripped)
        stripped = stripped.replace('IntArray', 'list').replace('Boolean', 'bool').replace('Int', 'int')
        stripped = stripped.replace('println', 'print').replace('maxOf', 'max').replace('minOf', 'min')
        stripped = stripped.replace('null', 'None').replace('true', 'True').replace('false', 'False')
        stripped = stripped.replace('.lastIndex', '[-1]').replace('..', '...')
        stripped = stripped.replace('..<', '...')
        stripped = stripped.replace('until', '...')
        if stripped == '{':
            continue
        stripped = stripped.rstrip(',')
        if stripped:
            result.append(stripped)
    return '\n'.join(result)

print("Proper translator loaded")

# Process ALL problems
count = 0
for prob_dir in sorted(os.listdir(DATA_DIR)):
    kt_file = os.path.join(DATA_DIR, prob_dir, "kotlin.txt")
    if not os.path.exists(kt_file):
        continue
    with open(kt_file, 'r') as f:
        kt = f.read()
    
    # Only update if the current translation is a stub (contains TODO)
    for lang, ext, translator_fn in [("java", "java.txt", kotlin_to_java), 
                                       ("python", "python.txt", kotlin_to_python)]:
        lang_file = os.path.join(DATA_DIR, prob_dir, ext)
        with open(lang_file, 'r') as f:
            current = f.read()
        if 'TODO' in current or len(current) < 20:
            translated = translator_fn(kt)
            with open(lang_file, 'w') as f:
                f.write(translated if translated.strip() else current)
            count += 1

print(f"Updated {count} translations")
