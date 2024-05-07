import google.generativeai as genai
import os
from dotenv import load_dotenv
class VertexHttpClient extends BaseClient {
  VertexHttpClient(this._projectUrl);

  final String _projectUrl;
  final _client = Client();

  @override
  Future<StreamedResponse> send(BaseRequest request) {
    if (request is! Request ||
        request.url.host != 'generativelanguage.googleapis.com') {
      return _client.send(request);
    }

    final vertexRequest = Request(
      request.method,
      Uri.parse(request.url.toString().replaceAll(
          'https://generativelanguage.googleapis.com/v1/models',
          _projectUrl))
      ..bodyBytes = request.bodyBytes;

    for (final header in request.headers.entries) {
      if (header.key != 'ya29.a0Ad52N3-Z6A2TaVqaDtODIhxLmWBMQb_OgSNXv_T20NM2ayQV-hYC-YFze8xocRzx7n4ANxyITopHj_NdzcGKyh0CSNqlcUNHkRrUPX9yqtogaL2jjkp7oezQUtxBY-gYWOw5v9eZxk2oTAZoW1REMzMBofAzvei2qtuCebOkiAaCgYKATISARISFQHGX2Mi8FBzHSRMe8hSWJigU-idCA0177') {
        vertexRequest.headers[header.key] = header.value;
      }
    }

    vertexRequest.headers['Authorization'] =
      'Bearer ${request.headers['ya29.a0Ad52N3-Z6A2TaVqaDtODIhxLmWBMQb_OgSNXv_T20NM2ayQV-hYC-YFze8xocRzx7n4ANxyITopHj_NdzcGKyh0CSNqlcUNHkRrUPX9yqtogaL2jjkp7oezQUtxBY-gYWOw5v9eZxk2oTAZoW1REMzMBofAzvei2qtuCebOkiAaCgYKATISARISFQHGX2Mi8FBzHSRMe8hSWJigU-idCA0177']}';

    return _client.send(vertexRequest);
  }
}
GenerativeModel(
  model: 'gemini-pro',
  apiKey: ya29.a0Ad52N3-Z6A2TaVqaDtODIhxLmWBMQb_OgSNXv_T20NM2ayQV-hYC-YFze8xocRzx7n4ANxyITopHj_NdzcGKyh0CSNqlcUNHkRrUPX9yqtogaL2jjkp7oezQUtxBY-gYWOw5v9eZxk2oTAZoW1REMzMBofAzvei2qtuCebOkiAaCgYKATISARISFQHGX2Mi8FBzHSRMe8hSWJigU-idCA0177,
  httpClient: VertexHttpClient(projectUrl),
);