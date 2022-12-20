from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ProcessRequestView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data['os'])
        msg = launch_kubernetes(request.data)
        return Response(
            {
                'msg': msg,
            },

        )


def launch_kubernetes(value):
    import os
    try:
        os.system('minikube start ctl')
        sd = os.system('ipconfig')
        print(sd)
        return "kubernetes started"
    except:
        return "error"
