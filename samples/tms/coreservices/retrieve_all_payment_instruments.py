from CyberSource import *
import samples.tms.coreservices.create_instrument_identifier
from data.Configaration import *

def retrieve_all_payments():
    try:
        api_instrument_identifier_response = samples.tms.coreservices.create_instrument_identifier.create_instrument_identifier()
        config_obj = Configaration()
        details_dict1 = config_obj.get_configaration()
        instrument_identifier = InstrumentIdentifierApi(details_dict1)
        return_data, status, body =instrument_identifier.instrumentidentifiers_token_id_paymentinstruments_get("93B32398-AD51-4CC2-A682-EA3E93614EB1",api_instrument_identifier_response.id)
        print(status)
        print(body)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    retrieve_all_payments()
