# FindHijackableDLL

Tools for identifying and exploiting DLL hijacking on Windows.

## Description

This project contains two Python scripts:

- `find_dll.py` : Recursively searches for DLL files in the user directory (excludes common user folders like Downloads, Desktop, Documents, etc.)
- `generate_ref.py` : Generates a C++ proxy DLL that forwards all exports to the original DLL while executing custom code

## Prerequisites

```bash
pip install pefile
```

## Usage

### Find DLLs

```bash
python find_dll.py
```

Lists all DLL files found in the user directory, excluding Downloads, Desktop, Documents, Pictures, Videos, Music, and Public folders. This ensures you only find DLLs where you have write permissions for hijacking.

### Generate Proxy DLL

```bash
python generate_ref.py <path_to_dll>
```

Generates the C++ code needed to create a proxy DLL that:
- Exports all functions from the original DLL
- Executes `calc.exe` on load (customizable in the generated code)
- Forwards calls to the legitimate DLL

## Example

```bash
python generate_ref.py C:\\path\\to\\target.dll
```

The generated code must be compiled into a DLL and placed in a location where it will be loaded before the original system DLL.

## Credits

The DLL proxy generation technique is heavily inspired by (copied from) the work at https://www.bordergate.co.uk/dll-proxying/
