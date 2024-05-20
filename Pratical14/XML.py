rom lxml import etree
import matplotlib.pyplot as plt
from datetime import datetime
import time

def parse_go_terms_with_dom(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    
    namespaces = {'': 'http://www.w3.org/2002/08/xforms'}  
    term_counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    
    for term in root.findall('.//{http://www.geneontology.org/}term', namespaces):
        namespace = term.find('{namespace}', namespaces).text
        if namespace in term_counts:
            term_counts[namespace] += 1
    
    return term_counts

def parse_go_terms_with_sax(xml_file):
  halder=etree.SAXHandler(etree.SAXHandler)
    
    parser = etree.XMLParser(target=handler)
    with open(xml_file, 'rb') as f:
        etree.parse(f, parser)
    
   
    return handler.term_counts


def main():
    xml_file = 'go_obo.xml'
    
    start_time_dom = time.time()
    dom_results = parse_go_terms_with_dom(xml_file)
    dom_time_taken = time.time() - start_time_dom
    
    start_time_sax = time.time()
    sax_results = parse_go_terms_with_sax(xml_file)
    sax_time_taken = time.time() - start_time_sax
    
    print(f"DOM Results: {dom_results}")
    print(f"SAX Results: {sax_results}")
    print(f"DOM Time Taken: {dom_time_taken} seconds")
    print(f"SAX Time Taken: {sax_time_taken} seconds")
    
    plt.bar(['Molecular Function', 'Biological Process', 'Cellular Component'], 
            [dom_results['molecular_function'], dom_results['biological_process'], dom_results['cellular_component']], 
            color='blue')
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title('Frequency of GO Terms in Different Ontologies (DOM API)')
    plt.show()
   
    fastest_api = 'DOM' if dom_time_taken < sax_time_taken else 'SAX'
    print(f"Fastest API: {fastest_api}")

if __name__ == "__main__":
    main()
