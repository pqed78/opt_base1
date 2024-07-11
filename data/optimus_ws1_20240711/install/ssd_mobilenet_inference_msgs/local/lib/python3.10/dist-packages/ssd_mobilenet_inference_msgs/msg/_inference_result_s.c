// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool ssd_mobilenet_inference_msgs__msg__inference_result__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[67];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("ssd_mobilenet_inference_msgs.msg._inference_result.InferenceResult", full_classname_dest, 66) == 0);
  }
  ssd_mobilenet_inference_msgs__msg__InferenceResult * ros_message = _ros_message;
  {  // class_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "class_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->class_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // spatial_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "spatial_x");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->spatial_x = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }
  {  // spatial_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "spatial_y");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->spatial_y = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }
  {  // spatial_z
    PyObject * field = PyObject_GetAttrString(_pymsg, "spatial_z");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->spatial_z = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * ssd_mobilenet_inference_msgs__msg__inference_result__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of InferenceResult */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("ssd_mobilenet_inference_msgs.msg._inference_result");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "InferenceResult");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  ssd_mobilenet_inference_msgs__msg__InferenceResult * ros_message = (ssd_mobilenet_inference_msgs__msg__InferenceResult *)raw_ros_message;
  {  // class_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->class_name.data,
      strlen(ros_message->class_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "class_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // spatial_x
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->spatial_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "spatial_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // spatial_y
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->spatial_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "spatial_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // spatial_z
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->spatial_z);
    {
      int rc = PyObject_SetAttrString(_pymessage, "spatial_z", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
