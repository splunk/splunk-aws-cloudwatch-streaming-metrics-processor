from unittest import TestCase
from main import app


class Test(TestCase):
	def test_lambda_handler(self):
		event = {
			"invocationId": "214e762e-a57f-48c7-9251-337e60f10dfd",
			"deliveryStreamArn": "arn:aws:firehose:us-east-1:134183635603:deliverystream/firehose-to-splunk",
			"region": "us-west-2",
			"records": [
				{
					"recordId": "49610520579565593542493647173350442178010946319379595266000000",
					"approximateArrivalTimestamp": 1601456607310,
					"data": "+AUS9QUS6wIKLQonYW1hem9uYXdzLmNvbS9DV0FnZW50L3N3YXBfdXNlZF9wZXJjZW50IAYoAiq5AgoUCglOYW1lc3BhY2USB0NXQWdlbnQKGQoJQWNjb3VudElkEgwxMTI1NDM4MTc2MjQKHwoKTWV0cmljTmFtZRIRc3dhcF91c2VkX3BlcmNlbnQKEwoGUmVnaW9uEgl1cy13ZXN0LTIKYAoPTWV0cmljU3RyZWFtQXJuEk1hcm46YXdzOmNsb3Vkd2F0Y2g6dXMtd2VzdC0yOjExMjU0MzgxNzYyNDptZXRyaWMtc3RyZWFtL3Rlc3QtY3ctbWV0cmljLXN0cmVhbQoXCgdJbWFnZUlkEgxhbWktZjAwOTFkOTEKGAoKSW5zdGFuY2VJZBIKaS1hYjU0YTI2YwoaCgxJbnN0YW5jZVR5cGUSCmM0LjR4bGFyZ2URAJgr2YOCRhYZAPBy0ZGCRhYgATIAMgkJAAAAAAAAWUAShAMKLAomYW1hem9uYXdzLmNvbS9DV0FnZW50L21lbV91c2VkX3BlcmNlbnQgBigCKtMCChQKCU5hbWVzcGFjZRIHQ1dBZ2VudAoZCglBY2NvdW50SWQSDDExMjU0MzgxNzYyNAoeCgpNZXRyaWNOYW1lEhBtZW1fdXNlZF9wZXJjZW50ChMKBlJlZ2lvbhIJdXMtd2VzdC0yCmAKD01ldHJpY1N0cmVhbUFybhJNYXJuOmF3czpjbG91ZHdhdGNoOnVzLXdlc3QtMjoxMTI1NDM4MTc2MjQ6bWV0cmljLXN0cmVhbS90ZXN0LWN3LW1ldHJpYy1zdHJlYW0KFwoHSW1hZ2VJZBIMYW1pLWYwMDkxZDkxChgKCkluc3RhbmNlSWQSCmktYWI1NGEyNmMKGgoMSW5zdGFuY2VUeXBlEgpjNC40eGxhcmdlEQCYK9mDgkYWGQDwctGRgkYWIAEprbolX+/WOUAyCRGtuiVf79Y5QDISCQAAAAAAAFlAEa26JV/v1jlA "
				}
			]
		}

		ret = app.lambda_handler(event, "")
		assert ret['records'][0]['result'] == "Ok"
