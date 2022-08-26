import pytest
from collections import OrderedDict
from parserator_web.views import AddressParse
import usaddress

def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    address_parse = AddressParse()
    assert address_parse.parse(address_string) == (
            OrderedDict([('AddressNumber', '123'), ('StreetName', 'main'), ('StreetNamePostType', 'st'), ('PlaceName', 'chicago'), ('StateName', 'il')]),
            'Street Address'
             )

def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    with pytest.raises(usaddress.RepeatedLabelError) as err:
        address_parse = AddressParse()
        address_parse.parse(address_string)
