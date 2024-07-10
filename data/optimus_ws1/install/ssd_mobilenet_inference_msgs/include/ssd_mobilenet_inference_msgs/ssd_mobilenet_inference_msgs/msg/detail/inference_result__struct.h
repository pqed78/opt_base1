// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ssd_mobilenet_inference_msgs:msg/InferenceResult.idl
// generated code does not contain a copyright notice

#ifndef SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_H_
#define SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'class_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/InferenceResult in the package ssd_mobilenet_inference_msgs.
typedef struct ssd_mobilenet_inference_msgs__msg__InferenceResult
{
  rosidl_runtime_c__String class_name;
  int64_t spatial_x;
  int64_t spatial_y;
  int64_t spatial_z;
} ssd_mobilenet_inference_msgs__msg__InferenceResult;

// Struct for a sequence of ssd_mobilenet_inference_msgs__msg__InferenceResult.
typedef struct ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence
{
  ssd_mobilenet_inference_msgs__msg__InferenceResult * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ssd_mobilenet_inference_msgs__msg__InferenceResult__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SSD_MOBILENET_INFERENCE_MSGS__MSG__DETAIL__INFERENCE_RESULT__STRUCT_H_
