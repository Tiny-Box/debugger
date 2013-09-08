from ctypes import *

# Let's map the Microsoft types to ctypes for clarity
WORD		= c_ushort
DWORD 		= c_ulong
LPBYTE		= POINTER(c_ubyte)
LPTSTR		= POINTER(c_char)
HANDLE		= c_void_p
PVOID 		= c_void_p
UINT_PTR	= c_ulong
BYTE		= c_ubyte
LONG		= c_long

# Constants
DEBUG_PROCESS 		= 0x00000001
CREATE_NEW_CONSOLE 	= 0x00000010
PROCESS_ALL_ACCESS	= 0x001F0FFF
DBG_CONTINUE		= 0x00010002
INFINITE			= 0xFFFFFFFF

# Thread constants for CreateToolhelp32Snapshot()
TH32CS_SNAPTHREAD	= 0x00000004

# Structures for CreateProcessA()function
class STARTUPINFO(Structure):
	_field_ = [
		("cb",				DWORD),
		("lpReserved", 		LPTSTR),
		("lpDesktop", 		LPTSTR),
		("lpTitle", 		LPTSTR),
		("dwX", 			DWORD),
		("dwY", 			DWORD),
		("dwXSize", 		DWORD),
		("dwYSize", 		DWORD),
		("dwXCountChars", 	DWORD),
		("dwYCountChars", 	DWORD),
		("dwFillAttribute", DWORD),
		("dwFlags", 		DWORD),
		("wShowWindow", 	WORD),
		("cbReserved2", 	WORD),
		("lpReserved2", 	LPBYTE),
		("hStdInput", 		HANDLE),
		("hStdOutput",		HANDLE),
		("hStdError", 		HANDLE),
	]
class PROCESS_INFORMATION(Structure):
	_fields_ = [
		("hProcess",	HANDLE),
		("hThread", 	HANDLE),
		("dwProcessId", DWORD),
		("dwThreadId", 	DWORD),
	]

class EXCEPTION_RECORD(Structure):
	pass

EXCEPTION_RECORD._fields_ = [
		("ExceptionCode",		 DWORD),
		("ExceptionFlags",		 DWORD),
		("ExceptionRecord",		 POINTER(EXCEPTION_RECORD)),
		("ExceptionAddress",	 PVOID),
		("NumberParameters",	 DWORD),
		("ExceptionInformation", UINT_PTR * 15),
	]

class EXCEPTION_RECORD(Structure):
	_fields_ = [
		("ExceptionCode",		 DWORD),
		("ExceptionFlags",		 DWORD),
		("ExceptionRecord",		 POINTER(EXCEPTION_RECORD)),
		("ExceptionAddress",	 PVOID),
		("NumberParameters",	 DWORD),
		("ExceptionInformation", UINT_PTR * 15),
	]

class EXCEPTION_DEBUG_INFO(Structure):
	_fields_ = [
		("ExceptionRecord",		EXCEPTION_RECORD),
		("dwFirstChance",		DWORD),
	]

class DEBUG_EVENT_UNION(Union):
	_fields_ = [
		("Exception",			EXCEPTION_DEBUG_INFO),
#		("CreateThread",		CREATE_THREAD_DEBUG_INFO),
#		("CreateProcessInfo",	CREATE_PROCESS_DEBUG_INFO),
#		("ExitThread",			EXIT_THREAD_DEBUG_INFO),
#		("ExitProcess",			EXIT_PROCESS_DEBUG_INFO),
#		("LoadDll",				LOAD_DLL_DEBUG_INFO),
#		("UnloadDll",			UNLOAD_DLL_DEBUG_INFO),
#		("DebugString",			OUTPUT_DEBUG_STRING_INFO),
#		("RipInfo",				RIP_INFO),
	]

class DEBUG_EVENT(Structure):
	_fields_ = [
		("dwDebugEventCode",	DWORD),
		("dwProcessId",			DWORD),
		("dwThreadId",			DWORD),
		("u",					DEBUG_EVENT_UNION),
	]

class FLOATING_SAVE_AREA(Structure):
	_fields_ = [
		("ControlWord",			DWORD),
		("StatusWord",			DWORD),
		("TagWord",				DWORD),
		("ErrorOffset",			DWORD),
		("ErrorSelector",		DWORD),
		("DataOffset",			DWORD),
		("DataSelector",		DWORD),
		("RegisterArea",		BYTE * 80),
		("Cr0NpxState",			DWORD),
	]

class CONTEXT(Structure):
	_fields_ = [
		("ContextFlags",		DWORD),
		("Dro",					DWORD),
		("Dr1",					DWORD),
		("Dr2",					DWORD),
		("Dr3",					DWORD),
		("Dr4",					DWORD),
		("Dr5",					DWORD),
		("Dr6",					DWORD),
		("Dr7",					DWORD),
		("FloatSave",			FLOATING_SAVE_AREA),
		("SegGs",				DWORD),
		("SegFs",				DWORD),
		("SegEs",				DWORD),
		("SegDs",				DWORD),
		("Edi",					DWORD),
		("Esi",					DWORD),
		("Ebx",					DWORD),
		("Edx",					DWORD),
		("Ecx",					DWORD),
		("Eax",					DWORD),
		("Ebp",					DWORD),
		("Eip",					DWORD),
		("SegCs",				DWORD),
		("EFlags",				DWORD),
		("Esp",					DWORD),
		("SegSs",				DWORD),
		("ExtendedRegisters",	BYTE * 512),
	]

class tagTHREADENTRY32(Structure):
	_fields_ = [
		("dwSize",				DWORD),
		("cntUsage",			DWORD),
		("th32ThreadID",		DWORD),
		("th32OwnerProcessID",	DWORD),
		("tpBasePri",			LONG),
		("tpDeltaPri",			LONG),
		("dwFlags",				DWORD),
	]
