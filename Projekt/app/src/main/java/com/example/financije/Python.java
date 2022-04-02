package com.example.financije;

import java.util.List;

public class Python {
    static final CPython cpython = CPython();

    public List<String> whereIsWaldo(String root) {
        ArrayList<String> result = new ArrayList<String>();
        Hashtable locals = new Hashtable();
        locals.put("result", result);
        locals.put("root", root);
        StringBuilder script = new StringBuilder();
        script.append("import os\n");
        script.append("import javabridge\n");
        script.append("root = javabridge.to_string(root)");
        script.append("result = javabridge.JWrapper(result)");
        script.append("for path, dirnames, filenames in os.walk(root):\n");
        script.append("  if 'waldo' in filenames:");
        script.append("     result.add(path)");
        cpython.exec(script.toString(), locals, null);
        return result;
    }

}
