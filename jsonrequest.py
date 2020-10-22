jsonfile="""{"name":"services_requests","properties":{"sr_number":{"type":"string"},"sr_type":{"type":"string"},"department_id":{"type":"number"},"status":{"type":"string"},"created_date":{"type":"string"},"last_modified_date":{"type":"string"},"closed_date":{"type":"string"},"street_address":{"type":"string"},"city":{"type":"string"},"state":{"type":"string"},"zip_code":{"type":"string"},"street_direction":{"type":"string"},"street_name":{"type":"string"},"street_type":{"type":"string"},"duplicate":{"type":"boolean"},"legacy_record":{"type":"boolean"},"legacy_sr_number":{"type":"string"},"parent_sr_number":{"type":"string"},"community_area":{"type":"number"},"ward":{"type":"string"},"electrical_district":{"type":"string"},"electricity_grid":{"type":"string"},"zip_codes":{"type":"string"},"police_sector":{"type":"string"},"police_district":{"type":"number"},"police_beat":{"type":"string"},"precinct":{"type":"string"},"sanitation_division_days":{"type":"string"},"created_hour":{"type":"string"},"created_day_of_week":{"type":"string"},"created_month":{"type":"string"},"x_coordinate":{"type":"string"},"y_coordinate":{"type":"string"},"latitude":{"type":"string"},"longitude":{"type":"string"},"location":{"type":"string"},"boundaries":{"type":"string"},"community_areas":{"type":"string"},"tracts":{"type":"string"},"wards":{"type":"string"}}}"""

import json
print(type(jsonfile))

j_obj= json.loads(jsonfile)
print(type(j_obj))

items=[*j_obj]
print (*j_obj['properties'])
print(j_obj['properties'])
print(j_obj['properties'])
column_name= [*j_obj['properties']]
column_type=[]
for item in column_name:
    print (item+" ==="+ str(*j_obj['properties'][item].values()))
    pass