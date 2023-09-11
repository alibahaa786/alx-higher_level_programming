#include <Python.h>

/**
 * print_python_list_info - Print some basic info about Python lists
 * @p: python list
*/

void print_python_list_info(PyObject *p)
{
	int size;
	int allocated;
	int i;

	PyObject *obj;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
