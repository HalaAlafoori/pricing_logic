import frappe
import json
import os

def create_doctype_from_json(file_path):
    """Create Doctype from the JSON file."""
    try:
        # Load the JSON data from the file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Check if the Doctype already exists
        if not frappe.get_all('DocType', filters={'name': data['name']}):
            # Create the Doctype
            frappe.get_doc(data).insert()
            frappe.db.commit()
            print(f"Doctype {data['name']} created successfully!")
        else:
            print(f"Doctype {data['name']} already exists.")
    except Exception as e:
        print(f"Error while creating Doctype from {file_path}: {e}")

def execute():
    # Get the path to the current project directory
    project_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to the JSON files inside the doctype_definitions directory
    pricing_logic_json = os.path.join(project_directory, 'pricing_logic', 'doctype_definitions', 'pricing_logic.json')
    pricing_tier_json = os.path.join(project_directory, 'pricing_logic', 'doctype_definitions', 'pricing_tier.json')
    tiered_pricing_logic_json = os.path.join(project_directory, 'pricing_logic', 'doctype_definitions', 'tiered_pricing_logic.json')

    # Create Doctypes from the JSON files
    create_doctype_from_json(pricing_logic_json)
    create_doctype_from_json(pricing_tier_json)
    create_doctype_from_json(tiered_pricing_logic_json)