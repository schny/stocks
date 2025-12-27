import pandas as pd

df = pd.read_csv('AAPL_5years.csv', skiprows=2)

with open('aapl.ttl', 'w') as f:
    f.write(f'@prefix : <http://example.org/stock/> .\n')
    f.write(f'@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n')
    f.write(f'@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n')
    f.write(f'@prefix owl: <http://www.w3.org/2002/07/owl#> .\n')
    f.write(f'@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n')
    f.write(f':hasStock rdf:type owl:ObjectProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range :Stock .\n')
    f.write(f':Stock rdfs:subClassOf [\n')
    f.write(f'      rdf:type owl:Restrictions ;\n')
    f.write(f'      owl:onProperty :hasDailyPrice ;\n')
    f.write(f'      owl:minCardinality "1"^^xsd:nonNegativeInteger\n')
    f.write(f'      ] .\n')
    f.write(f':Ticker rdf:type owl:DatatypeProperty ;\n')
    f.write(f'        rdfs:domain :Stock ;\n')
    f.write(f'        rdfs:range xsd:string .\n\n')
    f.write(':companyName rdf:type owl:DatatypeProperty ;\n')
    f.write('         rdfs:domain :Stock ;\n')
    f.write('         rdfs:range xsd:string .\n')
    f.write(f':date rdf:type owl:DatatypeProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range xsd:date .\n')
    f.write(f':open rdf:type owl:DatatypeProperty;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range xsd:decimal .\n')
    f.write(f':close rdf:type owl:DatatypeProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range xsd:decimal .\n')
    f.write(f':high rdf:type owl:DatatypeProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range xsd:decimal .\n')
    f.write(f':low rdf:type owl:DatatypeProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice ;\n')
    f.write(f'      rdfs:range xsd:decimal .\n')
    f.write(f':volume rdf:type owl:DatatypeProperty ;\n')
    f.write(f'      rdfs:domain :DailyPrice  ;\n')
    f.write(f'      rdfs:range xsd:integer .\n\n')
    f.write(f':AAPL rdf:type :Stock ;\n')
    f.write(f'      :ticker "AAPL" ;\n')
    f.write(f'      :companyName "Apple Inc." .\n\n')
    for _, row in df.iterrows():
        date = row[0]
        instance_name = 'dp_' + date.replace('-', '_')
        close = row[1]
        high = row[2]
        low = row[3]
        open = row[4]
        volume = row[5]
        print(date)

        f.write(f':{instance_name} rdf:type :DailyPrice ;\n')
        f.write(f'                :hasStock :AAPL ;\n')
        f.write(f'                :date "{date}"^^xsd:date ;\n')
        f.write(f'                :open "{open}"^^xsd:decimal ;\n')
        f.write(f'                :high "{high}"^^xsd:decimal ;\n')
        f.write(f'                :low "{low}"^^xsd:decimal ;\n')
        f.write(f'                :volume "{volume}"^^xsd:integer .\n')
