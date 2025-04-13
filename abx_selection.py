# This app requires the Streamlit library to run.
# Make sure you install it with `pip install streamlit`

import streamlit as st

# Antibiotic info is now defined globally so the UI can access it
antibiotic_info = {
    "Amoxicillin": "Broad-spectrum penicillin, safe in pregnancy. Dose: 500mg TID for 7-10 days.",
    "Ceftriaxone": "3rd-gen cephalosporin, good for meningitis and pneumonia. Dose: 1-2g IV daily for 5-14 days.",
    "Cefotaxime": "3rd-gen cephalosporin, similar to ceftriaxone, good for meningitis, pneumonia, and sepsis. Dose: 1-2g IV Q6-8H.",
    "Azithromycin": "Macrolide, effective against atypical pathogens. Dose: 500mg day 1, then 250mg daily for 4 days.",
    "Clindamycin": "Lincosamide, covers anaerobes and Gram-positives. Dose: 300-450mg PO QID for 7-10 days.",
    "Nitrofurantoin": "Urinary antiseptic, not for renal impairment. Dose: 100mg BID for 5-7 days.",
    "TMP-SMX": "Effective for UTI and MRSA, risk of hyperkalemia. Dose: 160/800mg BID for 3-14 days.",
    "Vancomycin": "Glycopeptide for MRSA and C. difficile. Dose: 15-20mg/kg IV BID (adjust per levels).",
    "Levofloxacin": "Fluoroquinolone, covers atypicals and Gram-negatives. Dose: 500-750mg daily for 5-10 days.",
    "Ciprofloxacin": "Fluoroquinolone, active against Gram-negative bacteria including Pseudomonas. Dose: 500mg BID for 5-7 days.",
    "Linezolid": "Oxazolidinone, good for MRSA and VRE. Risk of serotonin syndrome. Dose: 600mg BID for 10-14 days.",
    "Doxycycline": "Tetracycline, good for atypicals and some Gram-positives. Avoid in pregnancy. Dose: 100mg BID for 7-14 days.",
    "Piperacillin-Tazobactam": "Broad-spectrum beta-lactam/beta-lactamase inhibitor. Dose: 3.375-4.5g IV Q6-8H for 7-14 days.",
    "Cefepime": "4th-gen cephalosporin, broad Gram-negative coverage. Dose: 1-2g IV Q8-12H for 7-10 days.",
    "Amoxicillin-Clavulanate": "Broad-spectrum with beta-lactamase inhibitor. Useful for respiratory infections. Dose: 875/125mg BID for 7-10 days.",
    "Cefuroxime": "2nd-gen cephalosporin, effective for respiratory and urinary infections. Dose: 250-500mg BID for 7-10 days.",
    "Penicillin G": "Narrow-spectrum, used for susceptible streptococci and syphilis. Dose varies based on indication.",
    "Meropenem": "Carbapenem, broad-spectrum including ESBL-producing organisms. Dose: 500mg-1g IV Q8H.",
    "Cefdinir": "3rd-gen oral cephalosporin, good for otitis media. Dose: 300mg BID or 600mg once daily for 5-10 days.",
    "Cephalexin": "1st-gen cephalosporin, good for skin infections. Dose: 500mg QID for 7-10 days.",
    "Fosfomycin": "Single-dose treatment for uncomplicated UTI in women. Dose: 3g PO once."
}

# The rest of the app's logic would go here, including:
# - choose_antibiotic() function for decision logic
# - Streamlit UI inputs for user data entry
# - Displaying recommendations using st.success/st.expander, etc.
