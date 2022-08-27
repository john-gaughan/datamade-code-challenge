import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        # How do I grab the user input?
        # How do I return the parsed components to the frontend?
        # What errors do I need to account for?
            # Invalid addresses structures
            # inputs with just a space
            # Inputs with characters that shouldn't be in an address? (maybe /, <, >, [], %, etc.)
    def get(self, request):
        address = request.GET.get("address")
        address_components, address_type = self.parse(address)
        context = {
            "address_components": address_components,
            "address_type": address_type,
        }
        data = json.dumps(context, sort_keys=True, default=str)
        return HttpResponse(data, content_type='application/json')

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        address_components, address_type = usaddress.tag(address)
        return address_components, address_type
