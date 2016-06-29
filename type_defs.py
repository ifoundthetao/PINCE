PINCE_IPC_PATH = "/tmp/PINCE-connection/"
INITIAL_INJECTION_PATH = "/Injection/InitialCodeInjections.so"

INFERIOR_RUNNING = 0
INFERIOR_STOPPED = 1

NO_INJECTION = 0
SIMPLE_DLOPEN_CALL = 1
LINUX_INJECT = 2

INJECTION_SUCCESSFUL = 1
INJECTION_FAILED = 0
NO_INJECTION_ATTEMPT = -1

# represents the index of columns in address table
FROZEN_COL = 0  # Frozen
DESC_COL = 1  # Description
ADDR_COL = 2  # Address
TYPE_COL = 3  # Type
VALUE_COL = 4  # Value

# represents the index of valuetype combobox
# any change at indexes may require rework on the other dictionaries
COMBOBOX_BYTE = 0
COMBOBOX_2BYTES = 1
COMBOBOX_4BYTES = 2
COMBOBOX_8BYTES = 3
COMBOBOX_FLOAT = 4
COMBOBOX_DOUBLE = 5
COMBOBOX_STRING = 6
COMBOBOX_AOB = 7  # Array of Bytes

# Represents the texts at indexes in combobox
index_to_text_dict = {
    COMBOBOX_BYTE: "Byte",
    COMBOBOX_2BYTES: "2 Bytes",
    COMBOBOX_4BYTES: "4 Bytes",
    COMBOBOX_8BYTES: "8 Bytes",
    COMBOBOX_FLOAT: "Float",
    COMBOBOX_DOUBLE: "Double",
    COMBOBOX_STRING: "String",
    COMBOBOX_AOB: "AoB"
}

text_to_index_dict = {
    "Byte": COMBOBOX_BYTE,
    "2 Bytes": COMBOBOX_2BYTES,
    "4 Bytes": COMBOBOX_4BYTES,
    "8 Bytes": COMBOBOX_8BYTES,
    "Float": COMBOBOX_FLOAT,
    "Double": COMBOBOX_DOUBLE
}

# A dictionary used to convert value_combobox index to gdb/mi x command
# Check GDB_Engine for an exemplary usage
index_to_gdbcommand_dict = {
    COMBOBOX_BYTE: "db",
    COMBOBOX_2BYTES: "dh",
    COMBOBOX_4BYTES: "dw",
    COMBOBOX_8BYTES: "dg",
    COMBOBOX_FLOAT: "fw",
    COMBOBOX_DOUBLE: "fg",
    COMBOBOX_STRING: "xb",
    COMBOBOX_AOB: "xb"
}

# first value is the length and the second one is the type
# Check ScriptUtils for an exemplary usage
index_to_valuetype_dict = {
    COMBOBOX_BYTE: [1, "b"],
    COMBOBOX_2BYTES: [2, "h"],
    COMBOBOX_4BYTES: [4, "i"],
    COMBOBOX_8BYTES: [8, "q"],
    COMBOBOX_FLOAT: [4, "f"],
    COMBOBOX_DOUBLE: [8, "d"],
    COMBOBOX_STRING: [None, None],
    COMBOBOX_AOB: [None, None]
}

# Check ScriptUtils for an exemplary usage
index_to_struct_pack_dict = {
    COMBOBOX_BYTE: "B",
    COMBOBOX_2BYTES: "H",
    COMBOBOX_4BYTES: "I",
    COMBOBOX_8BYTES: "Q",
    COMBOBOX_FLOAT: "f",
    COMBOBOX_DOUBLE: "d"
}