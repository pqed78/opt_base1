// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__rosidl_typesupport_introspection_c.h"
#include "ssd_mobilenet_inference_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__functions.h"
#include "ssd_mobilenet_inference_msgs/msg/detail/inference_result__struct.h"


// Include directives for member types
// Member `class_name`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  ssd_mobilenet_inference_msgs__msg__InferenceResult__init(message_memory);
}

void ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_fini_function(void * message_memory)
{
  ssd_mobilenet_inference_msgs__msg__InferenceResult__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_member_array[4] = {
  {
    "class_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssd_mobilenet_inference_msgs__msg__InferenceResult, class_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "spatial_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssd_mobilenet_inference_msgs__msg__InferenceResult, spatial_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "spatial_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssd_mobilenet_inference_msgs__msg__InferenceResult, spatial_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "spatial_z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(ssd_mobilenet_inference_msgs__msg__InferenceResult, spatial_z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_members = {
  "ssd_mobilenet_inference_msgs__msg",  // message namespace
  "InferenceResult",  // message name
  4,  // number of fields
  sizeof(ssd_mobilenet_inference_msgs__msg__InferenceResult),
  ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_member_array,  // message members
  ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_init_function,  // function to initialize message memory (memory has to be allocated)
  ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_type_support_handle = {
  0,
  &ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_ssd_mobilenet_inference_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, ssd_mobilenet_inference_msgs, msg, InferenceResult)() {
  if (!ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_type_support_handle.typesupport_identifier) {
    ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ssd_mobilenet_inference_msgs__msg__InferenceResult__rosidl_typesupport_introspection_c__InferenceResult_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
