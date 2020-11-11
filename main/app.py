import base64
import copy
import json

from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.json_format import MessageToDict

from opentelemetry.proto.metrics.v1.metrics_pb2 import ResourceMetrics


def lambda_handler(event, context):
	metrics = []
	for record in event['records']:
		record_data = record['data']
		base64_decoded = base64.b64decode(record_data)
		metric_data = read_delimited(base64_decoded, ResourceMetrics)
		metric_data_dict = convert_protobuf_dict(metric_data)
		metric_encoded_bytes = base64.b64encode(
			bytearray(
				json.dumps(metric_data_dict['instrumentationLibraryMetrics'][0]['metrics']),
				'utf-8'))
		metric_encoded_string = str(metric_encoded_bytes, 'utf-8')
		event_map = copy.deepcopy(record)
		event_map['data'] = metric_encoded_string
		event_map['result'] = 'Ok'
		metrics.append(event_map)

	return {'records': metrics}


def convert_protobuf_dict(metric):
	return MessageToDict(metric)


def read_delimited(data, metric_type):
	if len(data) == 0:
		return
	(msg_length, hdr_length) = _DecodeVarint(data, 0)
	# read message as a byte string
	proto_str = data[hdr_length:msg_length + hdr_length]

	# EOF
	if len(proto_str) == 0:
		return

	# de-serialize the bytes into a protobuf message
	msg = metric_type()
	msg.ParseFromString(proto_str)
	return msg
