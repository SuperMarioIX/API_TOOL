import ExtractCredentials
from rep_api import RepApi
import json

def extractProntoInformationIntoJson(feature_id):
    # print(feature_id)
    api = RepApi(username=ExtractCredentials.username, password=ExtractCredentials.password, config='rep-prod-one')

    # Autentificare
    api.login()

    url = 'https://rep-portal.ext.net.nokia.com/api/pronto/report/?feature__pos_neg='+str(feature_id)+'&fields=pronto_id%2Cstatus_color%2Cpronto_tool_url%2Cfault_analysis%2Cfa_pronto_tool_url%2Ctitle%2Crd_info%2Crc_known%2Cavailable_estimate%2Cavailable_estimate_status%2Cpr_stats_currently_affected_tis%2Cpr_stats_ever_affected_tis%2Cpr_stats_ever_affected_runs%2Clast_modified_since%2Cdays_since_closure%2Cage%2Cstate%2Crelease%2Cpriority%2Crepeatability%2Cseverity%2Ctop_importance_arr%2Ccorrection_forms%2Cauthor%2Cauthor_group%2Cauthor_group_manager%2Cgroup_in_charge_name%2Cgroup_in_charge_manager%2Cgroup_in_charge_tribe_name%2Cgroup_in_charge_tribe_manager_name%2Cgroup_in_charge_tribe_quality_manager_name%2Cgroup_in_charge_tribe_group_name%2Cgroup_in_charge_tribe_group_manager%2Cgroup_in_charge_dev_unit_name%2Cgroup_in_charge_dev_unit_manager%2Cfault_coordinator%2Cothers_interested%2Cmodified_components%2Ccomponent%2Cproduct_name%2Caggregated_product_name_fields%2Cfeature%2Creported_date%2Cclosed_date%2Copen_days%2Ccomments%2Crep_comments&limit=100&ordering=-reported_date'
    response = api.get(url)

    if response.status_code == 200:
        try:
            api_data = response.json()

            json_file_path = 'output.json'

            with open(json_file_path, 'w') as json_file:
                json.dump(api_data, json_file, indent=2)

            # print(f'Data has been written to {json_file_path}')

        except json.JSONDecodeError:
            print("Error decoding JSON from the API response.")

    else:
        print(f"Failed to retrieve data from API. Status code: {response.status_code}")

    pronto_number_url = 'https://rep-portal.ext.net.nokia.com/api/pronto/count/?feature__pos_neg='+str(feature_id)+'&ordering=-reported_date'
    prontocount = api.get(pronto_number_url)

    if prontocount.status_code == 200:
        pr_numbers = prontocount.json()
        # print(pr_numbers)
    else:
        print(f"Failed to retrieve data from API. Status code: {response.status_code}")

    return pr_numbers, api       
  
# api.logout()

