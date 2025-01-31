from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from bs4 import BeautifulSoup

app = FastAPI()

class DrugIDRequest(BaseModel):
    drug_id: str

def import_database_from_xml(file):
    with open(file) as f:
        drugbank_file = f.read()
    return BeautifulSoup(drugbank_file, 'lxml-xml')

def create_drugs_pathways_dataframe(data):
    pathways_drugs = []
    for drug in data.find('drugbank').find_all('drug', recursive=False):
        name = drug.find('name', recursive=False).text
        id = drug.find('drugbank-id', recursive=False).text
        pathways = drug.find('pathways', recursive=False)
        if pathways:
            for pathway in pathways.find_all('pathway', recursive=False):
                pathway_name = pathway.find('name', recursive=False).text

                pathways_drugs.append({
                    'Drug ID': id,
                    'Drug Name': name,
                    'Pathway Name': pathway_name
                })

    return pd.DataFrame(pathways_drugs)

pathways_df = create_drugs_pathways_dataframe(import_database_from_xml('drugbank_partial.xml'))

@app.post("/get_pathways_count/")
def get_pathways_count(request: DrugIDRequest):
    pathways_count = len(pathways_df.loc[pathways_df['Drug ID'] == request.drug_id])
    return {"drug_id": request.drug_id, "pathways_count": pathways_count}